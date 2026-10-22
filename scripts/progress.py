#!/usr/bin/env python3
"""
Update progress in README.md and in every week folder's README.

Run from the repo root before you commit:
    python scripts/progress.py

It finds every .java file, reads its Plan ID (from the header comment,
or from the file name like A324_TwoSum.java), and marks those questions
as solved. Files in revision/ count as a redo, not a new solve.
Only the Python standard library is used.
"""
import json
import re
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = json.loads((ROOT / "scripts" / "plan.json").read_text(encoding="utf-8"))
QUESTIONS = PLAN["questions"]          # id -> question info
LINK_NAMES = {"LC": "LeetCode", "TUF": "Striver", "GFG": "GFG", "YT": "Video", "WEB": "Practice"}

ID_IN_HEADER = re.compile(r"Plan ID\s*:\s*([A-Za-z0-9_]+)")
ID_IN_NAME = re.compile(r"^([A-Z][A-Za-z0-9]*)_")


def find_id(path: Path):
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:1500]
    except OSError:
        head = ""
    m = ID_IN_HEADER.search(head)
    if m and m.group(1) in QUESTIONS:
        return m.group(1)
    m = ID_IN_NAME.match(path.name)
    if m and m.group(1) in QUESTIONS:
        return m.group(1)
    return None


def scan():
    solved, redone, unknown = {}, set(), []
    for f in sorted(ROOT.rglob("*.java")):
        rel = f.relative_to(ROOT)
        if rel.parts[0].startswith("."):
            continue
        qid = find_id(f)
        if not qid:
            unknown.append(str(rel))
            continue
        if rel.parts[0] == "revision":
            redone.add(qid)
        else:
            solved.setdefault(qid, str(rel).replace("\\", "/"))
    return solved, redone, unknown


def streak():
    """Days in a row (ending today or yesterday) with at least one commit."""
    try:
        out = subprocess.run(["git", "log", "--format=%ad", "--date=short"], cwd=ROOT,
                             capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return 0, 0
    days = {datetime.strptime(d, "%Y-%m-%d").date() for d in out.split() if d}
    if not days:
        return 0, 0
    cur, n = date.today(), 0
    if cur not in days:
        cur -= timedelta(days=1)
    while cur in days:
        n += 1
        cur -= timedelta(days=1)
    return n, len(days)


def bar(done, total, width=20):
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def links_md(q):
    return " · ".join(f"[{LINK_NAMES.get(k, k)}]({u})" for k, _, u in q["links"]) or "IDE"


def write_week_readmes(solved, redone):
    for folder in PLAN["folders"]:
        ids = [i for i in folder["ids"] if i in QUESTIONS]
        n = sum(1 for i in ids if i in solved)
        lines = [f"# {folder['title']}", ""]
        if folder.get("goal"):
            lines += [f"**Goal:** {folder['goal']}", ""]
        lines += [f"**Progress:** {n} / {len(ids)}  `{bar(n, len(ids))}`", "",
                  "| | ID | Problem | Level | Source | When | Links |",
                  "|---|---|---|---|---|---|---|"]
        for i in ids:
            q = QUESTIONS[i]
            mark = "✅" if i in solved else "⬜"
            name = q["name"] + (" ★" if q["star"] else "")
            if i in solved:
                name = f"[{name}]({Path(solved[i]).name})" if Path(solved[i]).parent.as_posix() == folder["path"] else f"[{name}](/{solved[i]})"
            if i in redone:
                name += " 🔁"
            lines.append(f"| {mark} | `{i}` | {name} | {q['lvl']} | {' + '.join(q['tags'])} | {q['when']} | {links_md(q)} |")
        lines += ["", "✅ solved · ⬜ pending · ★ interview favourite · 🔁 redone in `revision/`", ""]
        p = ROOT / folder["path"] / "README.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(lines), encoding="utf-8")


def write_main_readme(solved, redone):
    def count(pred):
        ids = [i for i, q in QUESTIONS.items() if pred(q)]
        return sum(1 for i in ids if i in solved), len(ids)

    s_days, active = streak()
    rows = ["| Track | Done | Total | Progress |", "|---|---:|---:|---|"]
    for label, pred in [
        ("Plan 1 (core, Oct–Jan)", lambda q: q["plan"] == "P1"),
        ("Plan 2 (advanced)", lambda q: q["plan"] == "P2"),
        ("Striver A2Z questions", lambda q: "Striver" in q["tags"]),
        ("Love Babbar 450 questions", lambda q: "Babbar" in q["tags"]),
        ("★ Interview favourites", lambda q: q["star"]),
    ]:
        d, t = count(pred)
        rows.append(f"| {label} | {d} | {t} | `{bar(d, t)}` |")
    lvl = {L: count(lambda q, L=L: q["lvl"] == L) for L in ("Basic", "Core", "Pro")}

    wk = ["| Folder | Topic | Done |", "|---|---|---:|"]
    for folder in PLAN["folders"]:
        if not folder["path"].startswith("W"):
            continue
        ids = folder["ids"]
        d = sum(1 for i in ids if i in solved)
        wk.append(f"| [`{folder['path']}`]({folder['path']}/) | {folder['topic']} | {d} / {len(ids)} |")
    p2_done = sum(1 for i, q in QUESTIONS.items() if q["plan"] == "P2" and i in solved)

    block = "\n".join([
        f"**{len(solved)} problem{'' if len(solved) == 1 else 's'} solved** · Basic {lvl['Basic'][0]} · Core {lvl['Core'][0]} · Pro {lvl['Pro'][0]}"
        f" · {len(redone)} redone · 🔥 {s_days}-day streak · {active} active days",
        "",
        *rows,
        "",
        "<details><summary>Week by week</summary>",
        "",
        *wk,
        f"| [`plan2/`](plan2/) | Advanced topics (after Plan 1) | {p2_done} / {sum(1 for q in QUESTIONS.values() if q['plan'] == 'P2')} |",
        "",
        "</details>",
        "",
        f"<sub>Updated {date.today():%d %b %Y} by `scripts/progress.py`</sub>",
    ])
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    text = re.sub(r"<!-- PROGRESS:START -->.*<!-- PROGRESS:END -->",
                  "<!-- PROGRESS:START -->\n" + block + "\n<!-- PROGRESS:END -->", text, flags=re.S)
    readme.write_text(text, encoding="utf-8")


def main():
    solved, redone, unknown = scan()
    write_week_readmes(solved, redone)
    write_main_readme(solved, redone)
    print(f"Solved: {len(solved)} · Redone: {len(redone)}")
    if unknown:
        print("Plan ID nahi mila in files (header mein 'Plan ID : A324' ya naam A324_... rakho):")
        for u in unknown:
            print("  -", u)


if __name__ == "__main__":
    main()
