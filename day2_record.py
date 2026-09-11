# -*- coding: utf-8 -*-
"""Day2: 今日记录器 — 问两句，追加写入 records.md"""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RECORDS = ROOT / "records.md"

def main():
    today = date.today().isoformat()
    done = input("今天完成了什么？").strip() or "(空)"
    mood_raw = input("今天心情 1-5？").strip() or "3"
    try:
        mood = str(max(1, min(5, int(mood_raw))))
    except ValueError:
        mood = "3"

    block = f"""
## {today}

- 完成：{done}
- 心情：{mood}/5
"""
    with RECORDS.open("a", encoding="utf-8") as f:
        if RECORDS.stat().st_size == 0 if RECORDS.exists() else True:
            f.write("# records\n")
        f.write(block)

    print("\n今日存根:")
    print(block.strip())
    print(f"\n已写入 {RECORDS.name}")

if __name__ == "__main__":
    main()
