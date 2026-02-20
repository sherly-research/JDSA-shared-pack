# Read Me

This share pack is a **minimal, self-contained** bundle to let readers reproduce the two evaluation programs:

1. **Silver Testing (intersection-based, quality-/context-aware reporting)**  
2. **Output-based Intrinsic Metrics (overall + by-source; ablation + baseline-aligned tracks)**

The pack contains:
- Patched notebooks (local paths; no Google Drive dependency)
- All input CSVs used by the notebooks
- Precomputed outputs (CSV summaries) used in the manuscript, to compare against regenerated outputs
- A file manifest (SHA256) for integrity checks

---

## Folder structure

```
shared_evaluasi_multi_metric/
  notebooks/
    01_Evaluate_SilverTesting_patched.ipynb
    02_Evaluate_outputbased_intrinsic_metrics_patched.ipynb
  data/
    dataset_baseline/        # the exact folder the notebooks expect
      rb_apect_terms_full_with_segtext.csv
      unsup_terms_ranked_full_with_segtext.csv
      dataset_hybrid_best_terms_sbert.csv
      baseline_aspect_terms_*.csv
      dataset_baseline_CTM.csv
  precomputed_outputs/
    silver/                  # manuscript silver summaries
    intrinsic/               # manuscript intrinsic summaries
  outputs/                   # created when you run notebooks (empty by default)
  requirements.txt
  MANIFEST.sha256.json
```

---

## Quickstart (recommended)

### Option A — run locally (conda/venv)
```bash
cd shared_evaluasi_multi_metric
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Open and run notebooks in this order:
1. `notebooks/01_Evaluate_SilverTesting_patched.ipynb`
2. `notebooks/02_Evaluate_outputbased_intrinsic_metrics_patched.ipynb`

All regenerated files will be written under:
- `./outputs/silver_intersection/`
- `./outputs/intrinsic_metrics/`

### Option B — run in Google Colab
Upload the whole folder to Colab (or Google Drive), then open the patched notebooks.
They use **relative paths**, so it will work as long as the current working directory is `shared_evaluasi_multi_metric/`.

---

## What each program does (high-level)

### 1) Silver testing notebook
**Goal:** build “silver” agreement tables by intersecting aspect-term outputs across methods at the **(comment_id, seg_id)** level.

**Inputs (from `data/dataset_baseline/`):**
- `rb_apect_terms_full_with_segtext.csv`
- `unsup_terms_ranked_full_with_segtext.csv`
- `dataset_hybrid_best_terms_sbert.csv`

**Key columns used:**
- keys: `comment_id`, `seg_id`
- terms:  
  - RB: `aspect_terms_rb_clean`  
  - UNSUP: `aspect_terms_unsup`  
  - HYB: `hybrid_topk_terms`
- segment text (for display / context checking): `seg_text` (fallbacks exist)

**Main outputs (regenerated):**
- `master_silver_raw_intersection.csv`
- `summary_silver_raw_intersection.csv`
- `master_silver_qualityaware_intersection.csv`
- `summary_silver_contextaware_silver_intersection.csv`

These regenerated outputs should match the precomputed files under `precomputed_outputs/silver/`
(modulo row ordering).

### 2) Intrinsic metrics notebook
**Goal:** compute output-based intrinsic metrics (coverage, density, diversity, surface evidence, context fit),
with two reporting tracks:
- **Ablation track:** RB vs UNSUP vs HYB on their natural segment sets
- **Baseline-aligned track:** baselines aligned to HYB segment set for fair comparison

**Inputs (from `data/dataset_baseline/`):**
- Core: `rb_apect_terms_full_with_segtext.csv`, `unsup_terms_ranked_full_with_segtext.csv`, `dataset_hybrid_best_terms_sbert.csv`
- Baselines: `baseline_aspect_terms_lda_nmf_topk3.csv`, `baseline_aspect_terms_btm.csv`, `dataset_baseline_CTM.csv`,
  `baseline_aspect_terms_bertopic.csv`, `baseline_aspect_terms_top2vec.csv`, `baseline_aspect_terms_abae_v2.csv`

**Main outputs (regenerated):**
- `intrinsic_overall_ablation_3methods.csv`
- `intrinsic_overall_baseline_aligned_to_hybrid.csv`
- `intrinsic_by_source_ablation_3methods.csv`
- `intrinsic_by_source_baseline_aligned_to_hybrid.csv`
- `intrinsic_evaluation_refactor_v2.xlsx`

These should match the precomputed files under `precomputed_outputs/intrinsic/`
(modulo numeric rounding and row ordering).

---

## Notes on data content / privacy
- The CSVs contain segment-level text (`seg_text`, `comment_ori`, etc.).  
  If anonymization is required for double-blind review, you can remove the raw text columns and still reproduce most intrinsic metrics
  **except** those relying on “InText” checks (surface evidence) or text-normalization steps.

---

## Troubleshooting
- If you see missing package errors, ensure you installed `requirements.txt`.
- If a notebook reports a missing file, confirm you are running from the folder `shared_evaluasi_multi_metric/`
  so relative paths like `./data/dataset_baseline/...` resolve correctly.

---

## Integrity
See `MANIFEST.sha256.json` for file checksums (SHA256) and sizes.
