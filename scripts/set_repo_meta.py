# -*- coding: utf-8 -*-
"""set_repo_meta.py — 设置 GitHub 仓库的双语描述、主页与 topics。

Token 从 git credential helper 读取，不落盘、不打印。
用法：python scripts/set_repo_meta.py
"""
import os
import subprocess

import requests

REPO = "lyp0746/interpretation-tradeoff"
GIT = os.environ.get("GIT_BIN", r"D:\Git\cmd\git.exe")

DESCRIPTION = (
    "《诠释的权衡》——为什么历史学永远有争论：历史学中的持久争论，大多不是谁对谁错，"
    "而是不同诠释者在同一张价目表上选择了不同的位置。用四把工具（容量级联、C-A-T 三角、"
    "时间错配、区分与边界）诊断六场深度争论与三十场快速争论，附可证伪登记簿。 "
    "The Interpretation Tradeoff — why historiography never settles: diagnosing the capacity, "
    "tradeoff, time, and boundary of interpretation. Text CC BY 4.0; code MIT."
)
HOMEPAGE = "https://github.com/lyp0746/interpretation-tradeoff"
TOPICS = [
    "historiography", "philosophy-of-history", "interpretation",
    "hermeneutics", "complex-systems", "knowledge-evolution",
    "impossibility-triangle", "epistemology", "evidence-grading",
    "cc-by-4-0",
]


def get_token():
    out = subprocess.run([GIT, "credential", "fill"],
                         input="protocol=https\nhost=github.com\n\n",
                         capture_output=True, text=True,
                         env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    for line in out.stdout.splitlines():
        if line.startswith("password="):
            return line[len("password="):].strip()
    raise SystemExit("未能从 git credential helper 取得 token")


def main():
    tok = get_token()
    h = {"Authorization": f"token {tok}", "Accept": "application/vnd.github+json",
         "User-Agent": "book-meta"}
    r = requests.patch(f"https://api.github.com/repos/{REPO}", headers=h,
                       json={"description": DESCRIPTION, "homepage": HOMEPAGE,
                             "has_issues": True, "has_wiki": False}, timeout=60)
    print("repo PATCH:", r.status_code)
    if r.status_code >= 300:
        print(r.text[:400])
    t = requests.put(f"https://api.github.com/repos/{REPO}/topics", headers=h,
                     json={"names": TOPICS}, timeout=60)
    print("topics PUT:", t.status_code)
    if t.status_code >= 300:
        print(t.text[:400])
    else:
        print("topics:", ", ".join(t.json().get("names", [])))


if __name__ == "__main__":
    main()
