from __future__ import annotations

from pathlib import Path
from src.parser import load_raw_file, parse_raw_text, profiles_to_dicts
from src.utils import save_json, save_csv
from src.analysis import compute_summary


def main() -> None:
    data_dir = Path("data")
    raw_path = data_dir / "initialdata.txt"
    json_path = data_dir / "data.json"
    csv_path = data_dir / "finaldata.csv"

    if not raw_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {raw_path}")

    raw_text = load_raw_file(raw_path)
    profiles = parse_raw_text(raw_text)
    rows = profiles_to_dicts(profiles)

    save_json(json_path, rows)
    save_csv(csv_path, rows)

    summary = compute_summary(rows)

    print(f"Total profiles: {summary['total']}")
    if summary["top_followers"]:
        p = summary["top_followers"]
        print(f"Top by followers: {p['username']} ({p['followers']})")
    if summary["top_posts"]:
        p = summary["top_posts"]
        print(f"Top by posts: {p['username']} ({p['posts']})")
    if summary["top_following"]:
        p = summary["top_following"]
        print(f"Top by following: {p['username']} ({p['following']})")

    print("\nCategory distribution:")
    for k, v in sorted(summary["category_distribution"].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {k}: {v}")


if __name__ == "__main__":
    main()
