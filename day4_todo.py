# -*- coding: utf-8 -*-
"""Day4: JSON 清单 CLI — add / list / done / quit"""
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
TODO_FILE = ROOT / "todo.json"

def load() -> list:
    if not TODO_FILE.exists():
        return []
    with TODO_FILE.open(encoding="utf-8") as f:
        return json.load(f)

def save(items: list) -> None:
    with TODO_FILE.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def cmd_add(items, text):
    items.append({
        "text": text,
        "done": False,
        "created": datetime.now().isoformat(timespec="seconds"),
    })
    save(items)
    print(f"+ {text}")

def cmd_list(items):
    if not items:
        print("(空)")
        return
    for i, it in enumerate(items, 1):
        mark = "x" if it.get("done") else " "
        print(f"[{mark}] {i}. {it['text']}")

def cmd_done(items, n):
    if not n.isdigit() or not (1 <= int(n) <= len(items)):
        print("序号无效")
        return
    items[int(n) - 1]["done"] = True
    save(items)
    print(f"done: {items[int(n) - 1]['text']}")

def main():
    print("命令: add <内容> | list | done <序号> | quit")
    while True:
        raw = input("> ").strip()
        if raw in {"q", "quit", "exit"}:
            break
        if raw == "list":
            cmd_list(load())
            continue
        if raw.startswith("done "):
            cmd_done(load(), raw[5:].strip())
            continue
        if raw.startswith("add "):
            cmd_add(load(), raw[4:].strip())
            continue
        if raw:
            print("不认识的命令")
    print("bye")

if __name__ == "__main__":
    main()
