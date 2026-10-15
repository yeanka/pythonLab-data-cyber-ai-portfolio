import json
from datetime import datetime
from pathlib import Path

QUESTIONS = [
    {"question": "Which type stores key-value pairs?", "options": ["list", "dict", "tuple"], "answer": "B"},
    {"question": "Which keyword defines a function?", "options": ["func", "define", "def"], "answer": "C"},
    {"question": "Which structure repeats while a condition is true?", "options": ["while loop", "import", "return"], "answer": "A"},
    {"question": "Which module handles JSON in Python?", "options": ["json", "math", "random"], "answer": "A"},
]
def run_quiz(questions):
    score = 0
    for number, q in enumerate(questions, 1):
        print(f"\n{number}. {q['question']}")
        for letter, option in zip("ABC", q["options"]):
            print(f"  {letter}. {option}")
        if input("Answer: ").strip().upper() == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Answer: {q['answer']}")
    return score

def main():
    score = run_quiz(QUESTIONS)
    result = {"completed_at": datetime.now().isoformat(timespec="seconds"),
              "score": score, "total": len(QUESTIONS)}
    Path("quiz_result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Final score: {score}/{len(QUESTIONS)}. Saved to quiz_result.json")
if __name__ == "__main__": main()
