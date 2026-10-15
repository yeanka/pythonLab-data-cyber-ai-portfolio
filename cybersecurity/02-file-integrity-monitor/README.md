# File Integrity Monitor
Creates a SHA-256 baseline for files in a directory and compares later snapshots to identify added, changed, and removed files.
## Run
`python monitor.py baseline /path/to/test-folder`
`python monitor.py check /path/to/test-folder`
Baseline is saved to `integrity_baseline.json` in the current directory. Use only folders you are authorized to monitor.
