# Split Files

For a reproducible release, replace the `*_TEMPLATE.csv` files with the exact subject assignments used in the final experiments.

## Required files

### `main_split.csv`

Required columns:

```text
subject_id,site,label,split
```

Expected split counts:
- train: 714
- validation: 153
- test: 154
- total: 1021

Recommended label convention:
- ASD = 1
- TD = 0

### `cv_folds.csv`

Required columns:

```text
subject_id,site,label,fold
```

Use fold values 1–5. Store the exact fold membership used to generate the reported five-fold results.

### `loso_sites.csv`

Required columns:

```text
site,eligible_for_loso,reason
```

Document every site-specific collection in the final cohort and state whether it was included in LOSO.

**Important:** The manuscript's final-cohort table contains 16 site-specific collections, while the LOSO results contain 14 evaluated sites. Verify and document the reason for the two excluded collections before release.
