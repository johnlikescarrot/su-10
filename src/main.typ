#import "style.typ": *

#set document(
  title: "Đề cương Ôn tập Giữa học kì I – Môn Lịch sử lớp 10 (Kết nối tri thức, 2026–2027)",
  author: "Biên soạn chuyên sâu bám sát Ma trận & Bảng đặc tả LS10-MTGK1-26-27-HHT",
  keywords: ("Lịch sử 10", "Kết nối tri thức", "Giữa học kì 1", "2026-2027", "Đề cương ôn tập", "Hà Huy Tập"),
)

#set text(
  font: "Be Vietnam Pro",
  lang: "vi",
  region: "VN",
  size: 9.35pt,
  fill: c-ink,
  hyphenate: false,
)

#set par(
  justify: true,
  leading: 0.58em,
  spacing: 0.72em,
)

#set list(
  marker: ([•], [◦], [▪]),
  indent: 4pt,
  body-indent: 5pt,
  spacing: 0.52em,
)

#set enum(
  indent: 4pt,
  body-indent: 5pt,
  spacing: 0.52em,
)

// Render inline code tags in Be Vietnam Pro for 100% crisp Vietnamese diacritics
#show raw.where(block: false): it => box(
  fill: rgb("#F1F5F9"),
  stroke: 0.45pt + rgb("#CBD5E1"),
  inset: (x: 3.5pt, y: 1pt),
  outset: (y: 1pt),
  radius: 2.5pt,
  text(font: "Be Vietnam Pro", size: 8.3pt, weight: "semibold", fill: c-navy)[#it.text],
)

// Style Level-1 entries in Table of Contents for clear visual hierarchy
#show outline.entry.where(level: 1): it => {
  v(6pt, weak: true)
  strong(text(fill: c-primary, size: 9.5pt)[#it])
}

#set page(
  paper: "a4",
  margin: (left: 1.75cm, right: 1.75cm, top: 1.95cm, bottom: 1.85cm),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 7.8pt, fill: c-muted)
      #grid(
        columns: (1fr, auto),
        align: (left + bottom, right + bottom),
        [*ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I — LỊCH SỬ 10 (KẾT NỐI TRI THỨC)*],
        [Năm học 2026 – 2027 • Ma trận HHT],
      )
      #v(3pt)
      #line(length: 100%, stroke: 0.5pt + c-border)
    ]
  },
  footer: context {
    if counter(page).get().first() > 1 [
      #line(length: 100%, stroke: 0.5pt + c-border)
      #v(3pt)
      #set text(size: 7.8pt, fill: c-muted)
      #grid(
        columns: (1fr, auto),
        align: (left + top, right + top),
        [Tối ưu hóa trí nhớ • 100% câu hỏi & đáp án theo Ma trận – Đặc tả (20 TN + 2 Đ/S + 1 TL)],
        [*Trang #counter(page).display("1 / 1", both: true)*],
      )
    ]
  },
)

#include "part0_cover_toc.typ"
#include "part1_matrix_strategy.typ"
#include "part2_memory_cheatsheet.typ"
#include "part3_theory_lessons.typ"
#include "part4_question_bank.typ"
#include "part5a_exams.typ"
#include "part5b_answers.typ"
