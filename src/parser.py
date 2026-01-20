from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any, Optional


@dataclass
class Profile:
    username: str
    followers: int
    following: int
    posts: int
    category: str


def _to_int(value: str) -> int:
    """
    Convert numbers like '1,200', '12k', '3.5M' into int.
    """
    v = value.strip().lower().replace(",", "")
    if v.endswith("k"):
        return int(float(v[:-1]) * 1_000)
    if v.endswith("m"):
        return int(float(v[:-1]) * 1_000_000)
    if v.endswith("b"):
        return int(float(v[:-1]) * 1_000_000_000)
    return int(float(v))


def parse_raw_text(raw_text: str) -> List[Profile]:
    """
    Parse instagram-style raw text.
    Supported formats (flexible):
      username: xyz
      followers: 1200
      following: 350
      posts: 44
      category: Blogger

    Records separated by blank line.
    """
    blocks = re.split(r"\n\s*\n", raw_text.strip(), flags=re.MULTILINE)
    profiles: List[Profile] = []

    for b in blocks:
        lines = [ln.strip() for ln in b.splitlines() if ln.strip()]
        data: Dict[str, str] = {}
        for ln in lines:
            if ":" in ln:
                k, v = ln.split(":", 1)
                data[k.strip().lower()] = v.strip()
            elif "," in ln:
                # CSV-like line: username,followers,posts,following,category
                parts = [p.strip() for p in ln.split(",")]
                if len(parts) >= 5:
                    data["username"] = parts[0]
                    data["followers"] = parts[1]
                    data["posts"] = parts[2]
                    data["following"] = parts[3]
                    data["category"] = parts[4]

        if "username" not in data:
            continue

        profiles.append(
            Profile(
                username=data["username"],
                followers=_to_int(data.get("followers", "0")),
                following=_to_int(data.get("following", "0")),
                posts=_to_int(data.get("posts", "0")),
                category=data.get("category", "Unknown").title(),
            )
        )

    return profiles


def load_raw_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def profiles_to_dicts(profiles: List[Profile]) -> List[Dict[str, Any]]:
    return [asdict(p) for p in profiles]
