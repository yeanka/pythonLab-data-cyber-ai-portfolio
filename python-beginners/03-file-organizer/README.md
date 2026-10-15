# File Organizer (Dry Run First)
Sorts files in one chosen folder into categories by extension. It defaults to dry-run mode so you can review changes before moving anything.
## Run
`python main.py /path/to/folder` (preview only)
`python main.py /path/to/folder --apply` (actually moves files)
## Safety
Use a test folder first. It skips directories and avoids overwriting existing filenames.
