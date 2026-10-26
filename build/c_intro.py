# -*- coding: utf-8 -*-
"""c_intro.py — Phần mở đầu: phân tích đề, bản đồ ôn tập, cách dùng đề cương."""
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from layout import (S, CW, h2, h3, p, bullets, numbered, card, data_table, quote,
                    band, NAVY, GOLD, RED, TEAL, GREY_L, GREY_M, WHITE, INK, MUTED,
                    CHECK, CROSS, ARROW, STAR, WARN)


def story():
    st = []
    st += band("0", "BẢN ĐỒ ÔN TẬP", "Trước khi học, hãy biết mình phải học cái gì")

    st.append(h2("1. Đề thi này kiểm tra đúng 3 bài — và chỉ 3 bài"))
    st.append(p(
        "Căn cứ <b>ma trận đề</b> và <b>bảng đặc tả</b> đi kèm đề kiểm tra định kì giữa học kì I "
        "(Lịch sử 10, năm học 2026–2027, thời gian 45 phút), đề gồm <b>20 câu trắc nghiệm "
        "nhiều lựa chọn + 2 câu trắc nghiệm đúng/sai (mỗi câu 4 ý) + 1 câu tự luận</b>. "
        "Toàn bộ nội dung nằm trong <b>Chương/Chủ đề 1 (Lịch sử và Sử học)</b> và "
        "<b>Chủ đề 2 (Vai trò của Sử học)</b> của sách <i>Lịch sử 10 – Kết nối tri thức với cuộc sống</i>: "
        "Bài 1, Bài 2 và Bài 3. <b>Không có câu nào nằm ngoài ba bài này.</b>"))

    st.append(card("chot", [
        Paragraph(
            "Ba bài – ba nhóm câu hỏi – ba cách học khác nhau. Học đúng cách sẽ tiết kiệm "
            "khoảng 60% thời gian so với đọc lại toàn bộ sách.", S["small"]),
    ], title="Nguyên tắc vàng"))

    st.append(h2("2. Bản đồ phân bổ câu hỏi (theo đúng bảng đặc tả)"))
    rows = [
        ["Bài / Chủ đề", "Câu hỏi trong đề", "Dạng", "Mức độ chủ yếu", "Trọng tâm ôn"],
        ["<b>Bài 1.</b> Hiện thực lịch sử và lịch sử được con người nhận thức<br/><i>(Chủ đề 1)</i>",
         "Câu 1 <font name='DJ'>→</font> 6<br/><font size=7 color='#5C6675'>TN nhiều lựa chọn</font>",
         "TN", "5 Biết · 1 Hiểu",
         "Khái niệm lịch sử, Sử học; đối tượng – chức năng – nhiệm vụ; phân biệt hiện thực lịch sử với nhận thức lịch sử"],
        ["<b>Bài 2.</b> Tri thức lịch sử và cuộc sống<br/><i>(Chủ đề 1)</i>",
         "Câu 7 <font name='DJ'>→</font> 13<br/>+ Câu Đ/S 1 (4 ý a–d)<br/><font size=7 color='#5C6675'>7 TN + 4 ý đúng/sai</font>",
         "TN + Đ/S", "7 Biết · 3 Hiểu · 1 Vận dụng",
         "Tri thức lịch sử và vai trò; học tập suốt đời; sử liệu; quy trình 4 bước thu thập – xử lí thông tin"],
        ["<b>Bài 3.</b> Vai trò của Sử học<br/><i>(Chủ đề 2)</i>",
         "Câu 14 <font name='DJ'>→</font> 20<br/>+ Câu Đ/S 2 (4 ý a–d)<br/>+ 1 câu tự luận",
         "TN + Đ/S + TL", "6 Biết · 4 Hiểu · 1 Vận dụng",
         "Di sản văn hoá – thiên nhiên; Sử học với bảo tồn và phát huy di sản; Sử học với du lịch"],
        ["<b>Tổng</b>", "<b>20 câu TN + 8 ý đúng/sai + 1 tự luận</b> = 28 lệnh hỏi TN + 1 TL",
         "—", "<b>≈50% Biết · 25% Hiểu · 25% Vận dụng</b>", "—"],
    ]
    st.append(data_table(rows, [42 * mm, 40 * mm, 17 * mm, 27 * mm, CW - 126 * mm],
                         align_center=[2], ))
    st.append(Spacer(1, 4))
    st.append(p(
        "<b>Đọc ra điều gì?</b> Một nửa số điểm là câu hỏi <b>nhận biết</b> (nhớ đúng định nghĩa, "
        "đúng đặc điểm, đúng tên di sản). Nghĩa là: <b>học thuộc có cấu trúc là đã có 5 điểm</b>. "
        "Phần <b>vận dụng</b> (25%) tập trung gần như toàn bộ ở <b>Bài 3</b> và ở <b>câu tự luận</b> — "
        "đây là nơi phân loại học sinh, và cũng là nơi dễ ăn điểm nhất nếu chuẩn bị sẵn “công thức” "
        "liên hệ địa phương.", S["small"]))

    st.append(h2("3. Ba năng lực được đo — và cách “chiều” từng năng lực"))
    rows = [
        ["Năng lực", "Đề hỏi kiểu gì", "Cách ôn hiệu quả"],
        ["<b>NL1.</b> Tìm hiểu lịch sử",
         "Nêu/trình bày khái niệm, các bước, cách sưu tầm và xử lí sử liệu",
         "Học theo <b>trật tự</b> (bước 1, 2, 3, 4). Vẽ lại quy trình bằng mũi tên, che sách đọc lại."],
        ["<b>NL2.</b> Nhận thức và tư duy lịch sử",
         "Giải thích, phân biệt, nhận diện qua ví dụ/tình huống cụ thể",
         "Luôn hỏi “<b>vì sao</b>” và tự tạo <b>phản ví dụ</b>: nếu đổi một từ trong định nghĩa thì sai ở đâu?"],
        ["<b>NL3.</b> Vận dụng kiến thức, kĩ năng",
         "Đề xuất biện pháp bảo tồn, liên hệ thực tiễn, đánh giá tác động của du lịch",
         "Chuẩn bị sẵn <b>3 bộ ví dụ địa phương</b> (di tích, lễ hội, di sản thiên nhiên) + 4 nhóm biện pháp."],
    ]
    st.append(data_table(rows, [40 * mm, 62 * mm, CW - 102 * mm]))

    st.append(h2("4. Năm bước dùng đề cương này cho đúng"))
    st += numbered([
        "<b>Bước 1 – Đọc “Bản đồ” (5 phút).</b> Nắm 3 bài, nắm dạng câu. Không học thuộc ở bước này.",
        "<b>Bước 2 – Học theo bài, không học theo đề (mỗi bài 25–30 phút).</b> Đọc mục kiến thức cốt lõi, "
        "tự vẽ lại sơ đồ trên giấy trắng. Nếu không vẽ được, chưa tính là đã học.",
        "<b>Bước 3 – Che đáp án, làm 20 câu trắc nghiệm (20 phút).</b> Ghi đáp án ra giấy, sau đó mới so bảng đáp án. "
        "Câu sai: đọc lại phần “Vì sao” và quay về đúng mục kiến thức tương ứng.",
        "<b>Bước 4 – Luyện 2 câu đúng/sai và câu tự luận (20 phút).</b> Tự luận phải <b>viết ra giấy</b>, "
        "bấm giờ 12–15 phút, rồi so với dàn ý. Đừng chỉ đọc bài mẫu.",
        "<b>Bước 5 – Ôn cách quãng (3 lần: sau 1 ngày – sau 3 ngày – trước giờ thi).</b> Mỗi lần chỉ 10 phút, "
        "chỉ dùng bảng flashcard ở Phần 5 và danh sách “10 lỗi mất điểm”.",
    ])

    st.append(card("thi", [
        Paragraph(
            "<b>Mẹo phân bổ 45 phút:</b> 20 câu trắc nghiệm <font name='DJ'>→</font> tối đa 15 phút (45 giây/câu); "
            "2 câu đúng/sai <font name='DJ'>→</font> 10 phút; câu tự luận <font name='DJ'>→</font> 15 phút; 5 phút cuối để rà lại và tô đáp án. "
            "Câu nào quá 60 giây mà chưa chắc: đánh dấu, làm tiếp, quay lại sau.", S["small"]),
    ]))

    st.append(h2("5. Ghi chú về tệp đề gốc (nên đọc)"))
    st.append(quote(
        "Tệp <b>“LS10- MTGK1-26-27-HHT.docx”</b> cung cấp <b>ma trận đề</b> và <b>bảng đặc tả</b> "
        "(số lệnh hỏi, dạng câu, mức độ tư duy, đơn vị kiến thức cho từng câu), "
        "nhưng không chứa nội dung chữ của các câu hỏi. "
        "Vì vậy, <b>Phần 4</b> của đề cương biên soạn đầy đủ 28 lệnh hỏi + 1 câu tự luận bám sát "
        "từng dòng của bảng đặc tả (Câu 1–6 <font name='DJ'>→</font> Bài 1; Câu 7–13 và câu Đ/S 1 <font name='DJ'>→</font> Bài 2; "
        "Câu 14–20, câu Đ/S 2 và tự luận <font name='DJ'>→</font> Bài 3), kèm đáp án và giải thích chi tiết. "
        "Nếu có tệp đề gốc, chỉ cần thay nội dung câu hỏi — cấu trúc, đáp án và phần kiến thức "
        "của đề cương vẫn dùng được nguyên vẹn."))
    return st
