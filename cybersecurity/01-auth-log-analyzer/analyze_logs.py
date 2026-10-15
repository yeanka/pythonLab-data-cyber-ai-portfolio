import argparse
from collections import Counter
from pathlib import Path

def analyze(path, threshold=3):
    failed = Counter(); users = Counter(); successes = 0; malformed = 0
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        parts = line.strip().split(",")
        if len(parts) != 4 or parts[3] not in {"FAIL","SUCCESS"}:
            malformed += 1; continue
        _, ip, user, status = parts
        if status == "FAIL":
            failed[ip] += 1; users[user] += 1
        else: successes += 1
    return {"failed_by_ip":failed, "failed_by_user":users, "successes":successes,
            "malformed":malformed, "alerts":{ip:n for ip,n in failed.items() if n >= threshold}}

def main():
    p=argparse.ArgumentParser(); p.add_argument("logfile"); p.add_argument("--threshold",type=int,default=3)
    a=p.parse_args(); result=analyze(a.logfile,a.threshold)
    print("Failed attempts by IP:",dict(result["failed_by_ip"]))
    print("Failed attempts by username:",dict(result["failed_by_user"]))
    print("Successful logins:",result["successes"],"| malformed rows:",result["malformed"])
    print("Review these IPs (threshold-based, not proof of attack):",result["alerts"])
if __name__ == "__main__": main()
