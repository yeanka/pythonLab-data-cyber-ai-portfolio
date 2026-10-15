import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md"},
    "Spreadsheets": {".csv", ".xlsx", ".xls"},
    "Audio": {".mp3", ".wav", ".m4a"},
    "Video": {".mp4", ".mov", ".mkv"},
    "Archives": {".zip", ".tar", ".gz", ".7z"}
}
def category_for(path):
    for category, extensions in CATEGORIES.items():
        if path.suffix.lower() in extensions:
            return category
    return "Other"

def organize(folder, apply=False):
    folder = Path(folder).expanduser().resolve()
    if not folder.is_dir():
        raise ValueError("Please provide an existing directory.")
    actions = []
    for item in folder.iterdir():
        if not item.is_file():
            continue
        destination_dir = folder / category_for(item)
        destination = destination_dir / item.name
        if destination.exists():
            actions.append((item, None, "skipped: destination exists"))
            continue
        actions.append((item, destination, "move" if apply else "preview"))
        if apply:
            destination_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
    return actions

def main():
    parser = argparse.ArgumentParser(description="Sort files by extension; preview is default.")
    parser.add_argument("folder")
    parser.add_argument("--apply", action="store_true", help="perform file moves")
    args = parser.parse_args()
    try:
        for source, target, status in organize(args.folder, args.apply):
            print(f"{status}: {source.name}" + (f" -> {target.relative_to(source.parent)}" if target else ""))
        if not args.apply:
            print("Dry run only. Add --apply after reviewing the preview.")
    except ValueError as exc:
        parser.error(str(exc))
if __name__ == "__main__": main()
