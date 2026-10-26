# -*- coding: utf-8 -*-
"""Dựng đề cương ôn tập Giữa học kì I – Lịch sử 10 (Kết nối tri thức) thành PDF.

Cách dùng:
    python build.py                      # xuất ra dist/De-cuong-on-tap-Giua-ky-I-Lich-su-10.pdf
    python build.py --output out.pdf     # xuất ra đường dẫn khác

Quy trình hai lượt:
    Lượt 1 dựng bản nháp để ghi lại số trang của từng tiêu đề;
    Lượt 2 dựng bản chính thức với mục lục đã có số trang.
    Hai lượt có cùng số dòng mục lục nên số trang không đổi.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from reportlab.lib.units import mm  # noqa: E402
from reportlab.platypus import NextPageTemplate, PageBreak, Paragraph, Spacer  # noqa: E402

from lib.blocks import cover_flow, render, rule  # noqa: E402
from lib.document import PAGES, GuideDoc, reset_pages, toc_flowables  # noqa: E402
from lib.theme import STYLES, register_fonts  # noqa: E402

from content.part1_orientation import part_i  # noqa: E402
from content.part2_bai1 import part_ii  # noqa: E402
from content.part3_bai2 import part_iii  # noqa: E402
from content.part4_bai3 import part_iv  # noqa: E402
from content.part5_cheatsheet import part_v  # noqa: E402
from content.part6_skills import part_vi  # noqa: E402
from content.part7_exam import part_vii  # noqa: E402
from content.part8_answers import part_viii  # noqa: E402
from content.part9_selftest import part_ix  # noqa: E402
from content.part10_plan import part_x  # noqa: E402
from content.part11_appendix import appendix  # noqa: E402

DEFAULT_OUTPUT = ROOT / "dist" / "De-cuong-on-tap-Giua-ky-I-Lich-su-10.pdf"

PART_BUILDERS = [part_i, part_ii, part_iii, part_iv, part_v, part_vi, part_vii,
                 part_viii, part_ix, part_x, appendix]

TAG_RE = re.compile(r"<[^>]+>")


def plain(text: str) -> str:
    return (TAG_RE.sub("", text).replace("▌", "").replace("&nbsp;", " ")
            .replace("&amp;", "&").strip())


def annotate(items_by_part):
    """Gắn khoá mục lục duy nhất cho từng tiêu đề; trả về (các phần, danh sách mục lục)."""
    entries = []
    parts = []
    counter = 0
    for items in items_by_part:
        new_items = []
        for item in items:
            if item[0] == "banner":
                counter += 1
                key = f"t{counter}"
                new_items.append(("banner", item[1], item[2], key))
                entries.append((0, f"{plain(item[1])}  ·  {plain(item[2])}", key))
            elif item[0] == "h2":
                counter += 1
                key = f"t{counter}"
                new_items.append(("h2", item[1], key))
                entries.append((1, plain(item[1]), key))
            else:
                new_items.append(item)
        parts.append(new_items)
    return parts, entries


def build_story(items_by_part, entries, pages) -> list:
    story = list(cover_flow())

    story.append(NextPageTemplate("body"))
    story.append(PageBreak())
    story.append(Paragraph("MỤC LỤC", STYLES["toc_title"]))
    story.append(rule(color=STYLES["toc_title"].textColor, thickness=1.2,
                      space_before=1, space_after=8))
    story.extend(toc_flowables(entries, pages))
    story.append(Spacer(1, 7 * mm))
    story.append(Paragraph(
        "Số trang in ở chân mỗi trang trùng với số trong mục lục. Phần I–VI là nội dung học; "
        "Phần VII–VIII là đề kiểm tra và đáp án; Phần IX–X là công cụ ôn nhanh và kế hoạch ôn tập.",
        STYLES["note"]))
    story.append(PageBreak())

    for index, items in enumerate(items_by_part):
        if index:
            story.append(PageBreak())
        story.extend(render(items))
    return story


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Dựng đề cương ôn tập Lịch sử 10 giữa kì I")
    parser.add_argument("--output", "-o", type=Path, default=DEFAULT_OUTPUT,
                        help="đường dẫn tệp PDF đầu ra")
    args = parser.parse_args(argv)

    register_fonts()
    out = args.output if args.output.is_absolute() else (ROOT / args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    raw_parts = [build() for build in PART_BUILDERS]
    items_by_part, entries = annotate(raw_parts)

    # Lượt 1: ghi số trang của từng tiêu đề.
    reset_pages()
    draft = GuideDoc(str(out))
    draft.build(build_story(items_by_part, entries, {}))

    # Lượt 2: mục lục có số trang thật.
    pages = dict(PAGES)
    doc = GuideDoc(str(out))
    doc.build(build_story(items_by_part, entries, pages))

    size_kb = out.stat().st_size / 1024
    print(f"Đã tạo: {out}  ({size_kb:,.0f} KB)")
    print(f"Tiêu đề trong mục lục: {len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
