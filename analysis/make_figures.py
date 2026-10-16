# -*- coding: utf-8 -*-
"""make_figures.py — 生成《诠释的权衡》正文插图（SVG，house palette）。

图 0.1  四把工具与诊断流程
图 2.1  容量级联的四层
图 4.1  C-A-T 三角与三种史学风格
图 6.1  四个帝国的“衰落期”长度（对数刻度）
图 13.1 历史学范式转移的轨迹
"""
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg")

BLUE, RED, GOLD, GREEN, GREY = "#3a6ea5", "#c94f4f", "#b8862f", "#009E73", "#666666"
INK, DIM = "#222222", "#555555"


def _wrap(body, w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">\n'
            f'<style>text{{font-family:"Microsoft YaHei","SimHei",Arial,sans-serif;}}'
            f'.t{{font-size:18px;fill:{INK};}}.s{{font-size:14px;fill:{DIM};}}'
            f'.b{{font-size:15px;font-weight:700;}}.cap{{font-size:16px;fill:{DIM};}}</style>\n'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff"/>\n'
            f'{body}\n</svg>\n')


def fig_tools():
    w, h = 900, 340
    b = []
    tools = [
        ("容量级联", "诠释者先压缩", BLUE),
        ("C-A-T 三角", "三选二的价目表", GREEN),
        ("时间错配", "尺度决定分辨率", GOLD),
        ("区分与边界", "划界与失效标记", RED),
    ]
    for i, (name, sub, col) in enumerate(tools):
        x = 40 + i * 200
        b.append(f'<rect x="{x}" y="60" width="170" height="80" rx="8" '
                 f'fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1.6"/>')
        b.append(f'<text x="{x+85}" y="94" class="b" fill="{col}" text-anchor="middle">{name}</text>')
        b.append(f'<text x="{x+85}" y="120" class="s" text-anchor="middle">{sub}</text>')
        b.append(f'<line x1="{x+85}" y1="140" x2="{x+85}" y2="190" stroke="{col}" stroke-width="1.4"/>')
    b.append(f'<rect x="200" y="190" width="500" height="56" rx="8" fill="{GREY}" fill-opacity="0.10" '
             f'stroke="{GREY}" stroke-width="1.4"/>')
    b.append(f'<text x="450" y="214" class="b" text-anchor="middle">诠释诊断五步</text>')
    b.append(f'<text x="450" y="236" class="s" text-anchor="middle">容量 → 权衡 → 时间 → 区分 → 复核</text>')
    b.append(f'<line x1="450" y1="246" x2="450" y2="280" stroke="{GREY}" stroke-width="1.4"/>')
    b.append(f'<text x="450" y="302" class="cap" text-anchor="middle">输出：一场争论的坐标，而非胜负</text>')
    b.append(f'<text x="450" y="34" class="t" text-anchor="middle">四把工具，一条链</text>')
    return _wrap("\n".join(b), w, h)


def fig_cascade():
    w, h = 820, 360
    b = []
    layers = [
        ("L1 观察", "文献说了什么", 0.95, BLUE),
        ("L2 推理", "它意味着什么", 0.70, GREEN),
        ("L3 诠释", "意图与时代逻辑", 0.40, GOLD),
        ("L4 因果", "它导致了什么", 0.15, RED),
    ]
    b.append(f'<text x="410" y="32" class="t" text-anchor="middle">容量级联：四层的可核对性递减</text>')
    for i, (name, sub, val, col) in enumerate(layers):
        y = 66 + i * 68
        b.append(f'<rect x="60" y="{y}" width="210" height="50" rx="6" '
                 f'fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1.4"/>')
        b.append(f'<text x="76" y="{y+22}" class="b" fill="{col}">{name}</text>')
        b.append(f'<text x="76" y="{y+41}" class="s">{sub}</text>')
        bw = 400 * val
        b.append(f'<rect x="300" y="{y+10}" width="{bw:.0f}" height="30" rx="4" fill="{col}" fill-opacity="0.55"/>')
        b.append(f'<text x="{300+bw+10:.0f}" y="{y+30}" class="s">{int(val*100)}%</text>')
    b.append(f'<text x="560" y="200" class="s" transform="rotate(90 560 200)">解释自由度递增 →</text>')
    b.append(f'<text x="160" y="342" class="cap" text-anchor="middle">越往上，可核对性越低；用 L1 的语气说 L4 的话，就是错配</text>')
    return _wrap("\n".join(b), w, h)


def fig_triangle():
    import math
    w, h = 760, 470
    b = []
    cx, cy, R = 380, 250, 170
    verts = {
        "C": (cx + R * math.cos(math.radians(-90)), cy + R * math.sin(math.radians(-90))),
        "A": (cx + R * math.cos(math.radians(150)), cy + R * math.sin(math.radians(150))),
        "T": (cx + R * math.cos(math.radians(30)), cy + R * math.sin(math.radians(30))),
    }
    labels = {"C": ("C 完备", "清晰论"), "A": ("A 可组合", "平衡论"), "T": ("T 传递", "细节论")}
    cols = {"C": BLUE, "A": GREEN, "T": GOLD}
    tri = " ".join(f"{x:.1f},{y:.1f}" for x, y in (verts["C"], verts["A"], verts["T"]))
    b.append(f'<polygon points="{tri}" fill="none" stroke="{GREY}" stroke-width="1.6"/>')
    for key, (x, y) in verts.items():
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{cols[key]}"/>')
        dx = {"C": 0, "A": -90, "T": 90}[key]
        dy = {"C": -40, "A": 34, "T": 34}[key]
        b.append(f'<text x="{x+dx:.0f}" y="{y+dy:.0f}" class="b" fill="{cols[key]}" '
                 f'text-anchor="middle">{labels[key][0]}</text>')
        b.append(f'<text x="{x+dx:.0f}" y="{y+dy+20:.0f}" class="s" text-anchor="middle">{labels[key][1]}</text>')
        b.append(f'<text x="{x+dx:.0f}" y="{y+dy+38:.0f}" class="s" fill="{cols[key]}" '
                 f'text-anchor="middle">让出 {[k for k in "CAT" if k!=key][0]}</text>')
    b.append(f'<text x="{cx}" y="{cy+6}" class="s" text-anchor="middle">至多同时满格两个</text>')
    b.append(f'<text x="{cx}" y="34" class="t" text-anchor="middle">C-A-T 三角的史学版本</text>')
    b.append(f'<text x="{cx}" y="452" class="cap" text-anchor="middle">三方不是在争谁对，而是在争用哪把尺子</text>')
    return _wrap("\n".join(b), w, h)


def fig_empires():
    import math
    w, h = 880, 360
    b = []
    data = [("东罗马", 400), ("奥斯曼", 240), ("清", 70), ("苏联", 12)]
    b.append(f'<text x="440" y="30" class="t" text-anchor="middle">四个帝国的“衰落期”长度（对数刻度，示意）</text>')
    x0, y0, bw = 150, 70, 650
    # 轴：10^1..10^3
    for tick in (10, 100, 1000):
        x = x0 + bw * (math.log10(tick) - 1) / 2
        b.append(f'<line x1="{x:.0f}" y1="{y0-6}" x2="{x:.0f}" y2="{y0+4*54}" stroke="#cccccc" stroke-width="1"/>')
        b.append(f'<text x="{x:.0f}" y="{y0+4*54+22}" class="s" text-anchor="middle">{tick} 年</text>')
    for i, (name, val) in enumerate(data):
        y = y0 + i * 54
        b.append(f'<text x="140" y="{y+22}" class="b" text-anchor="end">{name}</text>')
        bar = bw * (math.log10(val) - 1) / 2
        col = [BLUE, GREEN, GOLD, RED][i]
        b.append(f'<rect x="{x0}" y="{y+4}" width="{bar:.0f}" height="26" rx="4" fill="{col}" fill-opacity="0.6"/>')
        b.append(f'<text x="{x0+bar+8:.0f}" y="{y+23}" class="s">约 {val} 年</text>')
    b.append(f'<text x="440" y="{y0+4*54+52}" class="cap" text-anchor="middle">'
             f'跨度两个数量级——说明“衰落”定义本身决定了长度</text>')
    return _wrap("\n".join(b), w, h)


def fig_paradigm():
    w, h = 900, 400
    b = []
    eras = [
        ("宏大叙事", "资料稀缺", "高 C", BLUE, 120),
        ("社会史", "资料增加", "高 A", GREEN, 340),
        ("微观史", "数据过载", "高 T", GOLD, 560),
        ("全球史/新物质", "过载+跨学科", "A+T", RED, 760),
    ]
    b.append(f'<text x="450" y="30" class="t" text-anchor="middle">范式转移的约束轨迹</text>')
    b.append(f'<line x1="80" y1="170" x2="820" y2="170" stroke="#cccccc" stroke-width="1.4"/>')
    prev = None
    for name, cond, pos, col, x in eras:
        b.append(f'<circle cx="{x}" cy="170" r="12" fill="{col}"/>')
        b.append(f'<text x="{x}" y="140" class="b" fill="{col}" text-anchor="middle">{pos}</text>')
        b.append(f'<text x="{x}" y="210" class="b" text-anchor="middle">{name}</text>')
        b.append(f'<text x="{x}" y="232" class="s" text-anchor="middle">{cond}</text>')
        if prev is not None:
            b.append(f'<line x1="{prev}" y1="170" x2="{x}" y2="170" stroke="{GREY}" '
                     f'stroke-width="1.4" stroke-dasharray="5,4"/>')
        prev = x
    b.append(f'<text x="450" y="286" class="s" text-anchor="middle">'
             f'资料状态改变 → 划算的位置改变 → 主流范式迁移</text>')
    b.append(f'<text x="450" y="316" class="cap" text-anchor="middle">'
             f'不是“越来越接近真理”，而是在三角上重新选择</text>')
    return _wrap("\n".join(b), w, h)


def main():
    os.makedirs(OUT, exist_ok=True)
    figs = {
        "fig01-tools.svg": fig_tools(),
        "fig02-cascade.svg": fig_cascade(),
        "fig03-triangle.svg": fig_triangle(),
        "fig04-empires.svg": fig_empires(),
        "fig05-paradigm.svg": fig_paradigm(),
    }
    for name, svg in figs.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
