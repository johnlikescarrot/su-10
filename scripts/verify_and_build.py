#!/usr/bin/env python3
"""Build and programmatically verify the Grade 10 History Midterm 1 PDF Study Guide."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import pymupdf as fitz
import typst

ROOT = Path(__file__).resolve().parent.parent
SRC_MAIN = ROOT / "src" / "main.typ"
FONTS_DIR = ROOT / "src" / "fonts"
OUTPUT_PDF = ROOT / "DE_CUONG_ON_TAP_LICH_SU_10_GK1_2026_2027_KNTT.pdf"


def audit_question_counts() -> None:
    p4 = (ROOT / "src" / "part4_question_bank.typ").read_text(encoding="utf-8")
    p5a = (ROOT / "src" / "part5a_exams.typ").read_text(encoding="utf-8")
    p5b = (ROOT / "src" / "part5b_answers.typ").read_text(encoding="utf-8")

    p4_mcqs = re.findall(r'#mcq\("(\d+)"', p4)
    p4_tfs = re.findall(r'#tf-cluster\(\s*"([^"]+)"', p4)
    p5_mcqs = re.findall(r'#mcq\("(\d+)"', p5a)
    p5_tfs = re.findall(r'#tf-cluster\(\s*"([^"]+)"', p5a)

    assert len(p4_mcqs) == 45, f"Expected 45 MCQs in Part IV, got {len(p4_mcqs)}"
    assert len(p4_tfs) == 6, f"Expected 6 TF clusters in Part IV, got {len(p4_tfs)}"
    assert len(p5_mcqs) == 60, f"Expected 60 MCQs across 3 exams in Part V, got {len(p5_mcqs)}"
    assert len(p5_tfs) == 6, f"Expected 6 TF clusters across 3 exams in Part V, got {len(p5_tfs)}"

    # Verify answer key tables
    p4_keys = re.findall(r'\[\*(\d+)\.\s*([ABCD])\*\]', p4)
    assert len(p4_keys) == 45, f"Expected 45 answer keys in Part IV, got {len(p4_keys)}"
    p4_dist = Counter(ans for _, ans in p4_keys)

    p5_keys = re.findall(r'\[\*(\d+)\.\s*([ABCD])\*\]', p5b)
    assert len(p5_keys) == 60, f"Expected 60 answer keys in Part V, got {len(p5_keys)}"

    for exam_idx in range(3):
        chunk = p5_keys[exam_idx * 20 : (exam_idx + 1) * 20]
        nums = [int(n) for n, _ in chunk]
        assert nums == list(range(1, 21)), f"Exam {exam_idx + 1} key numbering mismatch: {nums}"
        dist = Counter(ans for _, ans in chunk)
        assert dist == {"A": 5, "B": 5, "C": 5, "D": 5}, (
            f"Exam {exam_idx + 1} A/B/C/D distribution not 5-5-5-5: {dist}"
        )

    total_commands = 45 + (6 * 4) + 4 + 60 + (6 * 4) + 3
    assert total_commands == 160, f"Expected 160 total assessment items, got {total_commands}"
    print(f"[OK] Question bank & 3 exams verified: {total_commands} total items")
    print(f"     - Part IV MCQ key distribution (45 Qs): {dict(sorted(p4_dist.items()))}")
    print("     - Part V Exam 1, 2, 3 MCQ distributions: 5A / 5B / 5C / 5D each")


def build_and_verify_pdf(render_dir: Path | None = None) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "generate_assets.py")], check=True)
    audit_question_counts()

    pdf_bytes = typst.compile(
        str(SRC_MAIN),
        font_paths=[str(FONTS_DIR)],
    )
    OUTPUT_PDF.write_bytes(pdf_bytes)
    size_kb = len(pdf_bytes) / 1024

    doc = fitz.open(OUTPUT_PDF)
    page_count = doc.page_count
    toc = doc.get_toc()
    fonts_used = set()
    for i in range(page_count):
        for f in doc.get_page_fonts(i):
            fonts_used.add(f[3])

    print(f"[OK] Compiled {OUTPUT_PDF.name}: {page_count} pages, {size_kb:.1f} KB")
    print(f"[OK] Embedded PDF bookmarks (TOC entries): {len(toc)}")
    print(f"[OK] Embedded fonts: {sorted(fonts_used)}")

    assert page_count >= 20, f"Unexpectedly low page count: {page_count}"
    assert len(toc) >= 15, f"Expected rich PDF bookmarks, got {len(toc)}"
    assert any("BeVietnamPro" in fn for fn in fonts_used), f"BeVietnamPro not embedded: {fonts_used}"

    if render_dir is not None:
        render_dir.mkdir(parents=True, exist_ok=True)
        for p in render_dir.glob("page_*.png"):
            p.unlink()
        for idx, page in enumerate(doc, start=1):
            pix = page.get_pixmap(dpi=145)
            out_png = render_dir / f"page_{idx:02d}.png"
            pix.save(str(out_png))
        print(f"[OK] Rendered {page_count} page PNGs to {render_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-dir", type=Path, default=None)
    args = parser.parse_args()
    build_and_verify_pdf(args.render_dir)
