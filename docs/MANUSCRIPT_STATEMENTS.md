# Manuscript-ready availability statements

## Data Availability Statement

The data analyzed in this study are publicly available through the Autism Brain Imaging Data Exchange II (ABIDE-II) repository. The present study used T1-weighted structural magnetic resonance imaging (sMRI) and corresponding phenotypic information from ABIDE-II for ASD-versus-typically-developing (TD) classification. The data were accessed and used in accordance with the applicable ABIDE/FCP-INDI/NITRC data-access and reuse requirements. Raw ABIDE-II imaging and phenotypic data are not redistributed as part of this study and should be obtained directly from the original repository.

Repository: https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html

**License note:** The NITRC parent resource currently displays the data license category as “Attribution Non-Commercial.” Before submission, verify the precise wording applicable to the ABIDE-II access route used in your study. Do not add a Creative Commons version number unless the source explicitly provides one.

## Code Availability and Reproducibility Statement

All experiments were implemented in Python 3.8 using TensorFlow/Keras [EXACT VERSION], NumPy [EXACT VERSION], Scikit-learn [EXACT VERSION], NiBabel [EXACT VERSION], and additional dependencies documented in the accompanying environment file. Experiments were conducted on NVIDIA RTX A6000 GPUs using CUDA 12.2. A random seed of 42 was used for the relevant Python, NumPy, and deep-learning framework operations to improve experimental repeatability. Exact subject-level train, validation, and test assignments, five-fold cross-validation fold assignments, and LOSO site definitions are provided with the released implementation.

All preprocessing operations requiring fitted parameters were performed without information leakage. Phenotypic imputation and standardization parameters were estimated exclusively from the corresponding training data and were subsequently applied unchanged to validation and test subjects. Model checkpointing, early stopping, learning-rate adjustment, and decision-threshold selection were based exclusively on validation performance. The independent test data were used only for final model evaluation.

The accompanying repository provides the preprocessing pipeline, MAP-ASDNet implementation, ablation configurations, training and evaluation scripts, five-fold cross-validation procedure, leave-one-site-out analysis, statistical significance testing, experimental configuration files, subject-split definitions, and exact software dependencies required to reproduce the reported experiments. Raw ABIDE-II data are not redistributed and must be obtained directly from the original repository in accordance with the applicable data-access and usage requirements. The source code and reproducibility materials are available at [GITHUB REPOSITORY URL], with the manuscript-matched archived release available at [ZENODO VERSION DOI].
