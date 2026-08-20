# MAP-ASDNet Reproducibility Repository

**MAP-ASDNet: A Multi-Slice CNN–BiLSTM Framework with Attention and Phenotypic Fusion for Autism Spectrum Disorder Classification**

This repository is a reproducibility starter package for the MAP-ASDNet study. It is structured to support a DOI-minted GitHub release archived through Zenodo.

> IMPORTANT: Replace every `REPLACE_WITH_...` placeholder and copy the **actual final experiment code and split files** into this repository before creating the Zenodo-backed release. Do not upload raw ABIDE-II MRI or phenotypic data.

## Study configuration represented here

The configuration mirrors the manuscript's reported experimental setup:

- Dataset: ABIDE-II
- Final cohort: 1,021 unique participants
- Diagnostic composition: 475 ASD, 546 TD
- Main split: 714 train / 153 validation / 154 test
- Imaging input: 25 ordered axial slices per subject
- Slice size: 160 × 160 × 1
- Slice interval: 3 voxels
- Resampling: 2 × 2 × 2 mm isotropic
- Intensity clipping: 1st–99th percentile
- Intensity normalization: min–max to [0,1]
- Shared CNN filters: 32, 64, 128, 256
- CNN slice embedding: 128 dimensions
- BiLSTM: 96 units per direction
- Attention dimension: 64
- Imaging projection: 128
- Phenotypic projection: 32
- Joint fused representation: 128
- Optimizer: Adam
- Initial learning rate: 3e-4
- Batch size: 8
- Maximum epochs: 80
- Early stopping: validation AUC, patience 12
- ReduceLROnPlateau: factor 0.5, patience 5, minimum LR 1e-6
- L2 coefficient: 1e-5
- Random seed: 42
- Model/threshold selection: validation data only
- Main test-set evaluation: independent held-out test set
- Additional evaluation: five-fold CV, subject-level paired significance testing, LOSO, site-adversarial experiment

See `config/config.yaml`.

## Repository structure

```text
MAP-ASDNet/
├── README.md
├── CITATION.cff
├── LICENSE
├── DATA_LICENSE_NOTICE.md
├── CHANGELOG.md
├── requirements.in
├── .gitignore
├── config/
│   └── config.yaml
├── docs/
│   ├── MANUSCRIPT_STATEMENTS.md
│   └── ZENODO_GITHUB_RELEASE_GUIDE.md
├── scripts/
│   ├── collect_versions.py
│   └── validate_release.py
├── splits/
│   ├── README.md
│   ├── main_split_TEMPLATE.csv
│   ├── cv_folds_TEMPLATE.csv
│   └── loso_sites_TEMPLATE.csv
├── src/
│   ├── preprocessing/
│   ├── models/
│   ├── training/
│   └── evaluation/
└── results/
    └── README.md
```

## 1. Add the actual study code

Copy your final scripts into the matching folders:

- `src/preprocessing/`: NIfTI loading, canonical reorientation, resampling, foreground crop, intensity clipping/normalization, ordered slice extraction, phenotypic preprocessing and augmentation.
- `src/models/`: CNN-only, LSTM-only, BiLSTM-only, CNN-LSTM, CNN-BiLSTM, attention variant, full MAP-ASDNet, and site-adversarial variant.
- `src/training/`: data generators, training loop, callbacks, checkpointing and validation-threshold selection.
- `src/evaluation/`: held-out test evaluation, five-fold CV, LOSO, ROC/confusion matrix generation, McNemar testing and Holm correction.

Do not upload a rewritten or simplified implementation if it differs from the code used to obtain the manuscript results.

## 2. Add exact subject assignments

Replace the template CSVs in `splits/` with the exact files used for the experiments.

Minimum recommended files:

- `main_split.csv`
- `cv_folds.csv`
- `loso_sites.csv`

The main split should contain the exact 714/153/154 subject membership, not merely the random seed.

## 3. Capture the exact software environment

Run this in the **same environment used for the final experiments**:

```bash
python scripts/collect_versions.py
python -m pip freeze > requirements.txt
```

Keep `requirements.in` as the human-readable package list, and commit the generated `requirements.txt` containing exact installed versions.

## 4. Validate the release package

After replacing placeholders and adding the real split files:

```bash
python scripts/validate_release.py
```

Resolve all reported warnings before creating the release.

## 5. Data access

Raw ABIDE-II imaging and phenotypic data are **not redistributed** in this repository. Researchers should obtain them from the original ABIDE-II resource and comply with the applicable access and reuse terms.

ABIDE-II:
https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html

## 6. Code license vs. dataset terms

The repository code is prepared under the MIT License. This license applies only to the original software in this repository. It does **not** relicense ABIDE-II data.

See `DATA_LICENSE_NOTICE.md`.

## 7. Citation

Before release, edit `CITATION.cff` with the authors' exact names and optional ORCID identifiers.

Once the GitHub release has been archived by Zenodo, cite the DOI shown on the Zenodo record. For a manuscript tied to a specific code snapshot, the **version-specific DOI** is the clearest choice.

## 8. Reproducibility principles

This release should preserve:

1. exact subject membership for all reported splits;
2. train-only fitting of imputation/standardization parameters;
3. no test-set use for model fitting, checkpoint selection, hyperparameter selection, or threshold selection;
4. validation-based early stopping/checkpointing;
5. exact configurations for every ablation;
6. exact LOSO definitions;
7. code producing the reported metrics and statistical tests;
8. package/library versions from the final environment.

## Release version

Recommended first archived release: **v1.0.0 — manuscript reproducibility release**.
