import argparse, hashlib, json
from pathlib import Path
BASELINE=Path("integrity_baseline.json")
def digest(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(65536),b""): h.update(chunk)
    return h.hexdigest()
def snapshot(root):
    root=Path(root).resolve()
    if not root.is_dir(): raise ValueError("Folder does not exist.")
    result={}
    for p in root.rglob("*"):
        if p.is_file(): result[str(p.relative_to(root))]=digest(p)
    return result
def compare(old,new):
    return {"added":sorted(new.keys()-old.keys()),"removed":sorted(old.keys()-new.keys()),
            "changed":sorted(k for k in old.keys() & new.keys() if old[k]!=new[k])}
def main():
    p=argparse.ArgumentParser(); p.add_argument("mode",choices=["baseline","check"]); p.add_argument("folder")
    a=p.parse_args(); current=snapshot(a.folder)
    if a.mode=="baseline":
        BASELINE.write_text(json.dumps(current,indent=2),encoding="utf-8"); print(f"Baseline saved for {len(current)} files.")
    else:
        if not BASELINE.exists(): p.error("No baseline found; run baseline first.")
        old=json.loads(BASELINE.read_text(encoding="utf-8")); print(json.dumps(compare(old,current),indent=2))
if __name__=="__main__": main()
