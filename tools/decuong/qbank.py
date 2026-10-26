# -*- coding: utf-8 -*-
"""Tiện ích cân bằng phân bố đáp án cho ngân hàng câu hỏi."""
import random as _random


def rotate(opts, cur, target):
    """Xoay vòng danh sách phương án sao cho đáp án đúng chuyển từ `cur` sang `target`."""
    c = "ABCD".index(cur)
    t = "ABCD".index(target)
    k = (c - t) % 4
    return opts[k:] + opts[:k]


def balance(data, target, locked=(), seed=20262027):
    """Cân bằng đáp án A/B/C/D mà không đổi nội dung câu hỏi.

    data   : [(đề, [4 phương án], đáp án), ...]
    target : {"A": n, "B": n, "C": n, "D": n} – phân bố mong muốn
    locked : tập chỉ số (0-based) giữ nguyên đáp án (thường là các câu đã được
             giải thích bằng chữ cái cụ thể ở phần đáp án)
    """
    locked_letters = [a for i, (_, _, a) in enumerate(data) if i in locked]
    free_idx = [i for i in range(len(data)) if i not in locked]

    need = {}
    for k in "ABCD":
        need[k] = target.get(k, 0) - locked_letters.count(k)

    pool = []
    for k in "ABCD":
        pool += [k] * max(need[k], 0)

    # Nếu số câu cần chia không khớp (do các câu bị khoá chiếm quá nhiều),
    # bù bằng chữ cái đang ít xuất hiện nhất.
    while len(pool) < len(free_idx):
        pool.append(min("ABCD", key=lambda c: locked_letters.count(c) + pool.count(c)))
    pool = pool[:len(free_idx)]

    _random.Random(seed).shuffle(pool)
    assign = dict(zip(free_idx, pool))

    out = []
    for i, (q, opts, ans) in enumerate(data):
        if i in assign:
            t = assign[i]
            out.append((q, rotate(opts, ans, t), t))
        else:
            out.append((q, opts, ans))
    return out
