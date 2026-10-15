import argparse, re
from pathlib import Path
def evaluate(value):
    return {"length_ok":len(value)>=12, "has_upper":bool(re.search(r"[A-Z]",value)),
            "has_lower":bool(re.search(r"[a-z]",value)), "has_digit":bool(re.search(r"\d",value)),
            "has_symbol":bool(re.search(r"[^A-Za-z0-9]",value))}
def main():
    p=argparse.ArgumentParser(); p.add_argument("file"); a=p.parse_args()
    for i,line in enumerate(Path(a.file).read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        checks=evaluate(line.strip()); print(f"Entry {i}: {sum(checks.values())}/{len(checks)} checks passed")
        print("  Missing:",", ".join(k for k,v in checks.items() if not v) or "none")
    print("Use fictional test data only; do not store real passwords in plaintext.")
if __name__=="__main__": main()
