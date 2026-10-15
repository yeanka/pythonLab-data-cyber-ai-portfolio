# Network Intrusion Detection Baseline (Synthetic Data)
Trains a baseline classifier on generated traffic-like features to demonstrate the ML workflow.
## Run
`python train.py`
## Important
The CSV is synthetic and deliberately simplified. This is not a validated IDS, and its scores must not be used to secure a live network. For a serious project, repeat the workflow on a documented dataset such as CICIDS2017 with a careful train/test split and leakage review.
