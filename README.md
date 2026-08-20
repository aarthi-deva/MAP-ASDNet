# MAP-ASDNet Reproducibility Repository

**MAP-ASDNet: A Multi-Slice CNN–BiLSTM Framework with Attention and Phenotypic Fusion for Autism Spectrum Disorder Classification**

## Overview

This repository contains the implementation and reproducibility materials associated with the MAP-ASDNet framework for Autism Spectrum Disorder (ASD) classification using structural magnetic resonance imaging (sMRI) and complementary phenotypic information.

MAP-ASDNet combines a shared two-dimensional Convolutional Neural Network (CNN) for slice-level feature extraction with a Bidirectional Long Short-Term Memory (BiLSTM) network for modelling contextual relationships across spatially ordered MRI slices. A slice-level attention mechanism is used to emphasize informative representations, followed by phenotypic feature fusion for subject-level ASD classification.

## Dataset

The study uses data from the publicly available Autism Brain Imaging Data Exchange II (ABIDE-II) repository.

ABIDE-II provides multi-site neuroimaging and phenotypic data from individuals with Autism Spectrum Disorder and typically developing controls.

Raw ABIDE-II data are not redistributed through this repository. Researchers should obtain the dataset directly from the official ABIDE-II repository and comply with the applicable data-access and usage requirements.

ABIDE-II repository:

https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html

## Repository Contents

The repository includes the implementation used for the MAP-ASDNet experiments together with supporting reproducibility files.

```text
MAP-ASDNet/
│
├── README.md
├── CITATION.cff
├── LICENSE
│
└── code/
    └── MAP-ASDNet_code.ipynb

## Disclaimer

MAP-ASDNet is intended for research purposes. The framework is not intended to replace professional clinical diagnosis or to be used as a standalone clinical diagnostic system.
