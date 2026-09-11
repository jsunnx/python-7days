# -*- coding: utf-8 -*-
"""Day3: 批量重命名 — 给文件夹内文件加日期前缀，默认不执行"""
from datetime import date
from pathlib import Path
import sys

def preview_names(folder: Path, prefix: str):
    old_new = []
    for p in folder.iterdir():
        if p.is_file() and not p.name.startswith(prefix):
            old_new.append((p, p.with_name(prefix + p.name)))
    return old_new

def main():
    folder = input("文件夹路径: ").strip().strip('"')
    if not folder:
        print("路径为空，退出")
        return
    path = Path(folder).expanduser()
    if not path.is_dir():
        print("不是有效文件夹")
        return

    prefix = date.today().strftime("%Y%m%d_")
    pairs = preview_names(path, prefix)
    if not pairs:
        print("没有需要重命名的文件")
        return

    print(f"将添加前缀: {prefix}")
    for src, dst in pairs:
        print(f"  {src.name}  ->  {dst.name}")
    if len(sys.argv) > 1 and sys.argv[1] == "--yes":
        answer = "y"
    else:
        answer = input("确认执行? y/N: ").strip().lower()
    if answer != "y":
        print("已取消")
        return

    ok = 0
    for src, dst in pairs:
        if dst.exists():
            print(f"跳过(目标已存在): {src.name}")
            continue
        src.rename(dst)
        ok += 1
        print(f"完成: {dst.name}")
    print(f"共改名 {ok} 个文件")

if __name__ == "__main__":
    main()
