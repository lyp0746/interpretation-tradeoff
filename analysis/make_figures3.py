# -*- coding: utf-8 -*-
"""make_figures3.py — 第三批正文插图（《诠释的权衡》）。

图 14.1 唐宋变革三派在坐标上的位置
图 20.2 框架适用性矩阵
"""
import math
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg")
BLUE, RED, GOLD, GREEN, GREY = "#3a6ea5", "#c94f4f", "#b8862f", "#009E73", "#666666"
INK, DIM = "#222222", "#555555"


def _wrap(body, w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">\n'
            f'<style>text{{font-family:"Microsoft YaHei","SimHei",Arial,sans-serif;}}'
            f'.t{{font-size:17px;fill:{INK};font-weight:700;}}'
            f'.b{{font-size:14px;fill:{INK};font-weight:700;}}'
            f'.s{{font-size:12px;fill:{DIM};}}'
            f'.cap{{font-size:13px;fill:{DIM};}}</style>\n'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff"/>\n'
            f'{body}\n</svg>\n')


def fig_tangsong():
    w, h = 780, 470
    cx, cy, R = 390, 250, 165
    verts = {
        "C": (cx + R * math.cos(math.radians(-90)), cy + R * math.sin(math.radians(-90))),
        "A": (cx + R * math.cos(math.radians(150)), cy + R * math.sin(math.radians(150))),
        "T": (cx + R * math.cos(math.radians(30)), cy + R * math.sin(math.radians(30))),
    }
    labels = {"C": ("C 完备", "唐宋变革论"), "A": ("A 可组合", "多维转变论"), "T": ("T 传递", "过渡与延续论")}
    cols = {"C": BLUE, "A": GREEN, "T": GOLD}
    b = [f'<text x="{cx}" y="30" class="t" text-anchor="middle">唐宋变革三派在坐标上的位置</text>']
    tri = " ".join(f"{x:.1f},{y:.1f}" for x, y in (verts["C"], verts["A"], verts["T"]))
    b.append(f'<polygon points="{tri}" fill="none" stroke="{GREY}" stroke-width="1.6"/>')
    for key, (x, y) in verts.items():
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{cols[key]}"/>')
        dx = {"C": 0, "A": -70, "T": 70}[key]
        dy = {"C": -42, "A": 30, "T": 30}[key]
        b.append(f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" class="b" fill="{cols[key]}" text-anchor="middle">{labels[key][0]}</text>')
        b.append(f'<text x="{x+dx:.0f}" y="{y+dy+18:.0f}" class="s" text-anchor="middle">{labels[key][1]}</text>')
        b.append(f'<text x="{x+dx:.0f}" y="{y+dy+36:.0f}" class="s" fill="{cols[key]}" text-anchor="middle">让出 {[k for k in "CAT" if k != key][0]}</text>')
    b.append(f'<text x="{cx}" y="{cy+4}" class="s" text-anchor="middle">预先登记：A / B / C</text>')
    b.append(f'<text x="{cx}" y="{cy+24}" class="s" text-anchor="middle">结果：A 带 B 的尾巴</text>')
    b.append(f'<text x="{cx}" y="452" class="cap" text-anchor="middle">三角形状重现，但 C 的读法变模糊——“分期标准”本身成为分歧的核心</text>')
    return _wrap("\n".join(b), w, h)


def fig_applicability():
    w, h = 880, 340
    b = [f'<text x="{w/2}" y="30" class="t" text-anchor="middle">框架适用性矩阵</text>']
    rows = [("适用于西方现代史学传统", "✔", GREEN, "六场诊断"),
            ("适用于同一传统内的不同学科", "◐", GOLD, "第 18 章"),
            ("适用于非西方学术传统", "◐", GOLD, "唐宋变革（A 带 B）"),
            ("适用于不以因果组织的传统", "✘", RED, "警告 14.1"),
            ("适用于质性 / 建模的权衡差异", "✘", GREY, "仅论证，无检验")]
    y0 = 62
    for i, (cond, mark, col, basis) in enumerate(rows):
        y = y0 + i * 48
        b.append(f'<rect x="60" y="{y}" width="520" height="38" rx="6" fill="{col}" fill-opacity="0.08" stroke="{col}" stroke-width="1.2"/>')
        b.append(f'<text x="76" y="{y+25}" class="b">{cond}</text>')
        b.append(f'<circle cx="620" cy="{y+19}" r="15" fill="{col}" fill-opacity="0.15" stroke="{col}" stroke-width="1.4"/>')
        b.append(f'<text x="620" y="{y+25}" class="b" fill="{col}" text-anchor="middle">{mark}</text>')
        b.append(f'<text x="650" y="{y+25}" class="s">{basis}</text>')
    b.append(f'<line x1="60" y1="{y0+5*48+6}" x2="820" y2="{y0+5*48+6}" stroke="{GREY}" stroke-width="1" opacity="0.5"/>')
    b.append(f'<text x="{w/2}" y="{y0+5*48+30}" class="cap" text-anchor="middle">✔ 基本成立 · ◐ 部分支持 · ✘ 未验证——越往下证据越薄，正是可接手之处（O32、O9）</text>')
    return _wrap("\n".join(b), w, h)


def main():
    os.makedirs(OUT, exist_ok=True)
    figs = {
        "fig16-tangsong.svg": fig_tangsong(),
        "fig17-applicability.svg": fig_applicability(),
    }
    for name, svg in figs.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
