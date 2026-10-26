# -*- coding: utf-8 -*-
"""c_questions.py — PHẦN 4: Hệ thống câu hỏi và đáp án (28 lệnh hỏi + 1 tự luận)."""
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle, KeepTogether,
                                PageBreak, CondPageBreak)
from layout import (S, CW, h2, h3, h4, p, bullets, numbered, card, data_table, quote,
                    band, NAVY, GOLD, RED, TEAL, INK, MUTED, GREY_L, GREY_M, WHITE,
                    CHECK, CROSS, ARROW, STAR, WARN)

UNIT_COLOR = {"Bài 1": NAVY, "Bài 2": TEAL, "Bài 3": colors.HexColor("#8A5B12")}
LEVEL_COLOR = {"Biết": MUTED, "Hiểu": TEAL, "Vận dụng": RED, "Vận dụng cao": RED}

S_Q = ParagraphStyle("q", fontName="BVPM", fontSize=9.8, leading=15.0, textColor=INK,
                     alignment=0, spaceAfter=2)
S_ANS = ParagraphStyle("ans", fontName="BVPB", fontSize=9.4, leading=12.6, textColor=TEAL)
S_WHY = ParagraphStyle("why", fontName="BVP", fontSize=8.7, leading=13.0, textColor=INK)
S_TAG = ParagraphStyle("tag", fontName="BVPM", fontSize=7.6, leading=10, textColor=MUTED,
                       alignment=2)


def _head(label, unit, level, extra=""):
    t = Table([[[Paragraph('<font color="white" name="BVPB" size=8.2>%s</font>' % label),
                 Paragraph("%s · Mức độ: <b>%s</b>%s" % (unit, level, extra), S_TAG)]]],
              colWidths=[CW - 16])
    inner = t._cellvalues[0][0]
    tt = Table([[Paragraph('<font color="white" name="BVPB" size=8.2>%s</font>' % label),
                 Paragraph("%s &nbsp;·&nbsp; Mức độ: <b>%s</b>%s" % (unit, level, extra), S_TAG)]],
               colWidths=[26 * mm, CW - 16 - 26 * mm])
    tt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), UNIT_COLOR.get(unit, NAVY)),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (0, 0), 7), ("RIGHTPADDING", (0, 0), (0, 0), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
        ("LEFTPADDING", (1, 0), (1, 0), 6),
    ]))
    return tt


def mcq(n, unit, level, question, opts, ans, why):
    """opts: list 4 chuỗi (A, B, C, D)."""
    body = [_head("CÂU %02d" % n, unit, level), Spacer(1, 5),
            Paragraph(question, S_Q), Spacer(1, 3)]

    letters = "ABCD"
    short = all(len(o) <= 46 for o in opts)
    cells = []
    for i, o in enumerate(opts):
        mark = "<b>%s.</b> " % letters[i]
        if letters[i] == ans:
            cells.append(Paragraph(mark + o, S["opt"]))
        else:
            cells.append(Paragraph(mark + o, S["opt"]))
    if short:
        rows = [[cells[0], cells[1]], [cells[2], cells[3]]]
        ot = Table(rows, colWidths=[(CW - 16) / 2] * 2)
    else:
        ot = Table([[c] for c in cells], colWidths=[CW - 16])
    ot.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 1.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.4),
    ]))
    body += [ot, Spacer(1, 5)]

    at = Table([[Paragraph("ĐÁP ÁN: %s" % ans, S_ANS),
                 Paragraph("<b>Vì sao:</b> " + why, S_WHY)]],
               colWidths=[27 * mm, CW - 16 - 27 * mm])
    at.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#E4F2EC")),
        ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#F6F9F7")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 4.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBEFORE", (0, 0), (-1, -1), 0.4, colors.HexColor("#CFE3D9")),
    ]))
    body.append(at)

    outer = Table([[body]], colWidths=[CW])
    outer.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, GREY_M),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return KeepTogether([outer, Spacer(1, 5)])


def tf(n, unit, level, intro, items, note=None):
    """items: list (label, statement, bold_answer('Đúng'/'Sai'), explain)"""
    flow = [_head("CÂU Đ/S %d" % n, unit, level, " &nbsp;·&nbsp; 4 ý a–d"), Spacer(1, 5)]
    if intro:
        flow.append(quote(intro))
    rows = []
    for label, stmt, ans, exp in items:
        ok = ans.strip().lower().startswith("đ")
        chip = Paragraph(
            '<font color="white" name="BVPB" size=7.6>%s</font>' % ans.upper(),
            ParagraphStyle("chip", alignment=1))
        cell = Paragraph(stmt +
                         '<br/><font color="#4C6B60" size=8.2><i>Giải thích:</i> ' + exp + "</font>",
                         S["tbl"])
        rows.append([Paragraph("<b>%s</b>" % label,
                               ParagraphStyle("lb", fontName="BVPB", fontSize=9, alignment=1)),
                     cell, chip])
    t = Table(rows, colWidths=[8 * mm, CW - 16 - 8 * mm - 20 * mm, 20 * mm])
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (0, -1), "MIDDLE"), ("VALIGN", (2, 0), (2, -1), "MIDDLE"),
        ("BOX", (0, 0), (-1, -1), 0.5, GREY_M),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, GREY_M),
    ]
    for i, (label, stmt, ans, exp) in enumerate(items):
        ok = ans.strip().lower().startswith("đ")
        col = colors.HexColor("#2F8A62") if ok else colors.HexColor("#B4443A")
        style += [("BACKGROUND", (2, i), (2, i), col)]
    style.append(("LINEBEFORE", (0, 0), (0, -1), 2.2, GREY_M))
    t.setStyle(TableStyle(style))
    flow.append(t)
    return flow + [Spacer(1, 8)]


def essay(prompt, outline, sample, score_note):
    flow = [_head("CÂU TỰ LUẬN", "Bài 3", "Vận dụng", " &nbsp;·&nbsp; 3,0 điểm"), Spacer(1, 6)]
    box = Table([[Paragraph("<b>ĐỀ BÀI</b><br/>" + prompt, S["body_l"])]], colWidths=[CW - 16])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FBF3E0")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    flow += [box, Spacer(1, 7)]
    flow.append(Paragraph("Dàn ý chi tiết (bám theo thang điểm)", S["h3"]))
    flow += outline
    flow.append(Spacer(1, 4))
    flow.append(Paragraph("Bài làm tham khảo", S["h3"]))
    flow.append(card("mau", sample, title="Bài làm tham khảo (khoảng 450 từ)"))
    flow.append(score_note)
    return flow


def story():
    st = []
    st += band("4", "HỆ THỐNG CÂU HỎI VÀ ĐÁP ÁN",
               "28 lệnh hỏi trắc nghiệm + 1 câu tự luận · bám sát bảng đặc tả của đề")

    st.append(p("Phần này gồm đầy đủ các câu hỏi theo đúng phân bổ của bảng đặc tả: "
                "<b>Câu 1–6</b> (Bài 1), <b>Câu 7–13</b> và <b>câu Đ/S 1</b> (Bài 2), "
                "<b>Câu 14–20</b>, <b>câu Đ/S 2</b> và <b>câu tự luận</b> (Bài 3). "
                "Cách dùng: <b>che phần đáp án</b> (dùng tờ giấy che dòng nền xanh), tự chọn đáp án, "
                "sau đó mới đọc mục “Vì sao”."))
    st.append(card("thi", [
        Paragraph("<b>Nguyên tắc làm bài trắc nghiệm lịch sử:</b> (1) đọc câu hỏi trước, gạch chân "
                  "<b>từ khoá giới hạn</b> (“đầu tiên”, “không đúng”, “quan trọng nhất”); (2) loại phương án "
                  "sai chắc chắn; (3) với câu “ngoại trừ / không đúng”, khoanh tròn chữ <b>KHÔNG</b>; "
                  "(4) câu hỏi về khái niệm — chọn phương án có <b>đủ các dấu hiệu bản chất</b>, không chọn "
                  "phương án chỉ đúng một phần.", S["small"]),
    ]))

    # ------------------------------------------------------------ PHẦN I
    st.append(h2("PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (Câu 1 – Câu 20)"))
    st.append(p("<i>Chọn một phương án đúng nhất trong mỗi câu.</i>", "small"))

    Q = []

    Q.append(mcq(1, "Bài 1", "Biết",
                 "Lịch sử là gì?",
                 ["Là khoa học nghiên cứu về quá khứ của loài người.",
                  "Là những ghi chép của con người về các sự kiện trong quá khứ.",
                  "Là toàn bộ những gì đã diễn ra trong quá khứ.",
                  "Là những di tích, hiện vật còn lại từ quá khứ."],
                 "C",
                 "Lịch sử (nghĩa chung) là toàn bộ những gì đã diễn ra trong quá khứ, tồn tại khách quan. "
                 "Phương án A là <i>Sử học</i>; B là <i>nhận thức/ghi chép</i> về quá khứ; D là <i>sử liệu</i> "
                 "— dấu vết còn lại."))

    Q.append(mcq(2, "Bài 1", "Biết",
                 "Các chức năng cơ bản của Sử học là",
                 ["khoa học, giáo dục và xã hội.",
                  "nghiên cứu, giảng dạy và xuất bản.",
                  "bảo tồn, phát huy và quảng bá.",
                  "nhận thức, dự báo và sáng tác nghệ thuật."],
                 "A",
                 "Sử học có ba chức năng: <b>khoa học</b> (nhận thức, tái hiện quá khứ chân thực), "
                 "<b>giáo dục</b> (truyền thống, nhân cách), <b>xã hội</b> (bài học kinh nghiệm, dự báo). "
                 "Các phương án khác chỉ là hoạt động cụ thể hoặc chức năng của ngành khác."))

    Q.append(mcq(3, "Bài 1", "Biết",
                 "Đối tượng nghiên cứu của Sử học là",
                 ["các di sản văn hoá vật thể và phi vật thể.",
                  "các nguồn sử liệu thành văn.",
                  "những sự kiện tiêu biểu của dân tộc.",
                  "toàn bộ quá trình phát triển của xã hội loài người."],
                 "D",
                 "Sử học nghiên cứu <b>toàn bộ quá trình phát sinh, phát triển của xã hội loài người</b> trên "
                 "mọi lĩnh vực, không chỉ sự kiện tiêu biểu hay tư liệu thành văn. Sử liệu chỉ là "
                 "<i>phương tiện</i>, không phải đối tượng."))

    Q.append(mcq(4, "Bài 1", "Hiểu",
                 "Nhận định nào sau đây đúng khi phân biệt “lịch sử” và “Sử học”?",
                 ["Hai khái niệm đồng nghĩa, chỉ khác cách gọi.",
                  "Lịch sử là đối tượng nghiên cứu, Sử học là khoa học nghiên cứu đối tượng đó.",
                  "Sử học ra đời trước, sau đó con người mới có lịch sử.",
                  "Lịch sử là một ngành khoa học, còn Sử học là những gì đã xảy ra."],
                 "B",
                 "Lịch sử <b>tồn tại</b> (cái đã xảy ra) còn Sử học <b>nghiên cứu</b> nó. Vì vậy lịch sử có "
                 "trước và tồn tại khách quan, còn Sử học là một ngành khoa học ra đời khi con người biết "
                 "nghiên cứu quá khứ một cách hệ thống."))

    Q.append(mcq(5, "Bài 1", "Biết",
                 "Sự kiện nào sau đây là hiện thực lịch sử?",
                 ["Truyền thuyết Sơn Tinh – Thuỷ Tinh.",
                  "Bộ phim “Hà Nội mùa đông năm 46”.",
                  "Ngày 2-9-1945, tại Quảng trường Ba Đình, Chủ tịch Hồ Chí Minh đọc Tuyên ngôn Độc lập.",
                  "Bức tranh dân gian “Hai Bà Trưng”."],
                 "C",
                 "Hiện thực lịch sử là sự việc <b>đã thực sự diễn ra</b>, khách quan. Truyền thuyết (A), "
                 "phim (B) và tranh dân gian (D) đều là <i>các hình thức nhận thức, tái hiện</i> quá khứ."))

    Q.append(mcq(6, "Bài 1", "Biết",
                 "Nhận định nào sau đây <b>không đúng</b> về lịch sử được con người nhận thức?",
                 ["Mang tính chủ quan, phụ thuộc vào người nhận thức.",
                  "Luôn trùng khớp hoàn toàn với hiện thực lịch sử.",
                  "Có thể được bổ sung, hoàn thiện khi có sử liệu mới.",
                  "Được biểu hiện qua nhiều hình thức khác nhau."],
                 "B",
                 "Nhận thức lịch sử <b>luôn có khoảng cách</b> với hiện thực lịch sử, không bao giờ trùng khít. "
                 "Đó chính là đặc điểm nổi bật nhất của nó. Ba phương án còn lại đều là đặc điểm đúng."))

    Q.append(mcq(7, "Bài 2", "Biết",
                 "Tri thức lịch sử là",
                 ["những hiểu biết của con người về quá khứ, được hình thành qua học tập, trải nghiệm và nghiên cứu.",
                  "những di vật, cổ vật còn lại từ quá khứ.",
                  "cảm xúc, tình cảm của con người khi nhớ về quá khứ.",
                  "các sự kiện đang diễn ra trong hiện tại."],
                 "A",
                 "Tri thức lịch sử là <b>hiểu biết</b> về quá khứ — sản phẩm của nhận thức, có hệ thống và có lí lẽ. "
                 "Hiện vật (B) là sử liệu; cảm xúc (C) không phải tri thức; (D) là hiện tại, chưa phải lịch sử."))

    Q.append(mcq(8, "Bài 2", "Biết",
                 "Sử liệu là",
                 ["những sự kiện đã xảy ra trong quá khứ.",
                  "các công trình nghiên cứu của sử gia hiện đại.",
                  "tài liệu, hiện vật, dấu vết phản ánh quá khứ, cung cấp thông tin về lịch sử.",
                  "các di tích đã được xếp hạng."],
                 "C",
                 "Sử liệu là <b>nguồn thông tin về quá khứ</b> (chữ viết, hiện vật, hình ảnh, truyền miệng…). "
                 "Nó không đồng nhất với sự kiện (A) và rộng hơn cả di tích đã xếp hạng (D)."))

    Q.append(mcq(9, "Bài 2", "Biết",
                 "Trong quá trình thu thập và xử lí thông tin, sử liệu, bước đầu tiên là",
                 ["phân loại, đánh giá sử liệu.",
                  "thu thập thông tin, sử liệu.",
                  "trình bày kết quả nghiên cứu.",
                  "xác định vấn đề, mục đích và xây dựng kế hoạch."],
                 "D",
                 "Quy trình 4 bước: <b>xác định vấn đề <font name='DJ'>→</font> thu thập <font name='DJ'>→</font> xử lí, đánh giá <font name='DJ'>→</font> trình bày kết quả</b>. "
                 "Không xác định vấn đề thì không biết cần thu thập cái gì, nên đây luôn là bước đầu tiên."))

    Q.append(mcq(10, "Bài 2", "Hiểu",
                 "Vì sao con người cần học tập và khám phá lịch sử suốt đời?",
                 ["Vì tri thức lịch sử là vô hạn, luôn được bổ sung và gắn với nhu cầu luôn đổi mới của cuộc sống.",
                  "Vì sách giáo khoa không cung cấp đủ kiến thức để làm bài kiểm tra.",
                  "Vì bản thân hiện thực lịch sử luôn thay đổi theo thời gian.",
                  "Vì mỗi người cần tích luỹ chứng chỉ, bằng cấp."],
                 "A",
                 "Học suốt đời vì tri thức lịch sử vô hạn, nhận thức lịch sử luôn vận động và cuộc sống "
                 "đặt ra vấn đề mới. Phương án C sai vì <b>hiện thực lịch sử không thay đổi</b> — chỉ nhận "
                 "thức thay đổi."))

    Q.append(mcq(11, "Bài 2", "Hiểu",
                 "Việc “kết nối tri thức lịch sử vào cuộc sống” được thể hiện rõ nhất ở hành vi nào?",
                 ["Học thuộc nhiều mốc thời gian nhất có thể.",
                  "Sưu tầm thật nhiều hiện vật, tư liệu.",
                  "Vận dụng bài học quá khứ để lí giải vấn đề hiện tại và ứng xử phù hợp.",
                  "Ghi nhớ tên tuổi các nhân vật lịch sử."],
                 "C",
                 "Kết nối là <b>dùng hiểu biết quá khứ để hiểu và hành động trong hiện tại</b>. "
                 "A, B, D mới dừng ở tích luỹ dữ kiện, chưa phải vận dụng."))

    Q.append(mcq(12, "Bài 2", "Biết",
                 "Khi đánh giá độ tin cậy của một nguồn sử liệu, yếu tố nào là quan trọng nhất?",
                 ["Số trang hoặc dung lượng của tài liệu.",
                  "Nguồn gốc xuất xứ, thời gian, tác giả và mục đích tạo ra nguồn.",
                  "Hình thức trình bày và số lượt chia sẻ trên mạng xã hội.",
                  "Tên người dịch hoặc người sưu tầm."],
                 "B",
                 "Ba câu hỏi vàng: <b>Ai? Khi nào? Vì sao?</b> — tức tác giả, thời điểm và mục đích. "
                 "Hình thức đẹp hay nhiều lượt chia sẻ (C) <b>không</b> nói lên giá trị khoa học."))

    Q.append(mcq(13, "Bài 2", "Biết",
                 "Nguồn nào sau đây là sử liệu gốc?",
                 ["Sách giáo khoa Lịch sử 10.",
                  "Bài viết tổng hợp trên một trang tin điện tử.",
                  "Phim tài liệu do một đài truyền hình sản xuất năm 2015.",
                  "Bia Vĩnh Lăng do Nguyễn Trãi soạn, được khắc năm 1433."],
                 "D",
                 "Sử liệu gốc được tạo ra <b>cùng thời</b> với sự kiện, bởi người liên quan trực tiếp. "
                 "Bia Vĩnh Lăng (1433) là hiện vật gốc; A, B, C đều ra đời sau và dựa trên nguồn khác "
                 "<font name='DJ'>→</font> sử liệu phái sinh."))

    Q.append(mcq(14, "Bài 3", "Biết",
                 "Di sản văn hoá phi vật thể bao gồm",
                 ["di tích, di vật, cổ vật, bảo vật quốc gia.",
                  "lễ hội, nghệ thuật trình diễn, nghề thủ công truyền thống, tri thức dân gian.",
                  "vườn quốc gia, hang động, danh lam thắng cảnh.",
                  "tất cả các phương án trên."],
                 "B",
                 "Phi vật thể là những giá trị <b>tinh thần, tồn tại trong con người và cộng đồng</b>: "
                 "tiếng nói, chữ viết, tín ngưỡng – lễ hội, trình diễn, nghề thủ công, tri thức dân gian, "
                 "ẩm thực. A là di sản <i>vật thể</i>; C là di sản <i>thiên nhiên</i>."))

    Q.append(mcq(15, "Bài 3", "Biết",
                 "Di sản nào sau đây là di sản thiên nhiên thế giới của Việt Nam?",
                 ["Phố cổ Hội An.", "Vịnh Hạ Long.",
                  "Nhã nhạc cung đình Huế.", "Khu trung tâm Hoàng thành Thăng Long."],
                 "B",
                 "Vịnh Hạ Long được UNESCO ghi danh là <b>di sản thiên nhiên thế giới</b> (1994). "
                 "Hội An, Hoàng thành Thăng Long là di sản <i>văn hoá vật thể</i>; Nhã nhạc là "
                 "<i>phi vật thể</i>."))

    Q.append(mcq(16, "Bài 3", "Hiểu",
                 "Vai trò cơ bản nhất của Sử học đối với công tác bảo tồn di sản là",
                 ["trang trí, làm mới di tích cho hấp dẫn du khách.",
                  "tổ chức lễ hội và bán vé tham quan.",
                  "nghiên cứu làm rõ nguồn gốc, niên đại, giá trị của di sản — cơ sở khoa học cho việc "
                  "xếp hạng, tu bổ, trùng tu.",
                  "di chuyển di tích về bảo tàng để dễ quản lí."],
                 "C",
                 "Muốn bảo tồn đúng thì trước hết phải <b>hiểu đúng</b>: biết di sản là gì, có từ bao giờ, "
                 "quý ở đâu. Đó là phần việc của Sử học — cơ sở cho xếp hạng, lập hồ sơ và tu bổ. "
                 "A, B chỉ là hoạt động phục vụ; D phản khoa học (di sản phải gắn với không gian gốc)."))

    Q.append(mcq(17, "Bài 3", "Biết",
                 "Địa danh nào sau đây là tài nguyên du lịch <b>văn hoá</b> của nước ta?",
                 ["Vịnh Hạ Long (Quảng Ninh).", "Động Phong Nha (Quảng Bình).",
                  "Khu di tích Kim Liên (Nam Đàn, Nghệ An).", "Bãi biển Nha Trang (Khánh Hoà)."],
                 "C",
                 "Kim Liên là <b>di tích lịch sử – văn hoá</b> (quê Chủ tịch Hồ Chí Minh) <font name='DJ'>→</font> tài nguyên du lịch "
                 "văn hoá. A, B, D là tài nguyên du lịch <i>tự nhiên</i>."))

    Q.append(mcq(18, "Bài 3", "Biết",
                 "Di sản văn hoá phi vật thể nào của Việt Nam được UNESCO ghi danh?",
                 ["Dân ca Ví, Giặm Nghệ Tĩnh.", "Thánh địa Mỹ Sơn.",
                  "Quần thể di tích Cố đô Huế.", "Vịnh Hạ Long."],
                 "A",
                 "Ví, Giặm Nghệ Tĩnh được ghi danh là <b>Di sản văn hoá phi vật thể đại diện của nhân loại</b> "
                 "(2014). Mỹ Sơn, Cố đô Huế là di sản văn hoá <i>vật thể</i>; Vịnh Hạ Long là di sản "
                 "<i>thiên nhiên</i>."))

    Q.append(mcq(19, "Bài 3", "Hiểu",
                 "Tác động <b>tiêu cực</b> của sự phát triển du lịch đối với di tích lịch sử – văn hoá là",
                 ["tạo thêm nguồn thu cho công tác trùng tu, tôn tạo.",
                  "lượng khách quá tải gây xuống cấp, cùng với thương mại hoá làm biến dạng không gian di tích.",
                  "quảng bá hình ảnh di sản đến du khách trong và ngoài nước.",
                  "tạo việc làm, nâng cao thu nhập cho cư dân địa phương."],
                 "B",
                 "A, C, D là tác động <b>tích cực</b>. Du lịch gây hại khi vượt <b>sức chứa</b> của di tích, "
                 "khi xây dựng ồ ạt quanh di tích, khi biến lễ hội thành sân khấu thương mại — làm mất "
                 "yếu tố gốc và tính thiêng."))

    Q.append(mcq(20, "Bài 3", "Hiểu",
                 "Lịch sử – văn hoá có vai trò như thế nào đối với sự phát triển du lịch?",
                 ["Chỉ ảnh hưởng đến hoạt động của các khách sạn, nhà hàng.",
                  "Hầu như không có vai trò vì du khách chỉ quan tâm cảnh đẹp tự nhiên.",
                  "Chủ yếu dùng để trang trí cho các ấn phẩm quảng cáo.",
                  "Là nền tảng tạo nên sản phẩm du lịch đặc sắc, tạo chiều sâu, câu chuyện và bản sắc riêng "
                  "cho điểm đến."],
                 "D",
                 "Di sản văn hoá – lịch sử chính là <b>“nguyên liệu” và “câu chuyện”</b> của sản phẩm du lịch: "
                 "tạo tuyến điểm, thuyết minh, thương hiệu điểm đến và là cơ sở để phát triển du lịch bền vững."))

    for q in Q:
        st.append(q)

    # ------------------------------------------------------------ PHẦN II
    st.append(CondPageBreak(80 * mm))
    st.append(h2("PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (Câu 1 – Câu 2)"))
    st.append(p("<i>Trong mỗi câu, thí sinh trả lời <b>đúng</b> hoặc <b>sai</b> cho từng ý a, b, c, d. "
                "Lưu ý: mỗi ý đúng được tính điểm riêng — sai một ý không mất điểm các ý còn lại, "
                "nên <b>phải trả lời đủ 4 ý</b>.</i>", "small"))

    st += tf(1, "Bài 2", "Biết <font name='DJ'>→</font> Vận dụng",
             "<b>Tình huống:</b> Nhóm học sinh lớp 10A thực hiện dự án “Tìm hiểu một di tích trên địa bàn”. "
             "Nhóm thu được: (1) bản photocopy một bài tạp chí năm 2019 viết về di tích; (2) ảnh chụp di tích "
             "do một thành viên tự chụp; (3) video giới thiệu của một kênh du lịch; (4) lời kể của một cụ già "
             "sống cạnh di tích. Nhóm băn khoăn không biết nên dùng nguồn nào trước và đánh giá độ tin cậy ra sao.",
             [("a", "Quy trình thu thập và xử lí thông tin, sử liệu gồm bốn bước: xác định vấn đề và lập kế hoạch; "
                    "thu thập sử liệu; xử lí và đánh giá sử liệu; trình bày kết quả.",
               "Đúng", "Đúng với bốn bước trong SGK. Sai lệch thường gặp là đảo bước 2 và bước 3."),
              ("b", "Sử liệu gốc là loại sử liệu ra đời sau sự kiện, được tạo ra dựa trên các nguồn tài liệu khác.",
               "Sai", "Đó là <b>sử liệu phái sinh</b>. Sử liệu gốc ra đời <b>cùng thời</b> với sự kiện, "
                      "bởi người trực tiếp liên quan."),
              ("c", "Với tấm ảnh chụp di tích, để đánh giá độ tin cậy cần xác định người chụp, thời điểm, "
                    "bối cảnh và đối chiếu với các nguồn khác.",
               "Đúng", "Ảnh có thể bị cắt ghép, chỉnh sửa hoặc chụp sai thời điểm; phải kiểm tra theo "
                       "ba câu hỏi Ai – Khi nào – Vì sao và đối chiếu chéo."),
              ("d", "Khi lời kể của cụ già mâu thuẫn với bài viết trên tạp chí, cách xử lí khoa học là chọn "
                    "nguồn mình thấy hợp lí và loại bỏ nguồn còn lại.",
               "Sai", "Phải <b>đối chiếu, so sánh bối cảnh</b> của từng nguồn, ưu tiên nguồn gốc, tìm thêm "
                      "nguồn thứ ba và ghi rõ mức độ tin cậy — không được loại bỏ tuỳ ý.")],
             note=None)

    st.append(Spacer(1, 4))
    st += tf(2, "Bài 3", "Biết <font name='DJ'>→</font> Vận dụng",
             "<b>Tình huống:</b> Một di tích lịch sử trên địa bàn đang xuống cấp. Chính quyền địa phương muốn "
             "vừa bảo tồn di tích, vừa khai thác để phát triển du lịch, nhưng lo ngại việc mở cửa cho khách "
             "tham quan sẽ làm di tích hư hại nhanh hơn.",
             [("a", "Di sản văn hoá phi vật thể bao gồm lễ hội, nghệ thuật trình diễn, nghề thủ công truyền thống, "
                    "tri thức dân gian.",
               "Đúng", "Đây là các loại hình phi vật thể cơ bản theo Luật Di sản văn hoá."),
              ("b", "Sử học chỉ có vai trò trong nghiên cứu và giảng dạy, không liên quan đến công tác bảo tồn "
                    "di sản và phát triển du lịch.",
               "Sai", "Sử học xác định giá trị, lập hồ sơ khoa học, tư vấn tu bổ, giáo dục – quảng bá và "
                      "gắn bảo tồn với phát triển; đây là cơ sở của du lịch văn hoá."),
              ("c", "Một trong những biện pháp bảo tồn và phát huy giá trị di sản là tăng cường giáo dục, "
                    "truyền thông và huy động sự tham gia của cộng đồng.",
               "Đúng", "Cộng đồng là chủ thể hưởng lợi và cũng là “người gác cổng” hiệu quả nhất của di sản."),
              ("d", "Để phát triển du lịch bền vững, chỉ cần khai thác tối đa di tích, không cần quan tâm đến "
                    "giới hạn sức chứa và công tác tu bổ.",
               "Sai", "Phải tôn trọng <b>sức chứa</b>, kết hợp khai thác với tu bổ, bảo quản; khai thác tối đa "
                      "sẽ dẫn tới xuống cấp và mất giá trị — tức là phá huỷ “nguồn vốn” của du lịch.")],
             note=None)

    # ------------------------------------------------------------ PHẦN III
    st.append(CondPageBreak(80 * mm))
    st.append(h2("PHẦN III. TỰ LUẬN (1 câu – 3,0 điểm)"))
    st.append(p("Theo bảng đặc tả, câu tự luận thuộc <b>Bài 3</b>, chia làm hai nửa: nửa <b>nhận biết – "
                "trình bày</b> (vai trò của Sử học với di sản) và nửa <b>vận dụng</b> (liên hệ, đề xuất biện pháp). "
                "Vì vậy bài làm <b>nhất thiết phải có phần liên hệ thực tiễn</b> — mất phần này là mất khoảng "
                "1,0 điểm.", S["small"]))

    outline = []
    outline.append(Paragraph("<b>Mở bài (0,25 điểm):</b> dẫn dắt bằng vai trò của di sản với đời sống; "
                             "nêu vấn đề: bảo tồn và phát huy di sản là yêu cầu cấp thiết, trong đó Sử học "
                             "giữ vai trò nền tảng.", S["body_l"]))
    outline.append(Spacer(1, 3))
    outline.append(Paragraph("<b>Thân bài (2,25 điểm)</b>", S["body_l"]))
    outline.append(Spacer(1, 2))
    outline += bullets([
        "<b>Ý 1 (0,5đ) – Khái niệm ngắn:</b> di sản văn hoá là hệ thống giá trị vật chất và tinh thần do con "
        "người sáng tạo, truyền lại qua các thế hệ; bảo tồn là giữ gìn, tu bổ, chống xuống cấp và xâm hại; "
        "phát huy là đưa giá trị di sản vào đời sống (giáo dục, du lịch, sáng tạo).",
        "<b>Ý 2 (1,5đ) – Vai trò của Sử học (nêu 4–5 ý, mỗi ý 1 câu):</b> "
        "(1) nghiên cứu làm rõ nguồn gốc, niên đại, giá trị của di sản; "
        "(2) cung cấp cơ sở khoa học để xếp hạng, lập hồ sơ, công nhận di sản; "
        "(3) tư vấn, thẩm định phương án tu bổ, trùng tu, quy hoạch bảo tồn; "
        "(4) giáo dục, truyền thông, nâng cao ý thức cộng đồng; "
        "(5) đào tạo nhân lực, cung cấp luận cứ cho chính sách, gắn bảo tồn với phát triển du lịch bền vững.",
        "<b>Ý 3 (0,75đ) – Liên hệ địa phương:</b> chọn <b>một</b> di sản (gợi ý: Khu di tích Kim Liên – Nam Đàn; "
        "Dân ca Ví, Giặm Nghệ Tĩnh; Vườn quốc gia Pù Mát; Truông Bồn). Nêu: tên, loại di sản, giá trị nổi bật, "
        "hiện trạng/thách thức. Dùng <b>1 câu</b> nêu việc Sử học đã làm (ví dụ: xác lập hồ sơ khoa học, "
        "số hoá tư liệu, biên soạn tài liệu thuyết minh).",
        "<b>Ý 4 (0,5đ) – Hai biện pháp cụ thể:</b> mỗi biện pháp phải có <b>chủ thể</b> và <b>cách làm</b>. "
        "Ví dụ: “Nhà trường đưa di sản vào tiết học trải nghiệm, cho học sinh làm sản phẩm số giới thiệu di tích”; "
        "“Chính quyền giới hạn số khách mỗi ngày và trích một phần doanh thu du lịch cho quỹ tu bổ”.",
    ])
    outline.append(Spacer(1, 2))
    outline.append(Paragraph("<b>Kết bài (0,25 điểm):</b> khẳng định lại vai trò của Sử học; liên hệ trách nhiệm "
                             "của thế hệ trẻ — hiểu, giữ gìn và lan toả giá trị di sản.", S["body_l"]))

    sample = [
        Paragraph("Di sản văn hoá là hệ thống những giá trị vật chất và tinh thần do cha ông sáng tạo, "
                  "gìn giữ và truyền lại cho chúng ta hôm nay. Giữ gìn di sản không chỉ là giữ lại những "
                  "bức tường đá hay làn điệu cũ, mà là giữ lại ký ức và bản sắc của cả một cộng đồng. "
                  "Trong công việc ấy, Sử học giữ vai trò nền tảng.", S["small"]),
        Paragraph("Trước hết, Sử học giúp <b>nhận diện và định giá</b> di sản. Nhờ nghiên cứu, ta biết một "
                  "ngôi đền có từ bao giờ, do ai dựng, thờ ai, quý ở kỹ thuật kiến trúc hay ở giá trị tâm linh. "
                  "Không có bước này, mọi hoạt động “bảo tồn” đều có thể trở thành phá hoại. Thứ hai, Sử học "
                  "cung cấp <b>cơ sở khoa học</b> để xếp hạng di tích và lập hồ sơ trình các cấp, trình UNESCO. "
                  "Thứ ba, Sử học <b>tư vấn và thẩm định</b> các phương án tu bổ, trùng tu, quy hoạch, phản biện "
                  "những cách “tôn tạo” làm sai lệch di tích. Thứ tư, Sử học <b>giáo dục và truyền thông</b>: "
                  "mỗi di tích là một bài học lịch sử sống động, giúp người dân hiểu và tự nguyện tham gia bảo vệ. "
                  "Cuối cùng, Sử học góp phần <b>đào tạo nhân lực</b>, hoạch định chính sách và <b>gắn bảo tồn với "
                  "phát triển</b>, biến di sản thành nguồn lực bền vững cho địa phương.", S["small"]),
        Paragraph("Ở quê em, <b>Dân ca Ví, Giặm Nghệ Tĩnh</b> là niềm tự hào của bao thế hệ. Năm 2014, "
                  "UNESCO đã ghi danh loại hình này là Di sản văn hoá phi vật thể đại diện của nhân loại. "
                  "Thế nhưng, người hát được ví, giặm trọn vẹn ngày càng ít, lớp trẻ nhiều người chỉ biết tên "
                  "mà không nghe hiểu lời. Chính các nhà nghiên cứu văn hoá – lịch sử đã sưu tầm, ghi âm, "
                  "phiên chú những làn điệu cổ, xác lập hồ sơ khoa học để bảo vệ và trao truyền.", S["small"]),
        Paragraph("Theo em, cần làm tốt hai việc. Một là, <b>đưa ví, giặm vào nhà trường</b>: mỗi lớp có ít nhất "
                  "một buổi học hát do nghệ nhân địa phương truyền dạy, học sinh làm sản phẩm số (video, "
                  "podcast) giới thiệu làn điệu mình yêu. Hai là, <b>gắn di sản với sinh kế</b>: chính quyền "
                  "hỗ trợ các câu lạc bộ dân ca biểu diễn phục vụ du lịch, trích một phần doanh thu lập quỹ "
                  "truyền dạy, đồng thời kiểm soát để hoạt động biểu diễn không làm mất đi tính mộc mạc, "
                  "chân chất vốn có.", S["small"]),
        Paragraph("Di sản chỉ thực sự sống khi có người hiểu nó. Vì vậy, hiểu biết lịch sử chính là cách bảo vệ "
                  "di sản bền vững nhất, và mỗi học sinh chúng ta có thể bắt đầu từ việc biết rõ, kể đúng và "
                  "lan toả những giá trị ngay trên quê hương mình.", S["small"]),
    ]

    score_rows = [
        ["Phần", "Yêu cầu", "Điểm"],
        ["Mở bài", "Dẫn dắt, nêu vấn đề rõ ràng", "0,25"],
        ["Khái niệm", "Nêu đúng di sản văn hoá, bảo tồn, phát huy", "0,50"],
        ["Vai trò của Sử học", "Từ 4–5 vai trò, có lí giải, có ví dụ", "1,50"],
        ["Liên hệ địa phương", "Đúng di sản, nêu được giá trị và thách thức", "0,75"],
        ["Biện pháp", "Hai biện pháp cụ thể, có chủ thể và cách làm", "0,50"],
        ["Kết bài", "Khẳng định, liên hệ trách nhiệm bản thân", "0,25"],
        ["<b>Tổng</b>", "", "<b>3,00</b>"],
    ]
    score_note = KeepTogether([
        Spacer(1, 4),
        Paragraph("Thang điểm tham khảo cho câu tự luận", S["h4"]),
        data_table(score_rows, [42 * mm, CW - 16 - 62 * mm, 20 * mm], align_center=[2]),
        Spacer(1, 6),
        card("thi", [
            Paragraph("<b>Ba lỗi khiến bài tự luận mất điểm oan:</b> (1) kể lể diễn biến lịch sử mà đề không hỏi; "
                      "(2) nêu biện pháp chung chung, không có chủ thể; (3) quên phần liên hệ địa phương — "
                      "mất trọn 1,0–1,25 điểm. Hãy viết theo đúng 4 khối: <b>khái niệm <font name='DJ'>→</font> vai trò <font name='DJ'>→</font> liên hệ <font name='DJ'>→</font> "
                      "biện pháp</b>.", S["small"]),
        ]),
    ])

    st.append(Spacer(1, 6))
    st += essay(
        "Trình bày vai trò của Sử học đối với công tác bảo tồn và phát huy giá trị di sản văn hoá. "
        "Liên hệ với một di sản văn hoá ở địa phương em và đề xuất hai biện pháp nhằm bảo tồn, phát huy "
        "giá trị di sản đó.",
        outline, sample, score_note)

    # ------------------------------------------------------------ bảng đáp án
    st.append(CondPageBreak(60 * mm))
    st.append(h2("BẢNG ĐÁP ÁN NHANH"))
    answers = ["C", "A", "D", "B", "C", "B", "A", "C", "D", "A",
               "C", "B", "D", "B", "B", "C", "C", "A", "B", "D"]
    hdr1 = ["Câu"] + [str(i) for i in range(1, 11)]
    row1 = ["Đáp án"] + answers[:10]
    hdr2 = ["Câu"] + [str(i) for i in range(11, 21)]
    row2 = ["Đáp án"] + answers[10:]
    w = [16 * mm] + [(CW - 16 * mm) / 10] * 10
    S_H = ParagraphStyle("ah", fontName="BVPSB", fontSize=8.6, leading=11,
                         textColor=WHITE, alignment=1)
    S_A = ParagraphStyle("aa", fontName="BVPB", fontSize=9.6, leading=12.5,
                         textColor=NAVY, alignment=1)
    for hdr, row in ((hdr1, row1), (hdr2, row2)):
        cells = [[Paragraph(h, S_H) for h in hdr],
                 [Paragraph(("ĐÁP ÁN" if i == 0 else r), S_H if i == 0 else S_A)
                  for i, r in enumerate(row)]]
        t = Table(cells, colWidths=w)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("BACKGROUND", (0, 1), (0, 1), NAVY),
            ("BACKGROUND", (1, 1), (-1, 1), colors.HexColor("#FBF6EA")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 0.5, GREY_M),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        st.append(t)
        st.append(Spacer(1, 4))
    st.append(Spacer(1, 4))

    rows = [
        ["Câu Đ/S 1", "a – Đúng", "b – Sai", "c – Đúng", "d – Sai"],
        ["Câu Đ/S 2", "a – Đúng", "b – Sai", "c – Đúng", "d – Sai"],
    ]
    st.append(data_table(rows, [30 * mm] + [(CW - 30 * mm) / 4] * 4, header=False, zebra=False,
                         align_center=[1, 2, 3, 4]))
    st.append(Spacer(1, 6))
    st.append(p("<b>Cách tự chấm:</b> mỗi câu trắc nghiệm đúng = 0,25 điểm (20 câu = 5,0 điểm); "
                "mỗi ý đúng/sai đúng = 0,25 điểm (8 ý = 2,0 điểm); câu tự luận = 3,0 điểm. "
                "Tổng 10 điểm. Nếu dưới 7 điểm, hãy quay lại Phần 1–3 và học theo sơ đồ, "
                "đừng làm thêm đề.", S["small"]))
    return st
