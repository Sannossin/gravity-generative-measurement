# Gravity as generative measurement

**A speculative physics essay with one dark-energy law, dated predictions, and a pre-registered test record.**
Sandhya Nossin · version 5.4 (November 2026) · essay and full archive on Zenodo: [doi.org/10.5281/zenodo.23422750](https://doi.org/10.5281/zenodo.23422750)

> I am not a physicist. The ideas are mine; the formalization, the calculations and the reviews were done with the help of an AI assistant (Claude, Anthropic), which is not a co-author. The calculations have been checked by other instances of the same AI, which is not an independent review. Comments and refutations from physicists are very welcome.

## In one paragraph

The essay proposes a dark-energy law, **S3-L**, in which a fraction of the Hubble horizon is progressively "inscribed",

&nbsp;&nbsp;&nbsp;&nbsp;f = 1 − exp[−μ0 (H0/H)³],

and the dark-energy density follows from a 1/a dilution of each inscription. For the expansion history it adds **no parameter** to ΛCDM: its single constant μ0 replaces Ω_Λ. Fitted to DESI DR2 + Planck, μ0 = 1.305 ± 0.016. The form of the law is posed, not derived, and was chosen after seeing the data. A second part of the essay gives an interpretation (six postulates, presented as hypotheses) that motivated the law.

## The one prediction specific to the framework

**The bet μ0 = 4/3.** With a counting convention fixed by the interpretation (a cell is a Planck area, one unit of information per four cells, one event per pixel of the source projected on a fixed depth) and the hypothesis that our horizon reaches the size of the source today, μ0 = 4/3 exactly. The dark-energy curve then has **no free parameter** and imposes

- **Ω_m = 0.3123**;
- D_M/D_H within 1.5 % of ΛCDM, the largest deviation near z ≈ 1.5.

Today it is compatible with the data (Δχ² = +2.1 against the free fit, about 1.4σ). **Final DESI and Euclid will judge it from 2027.** It is refuted if Ω_m is incompatible with 0.3123 at more than 3σ (S3-L with a fitted μ0 would survive). The counting convention was fixed while knowing the data: this is a fragile bet, not a derivation, and it does not explain why the coincidence happens in our epoch.

## Check it yourself in one minute

```
pip install numpy scipy
python3 s3l_check.py            # mu0 = 4/3  ->  Omega_m = 0.3123, w(0) = -0.816, w crosses -1 near z = 0.45
python3 s3l_check.py 1.305 0.6719   # fitted value -> Omega_m = 0.318, Omega_DE = 0.682, w(0) = -0.821
```

`s3l_check.py` solves the S3-L background (numpy + scipy only) and prints Ω_m, w(z) and D_M/D_H against flat ΛCDM. It is a background-only check; the full fits (CMB spectrum with CAMB, DESI DR2 BAO, four supernova catalogues) are in the source archive on Zenodo.

## Where it stands (v5.4)

All tests tried so far, successes and failures, are listed in [REGISTRE.md](REGISTRE.md) and [registre_hypotheses.csv](registre_hypotheses.csv) (in French).


| | |
|---|---|
| Fit vs ΛCDM | Δχ² = −5.2 before penalty (DESI DR2 + Planck, no SNe); with Dovekie SNe −9.2 raw, ≈ −2.8 after the penalty for the ~25 laws tried: a weak preference, not a win |
| Free exponent | 2.85 (+0.20/−0.18); exponents 1 and 2 excluded |
| S8 | the frozen prediction (0.850) has failed: DES Y6 measures 0.789 ± 0.012, below the threshold 0.798 set in advance. With the condensate loan, computed after the fact, the model gives ≈ 0.805, the same as ΛCDM: S8 no longer distinguishes them |
| Inflation | Starobinsky with the retained reheating (chosen after the fact): n_s = 0.9618 (0.7σ from Planck alone, 2.4σ from ACT DR6 + Planck, up to 4.5σ with lensing, DESI and BICEP/Keck). **No graviton: r ≈ 0**, whereas standard Starobinsky inflation predicts r ≈ 0.004; LiteBIRD will decide |
| Open track | a relation between the scalaron mass, the Higgs vacuum value and the Planck mass, (M/M_P)³ = v/M_P, gives G at 0.89–0.92 of its measured value without a loop; one form out of about twenty falls in the window (chance 7–15 %): undecided |

All dated predictions and what would refute them: [PREDICTIONS.md](PREDICTIONS.md).

## Method: predictions frozen before each calculation

Every test (numbered 1 to 492) follows the same protocol: the expected results are written down first, the file is fingerprinted (sha256) with its freeze time, the code is fingerprinted before it runs, and the result is reviewed afterwards. Failures are published as well as successes, in a separate document ("Pistes écartées, variantes et réfutées", same DOI). The fingerprints of all frozen-prediction files are in [`frozen_predictions_v5.4.tsv`](frozen_predictions_v5.4.tsv); the Zenodo deposit gives them an external date.

## Short note (3 pages, English)

[s3l-bet-note.pdf](s3l-bet-note.pdf), also on Zenodo: [doi.org/10.5281/zenodo.24226342](https://doi.org/10.5281/zenodo.24226342). The law, the current fits, the bet μ0 = 4/3 and what would refute it, without the interpretation.

## Documents (Zenodo, same DOI)

- **Short essay (French, reference text)** and **short paper (English)**: the model, the interpretation, the dated predictions.
- **Dated predictions** (4 pages).
- **Full dossier** (160 pages): every test, every attribution (who contributed what).
- **Discarded leads, variants and refuted ideas.**
- **Source archive**: LaTeX, figures, code, pre-registered tests with their reviews.

## En français

Essai de physique spéculative, écrit par une autrice qui n'est pas physicienne, avec l'aide d'une IA (Claude, Anthropic), qui n'est pas coautrice. Une loi d'énergie sombre, S3-L, sans réglage de plus que le modèle standard ; un pari, μ0 = 4/3, qui ne laisse aucun réglage et impose Ω_m = 0,3123, jugé par DESI et Euclid dès 2027 ; des prédictions datées, toutes figées avant le calcul. Le texte de référence est l'essai court en français, sur Zenodo : [doi.org/10.5281/zenodo.23422750](https://doi.org/10.5281/zenodo.23422750).

## Citation and contact

Sandhya Nossin, *La gravité comme mesure générative — Énergie sombre et gravité qui enregistre*, version 5.4 (2026), Zenodo, doi:10.5281/zenodo.23422750. See [CITATION.cff](CITATION.cff).

Contact: sandhya.nos@proton.me

Licences: code under MIT ([LICENSE](LICENSE)); texts under CC BY 4.0.
