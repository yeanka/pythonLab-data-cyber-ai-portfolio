import argparse
from urllib.parse import urlparse
SUSPICIOUS_WORDS={"login","verify","account","update","secure","password","wallet","confirm"}
def inspect_url(value):
    candidate=value if "://" in value else "http://"+value
    parsed=urlparse(candidate); host=(parsed.hostname or "").lower(); path=(parsed.path or "").lower()
    flags=[]
    if parsed.scheme != "https": flags.append("URL does not use HTTPS")
    if "@" in parsed.netloc: flags.append("Contains @ in the authority section")
    if host.startswith("xn--") or ".xn--" in host: flags.append("Contains an internationalized/punycode hostname")
    if host.count(".") >= 3: flags.append("Hostname has many subdomain levels")
    if any(word in (host+path) for word in SUSPICIOUS_WORDS): flags.append("Contains a word often seen in credential-themed links")
    if len(value) > 100: flags.append("Unusually long URL")
    if not host: flags.append("Could not parse a hostname")
    return {"host":host,"flags":flags,"score":len(flags)}
def main():
    p=argparse.ArgumentParser(); p.add_argument("url"); a=p.parse_args()
    result=inspect_url(a.url); print("Hostname:",result["host"]); print("Heuristic flags:",result["score"])
    for f in result["flags"]: print("-",f)
    print("Do not use this score alone to decide whether a URL is safe.")
if __name__=="__main__": main()
