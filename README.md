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
