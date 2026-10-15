# Python, Data Science, Cybersecurity & AI Portfolio

A GitHub-ready portfolio containing 16 practical projects across four tracks:
- Python programming for beginners (4)
- Data science for beginners (4)
- Cybersecurity (4)
- Artificial intelligence / machine learning (4)

## Important
These are learning and demonstration projects. Datasets are synthetic unless a project says otherwise. Security checks are defensive and intended for systems and data you own or are authorized to assess. Do not present example metrics as real-world results: run the projects, record your own results, and update your CV with verified numbers.

## Quick start
Requirements: Python 3.10 or later.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
```

Run individual projects from the repository root, for example:
```bash
python python-beginners/01-expense-tracker/main.py
python data-science/01-sales-analysis/analyze.py
python cybersecurity/01-auth-log-analyzer/analyze_logs.py cybersecurity/01-auth-log-analyzer/sample_auth.log
python ai-ml/01-spam-classifier/train.py
```

Some data science and AI projects use pandas, matplotlib, and scikit-learn. Install the root requirements before running them.

## Project index

### Python programming for beginners
1. Expense Tracker CLI — input validation, functions, JSON persistence.
2. Password Strength Checker — defensive password-quality feedback.
3. File Organizer — dry-run-first file categorization.
4. Quiz App — question bank, scoring, and JSON results.

### Data science for beginners
5. Sales Data Analysis — cleaning, KPIs, grouped summaries, chart output.
6. Hotel Occupancy Analysis — occupancy, room revenue, and monthly trend analysis using synthetic data.
7. Customer Churn Exploration — exploratory analysis and baseline churn model.
8. IT Support Ticket Analysis — resolution times, priorities, and category trends.

### Cybersecurity
9. Authentication Log Analyzer — summarizes failed logins and flags repeated failures.
10. File Integrity Monitor — SHA-256 baseline and change detection.
11. Phishing URL Heuristic Checker — explainable URL red flags, not a definitive verdict.
12. Password Audit — checks a local list against basic password policy without transmitting it.

### AI / machine learning
13. Spam Text Classifier — TF-IDF + logistic regression on a small illustrative dataset.
14. Network Intrusion Detection Demo — synthetic tabular traffic data and a baseline classifier.
15. Support Ticket Intent Classifier — text classification for routing support requests.
16. Explainable Customer Churn Model — baseline model with feature importance and evaluation.

## Suggested GitHub workflow
1. Create a public repository named `python-data-cyber-ai-portfolio`.
2. Upload this folder's contents.
3. Run each project and test locally.
4. Add screenshots or charts to each project's `images/` folder.
5. Replace generic descriptions with what you learned and the results you actually observed.
6. Pin 4–6 strongest repositories on your profile: auth log analyzer, intrusion detection demo, sales analysis, spam classifier, and file integrity monitor are good starting candidates.

## Resume and proposal guidance
Use the project-specific CV bullet templates in `CAREER_NOTES.md`. Keep claims factual: distinguish synthetic-data demonstrations from production deployments, and report only metrics you personally reproduce.
