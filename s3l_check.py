"""Quick check of the S3-L dark-energy law (Nossin, "Gravity as generative measurement", v5.4).

S3-L: the inscribed fraction of the Hubble horizon is
    f = 1 - exp[-mu0 (H0/H)^3],
and the dark-energy density follows from a 1/a dilution of each inscription:
    rho_DE(a) = H^3/a * Integral_0^a a' H' d(f/H'^2)      (units: critical density today, H in units of H0)
    E^2 = Om a^-3 + Or a^-4 + rho_DE / rho_crit,0
There is no extra amplitude: mu0 alone fixes the dark-energy curve, and flatness then fixes Omega_m.
So mu0 replaces Omega_Lambda (same number of parameters as LCDM).

This script (numpy + scipy only, about a minute):
  1. solves the background for a given mu0 and reports Omega_m, Omega_DE, f0, w0;
  2. reproduces the bet mu0 = 4/3  ->  Omega_m ~ 0.312 (the framework's only specific prediction);
  3. prints w(z) and the ratio D_M/D_H against a flat LCDM with a chosen Omega_m.
It is a background-only check. The full fits (CMB spectrum, DESI DR2 BAO, supernovae) are in the
source archive on Zenodo: https://doi.org/10.5281/zenodo.23422750

Usage:  python3 s3l_check.py [mu0] [h] [Om_LCDM]
        defaults: mu0 = 4/3, h = 0.6746, Om_LCDM = 0.303
"""
import sys
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.optimize import brentq

mu_in = float(eval(sys.argv[1])) if len(sys.argv) > 1 else 4.0/3.0
h = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6746
Om_lcdm = float(sys.argv[3]) if len(sys.argv) > 3 else 0.303

def omega_r(h):                      # photons + 3.046 massless neutrinos
    return 2.469e-5*(1 + 0.2271*3.046)/h**2

N_grid = np.linspace(-np.log(1 + 3e4), 0.0, 3001)   # N = ln a, from z = 3e4 to today

def solve(mu, Om, Or):
    """Integrate E(N) and Y(N), with Omega_DE(N) = E^3 e^-N Y and Y = Integral a E dX, X = f/E^2.
    The algebraic constraint E^2 = M + E^3 e^-N Y is enforced with a restoring term (kappa = 20)."""
    def rhs(N, s):
        E, Y = s
        u = mu/E**3
        f = -np.expm1(-u)
        Xp = (-3*u*np.exp(-u)/E)/E**2 - 2*f/E**3          # dX/dE
        FN = E**3*np.exp(-N)*Y + 3*Om*np.exp(-3*N) + 4*Or*np.exp(-4*N)
        FY = -E**3*np.exp(-N)
        FE = 2*E - 3*E**2*np.exp(-N)*Y
        M = Om*np.exp(-3*N) + Or*np.exp(-4*N)
        Fv = E**2 - E**3*np.exp(-N)*Y - M
        Ed = -(FN + 20.0*Fv)/(FE + FY*E*np.exp(N)*Xp)
        return [Ed, E*np.exp(N)*Xp*Ed]
    N0 = N_grid[0]
    M0 = Om*np.exp(-3*N0) + Or*np.exp(-4*N0)
    r = solve_ivp(rhs, (N0, 0.0), [np.sqrt(M0), 0.0], t_eval=N_grid, rtol=1e-10, atol=1e-30, method='LSODA')
    if not r.success:
        return None
    E, Y = r.y
    return E, E**3*np.exp(-N_grid)*Y

def Om_from_mu(mu, h):
    """Flatness today: Omega_DE(today) = 1 - Om - Or."""
    Or = omega_r(h)
    def g(Om):
        s = solve(mu, Om, Or)
        return np.nan if s is None else s[1][-1] - (1 - Om - Or)
    return brentq(g, 0.20, 0.45, xtol=1e-9)

Or = omega_r(h)
Om = Om_from_mu(mu_in, h)
E, ODE = solve(mu_in, Om, Or)
z = np.exp(-N_grid) - 1
f0 = -np.expm1(-mu_in)
rhoD = E**2 - (Om*np.exp(-3*N_grid) + Or*np.exp(-4*N_grid))
w = -1 - np.gradient(np.log(np.maximum(rhoD, 1e-300)), N_grid)/3

print(f"S3-L with mu0 = {mu_in:.4f}, h = {h}")
print(f"  Omega_m = {Om:.4f}   Omega_DE = {ODE[-1]:.4f}   f0 = {f0:.4f}   w(z=0) = {w[-1]:+.3f}")
low = (z < 3)
zz, ww = z[low][::-1], w[low][::-1]                   # increasing z
k = np.where(np.diff(np.sign(ww + 1)) != 0)[0]
if len(k):
    zc = zz[k[0]] - (ww[k[0]] + 1)*(zz[k[0]+1] - zz[k[0]])/(ww[k[0]+1] - ww[k[0]])
    print(f"  w crosses -1 once, near z = {zc:.2f}")
print()

# D_M/D_H against flat LCDM (radiation included); r_d cancels in this ratio
def EL(zz, Omc):
    return np.sqrt(Omc*(1 + zz)**3 + Or*(1 + zz)**4 + (1 - Omc - Or))
zs, Es = z[::-1], E[::-1]                       # increasing z
DM_s = cumulative_trapezoid(1/Es, zs, initial=0)
DM_l = cumulative_trapezoid(1/EL(zs, Om_lcdm), zs, initial=0)
print(f"  z      w(z)    D_M/D_H  S3-L vs flat LCDM (Om = {Om_lcdm})")
for zi in (0.30, 0.51, 0.71, 0.93, 1.32, 1.60, 2.00, 2.33):
    wi = np.interp(zi, zs, w[::-1])
    rs = np.interp(zi, zs, DM_s*Es)
    rl = np.interp(zi, zs, DM_l*EL(zs, Om_lcdm))
    print(f"  {zi:4.2f}  {wi:+.3f}   {100*(rs/rl - 1):+.2f} %")
print()
print("Note: the published -1.47 % (z ~ 1.5) compares with the best-fit LCDM of the same full chain (test 423);")
print("this background-only check uses a fixed LCDM, so its numbers differ slightly.")
