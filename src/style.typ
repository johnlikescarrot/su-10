// ============================================================================
// DESIGN SYSTEM & TYPOGRAPHIC COMPONENTS — LỊCH SỬ 10 KNTT (GK1 2026–2027)
// Compatible with Typst 0.15+
// ============================================================================

#let c-primary     = rgb("#7C1D26")
#let c-primary-lt  = rgb("#FEF2F2")
#let c-primary-bd  = rgb("#FCA5A5")

#let c-navy        = rgb("#1E3A5F")
#let c-navy-lt     = rgb("#EFF6FF")
#let c-navy-bd     = rgb("#93C5FD")

#let c-teal        = rgb("#0F766E")
#let c-teal-lt     = rgb("#F0FDFA")
#let c-teal-bd     = rgb("#5EEAD4")

#let c-amber       = rgb("#B45309")
#let c-amber-lt    = rgb("#FFFBEB")
#let c-amber-bd    = rgb("#FCD34D")

#let c-alert       = rgb("#B91C1C")
#let c-ink         = rgb("#1E293B")
#let c-muted       = rgb("#475569")
#let c-subtle      = rgb("#F8FAFC")
#let c-warm-bg     = rgb("#FAF8F5")
#let c-border      = rgb("#CBD5E1")

// Micro-badges for cognitive levels, competencies, and matrix coordinates
#let pill(label, bg, fg, bd: none) = box(
  fill: bg,
  stroke: if bd != none { 0.6pt + bd } else { none },
  inset: (x: 5pt, y: 2pt),
  outset: (y: 1pt),
  radius: 3pt,
  baseline: 15%,
  text(size: 7.6pt, weight: "bold", fill: fg)[#label],
)

#let nb  = pill("Biết", rgb("#DBEAFE"), rgb("#1E40AF"), bd: rgb("#93C5FD"))
#let th  = pill("Hiểu", rgb("#CCFBF1"), rgb("#0F766E"), bd: rgb("#5EEAD4"))
#let vd  = pill("Vận dụng", rgb("#FEF3C7"), rgb("#92400E"), bd: rgb("#FCD34D"))

#let nl1 = pill("NL1", rgb("#F1F5F9"), rgb("#334155"), bd: rgb("#CBD5E1"))
#let nl2 = pill("NL2", rgb("#F3E8FF"), rgb("#6B21A8"), bd: rgb("#D8B4FE"))
#let nl3 = pill("NL3", rgb("#FFE4E6"), rgb("#9F1239"), bd: rgb("#FDA4AF"))

#let slot(code) = pill(code, rgb("#1E293B"), white)
#let kw(word) = text(weight: "bold", fill: c-primary)[#word]
#let kwb(word) = text(weight: "bold", fill: c-navy)[#word]
#let kwt(word) = text(weight: "bold", fill: c-teal)[#word]

// Major Part Banner (Level-1 Heading Registered in PDF Bookmarks & Clean TOC)
#let part-banner(part-label, title, subtitle) = {
  block(
    width: 100%,
    breakable: false,
    above: 6pt,
    below: 12pt,
    fill: gradient.linear(c-primary, rgb("#58131A"), angle: 12deg),
    radius: 8pt,
    inset: (x: 16pt, y: 13pt),
    stroke: 1pt + rgb("#450A0A"),
  )[
    #place(hide(heading(level: 1, outlined: true, bookmarked: true)[#title]))
    #text(size: 8.5pt, weight: "bold", tracking: 1.2pt, fill: rgb("#FDE68A"))[#upper(part-label)]
    #v(3pt)
    #text(size: 14.5pt, weight: "extrabold", fill: white)[#title]
    #if subtitle != none [
      #v(3pt)
      #text(size: 9.1pt, style: "italic", fill: rgb("#FEE2E2"))[#subtitle]
    ]
  ]
}

// Section Heading (Level-2 Heading Registered in PDF Bookmarks & Clean TOC)
#let sec-heading(title, badge: none, outlined-sec: true) = {
  block(breakable: false, sticky: true, above: 13pt, below: 7pt)[
    #if outlined-sec [
      #place(hide(heading(level: 2, outlined: true, bookmarked: true)[#title]))
    ]
    #grid(
      columns: (4pt, 1fr, auto),
      column-gutter: 8pt,
      align: (left + horizon, left + horizon, right + horizon),
      rect(width: 4pt, height: 16pt, radius: 2pt, fill: c-primary),
      text(size: 11.6pt, weight: "bold", fill: c-navy)[#title],
      if badge != none { badge } else { [] },
    )
    #v(2pt)
    #line(length: 100%, stroke: 0.6pt + c-border)
  ]
}

// Sub-section Heading (Level-3)
#let sub-heading(title) = {
  block(breakable: false, sticky: true, above: 9pt, below: 5pt)[
    #text(size: 10.2pt, weight: "bold", fill: c-primary)[▸ #title]
  ]
}

// Memory Hook / Mnemonic Callout Box
#let memory-box(title, body, breakable-box: false) = block(
  width: 100%,
  breakable: breakable-box,
  above: 7pt,
  below: 7pt,
  fill: c-amber-lt,
  stroke: (left: 3.5pt + c-amber, top: 0.6pt + c-amber-bd, right: 0.6pt + c-amber-bd, bottom: 0.6pt + c-amber-bd),
  radius: (right: 6pt, left: 2pt),
  inset: (x: 11pt, y: 8.5pt),
)[
  #text(size: 9.5pt, weight: "bold", fill: c-amber)[★ #title]
  #v(3pt)
  #set text(size: 9.2pt, fill: c-ink)
  #body
]

// Exam Trap Alert Box
#let trap-box(title, body, breakable-box: false) = block(
  width: 100%,
  breakable: breakable-box,
  above: 7pt,
  below: 7pt,
  fill: c-primary-lt,
  stroke: (left: 3.5pt + c-alert, top: 0.6pt + c-primary-bd, right: 0.6pt + c-primary-bd, bottom: 0.6pt + c-primary-bd),
  radius: (right: 6pt, left: 2pt),
  inset: (x: 11pt, y: 8.5pt),
)[
  #text(size: 9.5pt, weight: "bold", fill: c-alert)[⚠ #title]
  #v(3pt)
  #set text(size: 9.2pt, fill: c-ink)
  #body
]

// Info / Synthesis Box
#let info-box(title, body, accent: c-navy, bg: c-navy-lt, bd: c-navy-bd, breakable-box: false) = block(
  width: 100%,
  breakable: breakable-box,
  above: 7pt,
  below: 7pt,
  fill: bg,
  stroke: (left: 3.5pt + accent, top: 0.6pt + bd, right: 0.6pt + bd, bottom: 0.6pt + bd),
  radius: (right: 6pt, left: 2pt),
  inset: (x: 11pt, y: 8.5pt),
)[
  #text(size: 9.5pt, weight: "bold", fill: accent)[#title]
  #v(3pt)
  #set text(size: 9.2pt, fill: c-ink)
  #body
]

// Historical Quote Box
#let quote-box(quote-text, attribution) = block(
  width: 100%,
  breakable: false,
  above: 6pt,
  below: 6pt,
  fill: c-warm-bg,
  stroke: (left: 3pt + c-teal, rest: 0.5pt + rgb("#D6CFC7")),
  radius: (right: 6pt, left: 2pt),
  inset: (x: 11pt, y: 7.5pt),
)[
  #text(size: 9.2pt, style: "italic", fill: c-ink)[“#quote-text”]
  #v(2pt)
  #align(right)[#text(size: 8.4pt, weight: "semibold", fill: c-teal)[— #attribution]]
]

// Multiple-Choice Question Item (compact, break-safe)
#let mcq(num, tags, stem, a, b, c, d, two-col: false) = block(
  width: 100%,
  breakable: false,
  above: 5.5pt,
  below: 5.5pt,
  inset: (x: 8pt, y: 6pt),
  fill: white,
  stroke: 0.5pt + rgb("#E2E8F0"),
  radius: 5pt,
)[
  #text(size: 9.3pt)[#strong(text(fill: c-primary)[Câu #num.]) #if tags != none [#tags ] #stem]
  #v(3pt)
  #set text(size: 9.0pt, fill: c-ink)
  #if two-col [
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 10pt,
      row-gutter: 3.5pt,
      [*A.* #a], [*B.* #b],
      [*C.* #c], [*D.* #d],
    )
  ] else [
    #stack(
      spacing: 3pt,
      [*A.* #a],
      [*B.* #b],
      [*C.* #c],
      [*D.* #d],
    )
  ]
]

// True/False Cluster Question Item (Part II GDPT 2018 Format)
#let tf-cluster(num, tags, source-note, passage, sa, sb, sc, sd) = block(
  width: 100%,
  breakable: false,
  above: 7pt,
  below: 7pt,
  inset: (x: 10pt, y: 8pt),
  fill: white,
  stroke: 0.8pt + c-teal-bd,
  radius: 6pt,
)[
  #text(size: 9.5pt)[#strong(text(fill: c-teal)[Câu #num.]) #if tags != none [#tags ] Đọc đoạn tư liệu sau đây:]
  #v(3.5pt)
  #block(
    width: 100%,
    fill: c-warm-bg,
    stroke: (left: 2.5pt + c-amber, rest: 0.4pt + rgb("#E2E8F0")),
    inset: (x: 9pt, y: 6.5pt),
    radius: 3pt,
  )[
    #text(size: 8.9pt, style: "italic", fill: c-ink)[#passage]
    #if source-note != none [
      #v(2pt)
      #align(right)[#text(size: 8.1pt, fill: c-muted)[(#source-note)]]
    ]
  ]
  #v(4pt)
  #set text(size: 9.0pt, fill: c-ink)
  #stack(
    spacing: 3.8pt,
    [*a)* #sa],
    [*b)* #sb],
    [*c)* #sc],
    [*d)* #sd],
  )
]

// Authentic School Midterm Exam Paper Header
#let exam-paper-banner(exam-code, subtitle) = block(
  width: 100%,
  breakable: false,
  above: 6pt,
  below: 9pt,
  fill: c-subtle,
  stroke: 1.2pt + c-navy,
  radius: 6pt,
  inset: (x: 12pt, y: 9pt),
)[
  #grid(
    columns: (1fr, 1.25fr),
    column-gutter: 10pt,
    align: (center + horizon, center + horizon),
    [
      #text(size: 8.6pt, weight: "semibold", fill: c-muted)[TRƯỜNG THPT HÀ HUY TẬP (HHT)] \
      #text(size: 9.2pt, weight: "bold", fill: c-navy)[TỔ LỊCH SỬ — KHỐI 10] \
      #line(length: 45%, stroke: 0.7pt + c-navy) \
      #v(2pt)
      #pill(exam-code, c-primary, white)
    ],
    [
      #text(size: 9.5pt, weight: "extrabold", fill: c-primary)[ĐỀ KIỂM TRA ĐỊNH KÌ GIỮA HỌC KÌ I] \
      #text(size: 8.8pt, weight: "bold", fill: c-ink)[NĂM HỌC 2026 – 2027 • MÔN: LỊCH SỬ 10 (KNTT)] \
      #text(size: 8.4pt, fill: c-muted)[Thời gian làm bài: *45 phút* (không kể thời gian phát đề)] \
      #text(size: 8.1pt, style: "italic", fill: c-teal)[#subtitle]
    ],
  )
]
