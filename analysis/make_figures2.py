# -*- coding: utf-8 -*-
"""make_figures2.py — 第二批正文插图（《诠释的权衡》）。

图 1.1  五个应用：由深而广
图 2.2  约束的三种类型
图 2.3  从置信度分布到坐标位置（粗粒化，不可反推）
图 6.1  一次带先验的更新
图 6.2  独立证据与假增强
图 7.1  集权度随政权生命周期变化
图 15.1 应用之间如何互馈：三个回路
图 15.2 框架放大的四种退化
图 16.1 十种历史理论的定位地图
图 20.1 地板、天花板、阁楼：三层强度的递进
"""
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "assets", "svg")
BLUE, RED, GOLD, GREEN, GREY = "#3a6ea5", "#c94f4f", "#b8862f", "#009E73", "#666666"
INK, DIM = "#222222", "#555555"


def _wrap(body, w, h, title=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">\n'
            f'<style>text{{font-family:"Microsoft YaHei","SimHei",Arial,sans-serif;}}'
            f'.t{{font-size:17px;fill:{INK};font-weight:700;}}'
            f'.b{{font-size:14px;fill:{INK};font-weight:700;}}'
            f'.s{{font-size:12px;fill:{DIM};}}'
            f'.cap{{font-size:13px;fill:{DIM};}}</style>\n'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff"/>\n'
            f'{body}\n</svg>\n')


def _arrow(x1, y1, x2, y2, col=GREY, sw=1.5):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    L = 8
    p1 = (x2 - L * math.cos(a - 0.4), y2 - L * math.sin(a - 0.4))
    p2 = (x2 - L * math.cos(a + 0.4), y2 - L * math.sin(a + 0.4))
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
            f'stroke="{col}" stroke-width="{sw}"/>'
            f'<polygon points="{x2:.0f},{y2:.0f} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}" fill="{col}"/>')


def fig_five_apps():
    w, h = 900, 260
    b = [f'<text x="{w/2}" y="30" class="t" text-anchor="middle">五个应用：由深而广</text>']
    items = [("一", "人物与事件", "贝叶斯·置信度", BLUE), ("二", "跨文明制度", "数据分析", GREEN),
             ("三", "既有争论", "分析还原论", GOLD), ("四", "历史理论", "综合分析", RED),
             ("五", "理论流变", "范式转移", GREY)]
    x0, dx = 80, 168
    for i, (n, name, tool, col) in enumerate(items):
        x = x0 + i * dx
        b.append(f'<circle cx="{x}" cy="120" r="34" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1.8"/>')
        b.append(f'<text x="{x}" y="126" class="b" fill="{col}" text-anchor="middle" font-size="20">{n}</text>')
        b.append(f'<text x="{x}" y="180" class="b" text-anchor="middle">{name}</text>')
        b.append(f'<text x="{x}" y="200" class="s" text-anchor="middle">{tool}</text>')
        if i < len(items) - 1:
            b.append(_arrow(x + 38, 120, x + dx - 38, 120, GREY, 1.4))
    b.append(f'<line x1="60" y1="232" x2="840" y2="232" stroke="{GREY}" stroke-width="1" opacity="0.5"/>')
    b.append(f'<text x="60" y="250" class="s">单位：一个人 → 一个制度 → 一场争论 → 一个理论 → 一门学科（尺度递增）</text>')
    return _wrap("\n".join(b), w, h)


def fig_constraint_types():
    w, h = 860, 300
    b = [f'<text x="{w/2}" y="30" class="t" text-anchor="middle">约束的三种类型：来源不同，后果不同</text>']
    rows = [("认知性", "容量、时间", "研究者一侧：注意力与时长有限", "工具可缓解，不会消失", BLUE),
            ("逻辑性", "权衡", "概念结构：三性质定义上互斥", "不可缓解，只能选择", RED),
            ("符号性", "区分", "符号系统：意义需要边界", "可用新形式化移动，但引入新边界", GOLD)]
    y0 = 60
    for i, (typ, names, src, cons, col) in enumerate(rows):
        y = y0 + i * 72
        b.append(f'<rect x="40" y="{y}" width="150" height="56" rx="6" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1.5"/>')
        b.append(f'<text x="115" y="{y+34}" class="b" fill="{col}" text-anchor="middle">{typ}</text>')
        b.append(f'<text x="215" y="{y+24}" class="b">{names}</text>')
        b.append(f'<text x="215" y="{y+46}" class="s">{src}</text>')
        b.append(f'<text x="560" y="{y+24}" class="s">后果：</text>')
        b.append(f'<text x="610" y="{y+24}" class="s">{cons}</text>')
    b.append(f'<text x="{w/2}" y="292" class="cap" text-anchor="middle">三者并置的理由：都作用于同一个操作——置信度的分配</text>')
    return _wrap("\n".join(b), w, h)


def fig_cascade_map():
    w, h = 880, 340
    b = [f'<text x="{w/2}" y="28" class="t" text-anchor="middle">从置信度分布到坐标位置：粗粒化，不可反推</text>']
    # left: four profiles
    prof = [("高浓度在 L4", "→ 高 C / 低 T", BLUE), ("分散在 L2–L3", "→ 高 A / 低 C", GREEN),
            ("压在 L1 细节", "→ 高 T / 低 C", GOLD)]
    for i, (p, r, col) in enumerate(prof):
        y = 70 + i * 66
        b.append(f'<rect x="60" y="{y}" width="260" height="46" rx="6" fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-width="1.4"/>')
        b.append(f'<text x="76" y="{y+29}" class="b">{p}</text>')
        b.append(_arrow(330, y + 23, 430, y + 23, GREY, 1.4))
        b.append(f'<text x="450" y="{y+29}" class="b" fill="{col}">{r}</text>')
    b.append(f'<rect x="620" y="88" width="210" height="150" rx="8" fill="{GREY}" fill-opacity="0.08" stroke="{GREY}" stroke-width="1.3"/>')
    b.append(f'<text x="725" y="150" class="b" text-anchor="middle">多个分布</text>')
    b.append(f'<text x="725" y="172" class="b" text-anchor="middle">→ 同一坐标</text>')
    b.append(f'<text x="725" y="200" class="s" text-anchor="middle">（多对一）</text>')
    b.append(f'<text x="{w/2}" y="300" class="cap" text-anchor="middle">知道“它是清晰论”，不等于知道它的四层分布；坐标不能反推剖面</text>')
    return _wrap("\n".join(b), w, h)


def fig_bayes():
    w, h = 820, 250
    b = [f'<text x="{w/2}" y="30" class="t" text-anchor="middle">一次带先验的更新</text>']
    boxes = [("先验", "读材料前的把握\n（基础率、机会、传统）", BLUE),
             ("证据 E", "似然：\nH 成立 / 不成立时 E 出现的可能", GOLD),
             ("后验", "更新后的置信度\n+ 它依赖哪些假设", GREEN)]
    xs = [70, 320, 570]
    for (name, sub, col), x in zip(boxes, xs):
        b.append(f'<rect x="{x}" y="70" width="180" height="90" rx="8" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1.6"/>')
        b.append(f'<text x="{x+90}" y="98" class="b" fill="{col}" text-anchor="middle">{name}</text>')
        for j, line in enumerate(sub.split("\n")):
            b.append(f'<text x="{x+90}" y="{122+j*18}" class="s" text-anchor="middle">{line}</text>')
    b.append(_arrow(252, 115, 318, 115, GREY))
    b.append(_arrow(502, 115, 568, 115, GREY))
    b.append(f'<text x="{w/2}" y="205" class="cap" text-anchor="middle">历史中先验与似然都是判断，不是测量；贝叶斯在此是记账纪律，不是计算器</text>')
    return _wrap("\n".join(b), w, h)


def fig_independence():
    w, h = 860, 300
    b = [f'<text x="{w/2}" y="28" class="t" text-anchor="middle">独立证据与假增强</text>']
    # left: fake
    b.append(f'<text x="210" y="60" class="b" fill="{RED}" text-anchor="middle">假增强（共享来源）</text>')
    for i, nm in enumerate(["E1 官方传记", "E3 后世编年", "E5 注释"]):
        b.append(f'<circle cx="{120+i*80}" cy="110" r="26" fill="{RED}" fill-opacity="0.12" stroke="{RED}" stroke-width="1.4"/>')
        b.append(f'<text x="{120+i*80}" y="115" class="s" text-anchor="middle">{nm.split()[0]}</text>')
    b.append(f'<text x="210" y="160" class="s" text-anchor="middle">都指向同一原始来源</text>')
    b.append(f'<text x="210" y="182" class="s" text-anchor="middle">→ 只算一次支持</text>')
    # right: real
    b.append(f'<text x="650" y="60" class="b" fill="{GREEN}" text-anchor="middle">独立证据</text>')
    for i, nm in enumerate(["E1 传记", "E2 书信", "E4 政敌"]):
        b.append(f'<circle cx="{560+i*90}" cy="110" r="26" fill="{GREEN}" fill-opacity="0.12" stroke="{GREEN}" stroke-width="1.4"/>')
        b.append(f'<text x="{560+i*90}" y="115" class="s" text-anchor="middle">{nm.split()[0]}</text>')
    b.append(f'<text x="650" y="160" class="s" text-anchor="middle">来源互不依赖</text>')
    b.append(f'<text x="650" y="182" class="s" text-anchor="middle">→ 分别移动置信度</text>')
    b.append(f'<line x1="430" y1="60" x2="430" y2="200" stroke="{GREY}" stroke-width="1" stroke-dasharray="5,4" opacity="0.5"/>')
    b.append(f'<text x="{w/2}" y="250" class="cap" text-anchor="middle">两条真正独立的支持，比十条互相抄录的支持更有力量</text>')
    return _wrap("\n".join(b), w, h)


def fig_lifecycle():
    import math
    w, h = 820, 300
    b = [f'<text x="{w/2}" y="28" class="t" text-anchor="middle">集权度随政权生命周期变化（示意）</text>']
    x0, y0, ww, hh = 90, 210, 620, 150
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x0+ww}" y2="{y0}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-hh}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(f'<text x="{x0-12}" y="{y0-hh+4}" class="s" text-anchor="end">高</text>')
    b.append(f'<text x="{x0-12}" y="{y0-4}" class="s" text-anchor="end">低</text>')
    for lab, x in [("兴起", x0 + 40), ("盛期", x0 + ww / 2), ("晚期", x0 + ww - 40)]:
        b.append(f'<text x="{x:.0f}" y="{y0+20}" class="s" text-anchor="middle">{lab}</text>')
    pts = []
    N = 40
    for i in range(N + 1):
        t = i / N
        v = math.exp(-((t - 0.5) ** 2) / 0.08)
        pts.append(f"{x0 + t*ww:.1f},{y0 - v*hh*0.92:.1f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="2.4"/>')
    b.append(f'<text x="{x0+ww*0.5:.0f}" y="{y0-hh*0.95:.0f}" class="s" fill="{BLUE}" text-anchor="middle">集权度</text>')
    b.append(f'<text x="{w/2}" y="270" class="cap" text-anchor="middle">集权不是静态属性，而是曲线——用一个值比较政权，等于把曲线压成一个点</text>')
    return _wrap("\n".join(b), w, h)


def fig_feedback():
    w, h = 820, 320
    b = [f'<text x="{w/2}" y="28" class="t" text-anchor="middle">应用之间如何互馈：三个回路</text>']
    pos = {"一": (410, 90), "二": (180, 230), "三": (640, 230), "四": (410, 270)}
    for n, (x, y) in pos.items():
        b.append(f'<circle cx="{x}" cy="{y}" r="30" fill="{BLUE}" fill-opacity="0.10" stroke="{BLUE}" stroke-width="1.6"/>')
        b.append(f'<text x="{x}" y="{y+6}" class="b" text-anchor="middle">应用{n}</text>')
    b.append(_arrow(210, 205, 385, 115, GOLD))
    b.append(f'<text x="150" y="150" class="s" fill="{GOLD}">①人物↔争论</text>')
    b.append(_arrow(215, 240, 610, 240, GREEN))
    b.append(f'<text x="410" y="232" class="s" fill="{GREEN}">②制度↔争论</text>')
    b.append(_arrow(410, 240, 410, 125, RED))
    b.append(f'<text x="420" y="200" class="s" fill="{RED}">③理论→人物</text>')
    b.append(f'<text x="{w/2}" y="308" class="cap" text-anchor="middle">五个应用不是五个独立案例，而是一个带反馈的系统</text>')
    return _wrap("\n".join(b), w, h)


def fig_degradation():
    w, h = 880, 280
    b = [f'<text x="{w/2}" y="28" class="t" text-anchor="middle">框架放大的四种退化</text>']
    items = [("维度退化", "τ 无法在 300 字内估计\n四维→三维", BLUE),
             ("证据退化", "只剩档位，无原文证据\n诊断→提问清单", GREEN),
             ("结构退化", "自由度超约束\n失去可证伪性", RED),
             ("地域退化", "七场中六场西方中心\n通用性未检验", GOLD)]
    for i, (name, desc, col) in enumerate(items):
        x = 50 + i * 210
        b.append(f'<rect x="{x}" y="60" width="185" height="120" rx="8" fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-width="1.5"/>')
        b.append(f'<text x="{x+92}" y="90" class="b" fill="{col}" text-anchor="middle">{name}</text>')
        for j, line in enumerate(desc.split("\n")):
            b.append(f'<text x="{x+92}" y="{120+j*20}" class="s" text-anchor="middle">{line}</text>')
    b.append(f'<text x="{w/2}" y="220" class="cap" text-anchor="middle">前两种是技术性的，后两种是结构性的——“扩大应用”不等于“扩大宣称”</text>')
    return _wrap("\n".join(b), w, h)


def fig_theory_map():
    w, h = 900, 420
    b = [f'<text x="{w/2}" y="28" class="t" text-anchor="middle">十种历史理论的定位地图（示意）</text>']
    # axes: x = A (low->high), y = C (high->low)
    x0, y0, ww, hh = 90, 360, 720, 290
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x0+ww}" y2="{y0}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-hh}" stroke="{GREY}" stroke-width="1.2"/>')
    b.append(f'<text x="{x0+ww}" y="{y0+22}" class="s" text-anchor="end">A 可组合（维度丰富）→</text>')
    b.append(f'<text x="{x0-60}" y="{y0-hh+4}" class="s">↑ C 因果清晰</text>')
    # (name, A, C)  A:0..1, C:0..1
    pts = [("宏大叙事", 0.15, 0.92, BLUE), ("历史唯物", 0.3, 0.88, BLUE), ("计量史学", 0.2, 0.8, BLUE),
           ("年鉴学派", 0.8, 0.45, GREEN), ("世界体系", 0.78, 0.55, GREEN), ("新文化史", 0.72, 0.35, GREEN),
           ("微观史", 0.45, 0.15, GOLD), ("全球微观史", 0.62, 0.18, GOLD), ("物质转向", 0.8, 0.2, GOLD),
           ("语言学转向", 0.55, 0.3, RED)]
    for name, A, C, col in pts:
        x = x0 + A * ww
        y = y0 - C * hh
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="{col}"/>')
        b.append(f'<text x="{x:.0f}" y="{y-9:.0f}" class="s" text-anchor="middle">{name}</text>')
    b.append(f'<text x="{w/2}" y="{y0+52}" class="cap" text-anchor="middle">每个理论占一个位置、让出一个顶点；地图标位置，不解释内容</text>')
    return _wrap("\n".join(b), w, h)


def fig_three_layers():
    w, h = 760, 320
    b = [f'<text x="{w/2}" y="28" class="t" text-anchor="middle">地板、天花板、阁楼：三层强度的递进</text>']
    rows = [("阁楼（推测）", "坐标可形式化、可自动化", RED, 0.75),
            ("天花板（有条件）", "置信度分配可跨立场、跨传统统一使用", GOLD, 0.55),
            ("地板（保底）", "分层标注的做法有用（独立成立）", GREEN, 0.35)]
    for i, (name, desc, col, wfrac) in enumerate(rows):
        y = 70 + i * 74
        bw = 560 * wfrac + 120
        x = (w - bw) / 2
        b.append(f'<rect x="{x:.0f}" y="{y}" width="{bw:.0f}" height="56" rx="8" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1.6"/>')
        b.append(f'<text x="{w/2}" y="{y+24}" class="b" fill="{col}" text-anchor="middle">{name}</text>')
        b.append(f'<text x="{w/2}" y="{y+44}" class="s" text-anchor="middle">{desc}</text>')
    b.append(f'<line x1="70" y1="290" x2="690" y2="290" stroke="{GREY}" stroke-width="1" opacity="0.5"/>')
    b.append(f'<text x="{w/2}" y="308" class="cap" text-anchor="middle">撤回“阁楼”只伤天花板，不伤地板；若地板不成立，上面两层一起失效</text>')
    return _wrap("\n".join(b), w, h)


def main():
    os.makedirs(OUT, exist_ok=True)
    figs = {
        "fig06-five-apps.svg": fig_five_apps(),
        "fig07-constraint-types.svg": fig_constraint_types(),
        "fig08-cascade-map.svg": fig_cascade_map(),
        "fig09-bayes.svg": fig_bayes(),
        "fig10-independence.svg": fig_independence(),
        "fig11-lifecycle.svg": fig_lifecycle(),
        "fig12-feedback.svg": fig_feedback(),
        "fig13-degradation.svg": fig_degradation(),
        "fig14-theory-map.svg": fig_theory_map(),
        "fig15-three-layers.svg": fig_three_layers(),
    }
    for name, svg in figs.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
