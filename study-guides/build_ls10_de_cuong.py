"""Build the LS10 mid-term study guide PDF (Kết nối tri thức, HK1 2026-2027).

Source of truth: "LS10- MTGK1-26-27-HHT.docx" (ma trận + bảng đặc tả).
Run: python3 study-guides/build_ls10_de_cuong.py
Requires: reportlab
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "LS10-de-cuong-on-tap-giua-ki-1-2026-2027.pdf")
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", FD + "DejaVuSans-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV", boldItalic="DV-B")

H1 = ParagraphStyle("h1", fontName="DV-B", fontSize=16, leading=20, spaceAfter=8, alignment=1)
H2 = ParagraphStyle("h2", fontName="DV-B", fontSize=12.5, leading=16, spaceBefore=10, spaceAfter=5,
                    textColor=colors.HexColor("#1F3A5F"))
H3 = ParagraphStyle("h3", fontName="DV-B", fontSize=10.5, leading=14, spaceBefore=6, spaceAfter=3)
BODY = ParagraphStyle("b", fontName="DV", fontSize=9.5, leading=13.5, spaceAfter=3)
BUL = ParagraphStyle("bul", parent=BODY, leftIndent=12, bulletIndent=2)
SMALL = ParagraphStyle("s", fontName="DV", fontSize=8.5, leading=11.5)
CELL = ParagraphStyle("c", fontName="DV", fontSize=8.3, leading=11)
CELLB = ParagraphStyle("cb", fontName="DV-B", fontSize=8.3, leading=11)

def P(t, s=BODY): return Paragraph(t, s)
def B(items): return [Paragraph(i, BUL, bulletText="•") for i in items]
def T(rows, widths, header=True):
    data = [[Paragraph(str(c), CELLB if (header and r == 0) else CELL) for c in row]
            for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    if header:
        st.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE6F1")))
    t.setStyle(TableStyle(st))
    return t

story = []
story += [P("ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ 1 — LỊCH SỬ 10", H1),
          P("Bộ sách <b>Kết nối tri thức với cuộc sống</b> · Năm học 2026–2027 · Thời gian làm bài: 45 phút", SMALL),
          Spacer(1, 6)]

story += [P("Phần 1. Cấu trúc đề và phạm vi kiến thức", H2),
          T([["Thành phần", "Số lượng", "Điểm"],
             ["Trắc nghiệm nhiều lựa chọn (I.1 – I.20)", "20 câu", "Theo ma trận gốc"],
             ["Trắc nghiệm Đúng/Sai (II.1, II.2; mỗi câu có ý a–d)", "2 câu", "Xem bảng ma trận"],
             ["Tự luận (TL)", "1 câu", "Xem bảng ma trận"],
             ["Tổng", "—", "10 điểm"]], [9.2 * cm, 3.2 * cm, 4.6 * cm]),
          Spacer(1, 4),
          P("Phạm vi: <b>Chủ đề 1 — Lịch sử và sử học</b> (Bài 1, Bài 2) và <b>Chủ đề 2 — Vai trò của sử học</b> (Bài 3).", BODY),
          P("Đề kiểm tra đánh giá 3 năng lực môn học: <b>NL1</b> Tìm hiểu lịch sử; <b>NL2</b> Nhận thức và tư duy lịch sử; "
            "<b>NL3</b> Vận dụng kiến thức, kĩ năng. Mỗi năng lực có 3 cấp độ tư duy: Biết, Hiểu, Vận dụng.", BODY)]

story += [P("Phần 2. Bảng phân bổ câu hỏi theo ma trận", H2),
          P("Số hiệu câu lấy đúng theo file ma trận. Theo ma trận, ô Vận dụng của NL1 và NL2 không có câu nào. "
            "", SMALL),
          Spacer(1, 3),
          T([["Bài", "Biết", "Hiểu", "Vận dụng", "Ghi chú từ ma trận"],
             ["Bài 1. Hiện thực lịch sử và lịch sử được con người nhận thức",
              "I.1, I.2, I.3", "I.4", "I.5, I.6", "Xem ghi chú dưới bảng"],
             ["Bài 2. Tri thức lịch sử và cuộc sống",
              "I.7, I.8, I.9", "I.10, I.11", "I.12, I.13; II.1a–d (Đ/S)", "Xem ghi chú dưới bảng"],
             ["Bài 3. Vai trò của Sử học",
              "I.14, I.15; 1/2 TL", "I.16; I.17, I.18", "I.19, I.20; II.2a–d (Đ/S); 1/2 TL", "Xem ghi chú dưới bảng"]],
            [4.6 * cm, 2.6 * cm, 2.6 * cm, 3.4 * cm, 4.2 * cm]),
          Spacer(1, 4),
          P("<b>Điểm theo ma trận:</b> NL1 — Biết 3,0 · Hiểu 1,0 · Vận dụng 0. NL2 — Biết 1,5 · Hiểu 1,5 · Vận dụng 0. "
            "NL3 — Biết 0,5 · Hiểu 0 · Vận dụng 2,5. <b>Tổng 10 điểm.</b>", SMALL),
          P("<i>Lưu ý:</i> Cách ghép cột trong file .docx không hoàn toàn rõ ràng ở một số ô. Hãy đối chiếu lại với "
            "bản ma trận gốc của trường nếu cần.", SMALL)]

story += [PageBreak(), P("Phần 3. Nội dung ôn tập theo từng bài", H2)]

story += [P("Chủ đề 1. Lịch sử và sử học", H3),
          P("<b>Bài 1. Hiện thực lịch sử và lịch sử được con người nhận thức</b>", BODY)]
story += B([
    "<b>Lịch sử</b> là toàn bộ quá khứ của xã hội loài người; đã xảy ra và không thể quay lại. Đó là <b>hiện thực lịch sử</b>, tồn tại khách quan.",
    "<b>Sử học</b> là khoa học nghiên cứu lịch sử: tìm hiểu, tái hiện và giải thích quá khứ dựa trên tư liệu còn lại.",
    "<b>Đối tượng</b> của sử học là quá khứ của loài người. <b>Chức năng</b>: nhận thức, giáo dục, dự báo. <b>Nhiệm vụ</b>: tái hiện, phục dựng và giải thích quá khứ.",
    "<b>Lịch sử được con người nhận thức</b> là bức tranh quá khứ do sử học xây dựng từ sử liệu. Nó khác hiện thực lịch sử ở chỗ: chỉ là một phần, mang dấu ấn người nghiên cứu, và có thể thay đổi khi xuất hiện sử liệu mới hoặc cách tiếp cận mới.",
    "<b>Phân biệt</b> hai khái niệm: hiện thực lịch sử là cái đã xảy ra (một lần, không lặp lại); lịch sử được nhận thức là cái được diễn giải hôm nay (có thể nhiều phiên bản).",
])
story += [P("<b>Bài 2. Tri thức lịch sử và cuộc sống</b>", BODY)]
story += B([
    "<b>Các bước thu thập, xử lí thông tin và sử liệu</b>: (1) xác định vấn đề nghiên cứu; (2) tìm và thu thập nguồn sử liệu (thành văn, hiện vật, hình ảnh, truyền miệng…); (3) thẩm định sử liệu (nguồn gốc, thời gian, tính xác thực); (4) xử lí: phân loại, đối chiếu, so sánh các nguồn; (5) rút ra kết luận và trình bày.",
    "<b>Học và khám phá lịch sử suốt đời</b>: lịch sử không chỉ học ở trường mà cần tiếp tục tự học, tự tìm hiểu trong đời sống.",
    "<b>Vận dụng tri thức lịch sử</b> để giải thích các vấn đề thời sự, vấn đề thực tiễn ở mức đơn giản; hình thành thái độ quan tâm, yêu thích tìm hiểu lịch sử, văn hoá dân tộc và thế giới.",
])

story += [P("Chủ đề 2. Vai trò của sử học", H3),
          P("<b>Bài 3. Vai trò của Sử học</b>", BODY)]
story += B([
    "Sử học có <b>mối quan hệ</b> trực tiếp với công tác <b>bảo tồn và phát huy giá trị di sản văn hoá, di sản thiên nhiên</b>: cung cấp cơ sở khoa học để xác định, bảo vệ và giới thiệu di sản.",
    "Các loại hình <b>di sản văn hoá</b> cần nhớ: di sản vật thể (di tích, hiện vật) và di sản phi vật thể (tập quán, lễ hội, nghề truyền thống, tri thức dân gian…). Di sản thiên nhiên gồm cảnh quan, hệ sinh thái có giá trị.",
    "Lịch sử – văn hoá là <b>tài nguyên du lịch</b>. Du lịch vừa thúc đẩy phát triển kinh tế, vừa <b>tác động</b> đến di tích: tích cực (quảng bá, nguồn lực đầu tư) và tiêu cực (quá tải, xuống cấp, thương mại hoá).",
    "<b>Biện pháp bảo tồn, phát huy giá trị di sản</b>: nghiên cứu khoa học; lập hồ sơ, kiểm kê và xếp hạng di tích; quy hoạch và kiểm soát lượng khách; giáo dục cộng đồng; kết hợp bảo tồn với phát triển du lịch có trách nhiệm; tuyên truyền để mọi người cùng tham gia bảo vệ.",
])

story += [PageBreak(), P("Phần 4. Bảng tóm tắt khái niệm cần nhớ", H2),
          T([["Khái niệm", "Nội dung cốt lõi"],
             ["Lịch sử", "Toàn bộ quá khứ của loài người, đã xảy ra, tồn tại khách quan."],
             ["Sử học", "Khoa học nghiên cứu, tái hiện và giải thích lịch sử."],
             ["Hiện thực lịch sử", "Quá khứ đã diễn ra; là cái khách quan, không lặp lại."],
             ["Lịch sử được con người nhận thức", "Bức tranh quá khứ do sử học xây dựng; mang tính chọn lọc, chủ quan có kiểm chứng, có thể điều chỉnh."],
             ["Sử liệu", "Mọi dấu vết còn lại của quá khứ dùng để nghiên cứu lịch sử."],
             ["Chức năng sử học", "Nhận thức, giáo dục, dự báo."],
             ["Đối tượng sử học", "Quá khứ của xã hội loài người."],
             ["Di sản văn hoá", "Di sản vật thể và phi vật thể mang giá trị lịch sử, văn hoá, khoa học."],
             ["Di sản thiên nhiên", "Cảnh quan, hệ sinh thái, địa chất có giá trị khoa học và thẩm mĩ."]],
            [5.0 * cm, 12.0 * cm])]

story += [P("Phần 5. Câu hỏi luyện tập (do soạn, không phải đề thi thật)", H2),
          P("Các câu dưới đây được soạn để luyện tập theo đặc tả. <b>Không</b> phải câu hỏi hay đáp án của đề kiểm tra thực tế.", SMALL),
          Spacer(1, 3)]
practice = [
    ("Biết (Bài 1)", "Đối tượng nghiên cứu của sử học là gì?",
     "Quá khứ của xã hội loài người."),
    ("Biết (Bài 1)", "Nêu sự khác nhau cơ bản giữa hiện thực lịch sử và lịch sử được con người nhận thức.",
     "Hiện thực lịch sử là quá khứ đã diễn ra, khách quan, không lặp lại. Lịch sử được nhận thức là bức tranh do sử học tái hiện từ sử liệu, có chọn lọc và có thể thay đổi."),
    ("Thông hiểu (Bài 1)", "Vì sao cùng một sự kiện lịch sử có thể được các nhà sử học giải thích khác nhau?",
     "Vì nhận thức lịch sử dựa trên sử liệu còn lại (không đầy đủ), phụ thuộc vào cách tiếp cận, quan điểm và thời đại của người nghiên cứu."),
    ("Biết (Bài 2)", "Nêu các bước trong việc thu thập và xử lí sử liệu.",
     "Xác định vấn đề → thu thập sử liệu → thẩm định sử liệu → xử lí, đối chiếu → rút ra kết luận và trình bày."),
    ("Thông hiểu (Bài 2)", "Vì sao cần học và khám phá lịch sử suốt đời?",
     "Lịch sử luôn được bổ sung bằng sử liệu và nhận thức mới; tri thức lịch sử giúp hiểu hiện tại, định hướng hành động và hình thành nhân cách."),
    ("Vận dụng (Bài 2)", "Nêu một cách vận dụng kiến thức lịch sử để giải thích một vấn đề thực tiễn đơn giản.",
     "Ví dụ: dùng kiến thức về lịch sử địa phương để giải thích vì sao một làng nghề được bảo tồn, hoặc lí giải tầm quan trọng của một di tích trong việc phát triển du lịch."),
    ("Biết (Bài 3)", "Kể tên các loại hình di sản văn hoá.",
     "Di sản văn hoá vật thể (di tích, hiện vật) và di sản văn hoá phi vật thể (lễ hội, nghề truyền thống, tập quán, tri thức dân gian)."),
    ("Thông hiểu (Bài 3)", "Phân tích tác động của du lịch đối với việc bảo tồn di tích lịch sử, văn hoá.",
     "Tích cực: quảng bá, tạo nguồn lực trùng tu. Tiêu cực: quá tải khách gây xuống cấp, thương mại hoá làm sai lệch giá trị, xây dựng lấn át di tích."),
    ("Vận dụng (Bài 3)", "Đề xuất hai biện pháp bảo tồn và phát huy giá trị của một di sản ở địa phương em.",
     "Ví dụ: lập hồ sơ khoa học và xếp hạng di tích; giới thiệu, giáo dục cộng đồng về giá trị di sản; kiểm soát lượng khách du lịch hợp lí."),
]
rows = [["Cấp độ", "Câu hỏi luyện tập", "Gợi ý đáp án"]] + [list(x) for x in practice]
story += [T(rows, [3.0 * cm, 6.8 * cm, 7.2 * cm])]

story += [Spacer(1, 8),
          P("<b>Lời khuyên ôn tập.</b> (1) Học thuộc các khái niệm ở Phần 4. (2) Với từng bài, tự viết lại các bước hoặc đặc điểm bằng lời của mình. "
            "(3) Ôn các ý Đúng/Sai theo từng chủ đề, chú ý những ý chứa từ khoá tuyệt đối như “luôn”, “chỉ”, “hoàn toàn”. "
            "(4) Luyện câu tự luận bằng cách nêu luận điểm, dẫn chứng và kết luận. "
            "(5) Đối chiếu nội dung với sách giáo khoa <i>Lịch sử 10 — Kết nối tri thức</i> để chốt cách diễn đạt chính xác.", BODY)]

def footer(c, d):
    c.saveState()
    c.setFont("DV", 8)
    c.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Trang {d.page}")
    c.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                        topMargin=1.8 * cm, bottomMargin=1.8 * cm,
                        title="Đề cương ôn tập giữa kì 1 Lịch sử 10", author="Arena Agent")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT)
