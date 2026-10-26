# -*- coding: utf-8 -*-
"""Lời nói đầu và hướng dẫn sử dụng."""
from style import *
from reportlab.platypus import PageBreak


def build():
    s = []
    s += [Spacer(1, 4)]
    s += [Paragraph("LỜI NÓI ĐẦU", ParagraphStyle("ln", fontName="Head-B", fontSize=17,
                                                  leading=22, textColor=NAVY,
                                                  spaceAfter=4))]
    s += [Paragraph("và hướng dẫn sử dụng tài liệu",
                    ParagraphStyle("ln2", fontName="Head", fontSize=10, leading=14,
                                   textColor=GOLD, spaceAfter=6))]
    s += rule(NAVY, 1.6, 4)

    s += [P("Tài liệu này được biên soạn cho các em học sinh lớp 10 đang chuẩn bị cho <b>bài kiểm tra định kì "
            "giữa học kì 1 môn Lịch sử</b>, theo bộ sách <b>Kết nối tri thức với cuộc sống</b>. "
            "Nội dung bám sát ba bài đầu tiên của chương trình:")]

    s += tb([
        ["Chủ đề", "Bài", "Tên bài"],
        ["<b>Chủ đề 1.</b> Lịch sử và Sử học",
         "Bài 1", "Hiện thực lịch sử và lịch sử được con người nhận thức"],
        ["", "Bài 2", "Tri thức lịch sử và cuộc sống"],
        ["<b>Chủ đề 2.</b> Vai trò của Sử học",
         "Bài 3", "Vai trò của Sử học"],
    ], widths=[2.1, 0.75, 3.75], align_center=[1], sp_after=8)

    s += [P("Điểm khác biệt của tài liệu này so với một cuốn “sách tóm tắt” thông thường là nó được thiết kế "
            "<b>để ghi nhớ</b>, chứ không chỉ để đọc. Mọi nội dung đều được chuyển thành một trong các dạng sau:")]
    s += bullets([
        "<b>Sơ đồ khối</b> – nhìn một lần thấy được toàn bộ cấu trúc bài.",
        "<b>Bảng so sánh</b> – đặt hai khái niệm cạnh nhau để thấy khác biệt ngay lập tức.",
        "<b>Bảng phân loại</b> – hệ thống hoá các loại hình, các bước, các vai trò.",
        "<b>Mẹo nhớ</b> – những cụm từ có vần, có hình ảnh, giúp lấy lại kiến thức trong vài giây.",
        "<b>Câu hỏi luyện tập</b> – kèm đáp án và giải thích để tự kiểm tra.",
    ])

    s += box("CẤU TRÚC TÀI LIỆU – NÊN ĐỌC THEO THỨ TỰ NÀY", [
        "<b>Phần A</b> – Phân tích đề: biết học gì, học đến đâu, phân bổ thời gian ra sao. Đọc trước tiên.",
        "<b>Phần B</b> – Chủ đề 1 (Bài 1 và Bài 2): kiến thức trọng tâm, sơ đồ, bảng so sánh, mẹo nhớ.",
        "<b>Phần C</b> – Chủ đề 2 (Bài 3): bài quan trọng nhất, chiếm gần một nửa số điểm.",
        "<b>Phần D</b> – Tổng hợp ghi nhớ nhanh: bảng tổng hợp, mẹo nhớ, bẫy đề. Dùng để ôn nước rút.",
        "<b>Phần E</b> – Ngân hàng câu hỏi: 50 câu trắc nghiệm, 8 câu Đúng/Sai, 6 câu tự luận có đáp án.",
        "<b>Phần F</b> – Đề mẫu bám ma trận và thang điểm chi tiết: dùng để thi thử đúng 45 phút.",
        "<b>Phần G</b> – Checklist tự kiểm tra: biết mình còn thiếu gì trước khi vào phòng thi.",
    ], "note")

    s += [P("Một lời nhắn nhỏ trước khi bắt đầu. Nhiều bạn nghĩ Lịch sử là môn “phải học thuộc”. "
            "Điều đó chỉ đúng một nửa. Phần lớn câu hỏi trong đề này không hỏi “năm nào, ai làm gì”, "
            "mà hỏi <b>“vì sao”, “phân biệt thế nào”, “điều đó có ý nghĩa gì”</b>. "
            "Vì vậy, hãy học bằng cách <b>tự đặt câu hỏi cho chính mình</b>: khái niệm này khác khái niệm kia ở đâu, "
            "vì sao nó quan trọng, nếu thiếu nó thì sao. Khi bạn trả lời được những câu hỏi đó bằng lời của mình, "
            "bạn không cần học thuộc nữa – kiến thức đã là của bạn.")]

    s += [P("Chúc các em ôn tập hiệu quả và đạt kết quả cao nhất.")]

    s += [Spacer(1, 10)]
    s += [Paragraph("Nhóm biên soạn", ParagraphStyle("sig", fontName="Head-B", fontSize=9.5,
                                                     leading=13, textColor=NAVY,
                                                     alignment=TA_RIGHT))]
    s += [Paragraph("Tài liệu ôn thi Lịch sử 10", ParagraphStyle("sig2", fontName="Head",
                                                                 fontSize=8.4, leading=11,
                                                                 textColor=GRAY,
                                                                 alignment=TA_RIGHT))]
    return s
