# JDSA-shared-pack

This repository is a reviewer-oriented share pack for the manuscript:

**Enhancing Aspect Discovery through a Bifurcated Hybrid Approach for Extracting Relevant Terms from Unstructured-Unlabeled Energy Data**  
**Authors:** Sherly Christina, Azhari Azhari, Yohanes Suyanto

It contains two components:
- `shared_proposed_models/` — notebooks/scripts for the proposed pipeline (UNSUP, RB, and Hybrid fusion-and-selection).
- `shared_evaluasi_multi_metric/` — notebooks for multi-metric evaluation (silver + output-based intrinsic metrics).

---

## Data availability (Zenodo)

Large datasets, baseline exports, and precomputed outputs used by the evaluation are archived on Zenodo:

- **Zenodo (v1.0.0)**: https://doi.org/10.5281/zenodo.18707970  
- **Zenodo (all versions / concept DOI)**: https://doi.org/10.5281/zenodo.18707969

The Zenodo record includes:
- `data.zip`
- `dataset_baselines.zip`
- `outputs_bifurcated_hybrid_ate.zip`

> If you run the evaluation notebooks, please download the ZIP files above and place the required CSVs under  
> `shared_evaluasi_multi_metric/data/dataset_baseline/` (see the evaluation README for exact file mapping).

---
## Citation

If you use this repository or the Zenodo artifacts, please cite:

Sherly Christina, Azhari Azhari, Yohanes Suyanto.
Enhancing Aspect Discovery through a Bifurcated Hybrid Approach for Extracting Relevant Terms from Unstructured-Unlabeled Energy Data. JDSA submission.
