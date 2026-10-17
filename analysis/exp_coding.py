# -*- coding: utf-8 -*-
"""exp_coding.py ——《诠释的权衡》新增数值实验（可复算，C 级示范）。

问题：当研究者要做 k 个“合理但可争议”的编码决定、且每个决定会改变一部分案例的取值时，
      最终结论（哪一组更高）的符号被翻转的概率有多大？

设定（透明、可复算、非经验数据）：
  - 两组各 n=20 个案例；真实效应 d（以“高/低”表达）；
  - 每个案例有一个“边界程度” b∈[0,1]，表示它对编码决定有多敏感；
  - 每个编码维度 j 的取值为 ±1；对案例 i 的取值影响为 δ * b_i * s_ij；
  - 研究者随机选一套编码（s_ij），计算两组均值差，记录符号。
输出：data/exp_coding.json
"""
import itertools
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(HERE, "data")
os.makedirs(DATA, exist_ok=True)
rng = np.random.default_rng(20261016)

N = 20
K = 5
REPS = 4000


def coding_disagreement(d, m, n=20, reps=300, n_codings=2000):
    """固定数据、随机抽 2000 种编码，测“结论符号不一致”的比例（向量化）。"""
    rates = []
    for _ in range(reps):
        a = rng.normal(d, 1.0, n)
        b = rng.normal(0.0, 1.0, n)
        t = (a.mean() + b.mean()) / 2.0
        cand = np.concatenate([np.abs(a - t), np.abs(b - t)])
        order = np.argsort(cand)[:m]
        idx_a = [i for i in order if i < n]
        idx_b = [i - n for i in order if i >= n]
        pool = np.concatenate([a[idx_a], b[idx_b]])
        a0 = np.delete(a, idx_a); b0 = np.delete(b, idx_b)
        R = rng.random((n_codings, m)) < 0.5          # 每行一种编码
        sum_a = a0.sum() + R @ pool
        sum_b = b0.sum() + (1 - R) @ pool
        cnt_a = len(a0) + R.sum(axis=1)
        cnt_b = len(b0) + (1 - R).sum(axis=1)
        diff = sum_a / cnt_a - sum_b / cnt_b
        share = max((diff > 0).mean(), (diff <= 0).mean())
        rates.append(1 - share)
    return float(np.mean(rates))


rows = []
for d in (0.2, 0.3, 0.5):
    for m in (4, 8, 12, 16, 20):
        p = coding_disagreement(d, m)
        rows.append(dict(d=d, m=m, p_disagree=round(p, 4)))
        print("d=%.1f m=%2d  P(disagree)=%.4f" % (d, m, p))

json.dump(dict(seed=20261016, n=N, reps=800, grid=rows),
          open(os.path.join(DATA, "exp_coding.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote data/exp_coding.json")
