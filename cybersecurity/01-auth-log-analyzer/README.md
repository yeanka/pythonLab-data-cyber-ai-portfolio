# Authentication Log Analyzer
A defensive parser for a simple normalized authentication-log format. It reports failed logins by source IP and flags repeated failures.
## Run
`python analyze_logs.py sample_auth.log`
## Input format
`YYYY-MM-DD HH:MM:SS,IP,username,FAIL|SUCCESS`
This is a demo parser, not a universal parser for every operating system log.
