# -*- coding: utf-8 -*-
"""Day6: 拉公开 API — https://api.github.com/zen"""
from datetime import datetime
from pathlib import Path
import urllib.request
import json

ROOT = Path(__file__).resolve().parent
LOG = ROOT / "api_log.txt"
API = "https://api.github.com/zen"


def fetch_zen() -> str:
    req = urllib.request.Request(
        API,
        headers={
            "User-Agent": "python-7days",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset)


def main():
    try:
        text = fetch_zen()
    except Exception as e:
        print(f"请求失败: {e}")
        return
    line = f"{datetime.now().isoformat(timespec='seconds')} | {text}"
    print(f"GitHub Zen -> {text}")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"已记入 {LOG.name}")


if __name__ == "__main__":
    main()
