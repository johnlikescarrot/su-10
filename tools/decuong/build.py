# -*- coding: utf-8 -*-
"""Builder: ghép toàn bộ đề cương thành một PDF duy nhất."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "decuong"))

from style import (Doc, register_fonts, S, P, toc_title,
                   CONTENT_W, NAVY, GOLD, GRAY, Spacer, Paragraph,
                   ParagraphStyle, PageBreak, NextPageTemplate,
                   colors, TA_CENTER, TA_JUSTIFY)

import content_intro
import content_a
import content_b
import content_c
import content_d
import content_e
import content_f
import content_g


def build(out_path):
    register_fonts()
    doc = Doc(out_path)
    story = []

    # ---- trang bìa (page template "cover") ----
    story += [Spacer(1, 1), NextPageTemplate("body"), PageBreak()]

    # ---- lời nói đầu ----
    story += content_intro.build()
    story += [PageBreak()]

    # ---- mục lục ----
    story += [toc_title(), Spacer(1, 8)]
    from style import make_toc
    story += [make_toc()]
    story += [PageBreak()]

    # ---- các phần ----
    for mod in (content_a, content_b, content_c, content_d,
                content_e, content_f, content_g):
        story += mod.build()
        story += [PageBreak()]

    doc.multiBuild(story)
    return out_path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "decuong.pdf"
    build(out)
    print("OK ->", out, os.path.getsize(out), "bytes")
