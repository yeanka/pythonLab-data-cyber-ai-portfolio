import json
from pathlib import Path
from datetime import date

DATA_FILE = Path("transactions.json")

def load_transactions():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("Could not read the data file; starting with an empty list.")
        return []

def save_transactions(items):
    DATA_FILE.write_text(json.dumps(items, indent=2), encoding="utf-8")

def add_transaction(items, kind, amount, category, note=""):
    if kind not in {"income", "expense"}:
        raise ValueError("kind must be income or expense")
    if amount <= 0:
        raise ValueError("amount must be greater than zero")
    items.append({"date": date.today().isoformat(), "type": kind,
                  "amount": round(float(amount), 2), "category": category.strip(),
                  "note": note.strip()})
    return items

def summary(items):
    income = sum(x["amount"] for x in items if x["type"] == "income")
    expenses = sum(x["amount"] for x in items if x["type"] == "expense")
    return {"income": round(income, 2), "expenses": round(expenses, 2),
            "balance": round(income - expenses, 2)}

def main():
    items = load_transactions()
    while True:
        print("\nExpense Tracker: [1] Add income [2] Add expense [3] List [4] Summary [q] Quit")
        choice = input("> ").strip().lower()
        if choice == "q":
            break
        if choice in {"1", "2"}:
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                note = input("Note (optional): ")
                add_transaction(items, "income" if choice == "1" else "expense",
                                amount, category, note)
                save_transactions(items)
                print("Saved.")
            except ValueError as exc:
                print(f"Invalid entry: {exc}")
        elif choice == "3":
            for i, item in enumerate(items, 1):
                print(f'{i}. {item["date"]} | {item["type"]} | {item["amount"]:.2f} | {item["category"]} | {item["note"]}')
            if not items:
                print("No transactions yet.")
        elif choice == "4":
            print(summary(items))
        else:
            print("Choose 1, 2, 3, 4, or q.")

if __name__ == "__main__":
    main()
