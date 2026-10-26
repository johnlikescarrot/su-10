"""Dựng PDF: Đề cương ôn tập giữa HKI – Lịch sử 10 (Kết nối tri thức), năm học 2026–2027.

Chạy:  python3 de-cuong/build_de_cuong.py
Kết quả: De_cuong_on_tap_GKI_Lich_su_10_KNTT_2026-2027.pdf ở thư mục gốc repo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib import colors  # noqa: E402
from reportlab.lib.units import cm  # noqa: E402
from reportlab.platypus import (  # noqa: E402
    BaseDocTemplate, Frame, KeepTogether, NextPageTemplate, PageBreak,
    PageTemplate, Spacer, Table, TableStyle,
)

import layout as L  # noqa: E402
from layout import (  # noqa: E402
    BLUE, CONTENT_W, CREAM, GREEN, LILAC, MINT, NAVY, PURPLE, RED, ROSE, SKY,
    H1, H2, H3, P, Paragraph, S, box, bullets, key_grid, mcq, table, tf_question,
)
from content_bank import BANK, QA  # noqa: E402
from content_de import (  # noqa: E402
    DE1_KEYS, DE1_MCQ, DE1_TF, DE1_TL, DE2_KEYS, DE2_MCQ, DE2_TF, DE2_TL,
    LEVELS, TF_LEVELS,
)
from content_kienthuc import (  # noqa: E402
    bai_1, bai_2, bai_3, ky_nang, phan_ma_tran, so_do_tong_hop,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "De_cuong_on_tap_GKI_Lich_su_10_KNTT_2026-2027.pdf")
TITLE = "Đề cương ôn tập giữa học kì I – Lịch sử 10 (Kết nối tri thức) – Năm học 2026–2027"


# ---------------------------------------------------------------- page decorations
def on_page(canvas, doc):
    canvas.saveState()
    w, h = L.PAGE_W, L.PAGE_H
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(0.8)
    canvas.line(L.MARGIN_X, h - 1.25 * cm, w - L.MARGIN_X, h - 1.25 * cm)
    canvas.setFont("BVP", 7.8)
    canvas.setFillColor(L.GREY)
    canvas.drawString(L.MARGIN_X, h - 1.08 * cm, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I • LỊCH SỬ 10 • KẾT NỐI TRI THỨC")
    canvas.drawRightString(w - L.MARGIN_X, h - 1.08 * cm, "Năm học 2026 – 2027")
    canvas.line(L.MARGIN_X, 1.25 * cm, w - L.MARGIN_X, 1.25 * cm)
    canvas.drawString(L.MARGIN_X, 0.85 * cm, "Học chắc – Hiểu sâu – Vận dụng tốt")
    canvas.setFont("BVP-H", 8.5)
    canvas.setFillColor(NAVY)
    canvas.drawRightString(w - L.MARGIN_X, 0.85 * cm, f"Trang {doc.page}")
    canvas.restoreState()


def on_cover(canvas, doc):
    canvas.saveState()
    w, h = L.PAGE_W, L.PAGE_H
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 10.5 * cm, w, 10.5 * cm, stroke=0, fill=1)
    canvas.setFillColor(BLUE)
    canvas.rect(0, h - 10.9 * cm, w, 0.4 * cm, stroke=0, fill=1)
    canvas.setFillColor(colors.HexColor("#c8102e"))
    canvas.rect(0, h - 11.15 * cm, w, 0.25 * cm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("BVP-B", 11)
    canvas.drawCentredString(w / 2, h - 2.3 * cm, "KIỂM TRA ĐỊNH KÌ GIỮA HỌC KÌ I • KHỐI 10 • NĂM HỌC 2026 – 2027")
    canvas.setFont("BVP-X", 34)
    canvas.drawCentredString(w / 2, h - 4.4 * cm, "ĐỀ CƯƠNG ÔN TẬP")
    canvas.setFont("BVP-X", 25)
    canvas.drawCentredString(w / 2, h - 5.75 * cm, "LỊCH SỬ 10")
    canvas.setFont("BVP", 13)
    canvas.drawCentredString(w / 2, h - 6.85 * cm, "Bộ sách Kết nối tri thức với cuộc sống")
    canvas.setFont("BVP-I", 10.5)
    canvas.drawCentredString(w / 2, h - 8.2 * cm, "Bám sát ma trận & bảng đặc tả: LS10- MTGK1-26-27-HHT")
    canvas.drawCentredString(w / 2, h - 8.85 * cm, "Thời gian làm bài 45 phút • 20 câu TN + 2 câu Đúng/Sai + 1 câu tự luận")
    canvas.setFont("BVP", 8)
    canvas.setFillColor(L.GREY)
    canvas.drawCentredString(w / 2, 1.0 * cm, "Font chữ: Be Vietnam Pro (SIL OFL 1.1) & DejaVu Sans")
    canvas.restoreState()


# ---------------------------------------------------------------- cover content
def cover():
    f = [Spacer(1, 10.6 * cm)]
    f += H2("Đề cương gồm")
    rows = [
        ["Phần", "Nội dung", "Dùng để"],
        ["I", "Giải mã ma trận đề: cấu trúc, điểm số, trọng số từng bài, danh sách yêu cầu cần đạt", "Biết học gì, ưu tiên gì"],
        ["II", "Kiến thức trọng tâm Bài 1, 2, 3 – bảng so sánh, sơ đồ, mẹo nhớ + Tóm tắt 1 trang + Lộ trình 7 ngày", "Học hiểu & ghi nhớ"],
        ["III", "Kĩ năng làm bài trắc nghiệm, Đúng/Sai, tự luận", "Tránh mất điểm oan"],
        ["IV", "Đề minh họa số 1 (bám sát 100% ma trận) + đáp án, giải thích, hướng dẫn chấm", "Luyện đề thật"],
        ["V", "Đề minh họa số 2 (bám sát 100% ma trận) + đáp án, giải thích, hướng dẫn chấm", "Luyện đề thật"],
        ["VI", "Ngân hàng 30 câu hỏi theo bài + đáp án", "Luyện thêm"],
        ["VII", "40 câu hỏi – đáp nhanh (che cột đáp án để tự kiểm tra)", "Ghi nhớ chủ động"],
    ]
    f += table(rows, [0.5, 4.6, 1.6], center_cols=(0,))
    f += box("Cách dùng hiệu quả nhất", [
        *bullets([
            "Học Phần II theo <b>lộ trình 7 ngày</b>; sau mỗi bài, che nội dung và <b>tự nói lại</b> các từ khóa in đậm.",
            "Làm đề minh họa <b>đúng 45 phút</b>, không xem đáp án trước; chấm điểm rồi mới đọc giải thích.",
            "Mỗi câu sai → ghi vào sổ “lỗi sai” kèm mục kiến thức cần xem lại.",
            "Ngày trước kiểm tra: đọc <b>Tóm tắt 1 trang</b> + <b>40 câu hỏi – đáp nhanh</b>.",
        ]),
    ], color=GREEN, bg=MINT, icon="✔")
    f.append(NextPageTemplate("main"))
    f.append(PageBreak())
    return f


# ---------------------------------------------------------------- exams
def exam(title, sub, mcqs, keys, tfs, tl, color):
    f = []
    f += H1(title, color=color, sub=sub)
    f += box(None, [P("<b>Thời gian làm bài: 45 phút.</b> Phần I: 20 câu (5,0 điểm) • Phần II: 2 câu Đúng/Sai – 8 ý (2,0 điểm) • "
                      "Phần III: Tự luận (3,0 điểm). Nhãn nhỏ màu xám sau mỗi câu cho biết <b>bài và cấp độ</b> theo ma trận.")],
             color=NAVY, bg=SKY)
    f += H2("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (5,0 điểm)")
    f += [P("<i>Thí sinh trả lời từ câu 1 đến câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án.</i>", "small"), Spacer(1, 4)]
    arranged = []
    for i, (stem, options, _exp) in enumerate(mcqs):
        fl, opts = mcq(i + 1, stem, options, keys[i], LEVELS[i])
        arranged.append(opts)
        f += fl
    f += H2("PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm)")
    f += [P("<i>Thí sinh trả lời câu 1, câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng (Đ) hoặc sai (S).</i>", "small"),
          Spacer(1, 4)]
    for j, tf in enumerate(tfs):
        f += tf_question(j + 1, tf["intro"], tf["source"], tf["statements"], TF_LEVELS)
    f += H2("PHẦN III. Tự luận (3,0 điểm)")
    f += [P(f'<font name="BVP-H" color="#14365d">Câu 1.</font> {tl["question"]} ' + L.tag("Bài 3 • ½ Biết + ½ Vận dụng")),
          Spacer(1, 6)]
    f += [P("— HẾT —", "body", alignment=1, fontName="BVP-H", textColor=L.GREY)]
    f.append(PageBreak())
    return f, arranged


def sort_letter_lists(text):
    """Sắp xếp lại các cụm chữ cái như "D, A, C" → "A, C, D" cho dễ đọc."""
    import re

    def fix(m):
        letters = sorted(re.findall(r"[ABCD]", m.group(0)))
        return ", ".join(letters)
    return re.sub(r"\b[ABCD](?:, [ABCD])+\b", fix, text)


def answers(title, mcqs, keys, arranged, tfs, tl, color):
    f = []
    f += H1(title, color=color)
    f += H2("Phần I – Bảng đáp án nhanh")
    f += key_grid(list(keys))
    f += H2("Phần I – Giải thích chi tiết")
    for i, (stem, opts, exp) in enumerate(mcqs):
        k = keys[i]
        correct = arranged[i]["ABCD".index(k)]
        # {1},{2},{3} trong lời giải = phương án nhiễu thứ 1, 2, 3 → đổi sang chữ cái thực tế
        for n in (1, 2, 3):
            exp = exp.replace("{%d}" % n, "ABCD"[arranged[i].index(opts[n])])
        exp = sort_letter_lists(exp)
        txt = (f'<font name="BVP-H" color="#14365d">Câu {i + 1}</font> '
               f'<font name="BVP-H" color="#b3261e">→ {k}.</font> <i>{correct}</i><br/>'
               f'<font color="#1e7b45"><b>Vì sao:</b></font> {exp}')
        f.append(KeepTogether([P(txt, "ans")]))
    f += H2("Phần II – Đáp án Đúng/Sai")
    rows = [["Câu", "a)", "b)", "c)", "d)"]]
    for j, tf in enumerate(tfs):
        rows.append([f"<b>Câu {j + 1}</b>"] + [
            f'<font name="BVP-H" color="{"#1e7b45" if ok else "#b3261e"}">{"Đúng" if ok else "Sai"}</font>'
            for _t, ok in tf["statements"]])
    f += table(rows, [1, 1, 1, 1, 1], center_cols=(0, 1, 2, 3, 4))
    for j, tf in enumerate(tfs):
        f += H3(f"Câu {j + 1} – giải thích")
        f += bullets(tf["explain"])
    f += H2("Phần III – Hướng dẫn chấm tự luận")
    rows = [["Ý", "Nội dung cần đạt", "Điểm"]] + tl["rubric"]
    f += table(rows, [0.8, 6, 0.6], center_cols=(0, 2), valign="TOP")
    if tl.get("model"):
        f += box("Bài làm mẫu ý b) (tham khảo)", [P(tl["model"])], color=PURPLE, bg=LILAC, icon="✎", keep=False)
    if tl.get("model"):
        f += box("Lưu ý khi chấm", [P("Học sinh có thể chọn di sản khác (Khu di tích Kim Liên, Đền Cuông, Thành cổ Vinh…) và diễn đạt khác, "
                                  "nếu đúng, hợp lí, cụ thể vẫn cho điểm tối đa. Khuyến khích ý sáng tạo (số hóa, mạng xã hội, CLB…).")],
                 color=GREEN, bg=MINT, icon="✔")
    f.append(PageBreak())
    return f


def bank_section():
    f = []
    f += H1("PHẦN VI. NGÂN HÀNG 30 CÂU HỎI LUYỆN THÊM", color=PURPLE)
    n = 1
    all_keys = []
    for bai, qs in BANK.items():
        f += H2(bai)
        for stem, options, key in qs:
            fl, _ = mcq(n, stem, options, key)
            f += fl
            all_keys.append(key)
            n += 1
    f += H2("Đáp án ngân hàng câu hỏi")
    f += key_grid(all_keys)
    f.append(PageBreak())
    return f


def qa_section():
    f = []
    f += H1("PHẦN VII. 40 CÂU HỎI – ĐÁP NHANH (ghi nhớ chủ động)", color=GREEN,
            sub="Cách dùng: lấy giấy che cột “Đáp” → tự trả lời → mở ra kiểm tra → đánh dấu ✔ câu đã thuộc.")
    rows = [["#", "Hỏi", "Đáp", "✔"]]
    for i, (q, a) in enumerate(QA, 1):
        rows.append([str(i), f"<b>{q}</b>", a, "☐"])
    f += table(rows, [0.35, 2.4, 4.2, 0.35], center_cols=(0, 3), head_bg=GREEN, font_size=8.8)
    f.append(Spacer(1, 6))
    f += box(None, [P("<b>Chúc các em ôn tập hiệu quả và đạt kết quả cao!</b>", alignment=1)], color=RED, bg=ROSE)
    return f


# ---------------------------------------------------------------- build
def build():
    doc = BaseDocTemplate(
        OUT, pagesize=L.A4, title=TITLE, author="Đề cương ôn tập – Lịch sử 10",
        subject="Ôn tập giữa học kì I – Lịch sử 10 – Kết nối tri thức",
        keywords="Lịch sử 10, Kết nối tri thức, đề cương, giữa kì 1, 2026-2027",
        leftMargin=L.MARGIN_X, rightMargin=L.MARGIN_X, topMargin=1.6 * cm, bottomMargin=1.6 * cm,
    )
    frame = Frame(L.MARGIN_X, 1.55 * cm, CONTENT_W, L.PAGE_H - 3.15 * cm, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    cover_frame = Frame(L.MARGIN_X, 1.4 * cm, CONTENT_W, L.PAGE_H - 2.0 * cm, id="c",
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=on_cover),
        PageTemplate(id="main", frames=[frame], onPage=on_page),
    ])

    story = []
    story += cover()
    story += phan_ma_tran()
    story += bai_1()
    story += bai_2()
    story += bai_3()
    story += so_do_tong_hop()
    story += ky_nang()

    de1, arr1 = exam("PHẦN IV. ĐỀ MINH HỌA SỐ 1", "Bám sát ma trận LS10- MTGK1-26-27-HHT • Có đáp án ở trang sau",
                     DE1_MCQ, DE1_KEYS, DE1_TF, DE1_TL, NAVY)
    story += de1
    story += answers("ĐÁP ÁN & GIẢI THÍCH – ĐỀ MINH HỌA SỐ 1", DE1_MCQ, DE1_KEYS, arr1, DE1_TF, DE1_TL, RED)

    de2, arr2 = exam("PHẦN V. ĐỀ MINH HỌA SỐ 2", "Bám sát ma trận LS10- MTGK1-26-27-HHT • Có đáp án ở trang sau",
                     DE2_MCQ, DE2_KEYS, DE2_TF, DE2_TL, NAVY)
    story += de2
    story += answers("ĐÁP ÁN & GIẢI THÍCH – ĐỀ MINH HỌA SỐ 2", DE2_MCQ, DE2_KEYS, arr2, DE2_TF, DE2_TL, RED)

    story += bank_section()
    story += qa_section()

    doc.build(story)
    print("Đã tạo:", OUT)


def self_check():
    """Kiểm tra dữ liệu khớp ma trận trước khi dựng."""
    for name, mcqs, keys, tfs in (("Đề 1", DE1_MCQ, DE1_KEYS, DE1_TF), ("Đề 2", DE2_MCQ, DE2_KEYS, DE2_TF)):
        assert len(mcqs) == 20 and len(keys) == 20, name
        assert all(len(o) == 4 for _s, o, _e in mcqs), name
        assert len(tfs) == 2 and all(len(t["statements"]) == 4 for t in tfs), name
    assert sum(len(v) for v in BANK.values()) == 30
    assert len(QA) == 40
    assert len(LEVELS) == 20


if __name__ == "__main__":
    self_check()
    build()
