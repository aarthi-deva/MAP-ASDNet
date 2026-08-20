# MAP-ASDNet Pre-Release Checklist

## Scientific match
- [ ] Repository code is the exact code used for the final reported results.
- [ ] Main held-out split reproduces 714/153/154 subjects.
- [ ] Diagnostic totals reproduce 475 ASD / 546 TD.
- [ ] Five-fold assignments are frozen and included.
- [ ] LOSO definitions are frozen and included.
- [ ] 16 final site-specific collections vs. 14 LOSO sites is explicitly explained and verified.
- [ ] BiLSTM-only ablation matches the manuscript.
- [ ] Site-adversarial architecture and loss weighting are fully documented.
- [ ] Validation-only threshold selection is implemented.
- [ ] Test set is not used for fitting/model selection.

## Environment
- [ ] `requirements.txt` created with `python -m pip freeze`.
- [ ] TensorFlow version recorded.
- [ ] Keras version recorded.
- [ ] NumPy version recorded.
- [ ] Scikit-learn version recorded.
- [ ] NiBabel version recorded.
- [ ] SciPy version recorded.
- [ ] Statsmodels version recorded if used.
- [ ] CUDA version recorded.
- [ ] GPU model recorded.

## Metadata
- [ ] `CITATION.cff` has exact author names.
- [ ] ORCID IDs added if desired.
- [ ] GitHub URL is correct.
- [ ] MIT code license approved by all code authors.
- [ ] Dataset license notice checked against the actual ABIDE-II access route.

## Zenodo
- [ ] GitHub account linked to Zenodo.
- [ ] Repository enabled in Zenodo.
- [ ] GitHub release tag `v1.0.0` published.
- [ ] Zenodo successfully archived release.
- [ ] Version DOI copied into manuscript.
