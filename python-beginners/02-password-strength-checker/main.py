import getpass
import re

def assess_password(password):
    checks = {
        "at least 12 characters": len(password) >= 12,
        "lowercase letter": bool(re.search(r"[a-z]", password)),
        "uppercase letter": bool(re.search(r"[A-Z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "symbol": bool(re.search(r"[^A-Za-z0-9]", password)),
        "not a common obvious password": password.lower() not in {
            "password", "password123", "123456789", "qwerty123"
        }
    }
    score = sum(checks.values())
    level = "weak" if score <= 2 else "moderate" if score <= 4 else "stronger"
    return {"score": score, "level": level, "checks": checks}

def main():
    value = getpass.getpass("Enter a password to assess (do not use a real password): ")
    result = assess_password(value)
    print(f"Assessment: {result['level']} ({result['score']}/6 checks)")
    for label, passed in result["checks"].items():
        print(f"[{'x' if passed else ' '}] {label}")
    print("Use a unique password and a password manager; length matters.")

if __name__ == "__main__":
    main()
