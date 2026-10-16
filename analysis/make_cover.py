# -*- coding: utf-8 -*-
"""make_cover.py — 生成《诠释的权衡》满版封面 SVG（A4 比例 1000×1414）。

系列统一版式：暗色渐变、顶部金线、同一标题/副标题/作者/英文行的位置与字号；
中心线描母题因书而异——本书为“三角之中看四层”：
C-A-T 三角为外框，内部四层水平线代表容量级联（观察/推理/诠释/因果），
一条斜向的“目光”穿过三角，表示诠释者对被诠释对象的注视。
"""
import math
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg", "cover.svg")


def build():
    W, H = 1000, 1414
    ink = "#e8e6df"
    dim = "#9aa0a6"
    layers = []
    cx, cy = 500, 640
    R = 240
    verts = {
        "C": (cx + R * math.cos(math.radians(-90)), cy + R * math.sin(math.radians(-90))),
        "A": (cx + R * math.cos(math.radians(150)), cy + R * math.sin(math.radians(150))),
        "T": (cx + R * math.cos(math.radians(30)), cy + R * math.sin(math.radians(30))),
    }
    cols = {"C": "#3a6ea5", "A": "#009E73", "T": "#b8862f"}

    # 外层三角
    tri = " ".join(f"{x:.1f},{y:.1f}" for x, y in
                   (verts["C"], verts["A"], verts["T"]))
    layers.append(f'<polygon points="{tri}" fill="none" stroke="#8fa0b5" '
                  f'stroke-width="1.6" opacity="0.75"/>')

    # 内部四层水平线（容量级联 L1-L4）
    for i, (frac, op) in enumerate([(0.18, 0.20), (0.38, 0.28), (0.58, 0.36), (0.74, 0.44)]):
        y = cy - R * 0.72 + frac * R * 1.5
        half = R * (0.30 + 0.16 * i)
        layers.append(f'<line x1="{cx-half:.1f}" y1="{y:.1f}" x2="{cx+half:.1f}" y2="{y:.1f}" '
                      f'stroke="#c9cfd8" stroke-width="1.2" opacity="{op:.2f}"/>')

    # 斜向“目光”：两条平行弧线穿过三角
    layers.append(f'<path d="M {cx-300} {cy+180} Q {cx} {cy-160} {cx+300} {cy-120}" '
                  f'fill="none" stroke="{cols["C"]}" stroke-width="2.2" opacity="0.65"/>')
    layers.append(f'<path d="M {cx-300} {cy+225} Q {cx} {cy-115} {cx+300} {cy-75}" '
                  f'fill="none" stroke="{cols["T"]}" stroke-width="2.2" opacity="0.65"/>')

    # 三条边（虚线，表示取舍）
    for a, b in (("C", "A"), ("A", "T"), ("T", "C")):
        (x1, y1), (x2, y2) = verts[a], verts[b]
        layers.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                      f'stroke="#c9c9c9" stroke-width="1.4" opacity="0.45" stroke-dasharray="7,6"/>')

    # 三顶点
    for key, (x, y) in verts.items():
        layers.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{cols[key]}" opacity="0.9"/>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#0e1117"/><stop offset="0.55" stop-color="#151a23"/>
<stop offset="1" stop-color="#0b0e14"/>
</linearGradient>
</defs>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bg)"/>
<rect x="0" y="0" width="{W}" height="8" fill="#b8862f" opacity="0.85"/>
{chr(10).join(layers)}
<style>
text{{font-family:'Microsoft YaHei','SimHei',Arial,sans-serif;}}
.ttl{{font-size:108px;font-weight:700;letter-spacing:12px;fill:{ink};}}
.sub{{font-size:27px;fill:{dim};letter-spacing:2px;}}
.eng{{font-size:21px;fill:{dim};letter-spacing:1px;}}
.au{{font-size:30px;fill:{ink};letter-spacing:2px;}}
.rule{{stroke:{dim};stroke-width:1;opacity:0.6;}}
.lab{{font-size:24px;font-weight:700;}}
</style>
<text x="80" y="176" class="eng">THE INTERPRETATION TRADEOFF</text>
<text x="80" y="300" class="ttl">诠释的权衡</text>
<line x1="84" y1="344" x2="700" y2="344" class="rule"/>
<text x="84" y="396" class="sub">为什么历史学永远有争论</text>
<text x="84" y="440" class="sub">——诠释的容量、权衡、时间与边界</text>
<text x="{verts['C'][0]-14:.0f}" y="{verts['C'][1]-22:.0f}" class="lab" fill="{cols['C']}" text-anchor="middle">C</text>
<text x="{verts['A'][0]-24:.0f}" y="{verts['A'][1]+34:.0f}" class="lab" fill="{cols['A']}" text-anchor="middle">A</text>
<text x="{verts['T'][0]+24:.0f}" y="{verts['T'][1]+34:.0f}" class="lab" fill="{cols['T']}" text-anchor="middle">T</text>
<text x="80" y="1180" class="au">李毅芃　著</text>
<text x="80" y="1232" class="eng">Diagnosing Interpretation: Capacity, Tradeoff, Time, Boundary</text>
<text x="80" y="1274" class="eng">史学理论专著 · 2026</text>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", OUT)


if __name__ == "__main__":
    build()
