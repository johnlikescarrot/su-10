#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh file PDF: ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KỲ I – LỊCH SỬ LỚP 10
(Bộ Kết nối tri thức với cuộc sống, năm học 2026–2027)

Nội dung bám sát ma trận đề kiểm tra trong tệp
"LS10- MTGK1-26-27-HHT.docx" (repo: johnlikescarrot/su-10):
  - Phần I : 20 câu TN nhiều lựa chọn  (I.1 – I.20)
  - Phần II: 2 câu TN đúng/sai         (II.1a–d, II.2a–d)
  - Phần III: 1 câu tự luận            (3 điểm: 1đ NL1–Biết + 2đ NL3–Vận dụng)
  - 45 phút, 10 điểm, 28 lệnh hỏi TN + 1 TL
"""
import os
import matplotlib  # chỉ để mượn bộ font DejaVu kèm theo

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
    Table, TableStyle, PageBreak, KeepTogether, HRFlowable,
)
from reportlab.platypus.tableofcontents import TableOfContents

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "De-cuong-on-tap-giua-ky-I-Lich-su-10-KNTT.pdf")
FONT_DIR = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")

# ---------------------------------------------------------------- fonts ----
def reg(name, fname):
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fname)))

reg("DJS", "DejaVuSans.ttf")
reg("DJS-B", "DejaVuSans-Bold.ttf")
reg("DJS-I", "DejaVuSans-Oblique.ttf")
reg("DJS-BI", "DejaVuSans-BoldOblique.ttf")
reg("DJR", "DejaVuSerif.ttf")
reg("DJR-B", "DejaVuSerif-Bold.ttf")
reg("DJR-I", "DejaVuSerif-Italic.ttf")
reg("DJR-BI", "DejaVuSerif-BoldItalic.ttf")
pdfmetrics.registerFontFamily("DJS", normal="DJS", bold="DJS-B", italic="DJS-I", boldItalic="DJS-BI")
pdfmetrics.registerFontFamily("DJR", normal="DJR", bold="DJR-B", italic="DJR-I", boldItalic="DJR-BI")

# ---------------------------------------------------------------- colors ---
NAVY = colors.HexColor("#1F3864")
BLUE = colors.HexColor("#2E5C8A")
LBLUE = colors.HexColor("#E8EEF7")
GREEN = colors.HexColor("#1E7B34")
LGREEN = colors.HexColor("#E7F5E9")
GOLD = colors.HexColor("#B07A00")
LGOLD = colors.HexColor("#FFF6DD")
RED = colors.HexColor("#B3261E")
LRED = colors.HexColor("#FDECEA")
GREY = colors.HexColor("#555555")
LGREY = colors.HexColor("#F2F2F2")

# ---------------------------------------------------------------- styles ---
def S(name, **kw):
    return ParagraphStyle(name, **kw)

body = S("Body", fontName="DJR", fontSize=9.6, leading=14.2, spaceAfter=5,
         textColor=colors.HexColor("#1A1A1A"), alignment=4)
bodyc = S("BodyC", parent=body, alignment=1)
lead = S("Lead", parent=body, fontSize=10.2, leading=15, textColor=colors.HexColor("#333333"))
h1 = S("H1", fontName="DJS-B", fontSize=15, leading=19, textColor=colors.white,
       backColor=NAVY, borderPadding=(7, 9, 7, 9), spaceBefore=14, spaceAfter=10,
       alignment=0)
h2 = S("H2", fontName="DJS-B", fontSize=12, leading=16, textColor=colors.white,
       backColor=BLUE, borderPadding=(5, 8, 5, 8), spaceBefore=12, spaceAfter=7)
h3 = S("H3", fontName="DJS-B", fontSize=10.5, leading=14, textColor=NAVY,
       spaceBefore=9, spaceAfter=4)
h4 = S("H4", fontName="DJS-B", fontSize=9.8, leading=13, textColor=BLUE,
       spaceBefore=7, spaceAfter=3)
title1 = S("Title1", fontName="DJS-B", fontSize=24, leading=30, alignment=1,
           textColor=NAVY, spaceAfter=4)
title2 = S("Title2", fontName="DJS", fontSize=14, leading=19, alignment=1,
           textColor=BLUE, spaceAfter=3)
title3 = S("Title3", fontName="DJS", fontSize=11, leading=15, alignment=1,
           textColor=GREY, spaceAfter=2)
bullet = S("Bullet", parent=body, leftIndent=13, bulletIndent=4, spaceAfter=3)
bullet2 = S("Bullet2", parent=body, leftIndent=27, bulletIndent=17, spaceAfter=2.5,
            fontSize=9.4, leading=13.6)
note = S("Note", parent=body, fontSize=9.2, leading=13.4, textColor=colors.HexColor("#4A4A4A"),
         leftIndent=8, rightIndent=6, spaceBefore=3, spaceAfter=5)
qhead = S("QHead", fontName="DJS", fontSize=10, leading=14, textColor=NAVY,
          spaceBefore=8, spaceAfter=3)
qtext = S("QText", parent=body, fontName="DJR-B", fontSize=9.8, leading=14, spaceAfter=4)
opt = S("Opt", parent=body, leftIndent=16, bulletIndent=2, spaceAfter=1.5, fontSize=9.5,
        leading=13.6)
ans = S("Ans", parent=body, fontName="DJR", fontSize=9.5, leading=13.6, backColor=LGREEN,
        borderPadding=(4, 6, 4, 6), spaceBefore=3, spaceAfter=6, textColor=colors.HexColor("#14532D"))
anssai = S("AnsSai", parent=ans, backColor=LRED, textColor=colors.HexColor("#7F1D1D"))
tag = S("Tag", fontName="DJS", fontSize=7.6, leading=10, textColor=GREY)
th = S("TH", fontName="DJS-B", fontSize=8.6, leading=11.6, textColor=colors.white, alignment=1)
td = S("TD", fontName="DJR", fontSize=8.5, leading=11.8, alignment=0)
tdc = S("TDC", parent=td, alignment=1)
tdb = S("TDB", parent=td, fontName="DJR-B", alignment=1)
mnem = S("Mnem", parent=body, fontName="DJS", fontSize=9.4, leading=13.6,
         backColor=LGOLD, borderPadding=(5, 7, 5, 7), spaceBefore=4, spaceAfter=6,
         textColor=colors.HexColor("#6B4E00"))
warn = S("Warn", parent=body, fontName="DJS", fontSize=9.2, leading=13.4,
         backColor=LRED, borderPadding=(5, 7, 5, 7), spaceBefore=4, spaceAfter=6,
         textColor=colors.HexColor("#7F1D1D"))
toc_lvl0 = S("TOC0", fontName="DJS-B", fontSize=10.5, leading=22, textColor=NAVY)
toc_lvl1 = S("TOC1", fontName="DJS", fontSize=9.5, leading=17, leftIndent=16,
             textColor=colors.HexColor("#333333"))

ALL_TEXT = []  # dùng để kiểm tra glyph tiếng Việt

def T(s):
    """Đánh dấu text sẽ hiển thị (phục vụ kiểm tra font)."""
    ALL_TEXT.append(s)
    return s

# ---------------------------------------------------------------- helpers --
def P(text, style=body):
    return Paragraph(T(text), style)

def UL(items, style=bullet, mark="•"):
    return [Paragraph(T(t), style, bulletText=mark) for t in items]

def table(data, widths, header=True, align_center_cols=(), font_size=8.5):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B8C4D9")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LBLUE]),
        ]
    t.setStyle(TableStyle(style))
    return t

def mc(code, meta, question, options, key, explain, ok=True):
    """Một câu TN nhiều lựa chọn."""
    rows = []
    rows.append(Paragraph(
        f'<font color="#1F3864"><b>[{T(code)}]</b></font>  <font size="7.6" color="#555555">{T(meta)}</font>',
        qhead))
    rows.append(Paragraph(T(question), qtext))
    for i, (let, txt) in enumerate(zip("ABCD", options)):
        mark = (f'<font color="#1E7B34"><b>{let}. {txt}   <font face="DJS">✔</font></b></font>'
                if let == key else f"{let}. {txt}")
        rows.append(Paragraph(T(mark), opt))
    ans_style = ans if ok else anssai
    rows.append(Paragraph(T(f"<b>Đáp án: {key}</b> — {explain}"), ans_style))
    return KeepTogether(rows)

def dungsai(code, meta, statement, verdict, explain):
    """Một ý TN đúng/sai."""
    rows = []
    vs = "ĐÚNG" if verdict == "D" else "SAI"
    vcolor = "#1E7B34" if verdict == "D" else "#B3261E"
    vbg = LGREEN if verdict == "D" else LRED
    rows.append(Paragraph(
        f'<font color="#1F3864"><b>[{T(code)}]</b></font>  <font size="7.6" color="#555555">{T(meta)}</font>',
        qhead))
    rows.append(Paragraph(T(statement), qtext))
    st = S("Verdict", parent=ans, backColor=vbg, textColor=colors.HexColor(vcolor),
           fontName="DJR-B")
    rows.append(Paragraph(T(f"ĐÁP ÁN: {vs} — {explain}"), st))
    return KeepTogether(rows)

# ---------------------------------------------------------------- doc -------
class DeCuongDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            sn = flowable.style.name
            if sn == "H1":
                self.notify("TOCEntry", (0, flowable.getPlainText(), self.page))
            elif sn == "H2":
                self.notify("TOCEntry", (1, flowable.getPlainText(), self.page))

def _frame(page_size):
    pw, ph = page_size
    return Frame(17 * mm, 16 * mm, pw - 34 * mm, ph - 34 * mm, id="main",
                 leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

def on_page(canvas, doc):
    canvas.saveState()
    pw, ph = A4
    # header
    canvas.setFont("DJS", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(17 * mm, ph - 12 * mm,
                      "Đề cương ôn tập giữa học kỳ I – Lịch sử lớp 10 (Kết nối tri thức với cuộc sống)")
    canvas.setStrokeColor(colors.HexColor("#B8C4D9"))
    canvas.setLineWidth(0.6)
    canvas.line(17 * mm, ph - 13.6 * mm, pw - 17 * mm, ph - 13.6 * mm)
    # footer
    canvas.line(17 * mm, 12.5 * mm, pw - 17 * mm, 12.5 * mm)
    canvas.setFont("DJS", 7.5)
    canvas.drawString(17 * mm, 9 * mm, "Năm học 2026 – 2027  ·  Soạn theo ma trận LS10- MTGK1-26-27-HHT")
    canvas.drawRightString(pw - 17 * mm, 9 * mm, f"Trang {canvas.getPageNumber()}")
    canvas.restoreState()

def on_page_cover(canvas, doc):
    pw, ph = A4
    canvas.saveState()
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(2.2)
    canvas.rect(12 * mm, 12 * mm, pw - 24 * mm, ph - 24 * mm)
    canvas.setLineWidth(0.7)
    canvas.rect(14 * mm, 14 * mm, pw - 28 * mm, ph - 28 * mm)
    canvas.restoreState()

# ================================================================ CONTENT ===
story = []
A = story.append

# ---------------------------------------------------------------- COVER -----
A(Spacer(1, 46 * mm))
A(P("ĐỀ CƯƠNG ÔN TẬP", title1))
A(P("GIỮA HỌC KỲ I", title1))
A(Spacer(1, 6 * mm))
A(P("Môn Lịch sử – Lớp 10", title2))
A(P("Bộ sách Kết nối tri thức với cuộc sống", title2))
A(P("Năm học 2026 – 2027", title3))
A(Spacer(1, 10 * mm))
A(HRFlowable(width="60%", thickness=1.2, color=BLUE, hAlign="CENTER", spaceBefore=4, spaceAfter=10))
A(P("Soạn theo Ma trận đề kiểm tra định kỳ giữa học kỳ I – Khối 10<br/>"
    "(tệp <b>LS10- MTGK1-26-27-HHT.docx</b>)", S("CoverNote", parent=bodyc, fontSize=10, leading=15)))
A(Spacer(1, 8 * mm))
cover_tbl = table(
    [[P("Thời gian làm bài", th), P("Tổng điểm", th), P("Cấu trúc", th)],
     [P("45 phút", tdc), P("10,0 điểm", tdc),
      P("20 câu TN nhiều lựa chọn + 2 câu TN đúng/sai (8 ý) + 1 câu tự luận", tdc)]],
    widths=[38 * mm, 28 * mm, 100 * mm])
A(cover_tbl)
A(Spacer(1, 12 * mm))
A(P("<b>Nội dung ôn tập:</b> Chủ đề 1 – Lịch sử và sử học (Bài 1, Bài 2); "
    "Chủ đề 2 – Vai trò của sử học (Bài 3).",
    S("CoverScope", parent=bodyc, fontSize=9.6, leading=14, textColor=GREY)))
A(PageBreak())

# ---------------------------------------------------------------- TOC -------
h1_plain = S("H1Plain", parent=h1)
A(Paragraph("MỤC LỤC", h1_plain))
toc = TableOfContents()
toc.levelStyles = [toc_lvl0, toc_lvl1]
A(toc)
A(PageBreak())

# ================================================================ PHẦN A ====
A(Paragraph("PHẦN A. PHÂN TÍCH MA TRẬN VÀ HƯỚNG DẪN ÔN TẬP", h1))

A(Paragraph("1. Nguồn tham chiếu và phạm vi ôn tập", h2))
A(P("Đề cương này được soạn <b>bám sát 100% từng lệnh hỏi</b> trong ma trận chính thức "
    "<i>“Ma trận kiểm tra định kỳ giữa học kỳ 1 – Khối 10, năm học 2026 – 2027”</i> "
    "lưu trong tệp <b>LS10- MTGK1-26-27-HHT.docx</b>. Tệp gốc chứa ma trận và bảng đặc tả "
    "(yêu cầu theo năng lực, cấp độ tư duy, thang điểm) chứ không kèm văn bản từng câu hỏi; "
    "do đó, <b>Phần C</b> của đề cương xây dựng trọn bộ câu hỏi cho đủ 28 lệnh hỏi trắc nghiệm "
    "và 1 câu tự luận theo đúng vị trí, bài học, năng lực và cấp độ tư duy đã quy định, kèm đáp án "
    "và giải thích chi tiết.", lead))
A(P("<b>Phạm vi kiến thức:</b> Chủ đề 1 – Lịch sử và sử học (Bài 1: Hiện thực lịch sử và lịch sử "
    "được con người nhận thức; Bài 2: Tri thức lịch sử và cuộc sống) và Chủ đề 2 – Vai trò của sử "
    "học (Bài 3: Vai trò của sử học), theo sách giáo khoa Lịch sử 10 – bộ Kết nối tri thức với cuộc sống."))

A(Paragraph("2. Cấu trúc đề kiểm tra", h2))
A(table(
    [[P("Phần", th), P("Nội dung", th), P("Mã câu hỏi", th), P("Số lệnh", th), P("Điểm", th)],
     [P("I", tdc), P("Trắc nghiệm nhiều lựa chọn (chọn 1 đáp án đúng)", td),
      P("I.1 → I.20", tdc), P("20", tdc), P("5,00", tdc)],
     [P("II", tdc), P("Trắc nghiệm đúng/sai (mỗi câu 4 ý a–d)", td),
      P("II.1a–d; II.2a–d", tdc), P("8 ý", tdc), P("2,00", tdc)],
     [P("III", tdc), P("Trắc nghiệm tự luận (TL)", td),
      P("TL", tdc), P("1", tdc), P("3,00", tdc)],
     [P("", tdb), P("<b>Tổng cộng</b>", td), P("28 lệnh TN + 1 TL", tdb), P("29", tdb), P("<b>10,00</b>", tdb)]],
    widths=[16 * mm, 78 * mm, 38 * mm, 22 * mm, 18 * mm]))
A(P("Mỗi lệnh hỏi trắc nghiệm được 0,25 điểm. Câu tự luận 3,00 điểm = 1,00 điểm cho ý "
    "<b>nhận biết</b> (nêu) + 2,00 điểm cho ý <b>vận dụng</b> (đề xuất biện pháp, vận động cộng đồng).", note))

A(Paragraph("3. Bảng phân bổ theo ma trận (tra cứu nhanh vị trí câu hỏi)", h2))
A(table(
    [[P("Câu hỏi", th), P("Bài học", th), P("Năng lực môn học", th), P("Cấp độ tư duy", th), P("Điểm", th)],
     [P("I.1, I.2, I.3", tdc), P("Bài 1", tdc), P("NL1 – Tìm hiểu lịch sử", td), P("Biết (nhận biết)", tdc), P("0,75", tdc)],
     [P("I.4", tdc), P("Bài 1", tdc), P("NL1 – Tìm hiểu lịch sử", td), P("Hiểu (thông hiểu)", tdc), P("0,25", tdc)],
     [P("I.5, I.6", tdc), P("Bài 1", tdc), P("NL2 – Nhận thức và tư duy lịch sử", td), P("Hiểu (thông hiểu)", tdc), P("0,50", tdc)],
     [P("I.7, I.8, I.9", tdc), P("Bài 2", tdc), P("NL1 – Tìm hiểu lịch sử", td), P("Biết (nhận biết)", tdc), P("0,75", tdc)],
     [P("I.10, I.11", tdc), P("Bài 2", tdc), P("NL1 – Tìm hiểu lịch sử", td), P("Hiểu (thông hiểu)", tdc), P("0,50", tdc)],
     [P("I.12, I.13; II.1a", tdc), P("Bài 2", tdc), P("NL2 – Nhận thức và tư duy lịch sử", td), P("Biết (nhận biết)", tdc), P("0,75", tdc)],
     [P("II.1b", tdc), P("Bài 2", tdc), P("NL2 – Nhận thức và tư duy lịch sử", td), P("Hiểu (thông hiểu)", tdc), P("0,25", tdc)],
     [P("II.1c", tdc), P("Bài 2", tdc), P("NL3 – Vận dụng kiến thức, kĩ năng", td), P("Biết (nhận biết)", tdc), P("0,25", tdc)],
     [P("II.1d", tdc), P("Bài 2", tdc), P("NL3 – Vận dụng kiến thức, kĩ năng", td), P("Vận dụng", tdc), P("0,25", tdc)],
     [P("I.14, I.15; ½ TL", tdc), P("Bài 3", tdc), P("NL1 – Tìm hiểu lịch sử", td), P("Biết (nhận biết)", tdc), P("1,75", tdc)],
     [P("I.16", tdc), P("Bài 3", tdc), P("NL1 – Tìm hiểu lịch sử", td), P("Hiểu (thông hiểu)", tdc), P("0,25", tdc)],
     [P("I.17, I.18; II.2a", tdc), P("Bài 3", tdc), P("NL2 – Nhận thức và tư duy lịch sử", td), P("Biết (nhận biết)", tdc), P("0,75", tdc)],
     [P("I.19, I.20; II.2b", tdc), P("Bài 3", tdc), P("NL2 – Nhận thức và tư duy lịch sử", td), P("Hiểu (thông hiểu)", tdc), P("0,75", tdc)],
     [P("II.2c", tdc), P("Bài 3", tdc), P("NL3 – Vận dụng kiến thức, kĩ năng", td), P("Biết (nhận biết)", tdc), P("0,25", tdc)],
     [P("II.2d; ½ TL", tdc), P("Bài 3", tdc), P("NL3 – Vận dụng kiến thức, kĩ năng", td), P("Vận dụng", tdc), P("2,25", tdc)]],
    widths=[36 * mm, 18 * mm, 66 * mm, 32 * mm, 14 * mm]))
A(P("Tổng theo cấp độ: <b>Biết 5,0 điểm (50%) · Hiểu 2,5 điểm (25%) · Vận dụng 2,5 điểm (25%)</b>. "
    "Tổng theo năng lực: NL1 = 3,0 điểm; NL2 = 3,5 điểm; NL3 = 3,5 điểm.", note))

A(Paragraph("4. Chiến thuật làm bài 45 phút", h2))
for t in [
    "<b>Phần I (khoảng 15 phút):</b> làm nhanh 20 câu nhiều lựa chọn; đánh dấu câu khó, không bấm đồng hồ ở một câu quá 45 giây.",
    "<b>Phần II (khoảng 10 phút):</b> đọc kỹ từng ý a–d, xác định từ khóa (ví dụ “phân loại, đánh giá, thẩm định” là <i>xử lý</i>, không phải <i>thu thập</i>), ghi Đ/S và sửa ý sai.",
    "<b>Phần III (khoảng 15 phút):</b> viết đủ 2 ý theo thang điểm – ý 1 nêu mối quan hệ (1 điểm), ý 2 đề xuất biện pháp kèm ví dụ địa phương (2 điểm); mỗi ý 3–5 dòng ngắn gọn, gạch đầu dòng cũng được chấp nhận.",
    "<b>Kiểm tra lại (khoảng 5 phút):</b> đối chiếu mã câu, không bỏ sót ý nào của phần đúng/sai.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))
A(PageBreak())

# ================================================================ PHẦN B ====
A(Paragraph("PHẦN B. HỆ THỐNG LÝ THUYẾT VÀ MẸO GHI NHỚ", h1))

# ---------- CHỦ ĐỀ 1 ----------
A(Paragraph("CHỦ ĐỀ 1. LỊCH SỬ VÀ SỬ HỌC", h2))

# ----- BÀI 1 -----
A(Paragraph("BÀI 1. HIỆN THỰC LỊCH SỬ VÀ LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC", h3))

A(Paragraph("1.1. Lịch sử là gì?", h4))
for t in [
    "<b>Lịch sử</b> là toàn bộ những gì đã diễn ra trong quá khứ.",
    "<b>Lịch sử loài người</b> là toàn bộ những hoạt động của con người từ khi xuất hiện đến ngày nay, bao gồm: lịch sử quá trình tương tác của con người với tự nhiên và lịch sử quá trình con người tương tác với nhau.",
    "“Lịch sử” được hiểu theo <b>hai nghĩa</b>: <font face='DJS'>①</font> hiện thực lịch sử; <font face='DJS'>②</font> lịch sử được con người nhận thức.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("1.2. Hiện thực lịch sử và lịch sử được con người nhận thức", h4))
A(table(
    [[P("Tiêu chí", th), P("HIỆN THỰC LỊCH SỬ", th), P("LỊCH SỬ ĐƯỢC CON NGƯỜI NHẬN THỨC", th)],
     [P("Khái niệm", tdb),
      P("Là tất cả những gì đã diễn ra trong quá khứ.", td),
      P("Là những hiểu biết của con người về hiện thực lịch sử, được trình bày, tái hiện theo những cách khác nhau: kể chuyện, ghi chép, nghiên cứu, trình diễn, lập đài tưởng niệm, thực hành các nghi lễ, phong tục…", td)],
     [P("Tính chất", tdb),
      P("Tồn tại <b>hoàn toàn khách quan</b>, không phụ thuộc vào ý muốn chủ quan của con người; <b>chỉ có một, không thể thay đổi</b>; có trước.", td),
      P("Vừa mang tính khách quan (phụ thuộc hiện thực), vừa mang dấu ấn <b>chủ quan</b> của người nhận thức; <b>đa dạng, có thể được bổ sung, chỉnh sửa</b> theo thời gian; có sau.", td)],
     [P("Phụ thuộc vào", tdb),
      P("Chính những diễn biến đã xảy ra trong quá khứ.", td),
      P("Nguồn sử liệu, hoàn cảnh lịch sử – xã hội, mục đích – quan điểm – phương pháp nghiên cứu, trình độ của người nhận thức.", td)],
     [P("Ví dụ", tdb),
      P("Ngày 2/9/1945, Chủ tịch Hồ Chí Minh đọc Tuyên ngôn độc lập khai sinh nước Việt Nam Dân chủ Cộng hòa.", td),
      P("Nhiều cách mô tả, đánh giá khác nhau về ý nghĩa của sự kiện ngày 2/9/1945. (Gợi nhớ: em đứng trước gương – em là <b>hiện thực</b>, hình ảnh trong gương là <b>nhận thức</b>.)", td)]],
    widths=[24 * mm, 66 * mm, 84 * mm]))
for t in [
    "<b>Khoảng cách giữa hai:</b> giữa hiện thực lịch sử và nhận thức lịch sử <b>luôn có khoảng cách</b>; dù cố gắng đến đâu, con người cũng không thể nhận thức và tái hiện hoàn toàn, đầy đủ hiện thực lịch sử đúng như nó đã xảy ra.",
    "<b>Nguyên nhân:</b> nhận thức lịch sử phụ thuộc vào nguồn sử liệu, hoàn cảnh lịch sử – xã hội, mục đích – quan điểm – phương pháp nghiên cứu và trình độ của người nhận thức.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))
A(Paragraph("MẸO GHI NHỚ: “HIỆN – NHẬN” – hiện thực là cái <b>ĐÃ XẢY RA</b> (khách quan, 1, không đổi, có trước); "
            "nhận thức là cái <b>CON NGƯỜI BIẾT</b> (chủ quan một phần, nhiều, có thể đổi, có sau).", mnem))

A(Paragraph("1.3. Sử học (khoa học lịch sử)", h4))
for t in [
    "<b>Khái niệm:</b> Sử học là <b>khoa học nghiên cứu về quá khứ loài người</b>.",
    "<b>Đối tượng nghiên cứu:</b> hiện thực lịch sử – toàn bộ quá khứ của loài người.",
    "<b>Chức năng:</b> (1) <i>Chức năng khoa học</i> – cung cấp tri thức khoa học, giúp con người tìm hiểu, khám phá hiện thực lịch sử một cách khách quan, khoa học, chân thực; (2) <i>Chức năng xã hội (giáo dục)</i> – truyền bá những giá trị và truyền thống tốt đẹp của lịch sử cho thế hệ sau, góp phần giáo dục đạo đức, tinh thần dân tộc, tình yêu quê hương – đất nước, bồi dưỡng lòng khoan dung, nhân ái.",
    "<b>Nhiệm vụ:</b> tìm hiểu, khám phá và tái hiện trung thực hiện thực lịch sử; giải thích, đánh giá các sự kiện, hiện tượng lịch sử; truyền bá tri thức lịch sử; phục vụ việc kết nối quá khứ với hiện tại và tương lai.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("1.4. Nguyên tắc và phương pháp của sử học", h4))
A(table(
    [[P("Nguyên tắc", th), P("Nội dung cốt lõi", th)],
     [P("Khách quan", tdb), P("<b>Nguyên tắc quan trọng nhất.</b> Sứ mệnh của sử học là tái hiện hiện thực lịch sử, đưa nhận thức đầy đủ nhất về quá khứ dựa trên những thông tin đáng tin cậy.", td)],
     [P("Trung thực", tdb), P("Tôn trọng sự thật lịch sử, tái hiện một cách chân thực dựa trên nguồn sử liệu đáng tin cậy, không xuyên tạc sự thật lịch sử.", td)],
     [P("Nhân văn, tiến bộ", tdb), P("Đặt sự thật lịch sử và lợi ích của con người, của cộng đồng lên trên; phục vụ sự tiến bộ của xã hội.", td)]],
    widths=[38 * mm, 136 * mm]))
A(P("<b>Phương pháp cơ bản:</b> phương pháp <b>lịch sử</b> và phương pháp <b>logic</b>; sử học còn phối hợp "
    "nhiều phương pháp khác (xử lý sử liệu, diễn giải…) và các ngành khoa học liên ngành.", bullet))
A(Paragraph("MẸO GHI NHỚ nguyên tắc: <b>“KHÁCH – TRUNG – NHÂN”</b> (Khách quan · Trung thực · Nhân văn); "
            "phương pháp: <b>“LỊCH – LỐ”</b> (Lịch sử · Logic).", mnem))

A(Paragraph("1.5. Ý nghĩa câu nói của Ét-uốt Ha-lét Ca", h4))
A(P("“<i>Lịch sử là quá trình tương tác không ngừng giữa nhà sử học và sự thật lịch sử, là cuộc đối thoại "
    "không bao giờ dứt giữa hiện tại và quá khứ.</i>”", note))
for t in [
    "Nhấn mạnh <b>mối quan hệ tương tác giữa nhà sử học và hiện thực (sự thật) lịch sử</b>;",
    "Nhấn mạnh <b>mối quan hệ giữa quá khứ và hiện tại</b>;",
    "Hàm ý: để nhận thức lịch sử, cần có sự tương tác liên tục giữa nhà sử học với sự thật, giữa hiện tại với quá khứ – bởi giữa hiện thực và nhận thức luôn có khoảng cách.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

# ----- BÀI 2 -----
A(Paragraph("BÀI 2. TRI THỨC LỊCH SỬ VÀ CUỘC SỐNG", h3))

A(Paragraph("2.1. Vai trò, ý nghĩa của tri thức lịch sử", h4))
for t in [
    "Trang bị những hiểu biết về quá khứ cho cá nhân và xã hội.",
    "Giúp con người <b>hội nhập với thế giới</b>, tôn trọng sự khác biệt, tiếp thu có chọn lọc thành tựu nhân loại, tôn vinh – bảo tồn – phát huy những giá trị tốt đẹp.",
    "Mở ra những <b>cơ hội nghề nghiệp</b> mới đầy thú vị.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("2.2. Sự cần thiết của việc học tập và khám phá lịch sử suốt đời", h4))
for t in [
    "<b>Vì sao:</b> tri thức lịch sử chỉ là một phần và <b>luôn chưa đầy đủ</b> về toàn bộ sự thật lịch sử, nhất là khi lịch sử đang diễn ra, chưa bộc lộ hết những diễn biến và bản chất của nó.",
    "<b>Ý nghĩa:</b> học tập, tìm hiểu, khám phá lịch sử suốt đời là điều kiện quan trọng giúp mỗi người <b>cập nhật và mở rộng tri thức, phát triển và hoàn thiện kĩ năng</b>.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("2.3. Sử liệu", h4))
for t in [
    "<b>Khái niệm:</b> sử liệu là <b>toàn bộ những hình thức khác nhau của tư liệu lịch sử, chứa đựng những thông tin về quá khứ loài người</b>.",
    "<b>Vai trò:</b> sử liệu là <b>cầu nối giữa hiện thực lịch sử và tri thức lịch sử</b>; nguồn sử liệu có vai trò <b>quan trọng nhất</b> trong quá trình khôi phục các sự kiện lịch sử. Vì hiện thực lịch sử tồn tại độc lập với ý thức con người, muốn hiểu biết sự thật lịch sử, về phương pháp phải <b>bắt đầu từ sử liệu, dùng sử liệu để khôi phục sự kiện</b>, sau đó mới giải thích và đánh giá sự kiện.",
    "<b>Loại hình:</b> sử liệu <b>thành văn</b> (sách, chiếu, sắc, báo chí…), <b>hiện vật</b>, <b>hình ảnh</b>, <b>lời nói – truyền khẩu</b>; sử liệu <b>sơ cấp</b> và <b>thứ cấp</b>.",
    "<b>Kĩ năng:</b> khi thu thập phải <b>ghi chép nguồn gốc, xuất xứ</b> của sử liệu.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("2.4. Thu thập và xử lý thông tin, sử liệu", h4))
A(table(
    [[P("Quá trình", th), P("Định nghĩa", th), P("Nhiệm vụ chính", th)],
     [P("<b>Thu thập</b> thông tin, sử liệu", td),
      P("Quá trình khảo sát, sưu tầm, tìm kiếm và tập hợp những thông tin liên quan đến đối tượng học tập, nghiên cứu, tìm hiểu lịch sử.", td),
      P("Lập danh mục; tìm kiếm, thu thập thông tin; ghi chép nguồn gốc, xuất xứ.", td)],
     [P("<b>Xử lý</b> thông tin, sử liệu", td),
      P("Quá trình phân loại, đánh giá, thẩm định, so sánh những nguồn sử liệu đã thu thập được.", td),
      P("Xác định <b>tính xác thực, độ tin cậy, giá trị thông tin</b> của sử liệu.", td)]],
    widths=[34 * mm, 78 * mm, 62 * mm]))
A(Paragraph("Quy trình 4 bước (thu thập – xử lý thông tin và sử liệu):", h4))
A(table(
    [[P("Bước", th), P("Nội dung", th)],
     [P("Bước 1", tdb), P("<b>Lập thư mục và danh mục</b> các nguồn sử liệu cần thu thập để phục vụ việc học tập, nghiên cứu, tìm hiểu lịch sử.", td)],
     [P("Bước 2", tdb), P("<b>Sưu tầm, đọc và ghi chép</b> thông tin sử liệu liên quan đến vấn đề nghiên cứu (có thể dùng phỏng vấn, bảng hỏi, khảo sát, quan sát, điền dã…).", td)],
     [P("Bước 3", tdb), P("<b>Chọn lọc, phân loại</b> sử liệu để thuận lợi cho việc xác minh và đánh giá.", td)],
     [P("Bước 4", tdb), P("<b>Xác minh, đánh giá</b> về nguồn gốc sử liệu, thời điểm ra đời, nội dung sử liệu phản ánh…", td)]],
    widths=[22 * mm, 152 * mm]))
A(Paragraph("MẸO GHI NHỚ quy trình 4 bước: <b>“Lập – Sưu – Chọn – Xác”</b> "
            "(1.Lập thư mục → 2.Sưu tầm ghi chép → 3.Chọn lọc phân loại → 4.Xác minh đánh giá). "
            "Câu hỏi sắp thứ tự chỉ cần bấm theo 4 chữ L – S – C – X.", mnem))

A(Paragraph("2.5. Kết nối tri thức, bài học lịch sử vào cuộc sống", h4))
for t in [
    "<b>Khái niệm:</b> kết nối tri thức, bài học lịch sử vào cuộc sống chính là <b>sử dụng tri thức lịch sử để giải thích và hiểu rõ hơn những vấn đề của cuộc sống hiện tại</b> (vấn đề thời sự trong nước và thế giới, vấn đề thực tiễn – ở mức độ đơn giản).",
    "<b>Cơ sở:</b> <i>hiện tại luôn khởi nguồn từ quá khứ</i> – những vấn đề thực tiễn hiện nay đều bắt nguồn từ những gì đã diễn ra trong quá khứ, là kết quả của quá trình hình thành, phát triển, biến đổi qua thời gian; tri thức lịch sử liên hệ chặt chẽ với các lĩnh vực chính trị, kinh tế, văn hóa, giáo dục, môi trường…",
    "<b>Quan hệ ba kỳ:</b> quá khứ (lịch sử đã qua) → hiện tại (kế thừa, xây dựng trên nền quá khứ) → tương lai (định hướng trên cơ sở quá khứ và hiện tại).",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

# ----- CHỦ ĐỀ 2 / BÀI 3 -----
A(Paragraph("CHỦ ĐỀ 2. VAI TRÒ CỦA SỬ HỌC", h2))
A(Paragraph("BÀI 3. VAI TRÒ CỦA SỬ HỌC", h3))

A(Paragraph("3.1. Sử học với công tác bảo tồn và phát huy giá trị di sản văn hóa, di sản thiên nhiên", h4))
A(Paragraph("<b>a) Mối quan hệ giữa sử học và công tác bảo tồn, phát huy giá trị di sản</b>", h4))
for t in [
    "Giá trị của các di sản được thể hiện ở nhiều khía cạnh: <b>lịch sử, văn hóa, kiến trúc, mỹ thuật…</b>",
    "Mọi sự kiện, hiện tượng lịch sử đều gắn với điều kiện tự nhiên và bối cảnh chính trị – xã hội cụ thể; nhà sử học không thể mô tả, phục dựng đầy đủ bức tranh quá khứ nếu chỉ dùng tri thức hoặc phương pháp lịch sử đơn thuần.",
    "Việc sử dụng phương pháp nghiên cứu của sử học với tư cách là một <b>khoa học có tính liên ngành</b> <b>đóng vai trò quan trọng nhất trong việc khẳng định giá trị của di sản</b>.",
    "Kết quả nghiên cứu của sử học về giá trị di sản là <b>cơ sở khoa học vững chắc</b> cho công tác bảo tồn và phát huy giá trị di sản <b>một cách bền vững, vì lợi ích chung của toàn xã hội</b>.",
    "<b>Yêu cầu cốt lõi</b> của bảo tồn: đảm bảo <b>tính nguyên trạng</b>, giữ được <b>“yếu tố gốc cấu thành di tích”</b>, đảm bảo <b>“tính xác thực”, “tính toàn vẹn”, “giá trị nổi bật”</b> của di sản, dựa trên cơ sở <b>cứ liệu và phương pháp khoa học</b>.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))
A(Paragraph("MẸO GHI NHỚ yêu cầu bảo tồn: <b>“NGUYÊN – GỐC – XÁC – TOÀN – NỔI”</b> "
            "(nguyên trạng · yếu tố gốc · xác thực · toàn vẹn · giá trị nổi bật), tất cả dựa trên <b>cứ liệu và phương pháp khoa học</b>.", mnem))

A(Paragraph("<b>b) Vai trò của công tác bảo tồn và phát huy giá trị di sản</b>", h4))
A(table(
    [[P("Loại hình di sản", th), P("Thách thức, nguy cơ", th), P("Vai trò của bảo tồn và phát huy", th)],
     [P("<b>Di sản văn hóa vật thể</b> (thành quách, lăng tẩm, đền, tháp, cung điện, nhà cổ… làm bằng đất, đá, gạch, gỗ, tre, nứa, lá…)", td),
      P("Dễ biến dạng, xuống cấp, hư hỏng theo thời gian; chịu tác động của điều kiện tự nhiên và của con người.", td),
      P("Hạn chế và khắc phục có hiệu quả những tác động tiêu cực của điều kiện tự nhiên và con người.", td)],
     [P("<b>Di sản văn hóa phi vật thể</b> (lễ hội, nghề thủ công truyền thống, nghệ thuật trình diễn…)", td),
      P("Đối mặt với nhiều thách thức và nguy cơ mai một.", td),
      P("Thông qua sưu tầm, lưu giữ, truyền nghề, trình diễn… mà di sản được <b>tái tạo, giữ gìn và lưu truyền từ thế hệ này sang thế hệ khác</b>.", td)],
     [P("<b>Di sản thiên nhiên</b> (vịnh, hang động, vườn quốc gia…)", td),
      P("Suy giảm đa dạng sinh học, mất giá trị khoa học.", td),
      P("Góp phần phát triển <b>đa dạng sinh học</b>, làm tăng <b>giá trị khoa học</b> của di sản.", td)]],
    widths=[52 * mm, 54 * mm, 68 * mm]))
for t in [
    "Bảo tồn và phát huy giá trị các di sản góp phần <b>phát triển kinh tế – xã hội địa phương</b>;",
    "Góp phần <b>duy trì kí ức và bản sắc cộng đồng</b>, <b>giáo dục thế hệ trẻ</b>, <b>bảo vệ đa dạng văn hóa</b>.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("<b>c) Loại hình di sản và địa danh tài nguyên du lịch</b>", h4))
for t in [
    "<b>Loại hình di sản văn hóa:</b> <font face='DJS'>①</font> di sản văn hóa <b>vật thể</b>; <font face='DJS'>②</font> di sản văn hóa <b>phi vật thể</b> (riêng di sản <b>thiên nhiên</b> là loại hình độc lập).",
    "<b>Một số địa danh là tài nguyên du lịch của Việt Nam</b> (ví dụ): Vịnh Hạ Long (Quảng Ninh), Quần thể di tích Cố đô Huế (Thừa Thiên Huế), Phố cổ Hội An và Thánh địa Mỹ Sơn (Quảng Nam), Động Phong Nha – Kẻ Bàng (Quảng Bình), Văn Miếu – Quốc Tử Giám (Hà Nội), Đền Hùng (Phú Thọ)…",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("3.2. Sử học với sự phát triển du lịch", h4))
A(Paragraph("<b>a) Vai trò của lịch sử và văn hóa đối với sự phát triển du lịch</b>", h4))
for t in [
    "Những giá trị về lịch sử và văn hóa của mỗi dân tộc, của toàn nhân loại là <b>nguồn tài nguyên quý báu của du lịch</b>, đặc biệt là <b>du lịch văn hóa</b>.",
    "Lịch sử – văn hóa cung cấp tri thức để quảng bá, thúc đẩy du lịch phát triển bền vững; cung cấp bài học kinh nghiệm, mô hình khai thác phù hợp.",
]:
    A(Paragraph(T(t), bullet, bulletText="•"))

A(Paragraph("<b>b) Vai trò của du lịch đối với công tác bảo tồn di tích lịch sử, di sản văn hóa</b> "
            "(mối quan hệ tương tác hai chiều)", h4))
A(table(
    [[P("Tác động TÍCH CỰC", th), P("Tiêu cực (nếu khai thác thiếu kiểm soát)", th)],
     [P("Nhu cầu tham quan, tìm hiểu, trải nghiệm của du khách <b>thôi thúc chính quyền và nhân dân</b> gìn giữ, bảo tồn, phục dựng, phát huy giá trị di tích, di sản.", td),
      P("Xây dựng tùy tiện, thương mại hóa lễ hội, khai thác quá mức làm di sản <b>bị tổn hại</b>.", td)],
     [P("<b>Một phần doanh thu của du lịch được tái đầu tư</b> vào việc bảo tồn, tôn tạo, phục dựng và quản lí di tích, di sản.", td),
      P("Áp lực lượng khách làm xuống cấp công trình, biến dạng không gian văn hóa.", td)],
     [P("Các di sản văn hóa phi vật thể cũng được <b>sưu tầm, nghiên cứu, phục dựng, truyền dạy</b>…", td),
      P("…", td)]],
    widths=[87 * mm, 87 * mm]))
A(Paragraph("KẾT LUẬN (hay gặp trong câu vận dụng): phải <b>phát triển du lịch gắn với bảo tồn</b> – "
            "khai thác hiệu quả nhưng giữ nguyên không gian, yếu tố gốc của di sản.", mnem))

A(Paragraph("3.3. Bảng tổng hợp ghi nhớ nhanh toàn Chủ đề 1 và Chủ đề 2", h4))
A(table(
    [[P("Chủ đề/Bài", th), P("“Xương sống” cần nhớ", th)],
     [P("<b>Bài 1</b><br/>Hiện thực & nhận thức", td),
      P("Lịch sử = những gì đã diễn ra trong quá khứ → 2 nghĩa: hiện thực (khách quan, 1, không đổi) + nhận thức (chủ quan một phần, đa dạng) → luôn có khoảng cách → sử học: nghiên cứu quá khứ loài người, đối tượng = hiện thực lịch sử, chức năng khoa học + xã hội, nguyên tắc KHÁCH – TRUNG – NHÂN, phương pháp LỊCH – LỐ.", td)],
     [P("<b>Bài 2</b><br/>Tri thức lịch sử & cuộc sống", td),
      P("Tri thức lịch sử chưa đầy đủ → học khám phá lịch sử suốt đời → sử liệu (cầu nối hiện thực – tri thức; quan trọng nhất để khôi phục sự kiện) → thu thập vs xử lý → quy trình LẬP – SƯU – CHỌN – XÁC → kết nối tri thức vào cuộc sống = dùng tri thức lịch sử giải thích vấn đề hiện tại.", td)],
     [P("<b>Bài 3</b><br/>Vai trò của sử học", td),
      P("Sử học liên ngành = vai trò quan trọng nhất khẳng định giá trị di sản, cơ sở khoa học cho bảo tồn → yêu cầu NGUYÊN – GỐC – XÁC – TOÀN – NỔI → 3 loại hình di sản (vật thể, phi vật thể, thiên nhiên) → lịch sử – văn hóa = tài nguyên du lịch quý báu ↔ du lịch tái đầu tư, thôi thúc bảo tồn → phát triển du lịch GẮN VỚI BẢO TỒN.", td)]],
    widths=[38 * mm, 136 * mm]))

A(Paragraph("3.4. Lỗi sai thường gặp khi làm bài", h4))
A(Paragraph("• Nhầm “lịch sử được con người nhận thức” là cái đã xảy ra – đó là <b>hiện thực lịch sử</b>.<br/>"
            "• Cho rằng hiện thực lịch sử thay đổi theo quan điểm người viết – hiện thực <b>không đổi</b>, chỉ nhận thức thay đổi.<br/>"
            "• Tưởng khoảng cách giữa hiện thực và nhận thức là do “sự liệu luôn sai” – thực ra do nhiều yếu tố: sử liệu, hoàn cảnh, quan điểm, phương pháp, trình độ người nhận thức.<br/>"
            "• Đổi thứ tự thu thập ↔ xử lý: <b>thu thập = sưu tầm, tìm kiếm, tập hợp</b>; <b>xử lý = phân loại, đánh giá, thẩm định, so sánh</b>.<br/>"
            "• Nhầm quy trình 4 bước (Lập → Sưu → Chọn → Xác).<br/>"
            "• Tưởng di sản thiên nhiên là một loại hình của di sản văn hóa – hai khái niệm <b>khác nhau</b>.<br/>"
            "• Tưởng “bảo tồn” là xây mới, hiện đại hóa – bảo tồn là giữ <b>nguyên trạng, xác thực</b>.<br/>"
            "• Quên mặt trái của du lịch: khai thác thiếu kiểm soát sẽ phá hoại di sản.", warn))
A(PageBreak())

# ================================================================ PHẦN C ====
A(Paragraph("PHẦN C. HỆ THỐNG CÂU HỎI THEO MA TRẬN – KÈM ĐÁP ÁN", h1))
A(P("Đủ 28 lệnh hỏi trắc nghiệm (20 câu nhiều lựa chọn + 8 ý đúng/sai) và 1 câu tự luận, "
    "theo đúng mã câu, bài học, năng lực và cấp độ tư duy trong ma trận đề kiểm tra.", lead))

A(Paragraph("PHẦN I. 20 CÂU TRẮC NGHIỆN NHIỀU LỰA CHỌN (I.1 – I.20)", h2))
A(P("Hướng dẫn: chọn một đáp án đúng nhất. Mỗi câu 0,25 điểm.", note))

# --- Bài 1: I.1 - I.6
A(Paragraph("Các câu I.1 – I.6 · Bài 1: Hiện thực lịch sử và lịch sử được con người nhận thức", h4))
A(mc("I.1", "Bài 1 · NL1 · Biết · 0,25 đ",
     "Lịch sử được hiểu là:",
     ["những gì đã diễn ra trong quá khứ.",
      "những gì đang diễn ra ở hiện tại.",
      "ngành khoa học dự đoán về tương lai.",
      "những gì sẽ diễn ra trong tương lai."],
     "A",
     "Theo SGK, lịch sử là những gì đã diễn ra trong quá khứ; lịch sử loài người là toàn bộ hoạt động của con người từ khi xuất hiện đến ngày nay."))
A(mc("I.2", "Bài 1 · NL1 · Biết · 0,25 đ",
     "Hiện thực lịch sử là:",
     ["quá trình con người tái hiện lại quá khứ.",
      "những hiểu biết của con người về quá khứ.",
      "những nghiên cứu của con người về quá khứ.",
      "toàn bộ những gì đã diễn ra trong quá khứ."],
     "D",
     "Hiện thực lịch sử là tất cả những gì đã diễn ra trong quá khứ, tồn tại hoàn toàn khách quan, không phụ thuộc vào ý muốn chủ quan của con người."))
A(mc("I.3", "Bài 1 · NL1 · Biết · 0,25 đ",
     "Lịch sử được con người nhận thức là:",
     ["những hiểu biết của con người về hiện thực lịch sử, được trình bày, tái hiện theo những cách khác nhau.",
      "toàn bộ những hoạt động của con người trong quá khứ.",
      "ngành khoa học nghiên cứu về quá khứ loài người.",
      "hệ thống hiện vật được lưu giữ trong các bảo tàng."],
     "A",
     "Đó là những hiểu biết của con người về hiện thực lịch sử, được trình bày, tái hiện bằng nhiều cách: kể chuyện, ghi chép, nghiên cứu, trình diễn, lập đài tưởng niệm…"))
A(mc("I.4", "Bài 1 · NL1 · Hiểu · 0,25 đ",
     "Phát biểu: “Lịch sử là quá trình tương tác không ngừng giữa nhà sử học và sự thật lịch sử, "
     "là cuộc đối thoại không bao giờ dứt giữa hiện tại và quá khứ” (Ét-uốt Ha-lét Ca). "
     "Phát biểu trên hàm ý nhấn mạnh:",
     ["lịch sử chỉ là những câu chuyện được kể lại cho hậu thế.",
      "mối quan hệ tương tác giữa nhà sử học và hiện thực lịch sử, giữa hiện tại và quá khứ trong quá trình nhận thức lịch sử.",
      "lịch sử luôn lặp lại theo những chu kỳ cố định.",
      "hiện thực lịch sử và nhận thức lịch sử là một."],
     "B",
     "Câu nói thể hiện mối quan hệ giữa nhà sử học với sự thật lịch sử và giữa hiện tại với quá khứ; "
     "do giữa hiện thực và nhận thức luôn có khoảng cách nên nhà sử học phải không ngừng tương tác với sự thật lịch sử."))
A(mc("I.5", "Bài 1 · NL2 · Hiểu · 0,25 đ",
     "Trong các nhận định sau, nhận định thể hiện đúng mối quan hệ giữa hiện thực lịch sử và lịch sử được con người nhận thức là:",
     ["hiện thực lịch sử chỉ có một và không thể thay đổi; nhận thức lịch sử tuy phụ thuộc hiện thực nhưng có thể khác nhau và được bổ sung theo thời gian.",
      "hiện thực lịch sử thay đổi theo quan điểm của mỗi người.",
      "nhận thức lịch sử luôn phản ánh đúng và đầy đủ hiện thực lịch sử.",
      "không có hiện thực lịch sử thì vẫn có thể có nhận thức lịch sử."],
     "A",
     "Hiện thực là duy nhất, khách quan, không đổi; nhận thức có trước có sau, đa dạng, vừa khách quan vừa chủ quan. "
     "Không có hiện thực lịch sử thì không có nhận thức lịch sử; nhận thức không thể phản ánh đầy đủ hiện thực."))
A(mc("I.6", "Bài 1 · NL2 · Hiểu · 0,25 đ",
     "Cùng một sự kiện lịch sử (ví dụ: ngày 2/9/1945) lại được nhiều tác giả mô tả, đánh giá khác nhau. "
     "Thông tin trên làm căn cứ để khẳng định điều gì?",
     ["hiện thực lịch sử tồn tại ở nhiều dạng khác nhau.",
      "giữa hiện thực lịch sử và lịch sử được con người nhận thức luôn có khoảng cách.",
      "tất cả các mô tả về sự kiện đó đều sai lệch.",
      "lịch sử không phải là hiện thực khách quan."],
     "B",
     "Khoảng cách nảy sinh vì nhận thức lịch sử phụ thuộc vào nguồn sử liệu, hoàn cảnh lịch sử – xã hội, "
     "mục đích, quan điểm, phương pháp nghiên cứu và trình độ của người nhận thức; hiện thực vẫn chỉ có một và không đổi."))

# --- Bài 2: I.7 - I.13
A(Paragraph("Các câu I.7 – I.13 · Bài 2: Tri thức lịch sử và cuộc sống", h4))
A(mc("I.7", "Bài 2 · NL1 · Biết · 0,25 đ",
     "Thứ tự đúng của quy trình thu thập, xử lý thông tin và sử liệu trong học tập, khám phá lịch sử là:",
     ["xác minh, đánh giá → lập thư mục → chọn lọc, phân loại → sưu tầm, ghi chép.",
      "sưu tầm, ghi chép → lập thư mục → xác minh, đánh giá → chọn lọc, phân loại.",
      "lập thư mục và danh mục → sưu tầm, đọc và ghi chép → chọn lọc, phân loại → xác minh, đánh giá.",
      "chọn lọc, phân loại → sưu tầm, đọc và ghi chép → lập thư mục → xác minh, đánh giá."],
     "C",
     "Ghi nhớ 4 bước “Lập – Sưu – Chọn – Xác”."))
A(mc("I.8", "Bài 2 · NL1 · Biết · 0,25 đ",
     "Việc phân loại, đánh giá, thẩm định, so sánh những nguồn sử liệu đã thu thập được thuộc quá trình:",
     ["thu thập thông tin và sử liệu.",
      "xử lý thông tin và sử liệu.",
      "lập thư mục và danh mục các nguồn sử liệu.",
      "trình bày kết quả tìm hiểu lịch sử."],
     "B",
     "Xử lý thông tin, sử liệu là quá trình phân loại, đánh giá, thẩm định, so sánh nguồn sử liệu đã thu thập; "
     "mục đích xác định tính xác thực, độ tin cậy và giá trị thông tin."))
A(mc("I.9", "Bài 2 · NL1 · Biết · 0,25 đ",
     "Sử liệu là:",
     ["toàn bộ những hình thức khác nhau của tư liệu lịch sử, chứa đựng những thông tin về quá khứ loài người.",
      "những hiểu biết của con người về hiện thực lịch sử.",
      "khoa học nghiên cứu về quá khứ loài người.",
      "phương pháp tái hiện lại các sự kiện trong quá khứ."],
     "A",
     "Đúng theo định nghĩa SGK; sử liệu gồm hình thức thành văn, hiện vật, hình ảnh, lời nói – truyền khẩu…"))
A(mc("I.10", "Bài 2 · NL1 · Hiểu · 0,25 đ",
     "Vì sao mỗi người cần học tập và khám phá lịch sử suốt đời?",
     ["vì lịch sử luôn thay đổi nên kiến thức cũ nhanh chóng trở nên sai lệch.",
      "vì tri thức lịch sử chỉ là một phần và luôn chưa đầy đủ về toàn bộ sự thật lịch sử, nhất là khi lịch sử đang diễn ra.",
      "vì sách giáo khoa không ghi chép đầy đủ các sự kiện lịch sử.",
      "vì lịch sử chỉ có giá trị đối với các nhà nghiên cứu chuyên nghiệp."],
     "B",
     "Học tập, khám phá lịch sử suốt đời giúp cập nhật, mở rộng tri thức và phát triển, hoàn thiện kĩ năng."))
A(mc("I.11", "Bài 2 · NL1 · Hiểu · 0,25 đ",
     "Kết nối tri thức, bài học lịch sử vào cuộc sống chính là:",
     ["sử dụng tri thức lịch sử để giải thích và hiểu rõ hơn những vấn đề của cuộc sống hiện tại.",
      "kết nối hiện thực lịch sử với nhận thức lịch sử bằng nguồn sử liệu.",
      "sưu tầm và lưu giữ sử liệu trong thư viện.",
      "ghi nhớ các sự kiện lịch sử để phục vụ kiểm tra."],
     "A",
     "Đúng theo SGK; vì hiện tại luôn khởi nguồn từ quá khứ nên có thể dùng tri thức lịch sử để giải thích "
     "vấn đề thời sự, thực tiễn của hiện tại."))
A(mc("I.12", "Bài 2 · NL2 · Biết · 0,25 đ",
     "Yếu tố đóng vai trò quan trọng nhất trong quá trình khôi phục các sự kiện lịch sử là:",
     ["trí tưởng tượng của nhà nghiên cứu.",
      "nguồn sử liệu.",
      "quan điểm của người kể chuyện.",
      "phương tiện truyền thông hiện đại."],
     "B",
     "Hiện thực lịch sử tồn tại độc lập với ý thức con người; muốn hiểu sự thật lịch sử phải bắt đầu từ sử liệu, "
     "dùng sử liệu để khôi phục sự kiện, sau đó mới giải thích và đánh giá."))
A(mc("I.13", "Bài 2 · NL2 · Biết · 0,25 đ",
     "Trong học tập và khám phá lịch sử, sử liệu được ví là:",
     ["cầu nối giữa hiện thực lịch sử và tri thức lịch sử.",
      "kết quả cuối cùng của quá trình nghiên cứu lịch sử.",
      "sự thay thế hoàn toàn cho hiện thực lịch sử.",
      "quan điểm của nhà sử học về quá khứ."],
     "A",
     "Sử liệu nối liền hiện thực lịch sử (cái đã xảy ra) với tri thức lịch sử (cái con người biết về quá khứ)."))

# --- Bài 3: I.14 - I.20
A(Paragraph("Các câu I.14 – I.20 · Bài 3: Vai trò của sử học", h4))
A(mc("I.14", "Bài 3 · NL1 · Biết · 0,25 đ",
     "Di sản văn hóa được chia thành các loại hình:",
     ["di sản văn hóa vật thể và di sản văn hóa phi vật thể.",
      "di sản văn hóa và di sản thiên nhiên.",
      "di sản vật chất và di sản tinh thần.",
      "di tích lịch sử và danh lam thắng cảnh."],
     "A",
     "Di sản văn hóa gồm hai loại hình: vật thể và phi vật thể; di sản thiên nhiên là loại hình riêng."))
A(mc("I.15", "Bài 3 · NL1 · Biết · 0,25 đ",
     "Trong các di sản sau, di sản văn hóa phi vật thể là:",
     ["chùa Một Cột (Hà Nội).",
      "nghệ thuật hát Ca trù.",
      "thành Nhà Hồ (Thanh Hóa).",
      "đền Hùng (Phú Thọ)."],
     "B",
     "Ca trù là nghệ thuật trình diễn, thuộc di sản văn hóa phi vật thể (được UNESCO ghi danh); "
     "chùa Một Cột, thành Nhà Hồ, đền Hùng là di sản văn hóa vật thể (công trình kiến trúc, di tích)."))
A(mc("I.16", "Bài 3 · NL1 · Hiểu · 0,25 đ",
     "Điểm chung cốt lõi của các yêu cầu bảo tồn di sản (tính nguyên trạng, “yếu tố gốc cấu thành di tích”, "
     "“tính xác thực”, “tính toàn vẹn”, “giá trị nổi bật”) là gì?",
     ["phải thay thế di sản cũ bằng công trình hiện đại hơn.",
      "phải giữ gìn tính nguyên gốc, chân xác của di sản, dựa trên cơ sở cứ liệu và phương pháp khoa học.",
      "phải hạn chế mọi hoạt động tham quan tại di tích.",
      "phải ưu tiên phát triển kinh tế trước khi nghĩ đến bảo tồn."],
     "B",
     "Điểm chung là giữ nguyên trạng, xác thực, toàn vẹn cho di sản, mọi việc tu bổ, phục dựng đều phải "
     "dựa trên cứ liệu và phương pháp khoa học; xây mới, hiện đại hóa sẽ phá hủy giá trị lịch sử của di sản."))
A(mc("I.17", "Bài 3 · NL2 · Biết · 0,25 đ",
     "Kết quả nghiên cứu của sử học về giá trị của di sản có vai trò gì đối với công tác bảo tồn?",
     ["là cơ sở khoa học vững chắc cho công tác bảo tồn và phát huy giá trị di sản một cách bền vững, vì lợi ích chung của toàn xã hội.",
      "quyết định sự tồn tại vật chất của chính di sản.",
      "thay thế toàn bộ hoạt động bảo tồn di sản.",
      "chỉ có ý nghĩa đối với các nhà sử học."],
     "A",
     "Sử học không quyết định sự tồn tại của di sản (di sản tồn tại khách quan) mà cung cấp cơ sở khoa học "
     "để khẳng định giá trị, bảo tồn và phát huy giá trị di sản bền vững."))
A(mc("I.18", "Bài 3 · NL2 · Biết · 0,25 đ",
     "Theo SGK, giá trị của các di sản được thể hiện ở nhiều khía cạnh. Trong các khía cạnh sau, "
     "khía cạnh KHÔNG nằm trong số đó là:",
     ["lịch sử.",
      "văn hóa.",
      "kiến trúc.",
      "kinh tế."],
     "D",
     "Giá trị của di sản được thể hiện ở các khía cạnh: lịch sử, văn hóa, kiến trúc, mỹ thuật… "
     "“Kinh tế” là lợi ích có được khi khai thác di sản, không phải khía cạnh giá trị của di sản theo SGK."))
A(mc("I.19", "Bài 3 · NL2 · Hiểu · 0,25 đ",
     "Vì sao những giá trị lịch sử, văn hóa được coi là tài nguyên của du lịch?",
     ["vì chúng là nguồn tài nguyên quý báu của du lịch, đặc biệt là du lịch văn hóa.",
      "vì du lịch hiện đại không cần đến bất kỳ tài nguyên nào khác.",
      "vì lịch sử – văn hóa chỉ phục vụ mục đích nghiên cứu khoa học.",
      "vì di sản có thể dễ dàng thay thế bằng công trình mới."],
     "A",
     "Những giá trị lịch sử, văn hóa của mỗi dân tộc, của toàn nhân loại là nguồn tài nguyên quý báu "
     "của du lịch, nhất là du lịch văn hóa; tri thức lịch sử – văn hóa còn giúp quảng bá, thúc đẩy du lịch bền vững."))
A(mc("I.20", "Bài 3 · NL2 · Hiểu · 0,25 đ",
     "Du lịch có tác động tích cực đối với công tác bảo tồn di tích, di sản khi:",
     ["một phần doanh thu của du lịch được tái đầu tư vào việc bảo tồn, tôn tạo, phục dựng và quản lí di tích, di sản.",
      "xây dựng nhiều công trình hiện đại xung quanh khu di tích.",
      "thương mại hóa các lễ hội truyền thống để tăng doanh thu.",
      "khai thác quá mức nhằm gia tăng số lượng du khách."],
     "A",
     "Tích cực: nhu cầu tham quan thôi thúc chính quyền và nhân dân gìn giữ, bảo tồn, phục dựng di tích; "
     "doanh thu du lịch tái đầu tư cho bảo tồn. Nếu khai thác thiếu kiểm soát sẽ gây tổn hại cho di sản, "
     "vì vậy phải phát triển du lịch gắn với bảo tồn."))

# --- Phần II ---
A(Spacer(1, 4 * mm))
A(Paragraph("PHẦN II. 2 CÂU TRẮC NGHIỆN ĐÚNG/SAI (II.1 và II.2 – 8 Ý, 2,00 ĐIỂM)", h2))
A(P("Hướng dẫn: với mỗi ý, ghi ĐÚNG hoặc SAI; nếu sai, nêu lại nội dung đúng. Mỗi ý 0,25 điểm.", note))

A(Paragraph("CÂU II.1 · Bài 2: Tri thức lịch sử và cuộc sống (1,00 điểm)", h4))
A(dungsai("II.1a", "NL2 · Biết · 0,25 đ",
          "Ý a. Quy trình thu thập, xử lý thông tin và sử liệu gồm 4 bước: (1) lập thư mục và danh mục "
          "các nguồn sử liệu; (2) sưu tầm, đọc và ghi chép thông tin sử liệu; (3) chọn lọc, phân loại "
          "sử liệu; (4) xác minh, đánh giá về nguồn gốc, thời điểm ra đời, nội dung sử liệu phản ánh.",
          "D",
          "Đúng theo quy trình trong SGK – thứ tự “Lập → Sưu → Chọn → Xác” không đảo lộn."))
A(dungsai("II.1b", "NL2 · Hiểu · 0,25 đ",
          "Ý b. Vì toàn bộ sự thật lịch sử đã được ghi chép đầy đủ trong sách nên con người không cần "
          "học tập và khám phá lịch sử suốt đời.",
          "S",
          "Sai. Tri thức lịch sử chỉ là một phần và luôn chưa đầy đủ về toàn bộ sự thật lịch sử, "
          "nhất là khi lịch sử đang diễn ra; do đó phải học tập, khám phá lịch sử suốt đời để "
          "cập nhật, mở rộng tri thức, phát triển và hoàn thiện kĩ năng."))
A(dungsai("II.1c", "NL3 · Biết · 0,25 đ",
          "Ý c. Để thu thập thông tin, sử liệu phục vụ việc học tập, khám phá lịch sử, chỉ cần tra cứu "
          "sách vở trong thư viện, không cần các phương pháp khác.",
          "S",
          "Sai. Có thể thu thập bằng nhiều cách: phỏng vấn, sử dụng bảng hỏi, khảo sát, quan sát, điền dã… "
          "bên cạnh việc đọc, ghi chép từ sách, tư liệu; nguồn gồm sử liệu sơ cấp, thứ cấp và nhiều loại hình "
          "(thành văn, hiện vật, hình ảnh, lời nói – truyền khẩu)."))
A(dungsai("II.1d", "NL3 · Vận dụng · 0,25 đ",
          "Ý d. Bài học “hiện tại luôn khởi nguồn từ quá khứ” cho phép ta vận dụng tri thức lịch sử "
          "để giải thích những vấn đề thời sự, thực tiễn của cuộc sống hiện tại, vì các vấn đề hiện nay "
          "đều xuất phát và là kết quả của quá trình hình thành, phát triển trong quá khứ.",
          "D",
          "Đúng. Đó chính là “kết nối tri thức, bài học lịch sử vào cuộc sống” – giải thích vấn đề hiện tại "
          "bằng mối liên hệ với quá khứ (ở mức độ đơn giản)."))

A(Paragraph("CÂU II.2 · Bài 3: Vai trò của sử học (1,00 điểm)", h4))
A(dungsai("II.2a", "NL2 · Biết · 0,25 đ",
          "Ý a. Sử học, với tư cách là một khoa học có tính liên ngành, đóng vai trò quan trọng nhất "
          "trong việc khẳng định giá trị của di sản; kết quả nghiên cứu của sử học về giá trị di sản "
          "là cơ sở khoa học vững chắc cho công tác bảo tồn và phát huy giá trị di sản.",
          "D",
          "Đúng. Đây là mối quan hệ giữa sử học và công tác bảo tồn, phát huy giá trị di sản văn hóa, "
          "di sản thiên nhiên; kết quả nghiên cứu phục vụ bảo tồn bền vững, vì lợi ích chung của toàn xã hội."))
A(dungsai("II.2b", "NL2 · Hiểu · 0,25 đ",
          "Ý b. Lịch sử và văn hóa không có ý nghĩa đối với sự phát triển du lịch vì du lịch hiện đại "
          "chỉ dựa vào cơ sở hạ tầng và dịch vụ.",
          "S",
          "Sai. Những giá trị lịch sử, văn hóa của mỗi dân tộc, của toàn nhân loại là nguồn tài nguyên "
          "quý báu của du lịch, đặc biệt là du lịch văn hóa; lịch sử – văn hóa cung cấp tri thức để "
          "quảng bá và thúc đẩy du lịch phát triển bền vững."))
A(dungsai("II.2c", "NL3 · Biết · 0,25 đ",
          "Ý c. Một số địa danh ở Việt Nam được xem là tài nguyên du lịch gắn với giá trị lịch sử – văn hóa, "
          "ví dụ: Vịnh Hạ Long, Quần thể di tích Cố đô Huế, Phố cổ Hội An, Văn Miếu – Quốc Tử Giám.",
          "D",
          "Đúng. Đây là những địa danh – tài nguyên du lịch tiêu biểu của nước ta; có thể nêu thêm "
          "Thánh địa Mỹ Sơn, Động Phong Nha – Kẻ Bàng, Đền Hùng…"))
A(dungsai("II.2d", "NL3 · Vận dụng · 0,25 đ",
          "Ý d. Để bảo tồn và phát huy giá trị một di tích lịch sử – văn hóa ở địa phương, có thể đề xuất: "
          "tu bổ, tôn tạo theo đúng nguyên tắc bảo tồn (giữ tính nguyên trạng, yếu tố gốc, tính xác thực); "
          "tổ chức tuyên truyền, giới thiệu rộng rãi; kết hợp du lịch để tạo nguồn vốn tái đầu tư cho bảo tồn; "
          "vận động nhân dân, nhất là thế hệ trẻ, cùng tham gia bảo vệ di sản.",
          "D",
          "Đúng. Các biện pháp đảm bảo yêu cầu cốt lõi của bảo tồn và phát huy giá trị di sản, "
          "phù hợp tinh thần “có ý thức vận động mọi người xung quanh cùng tham gia bảo vệ di sản”."))

# --- Phần III ---
A(Paragraph("PHẦN III. CÂU TRẮC NGHIỆN TỰ LUẬN (3,00 ĐIỂM)", h2))
A(KeepTogether([
    Paragraph('<font color="#1F3864"><b>[TL]</b></font>  <font size="7.6" color="#555555">'
              'Bài 3 · Chủ đề 2 · Ý 1: NL1 – Biết (1,00 đ) + Ý 2: NL3 – Vận dụng (2,00 đ)</font>', qhead),
    Paragraph(T("<b>Đề bài:</b> Theo em, sử học có vai trò như thế nào đối với công tác bảo tồn và phát huy "
                "giá trị di sản văn hóa, di sản thiên nhiên? Từ những hiểu biết của mình, hãy đề xuất ít nhất "
                "hai biện pháp để bảo tồn và phát huy giá trị một di sản ở địa phương em và vận động mọi người "
                "cùng tham gia bảo vệ di sản đó."), qtext),
]))
A(Paragraph("<b>ĐÁP ÁN MẪU – THANG ĐIỂM</b>", h4))
A(P("<b>Ý 1 – Mối quan hệ giữa sử học và công tác bảo tồn, phát huy giá trị di sản (1,00 điểm):</b>", bullet))
for t in [
    "Giá trị của di sản thể hiện ở nhiều khía cạnh: lịch sử, văn hóa, kiến trúc, mỹ thuật…; mỗi sự kiện, hiện tượng lịch sử gắn với điều kiện tự nhiên và bối cảnh chính trị – xã hội cụ thể.",
    "Sử học, với tư cách khoa học có tính liên ngành, <b>đóng vai trò quan trọng nhất trong việc khẳng định giá trị của di sản</b>.",
    "Kết quả nghiên cứu của sử học về giá trị di sản là <b>cơ sở khoa học vững chắc</b> cho công tác bảo tồn và phát huy giá trị di sản <b>bền vững, vì lợi ích chung của toàn xã hội</b>; bảo tồn phải đảm bảo tính nguyên trạng, “yếu tố gốc cấu thành di tích”, “tính xác thực”, “tính toàn vẹn”, “giá trị nổi bật”, dựa trên cứ liệu và phương pháp khoa học.",
]:
    A(Paragraph(T(t), bullet2, bulletText="+"))
A(P("<i>(Mỗi ý chính xác, đầy đủ: khoảng 0,25 – 0,35 điểm; đủ 3 ý: 1,00 điểm.)</i>", note))
A(P("<b>Ý 2 – Đề xuất biện pháp bảo tồn, phát huy và vận động cộng đồng tham gia (2,00 điểm):</b> "
    "(VD: di tích ở địa phương – đình, đền, chùa, nhà thờ họ, làng nghề, lễ hội…)", bullet))
for t in [
    "<b>Biện pháp 1 – Tu bổ, tôn tạo đúng nguyên tắc:</b> giữ nguyên trạng, yếu tố gốc cấu thành; kiểm tra, đánh giá bằng cứ liệu và phương pháp khoa học trước khi can thiệp; không xây mới, hiện đại hóa làm mất giá trị gốc.",
    "<b>Biện pháp 2 – Tuyên truyền, giới thiệu giá trị di sản:</b> tổ chức giới thiệu, tuyên truyền (nhà trường, địa phương, mạng xã hội…) để mọi người hiểu giá trị và ý thức bảo vệ; đưa nội dung liên quan vào hoạt động ngoại khóa, tìm hiểu lịch sử – văn hóa địa phương.",
    "<b>Biện pháp 3 – Kết hợp du lịch bền vững:</b> khai thác du lịch gắn với bảo tồn, dùng một phần doanh thu tái đầu tư vào bảo tồn, tôn tạo, phục dựng; tránh thương mại hóa, xây dựng tùy tiện.",
    "<b>Biện pháp 4 – Bảo tồn di sản phi vật thể:</b> sưu tầm, lưu giữ, truyền nghề, trình diễn, phục dựng lễ hội để lưu truyền giữa các thế hệ.",
    "<b>Vận động cộng đồng:</b> kêu gọi, vận động nhân dân và thế hệ trẻ cùng tham gia bảo vệ di sản; lên tiếng, ngăn chặn hành vi phá hoại; duy trì hoạt động tình nguyện làm sạch, giữ gìn di tích.",
]:
    A(Paragraph(T(t), bullet2, bulletText="+"))
A(P("<i>(Đủ 2 biện pháp cụ thể, khả thi + nội dung vận động: khoảng 1,20 điểm; diễn đạt rõ ràng, "
    "liên hệ được thực tế địa phương: thêm 0,80 điểm. Trình bày khoa học, đúng thuật ngữ: được xét thêm.)</i>", note))
A(Paragraph("MẸO CHẤM ĐIỂM: câu TL đúng cấu trúc = <b>1 ý “NÓI VAI TRÒ” (1đ) + tối thiểu 2 ý “LÀM GÌ” (2đ)</b>. "
            "Viết đủ 4 dòng mỗi ý, gạch đầu dòng rõ ràng.", mnem))
A(Spacer(1, 4 * mm))

# ================================================================ PHẦN D ====
A(Paragraph("PHẦN D. CHECKLIST ÔN TẬP NHANH TRƯỚC NGÀY THI", h1))
A(P("Đánh dấu <font face='DJS'>✔</font> vào ô tương ứng sau khi chắc chắn trả lời được “phiếu hỏi” từng mục.", lead))
checklist = [
    "Nêu được khái niệm lịch sử, lịch sử loài người; hai nghĩa của lịch sử.",
    "Phân biệt được hiện thực lịch sử và lịch sử được con người nhận thức qua bảng so sánh và ví dụ cụ thể.",
    "Giải thích được vì sao giữa hiện thực và nhận thức luôn có khoảng cách; nêu được các nguyên nhân.",
    "Nêu được đối tượng, chức năng, nhiệm vụ của sử học.",
    "Kể tên nguyên tắc (khách quan – trung thực – nhân văn) và phương pháp (lịch sử – logic) của sử học.",
    "Giải thích được ý nghĩa phát biểu của Ét-uốt Ha-lét Ca.",
    "Nêu được vai trò, ý nghĩa của tri thức lịch sử; giải thích sự cần thiết của học tập, khám phá lịch sử suốt đời.",
    "Nhớ khái niệm, vai trò (cầu nối) và các loại hình sử liệu.",
    "Phân biệt được thu thập và xử lý thông tin, sử liệu; nhớ quy trình 4 bước “Lập – Sưu – Chọn – Xác”.",
    "Nêu được cách kết nối tri thức, bài học lịch sử vào cuộc sống (dùng quá khứ giải thích hiện tại).",
    "Nêu mối quan hệ giữa sử học và công tác bảo tồn, phát huy giá trị di sản văn hóa, di sản thiên nhiên.",
    "Nhớ yêu cầu cốt lõi khi bảo tồn: NGUYÊN – GỐC – XÁC – TOÀN – NỔI dựa trên cứ liệu, phương pháp khoa học.",
    "Nêu vai trò của bảo tồn với từng loại hình di sản (vật thể, phi vật thể, thiên nhiên).",
    "Kể tên loại hình di sản văn hóa và ít nhất 5 địa danh tài nguyên du lịch của Việt Nam.",
    "Giải thích vai trò của lịch sử, văn hóa đối với du lịch và tác động hai chiều của du lịch đối với bảo tồn.",
    "Đề xuất được biện pháp bảo tồn, phát huy một di sản ở địa phương kèm việc vận động cộng đồng.",
]
for i, item in enumerate(checklist, 1):
    A(Paragraph(T(f"[&nbsp;&nbsp;] <b>{i}.</b> {item}"), bullet, bulletText=""))

A(Spacer(1, 6 * mm))
A(Paragraph("MẸO NHỚ NHANH “5 NGÔN LỆ” TRONG BÀI KIỂM TRA", h4))
A(table(
    [[P("Nhớ", th), P("Điều cần nhớ", th)],
     [P("<b>HÀN</b>", tdc), P("<b>H</b>iện thực – <b>A</b>i biết (nhận thức): khách quan/một/không đổi – chủ quan/đa dạng/đổi.", td)],
     [P("<b>LẦN LƯỢT</b>", tdc), P("Quy trình sử liệu: <b>L</b>ập → <b>S</b>ưu → <b>C</b>họn → <b>X</b>ác minh.", td)],
     [P("<b>QUYỀN</b>", tdc), P("Nguyên tắc sử học: <b>quy</b> tắc “KHÁCH – TRUNG – NHÂN”.", td)],
     [P("<b>NGUYÊN GỐC</b>", tdc), P("Bảo tồn: <b>nguyên</b> trạng, <b>gốc</b> cấu thành, xác thực, toàn vẹn, nổi bật.", td)],
     [P("<b>ĐI ĐỂ TRẢ</b>", tdc), P("Du lịch ↔ bảo tồn: du lịch <b>đi</b> = doanh thu <b>trả</b> lại cho bảo tồn.", td)]],
    widths=[26 * mm, 148 * mm]))

A(Spacer(1, 4 * mm))
A(KeepTogether([
    P("— Hết đề cương —", S("End", parent=bodyc, fontName="DJR-I", textColor=GREY)),
    P("Nguồn: Ma trận LS10- MTGK1-26-27-HHT.docx; SGK Lịch sử 10 – Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).",
      S("Src", parent=body, fontSize=7.8, leading=10.5, textColor=GREY, alignment=1)),
]))

# ================================================================ BUILD =====
def build():
    doc = DeCuongDoc(
        OUT, pagesize=A4,
        leftMargin=17 * mm, rightMargin=17 * mm,
        topMargin=17 * mm, bottomMargin=16 * mm,
        title="Đề cương ôn tập giữa học kỳ I – Lịch sử lớp 10 (Kết nối tri thức)",
        author="Soạn theo ma trận LS10- MTGK1-26-27-HHT",
        subject="Ôn tập giữa kỳ I Lịch sử 10",
    )
    frame = _frame(A4)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[Frame(20 * mm, 20 * mm, A4[0] - 40 * mm,
                                               A4[1] - 40 * mm, id="cover",
                                               leftPadding=0, rightPadding=0,
                                               topPadding=0, bottomPadding=0)],
                     onPage=on_page_cover),
        PageTemplate(id="main", frames=[frame], onPage=on_page),
    ])
    # trang 1 dùng template "cover" (template đầu tiên), các trang sau dùng "main"
    from reportlab.platypus import NextPageTemplate
    story.insert(0, NextPageTemplate("main"))
    doc.multiBuild(story)

    # ---- kiểm tra glyph tiếng Việt ----
    from fontTools.ttLib import TTFont as FT
    cmap = FT(os.path.join(FONT_DIR, "DejaVuSerif.ttf")).getBestCmap()
    cmap.update(FT(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")).getBestCmap())
    missing = set()
    for s in ALL_TEXT:
        for ch in s:
            if ch not in "\n\t" and ord(ch) not in cmap:
                missing.add(ch)
    if missing:
        print("!! MISSING GLYPHS:", sorted(missing))
    else:
        print("Glyph check: OK (all Vietnamese characters covered)")
    print("PDF written:", OUT)

if __name__ == "__main__":
    build()
