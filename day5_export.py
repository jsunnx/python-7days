# -*- coding: utf-8 -*-
"""Day5: 函数化清单 + 导出日报"""
import json
from pathlib import Path
from datetime import datetime, date

ROOT = Path(__file__).resolve().parent
TODO_FILE = ROOT / "todo.json"
REPORT_FILE = ROOT / "daily_report.md"


def load_tasks() -> list:
    if not TODO_FILE.exists():
        return []
    with TODO_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def save_tasks(items: list) -> None:
    with TODO_FILE.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def add_task(text: str) -> None:
    items = load_tasks()
    items.append({
        "text": text,
        "done": False,
        "created": datetime.now().isoformat(timespec="seconds"),
    })
    save_tasks(items)
    print(f"+ {text}")


def list_tasks() -> list:
    items = load_tasks()
    if not items:
        print("(空)")
        return items
    for i, it in enumerate(items, 1):
        mark = "x" if it.get("done") else " "
        print(f"[{mark}] {i}. {it['text']}")
    return items


def complete_task(n: str) -> None:
    items = load_tasks()
    if not n.isdigit() or not (1 <= int(n) <= len(items)):
        print("序号无效")
        return
    items[int(n) - 1]["done"] = True
    save_tasks(items)
    print(f"done: {items[int(n) - 1]['text']}")


def export_report() -> Path:
    items = load_tasks()
    today = date.today().isoformat()
    done = sum(1 for it in items if it.get("done"))
    lines = [
        f"# {today} 日报",
        "",
        f"- 任务总数：{len(items)}",
        f"- 已完成：{done}",
        f"- 未完成：{len(items) - done}",
        "",
        "## 任务",
        "",
    ]
    if not items:
        lines.append("(今天没有任务)")
    else:
        for it in items:
            box = "x" if it.get("done") else " "
            lines.append(f"- [{box}] {it['text']}")
    lines.append("")
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"已导出 -> {REPORT_FILE.name}")
    return REPORT_FILE


def main():
    print("命令: add <内容> | list | done <序号> | export | quit")
    while True:
        raw = input("> ").strip()
        if raw in {"q", "quit", "exit"}:
            break
        if raw == "list":
            list_tasks()
            continue
        if raw == "export":
            export_report()
            continue
        if raw.startswith("done "):
            complete_task(raw[5:].strip())
            continue
        if raw.startswith("add "):
            add_task(raw[4:].strip())
            continue
        if raw:
            print("不认识的命令")
    print("bye")


if __name__ == "__main__":
    main()
