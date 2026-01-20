from __future__ import annotations

from collections import Counter
from typing import Dict, Any, List


def compute_summary(profiles: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Returns:
      total, top_followers, top_posts, top_following, category_distribution
    """
    if not profiles:
        return {
            "total": 0,
            "top_followers": None,
            "top_posts": None,
            "top_following": None,
            "category_distribution": {},
        }

    top_followers = max(profiles, key=lambda x: x.get("followers", 0))
    top_posts = max(profiles, key=lambda x: x.get("posts", 0))
    top_following = max(profiles, key=lambda x: x.get("following", 0))

    cats = [p.get("category", "Unknown") for p in profiles]
    dist = dict(Counter(cats))

    return {
        "total": len(profiles),
        "top_followers": top_followers,
        "top_posts": top_posts,
        "top_following": top_following,
        "category_distribution": dist,
    }
