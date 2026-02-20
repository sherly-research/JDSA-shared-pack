from __future__ import annotations
import argparse, json, ast, re
from pathlib import Path
import pandas as pd
import numpy as np

def parse_list_cell(x):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return []
    if isinstance(x, list):
        return [str(t).strip() for t in x if str(t).strip()]
    s = str(x).strip()
    if not s or s.lower() in {"nan","none","null","[]"}:
        return []
    if s.startswith("[") and s.endswith("]"):
        try:
            v = json.loads(s)
            if isinstance(v, list):
                return [str(t).strip() for t in v if str(t).strip()]
        except Exception:
            pass
        try:
            v = ast.literal_eval(s)
            if isinstance(v, (list, tuple)):
                return [str(t).strip() for t in v if str(t).strip()]
        except Exception:
            pass
    for sep in [";", "|"]:
        if sep in s:
            return [p.strip() for p in s.split(sep) if p.strip()]
    if "," in s:
        parts = [p.strip() for p in s.split(",") if p.strip()]
        if all(len(p.split()) <= 6 for p in parts):
            return parts
    return [s]

def norm_term(t: str) -> str:
    return re.sub(r"\s+", " ", str(t)).strip().lower()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fusion_input", default="data/dataset_merged_with_unsup_rb_aspects_ALLCOLS.csv")
    ap.add_argument("--out", default="outputs/hybrid_from_merge_minimal.csv")
    args = ap.parse_args()

    df = pd.read_csv(args.fusion_input)
    # Minimal reproducible hybrid: union of cleaned RB and UNSUP lists, then choose best term by simple heuristic (prefer overlap, else first)
    rb = df.get("aspect_terms_rb_clean", pd.Series([None]*len(df))).apply(parse_list_cell)
    un = df.get("aspect_terms_unsup", pd.Series([None]*len(df))).apply(parse_list_cell)

    best=[]
    origin=[]
    topk=[]
    for r,u in zip(rb.tolist(), un.tolist()):
        r=[norm_term(t) for t in r if norm_term(t)]
        u=[norm_term(t) for t in u if norm_term(t)]
        inter = [t for t in r if t in set(u)]
        if inter:
            best.append(inter[0]); origin.append("overlap"); topk.append(inter[:5])
        elif r:
            best.append(r[0]); origin.append("rb"); topk.append(r[:5])
        elif u:
            best.append(u[0]); origin.append("unsup"); topk.append(u[:5])
        else:
            best.append(""); origin.append("empty"); topk.append([])

    out = df[["seg_key","comment_id","seg_id","source","date"]].copy() if "seg_key" in df.columns else df[["comment_id","seg_id","source","date"]].copy()
    out["hybrid_best_term"] = best
    out["hybrid_best_origin_minimal"] = origin
    out["hybrid_topk_terms_minimal"] = [json.dumps(x, ensure_ascii=False) for x in topk]
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    print("Wrote:", args.out, "rows:", len(out))

if __name__ == "__main__":
    main()
