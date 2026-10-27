#!/usr/bin/env python3
"""Generate crisp, publication-grade vector SVG diagrams for Grade 10 History Study Guide."""

from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "src" / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

FONT = "Be Vietnam Pro, sans-serif"


def write_svg(name: str, content: str) -> None:
    path = ASSETS_DIR / name
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Generated {path.relative_to(ASSETS_DIR.parent.parent)} ({len(content)} chars)")


def gen_matrix_weight_chart() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 285" width="860" height="285">
  <defs>
    <linearGradient id="bgCard" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FAF8F5"/>
      <stop offset="100%" stop-color="#F3EFEA"/>
    </linearGradient>
  </defs>
  <rect x="2" y="2" width="856" height="281" rx="12" fill="url(#bgCard)" stroke="#D6CFC7" stroke-width="1.5"/>
  <text x="430" y="28" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="700" fill="#7C1D26">BỨC TRANH TRỌNG SỐ ĐIỂM SỐ ĐỀ KIỂM TRA GIỮA HỌC KÌ 1 (10,0 ĐIỂM — 45 PHÚT)</text>

  <!-- Panel 1: By Lesson -->
  <rect x="18" y="44" width="272" height="225" rx="9" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2"/>
  <text x="154" y="66" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="700" fill="#1E3A5F">1. THEO BÀI HỌC (SGK KNTT)</text>

  <!-- Bai 1 -->
  <text x="32" y="94" font-family="{FONT}" font-size="10.5" font-weight="600" fill="#334155">Bài 1. Hiện thực &amp; Nhận thức LS</text>
  <text x="276" y="94" text-anchor="end" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#1E3A5F">1,50đ (15%)</text>
  <rect x="32" y="101" width="244" height="14" rx="7" fill="#E2E8F0"/>
  <rect x="32" y="101" width="37" height="14" rx="7" fill="#2563EB"/>
  <text x="32" y="128" font-family="{FONT}" font-size="9.2" fill="#64748B">6 câu TN (I.1→I.6) • Không Đ/S, không TL</text>

  <!-- Bai 2 -->
  <text x="32" y="152" font-family="{FONT}" font-size="10.5" font-weight="600" fill="#334155">Bài 2. Tri thức LS &amp; Cuộc sống</text>
  <text x="276" y="152" text-anchor="end" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#0F766E">2,75đ (27,5%)</text>
  <rect x="32" y="159" width="244" height="14" rx="7" fill="#E2E8F0"/>
  <rect x="32" y="159" width="67" height="14" rx="7" fill="#0F766E"/>
  <text x="32" y="186" font-family="{FONT}" font-size="9.2" fill="#64748B">7 câu TN (I.7→I.13) + 1 câu Đ/S (II.1a–d)</text>

  <!-- Bai 3 -->
  <text x="32" y="210" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#7C1D26">Bài 3. Vai trò của Sử học ★</text>
  <text x="276" y="210" text-anchor="end" font-family="{FONT}" font-size="11" font-weight="800" fill="#7C1D26">5,75đ (57,5%)</text>
  <rect x="32" y="217" width="244" height="16" rx="8" fill="#FEE2E2"/>
  <rect x="32" y="217" width="140" height="16" rx="8" fill="#991B1B"/>
  <text x="32" y="248" font-family="{FONT}" font-size="9.2" font-weight="600" fill="#991B1B">7 câu TN + 1 câu Đ/S + Trọn vẹn 3,0đ TL!</text>

  <!-- Panel 2: By Exam Part -->
  <rect x="302" y="44" width="256" height="225" rx="9" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2"/>
  <text x="430" y="66" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="700" fill="#1E3A5F">2. THEO DẠNG THỨC ĐỀ THI</text>

  <rect x="316" y="82" width="228" height="50" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
  <text x="328" y="101" font-family="{FONT}" font-size="11" font-weight="700" fill="#1D4ED8">Phần I: TN Nhiều lựa chọn</text>
  <text x="532" y="101" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="800" fill="#1D4ED8">5,0đ</text>
  <text x="328" y="120" font-family="{FONT}" font-size="9.5" fill="#475569">20 câu (I.1 → I.20) × 0,25đ/câu (50%)</text>

  <rect x="316" y="142" width="228" height="50" rx="8" fill="#F0FDFA" stroke="#99F6E4" stroke-width="1"/>
  <text x="328" y="161" font-family="{FONT}" font-size="11" font-weight="700" fill="#0F766E">Phần II: TN Đúng / Sai</text>
  <text x="532" y="161" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="800" fill="#0F766E">2,0đ</text>
  <text x="328" y="180" font-family="{FONT}" font-size="9.5" fill="#475569">2 câu (8 ý a–d) × 1,0đ/câu (20%)</text>

  <rect x="316" y="202" width="228" height="54" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
  <text x="328" y="221" font-family="{FONT}" font-size="11" font-weight="700" fill="#991B1B">Phần III: Tự luận (Bài 3)</text>
  <text x="532" y="221" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="800" fill="#991B1B">3,0đ</text>
  <text x="328" y="239" font-family="{FONT}" font-size="9.3" fill="#475569">1 câu 2 vế: Ý 1 Biết (1,0đ) + Ý 2 VD (2,0đ)</text>

  <!-- Panel 3: By Cognitive Level & Competency -->
  <rect x="570" y="44" width="272" height="225" rx="9" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2"/>
  <text x="706" y="66" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="700" fill="#1E3A5F">3. CẤP ĐỘ TƯ DUY &amp; NĂNG LỰC</text>

  <!-- Stacked bar for Thinking levels -->
  <text x="584" y="90" font-family="{FONT}" font-size="10" font-weight="700" fill="#334155">Tỷ lệ cấp độ tư duy (50% – 25% – 25%):</text>
  <rect x="584" y="98" width="122" height="24" rx="4" fill="#1E40AF"/>
  <text x="645" y="114" text-anchor="middle" font-family="{FONT}" font-size="9.5" font-weight="700" fill="#FFFFFF">Biết: 5,0đ</text>
  <rect x="708" y="98" width="60" height="24" rx="4" fill="#0D9488"/>
  <text x="738" y="114" text-anchor="middle" font-family="{FONT}" font-size="9.5" font-weight="700" fill="#FFFFFF">Hiểu 2,5</text>
  <rect x="770" y="98" width="58" height="24" rx="4" fill="#B45309"/>
  <text x="799" y="114" text-anchor="middle" font-family="{FONT}" font-size="9.5" font-weight="700" fill="#FFFFFF">VD 2,5</text>

  <text x="584" y="140" font-family="{FONT}" font-size="9.2" fill="#475569">• Biết: 16 lệnh TN (4,0đ) + 1/2 TL (1,0đ)</text>
  <text x="584" y="156" font-family="{FONT}" font-size="9.2" fill="#475569">• Hiểu: 10 lệnh TN (2,5đ)</text>
  <text x="584" y="172" font-family="{FONT}" font-size="9.2" fill="#475569">• Vận dụng: 2 ý Đ/S d (0,5đ) + 1/2 TL (2,0đ)</text>

  <line x1="584" y1="184" x2="828" y2="184" stroke="#E2E8F0" stroke-width="1"/>
  <text x="584" y="202" font-family="{FONT}" font-size="10" font-weight="700" fill="#334155">Tỷ lệ 3 năng lực Lịch sử (40%–30%–30%):</text>
  <text x="584" y="220" font-family="{FONT}" font-size="9.3" fill="#1E3A5F">• NL1 (Tìm hiểu lịch sử): 4,0 điểm (40%)</text>
  <text x="584" y="236" font-family="{FONT}" font-size="9.3" fill="#0F766E">• NL2 (Nhận thức &amp; tư duy): 3,0 điểm (30%)</text>
  <text x="584" y="252" font-family="{FONT}" font-size="9.3" fill="#991B1B">• NL3 (Vận dụng kiến thức): 3,0 điểm (30%)</text>
</svg>"""
    write_svg("matrix_weight_chart.svg", svg)


def gen_timeline_strategy() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 155" width="860" height="155">
  <rect x="2" y="2" width="856" height="151" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.3"/>
  <text x="430" y="26" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" fill="#1E3A5F">CHIẾN THUẬT PHÂN BỔ 45 PHÚT LÀM BÀI THỰC CHIẾN — TỐI ĐA HÓA TỪNG 0,25 ĐIỂM</text>

  <!-- Step 1 -->
  <rect x="18" y="42" width="198" height="96" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
  <rect x="18" y="42" width="198" height="24" rx="8" fill="#2563EB"/>
  <text x="117" y="58" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#FFFFFF">CHẶNG 1: PHÚT 00 → 12 (12p)</text>
  <text x="117" y="83" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#1E3A5F">20 câu Phần I (5,0 điểm)</text>
  <text x="117" y="101" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#475569">~35 giây/câu • Gạch chân từ khóa</text>
  <text x="117" y="117" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#475569">Làm chắc 14 câu Biết trước</text>

  <!-- Arrow 1 -->
  <polygon points="233,90 221,84 221,96" fill="#64748B"/>

  <!-- Step 2 -->
  <rect x="236" y="42" width="198" height="96" rx="8" fill="#F0FDFA" stroke="#14B8A6" stroke-width="1.5"/>
  <rect x="236" y="42" width="198" height="24" rx="8" fill="#0F766E"/>
  <text x="335" y="58" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#FFFFFF">CHẶNG 2: PHÚT 12 → 22 (10p)</text>
  <text x="335" y="83" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#0F766E">2 câu Đúng/Sai (2,0 điểm)</text>
  <text x="335" y="101" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#475569">5 phút/câu • Soi từ tuyệt đối</text>
  <text x="335" y="117" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#991B1B">Cẩn trọng: sai 1 ý mất 0,5đ!</text>

  <!-- Arrow 2 -->
  <polygon points="451,90 439,84 439,96" fill="#64748B"/>

  <!-- Step 3 -->
  <rect x="454" y="42" width="214" height="96" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.5"/>
  <rect x="454" y="42" width="214" height="24" rx="8" fill="#991B1B"/>
  <text x="561" y="58" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#FFFFFF">CHẶNG 3: PHÚT 22 → 41 (19p)</text>
  <text x="561" y="83" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#991B1B">Câu Tự luận 2 vế (3,0 điểm)</text>
  <text x="561" y="101" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#475569">6p cho Ý 1 (1,0đ) + 13p cho Ý 2 (2,0đ)</text>
  <text x="561" y="117" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#475569">Trình bày tách ý, nêu ví dụ cụ thể</text>

  <!-- Arrow 3 -->
  <polygon points="685,90 673,84 673,96" fill="#64748B"/>

  <!-- Step 4 -->
  <rect x="688" y="42" width="154" height="96" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5"/>
  <rect x="688" y="42" width="154" height="24" rx="8" fill="#B45309"/>
  <text x="765" y="58" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#FFFFFF">PHÚT 41 → 45 (4p)</text>
  <text x="765" y="83" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#92400E">Rà soát phiếu đáp án</text>
  <text x="765" y="101" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#475569">Đếm đủ 20 câu I + 8 ý II</text>
  <text x="765" y="117" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#475569">Kiểm tra từ phủ định</text>
</svg>"""
    write_svg("timeline_45min_strategy.svg", svg)


def gen_bai1_diagram() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 250" width="860" height="250">
  <rect x="2" y="2" width="856" height="246" rx="12" fill="#FAF8F5" stroke="#D6CFC7" stroke-width="1.4"/>
  <text x="430" y="26" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" fill="#7C1D26">SƠ ĐỒ TƯ DUY BÀI 1: HIỆN THỰC LỊCH SỬ — NHẬN THỨC LỊCH SỬ — SỬ HỌC (1,50 ĐIỂM)</text>

  <!-- Box Left: Hien thuc lich su -->
  <rect x="20" y="42" width="248" height="106" rx="9" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.6"/>
  <rect x="20" y="42" width="248" height="26" rx="9" fill="#1E40AF"/>
  <text x="144" y="59" text-anchor="middle" font-family="{FONT}" font-size="11" font-weight="700" fill="#FFFFFF">HIỆN THỰC LỊCH SỬ (Khẩu quyết: 1–K–B)</text>
  <text x="32" y="84" font-family="{FONT}" font-size="9.6" fill="#1E293B">• Tất cả những gì ĐÃ DIỄN RA trong quá khứ</text>
  <text x="32" y="101" font-family="{FONT}" font-size="9.6" font-weight="600" fill="#1E40AF">• Duy nhất (chỉ có 1) • Tồn tại KHÁCH QUAN</text>
  <text x="32" y="118" font-family="{FONT}" font-size="9.6" fill="#1E293B">• BẤT BIẾN (không thể thay đổi, độc lập ý muốn)</text>
  <text x="32" y="135" font-family="{FONT}" font-size="9.2" font-style="italic" fill="#475569">VD: Sự kiện Bác Hồ đọc Tuyên ngôn 2/9/1945</text>

  <!-- Bridge: Su lieu -->
  <rect x="294" y="66" width="132" height="58" rx="29" fill="#FEF3C7" stroke="#D97706" stroke-width="1.6"/>
  <text x="360" y="90" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#92400E">SỬ LIỆU</text>
  <text x="360" y="106" text-anchor="middle" font-family="{FONT}" font-size="8.8" fill="#78350F">Cầu nối trung gian</text>
  <line x1="268" y1="95" x2="294" y2="95" stroke="#D97706" stroke-width="2"/>
  <line x1="426" y1="95" x2="452" y2="95" stroke="#D97706" stroke-width="2"/>
  <polygon points="454,95 445,90 445,100" fill="#D97706"/>

  <!-- Box Right: Nhan thuc lich su -->
  <rect x="456" y="42" width="384" height="106" rx="9" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.6"/>
  <rect x="456" y="42" width="384" height="26" rx="9" fill="#991B1B"/>
  <text x="648" y="59" text-anchor="middle" font-family="{FONT}" font-size="11" font-weight="700" fill="#FFFFFF">NHẬN THỨC LỊCH SỬ (Khẩu quyết: N–K/C–Đ)</text>
  <text x="468" y="84" font-family="{FONT}" font-size="9.6" fill="#1E293B">• Những HIỂU BIẾT của con người về hiện thực lịch sử</text>
  <text x="468" y="101" font-family="{FONT}" font-size="9.6" font-weight="600" fill="#991B1B">• Đa dạng, NHIỀU CÁCH tái hiện • Vừa KHÁCH QUAN vừa CHỦ QUAN</text>
  <text x="468" y="118" font-family="{FONT}" font-size="9.6" fill="#1E293B">• Có khoảng cách với hiện thực; ĐỔI MỚI khi có sử liệu mới</text>
  <text x="468" y="135" font-family="{FONT}" font-size="9.2" fill="#475569">Chi phối bởi: (1) Nhu cầu/năng lực • (2) Phương pháp • (3) Sử liệu • (4) Thái độ</text>

  <!-- Bottom Row: Su hoc -->
  <rect x="20" y="162" width="820" height="74" rx="9" fill="#FFFFFF" stroke="#0F766E" stroke-width="1.5"/>
  <rect x="20" y="162" width="190" height="74" rx="9" fill="#0F766E"/>
  <text x="115" y="187" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="700" fill="#FFFFFF">SỬ HỌC LÀ GÌ?</text>
  <text x="115" y="205" text-anchor="middle" font-family="{FONT}" font-size="9.2" fill="#CCFBF1">Khoa học nghiên cứu</text>
  <text x="115" y="220" text-anchor="middle" font-family="{FONT}" font-size="9.2" font-weight="700" fill="#FFFFFF">quá khứ của LOÀI NGƯỜI</text>

  <text x="222" y="182" font-family="{FONT}" font-size="9.0" font-weight="700" fill="#0F766E">Đối tượng:</text>
  <text x="282" y="182" font-family="{FONT}" font-size="8.8" fill="#1E293B">Toàn bộ quá khứ loài người (cá nhân, nhóm, cộng đồng, quốc gia, khu vực, nhân loại) — toàn diện, đa dạng.</text>

  <text x="222" y="203" font-family="{FONT}" font-size="9.0" font-weight="700" fill="#1E40AF">2 Chức năng:</text>
  <text x="294" y="203" font-family="{FONT}" font-size="8.8" fill="#1E293B">(1) Khoa học (khôi phục sự kiện + tìm quy luật) • (2) Xã hội (giáo dục đạo đức + rút bài học hiện tại).</text>

  <text x="222" y="223" font-family="{FONT}" font-size="9.0" font-weight="700" fill="#991B1B">3 Nhiệm vụ:</text>
  <text x="290" y="223" font-family="{FONT}" font-size="8.8" fill="#1E293B">(1) Nhận thức (tri thức khoa học) • (2) Giáo dục (truyền thống, nhân cách) • (3) Dự báo (xu thế tương lai).</text>
</svg>"""
    write_svg("bai1_hienthuc_nhanthuc.svg", svg)


def gen_bai2_diagram() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 235" width="860" height="235">
  <rect x="2" y="2" width="856" height="231" rx="12" fill="#FAF8F5" stroke="#D6CFC7" stroke-width="1.4"/>
  <text x="430" y="26" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" fill="#0F766E">SƠ ĐỒ TƯ DUY BÀI 2: QUY TRÌNH 4 BƯỚC SỬ LIỆU &amp; HỌC TẬP LỊCH SỬ SUỐT ĐỜI (2,75 ĐIỂM)</text>

  <!-- 4 Steps Pipeline -->
  <!-- Step 1 -->
  <rect x="18" y="42" width="192" height="92" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.4"/>
  <rect x="18" y="42" width="192" height="24" rx="8" fill="#1D4ED8"/>
  <text x="114" y="58" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="700" fill="#FFFFFF">BƯỚC 1: LẬP DANH MỤC (L)</text>
  <text x="28" y="81" font-family="{FONT}" font-size="9.2" fill="#1E293B">• Xác định vấn đề tìm hiểu</text>
  <text x="28" y="98" font-family="{FONT}" font-size="9.2" fill="#1E293B">• Lập thư mục &amp; danh sách</text>
  <text x="28" y="115" font-family="{FONT}" font-size="9.2" font-weight="600" fill="#1D4ED8">  nguồn sử liệu cần sưu tầm</text>

  <polygon points="222,88 213,83 213,93" fill="#64748B"/>

  <!-- Step 2 -->
  <rect x="226" y="42" width="194" height="92" rx="8" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.4"/>
  <rect x="226" y="42" width="194" height="24" rx="8" fill="#0F766E"/>
  <text x="323" y="58" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="700" fill="#FFFFFF">BƯỚC 2: SƯU TẦM &amp; ĐỌC (S)</text>
  <text x="236" y="81" font-family="{FONT}" font-size="9.2" fill="#1E293B">• Tìm kiếm, khảo sát, phỏng vấn</text>
  <text x="236" y="98" font-family="{FONT}" font-size="9.2" fill="#1E293B">• Đọc và ghi chép thông tin</text>
  <text x="236" y="115" font-family="{FONT}" font-size="9.2" font-weight="600" fill="#0F766E">→ Khâu: THU THẬP SỬ LIỆU</text>

  <polygon points="432,88 423,83 423,93" fill="#64748B"/>

  <!-- Step 3 -->
  <rect x="436" y="42" width="194" height="92" rx="8" fill="#FFFBEB" stroke="#D97706" stroke-width="1.4"/>
  <rect x="436" y="42" width="194" height="24" rx="8" fill="#B45309"/>
  <text x="533" y="58" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="700" fill="#FFFFFF">BƯỚC 3: CHỌN LỌC (C)</text>
  <text x="446" y="81" font-family="{FONT}" font-size="9.2" fill="#1E293B">• Chọn lọc tư liệu sát chủ đề</text>
  <text x="446" y="98" font-family="{FONT}" font-size="9.2" fill="#1E293B">• Phân loại theo nhóm/dạng</text>
  <text x="446" y="115" font-family="{FONT}" font-size="9.2" font-weight="600" fill="#B45309">→ Mở đầu XỬ LÍ SỬ LIỆU</text>

  <polygon points="642,88 633,83 633,93" fill="#64748B"/>

  <!-- Step 4 -->
  <rect x="646" y="42" width="196" height="92" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.4"/>
  <rect x="646" y="42" width="196" height="24" rx="8" fill="#991B1B"/>
  <text x="744" y="58" text-anchor="middle" font-family="{FONT}" font-size="10" font-weight="700" fill="#FFFFFF">BƯỚC 4: XÁC MINH (X)</text>
  <text x="656" y="81" font-family="{FONT}" font-size="9.2" fill="#1E293B">• Thẩm định nguồn gốc, niên đại</text>
  <text x="656" y="98" font-family="{FONT}" font-size="9.2" fill="#1E293B">• So sánh, đánh giá độ tin cậy</text>
  <text x="656" y="115" font-family="{FONT}" font-size="9.2" font-weight="600" fill="#991B1B">→ Cốt lõi XỬ LÍ SỬ LIỆU</text>

  <!-- Bottom 2 Panels -->
  <rect x="18" y="146" width="402" height="75" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="30" y="165" font-family="{FONT}" font-size="10.2" font-weight="700" fill="#1E3A5F">4 Loại hình Sử liệu (Khẩu quyết: K – V – A – T):</text>
  <text x="30" y="184" font-family="{FONT}" font-size="9.3" fill="#334155">1. Truyền Khẩu (truyền thuyết, lời kể) • 2. Hiện Vật (trống đồng, lá đề)</text>
  <text x="30" y="201" font-family="{FONT}" font-size="9.3" fill="#334155">3. Hình Ảnh (ảnh chụp, băng hình) • 4. Thành Văn (bia đá, Tuyên ngôn)</text>
  <text x="30" y="215" font-family="{FONT}" font-size="8.8" font-style="italic" fill="#0F766E">Phân cấp: Sử liệu sơ cấp (bản gốc đương thời) &gt; Sử liệu thứ cấp (biên soạn sau)</text>

  <rect x="436" y="146" width="406" height="75" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="448" y="165" font-family="{FONT}" font-size="10.2" font-weight="700" fill="#7C1D26">4 Lí do Học tập &amp; Khám phá Lịch sử Suốt đời (V – B – H – N):</text>
  <text x="448" y="184" font-family="{FONT}" font-size="9.3" fill="#334155">• (V) Vận dụng kinh nghiệm quá khứ vào hiện tại &amp; định hướng tương lai</text>
  <text x="448" y="200" font-family="{FONT}" font-size="9.3" fill="#334155">• (B) Bí ẩn/khoảng trống &amp; sử liệu mới • (H) Hội nhập, giữ bản sắc văn hóa</text>
  <text x="448" y="215" font-family="{FONT}" font-size="9.3" fill="#334155">• (N) Nghề nghiệp mới &amp; nguồn cảm hứng cho công nghiệp văn hóa, du lịch</text>
</svg>"""
    write_svg("bai2_quytrinh_sulieu.svg", svg)


def gen_bai3_diagram() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 255" width="860" height="255">
  <rect x="2" y="2" width="856" height="251" rx="12" fill="#FAF8F5" stroke="#D6CFC7" stroke-width="1.4"/>
  <text x="430" y="26" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="700" fill="#7C1D26">SƠ ĐỒ TƯ DUY BÀI 3: SỬ HỌC — BẢO TỒN DI SẢN — PHÁT TRIỂN DU LỊCH (TRỌNG TÂM 5,75 ĐIỂM!)</text>

  <!-- Pillar 1: Su hoc -->
  <rect x="18" y="44" width="232" height="136" rx="9" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
  <rect x="18" y="44" width="232" height="26" rx="9" fill="#1E3A5F"/>
  <text x="134" y="61" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#FFFFFF">1. NGHIÊN CỨU SỬ HỌC</text>
  <text x="28" y="86" font-family="{FONT}" font-size="9.3" font-weight="600" fill="#1E3A5F">Khoa học có tính LIÊN NGÀNH:</text>
  <text x="28" y="103" font-family="{FONT}" font-size="9.1" fill="#334155">• Xác định giá trị lịch sử, văn hóa,</text>
  <text x="28" y="118" font-family="{FONT}" font-size="9.1" fill="#334155">  kiến trúc, mĩ thuật, khoa học</text>
  <text x="28" y="135" font-family="{FONT}" font-size="9.1" font-weight="700" fill="#991B1B">• Là CƠ SỞ KHOA HỌC vững chắc</text>
  <text x="28" y="151" font-family="{FONT}" font-size="9.1" fill="#334155">• Giữ 3 nguyên tắc vàng (3G):</text>
  <text x="28" y="167" font-family="{FONT}" font-size="9.1" font-weight="700" fill="#1D4ED8">  Yếu tố Gốc • Xác thực • Toàn vẹn</text>

  <!-- Arrow 1->2 -->
  <line x1="250" y1="112" x2="286" y2="112" stroke="#1E3A5F" stroke-width="2.2"/>
  <polygon points="290,112 280,106 280,118" fill="#1E3A5F"/>

  <!-- Pillar 2: Di san -->
  <rect x="292" y="44" width="268" height="136" rx="9" fill="#FFFBEB" stroke="#D97706" stroke-width="1.6"/>
  <rect x="292" y="44" width="268" height="26" rx="9" fill="#B45309"/>
  <text x="426" y="61" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#FFFFFF">2. DI SẢN VĂN HÓA &amp; THIÊN NHIÊN</text>
  <text x="302" y="86" font-family="{FONT}" font-size="8.8" fill="#1E293B">• <tspan font-weight="700" fill="#92400E">DSVH Vật thể:</tspan> chống xuống cấp, kéo dài tuổi thọ</text>
  <text x="302" y="104" font-family="{FONT}" font-size="8.8" fill="#1E293B">• <tspan font-weight="700" fill="#92400E">DSVH Phi vật thể:</tspan> truyền nghề, lưu truyền thế hệ</text>
  <text x="302" y="122" font-family="{FONT}" font-size="8.8" fill="#1E293B">• <tspan font-weight="700" fill="#0F766E">DS Thiên nhiên:</tspan> bảo vệ đa dạng sinh học, khoa học</text>
  <text x="302" y="140" font-family="{FONT}" font-size="8.8" fill="#1E293B">• <tspan font-weight="700" fill="#7C1D26">DS Hỗn hợp:</tspan> hội tụ văn hóa &amp; thiên nhiên (Tràng An)</text>
  <text x="302" y="160" font-family="{FONT}" font-size="8.5" font-weight="700" fill="#0F766E">→ Động lực phát triển KT–XH địa phương bền vững</text>

  <!-- Two-way arrows 2 <-> 3 -->
  <line x1="560" y1="95" x2="602" y2="95" stroke="#0F766E" stroke-width="2.2"/>
  <polygon points="606,95 596,89 596,101" fill="#0F766E"/>
  <text x="583" y="87" text-anchor="middle" font-family="{FONT}" font-size="8.2" font-weight="700" fill="#0F766E">Tài nguyên</text>

  <line x1="606" y1="132" x2="564" y2="132" stroke="#991B1B" stroke-width="2.2"/>
  <polygon points="560,132 570,126 570,138" fill="#991B1B"/>
  <text x="583" y="146" text-anchor="middle" font-family="{FONT}" font-size="8.2" font-weight="700" fill="#991B1B">Tái đầu tư</text>

  <!-- Pillar 3: Du lich -->
  <rect x="608" y="44" width="234" height="136" rx="9" fill="#F0FDFA" stroke="#0F766E" stroke-width="1.5"/>
  <rect x="608" y="44" width="234" height="26" rx="9" fill="#0F766E"/>
  <text x="725" y="61" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="#FFFFFF">3. PHÁT TRIỂN DU LỊCH</text>
  <text x="618" y="86" font-family="{FONT}" font-size="9.2" font-weight="700" fill="#0F766E">Tác động ngược lại bảo tồn:</text>
  <text x="618" y="103" font-family="{FONT}" font-size="9.1" fill="#334155">• Thúc đẩy bảo vệ di tích quốc gia</text>
  <text x="618" y="119" font-family="{FONT}" font-size="9.1" fill="#334155">• Thôi thúc chính quyền &amp; dân giữ gìn</text>
  <text x="618" y="135" font-family="{FONT}" font-size="9.1" font-weight="600" fill="#991B1B">• Trích doanh thu tái đầu tư tôn tạo</text>
  <text x="618" y="151" font-family="{FONT}" font-size="9.1" fill="#334155">• Phục dựng, truyền dạy phi vật thể</text>
  <text x="618" y="167" font-family="{FONT}" font-size="9.1" fill="#334155">• Quảng bá văn hóa VN ra thế giới</text>

  <!-- Bottom Banner: Essay 4T Formula -->
  <rect x="18" y="192" width="824" height="50" rx="8" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.3"/>
  <text x="32" y="212" font-family="{FONT}" font-size="10" font-weight="700" fill="#991B1B">CÔNG THỨC 4T GIẢI QUYẾT CÂU TỰ LUẬN VẬN DỤNG (2,0 ĐIỂM) — BIỆN PHÁP BẢO TỒN &amp; PHÁT HUY DI SẢN:</text>
  <text x="32" y="230" font-family="{FONT}" font-size="9.3" fill="#1E293B">(1) <tspan font-weight="700" fill="#991B1B">Tuyên truyền</tspan> nâng cao ý thức cộng đồng  •  (2) <tspan font-weight="700" fill="#991B1B">Tôn tạo</tspan> khoa học (giữ yếu tố gốc)  •  (3) <tspan font-weight="700" fill="#991B1B">Thích ứng</tspan> du lịch bền vững &amp; số hóa  •  (4) <tspan font-weight="700" fill="#991B1B">Thanh tra</tspan> bảo vệ &amp; hành động học sinh</text>
</svg>"""
    write_svg("bai3_disan_dulich_2chieu.svg", svg)


def gen_unesco_9_disan() -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 245" width="860" height="245">
  <rect x="2" y="2" width="856" height="241" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.4"/>
  <rect x="2" y="2" width="856" height="32" rx="12" fill="#1E3A5F"/>
  <text x="430" y="23" text-anchor="middle" font-family="{FONT}" font-size="12.2" font-weight="700" fill="#FFFFFF">BẢN ĐỒ TƯ DUY 09 DI SẢN THẾ GIỚI UNESCO TẠI VIỆT NAM (CẬP NHẬT MỚI NHẤT 2025–2026)</text>

  <!-- Col 1: 6 Cultural -->
  <rect x="16" y="44" width="410" height="186" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.2"/>
  <text x="28" y="64" font-family="{FONT}" font-size="10.8" font-weight="700" fill="#991B1B">A. DI SẢN VĂN HÓA THẾ GIỚI (06 DI SẢN)</text>
  <text x="28" y="84" font-family="{FONT}" font-size="9.4" fill="#1E293B">1. <tspan font-weight="700">Quần thể di tích Cố đô Huế</tspan> (1993 — Huế, di sản TG đầu tiên của VN)</text>
  <text x="28" y="103" font-family="{FONT}" font-size="9.4" fill="#1E293B">2. <tspan font-weight="700">Đô thị cổ Hội An</tspan> (1999 — thương cảng cổ thế kỉ XVI–XVIII)</text>
  <text x="28" y="122" font-family="{FONT}" font-size="9.4" fill="#1E293B">3. <tspan font-weight="700">Khu đền tháp Mỹ Sơn</tspan> (1999 — trung tâm tôn giáo Chăm-pa cổ)</text>
  <text x="28" y="141" font-family="{FONT}" font-size="9.4" fill="#1E293B">4. <tspan font-weight="700">Khu Trung tâm Hoàng thành Thăng Long</tspan> (2010 — Hà Nội, 13 thế kỉ)</text>
  <text x="28" y="160" font-family="{FONT}" font-size="9.4" fill="#1E293B">5. <tspan font-weight="700">Thành nhà Hồ</tspan> (2011 — Thanh Hóa, kiến trúc đá vôi độc đáo 1397)</text>
  <text x="28" y="179" font-family="{FONT}" font-size="9.4" fill="#991B1B">6. <tspan font-weight="700">Yên Tử – Vĩnh Nghiêm – Côn Sơn, Kiếp Bạc</tspan> (7/2025 — Mới nhất!)</text>
  <text x="40" y="196" font-family="{FONT}" font-size="8.8" font-style="italic" fill="#7F1D1D">→ Di sản chuỗi liên tỉnh gắn với Phật giáo Trúc Lâm thời Trần (TK XIII–XIV)</text>
  <text x="28" y="218" font-family="{FONT}" font-size="8.9" font-weight="600" fill="#475569">+ DSVH Phi vật thể tiêu biểu: Nhã nhạc Huế, Cồng chiêng TN, Quan họ, Ví Giặm...</text>

  <!-- Col 2 Top: 2 Natural -->
  <rect x="440" y="44" width="404" height="88" rx="8" fill="#F0FDFA" stroke="#99F6E4" stroke-width="1.2"/>
  <text x="452" y="64" font-family="{FONT}" font-size="10.8" font-weight="700" fill="#0F766E">B. DI SẢN THIÊN NHIÊN THẾ GIỚI (02 DI SẢN)</text>
  <text x="452" y="85" font-family="{FONT}" font-size="9.4" fill="#1E293B">7. <tspan font-weight="700">Vịnh Hạ Long – Quần đảo Cát Bà</tspan> (1994, 2000; mở rộng 2023)</text>
  <text x="452" y="105" font-family="{FONT}" font-size="9.4" fill="#1E293B">8. <tspan font-weight="700">Vườn quốc gia Phong Nha – Kẻ Bàng</tspan> (2003, 2015; liên biên giới 2025)</text>
  <text x="452" y="122" font-family="{FONT}" font-size="8.8" font-style="italic" fill="#0F766E">→ Giá trị địa chất – địa mạo karst, hang động &amp; đa dạng sinh học đặc hữu</text>

  <!-- Col 2 Bottom: 1 Mixed -->
  <rect x="440" y="142" width="404" height="88" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.4"/>
  <text x="452" y="162" font-family="{FONT}" font-size="10.8" font-weight="700" fill="#B45309">C. DI SẢN HỖN HỢP THẾ GIỚI (01 DI SẢN DUY NHẤT!)</text>
  <text x="452" y="182" font-family="{FONT}" font-size="9.5" fill="#1E293B">9. <tspan font-weight="700" fill="#92400E">Quần thể danh thắng Tràng An</tspan> (Ninh Bình — công nhận năm 2014)</text>
  <text x="452" y="200" font-family="{FONT}" font-size="9.1" fill="#334155">• Kết hợp Cố đô Hoa Lư + Hang động Tràng An – Tam Cốc – Bích Động + Rừng đặc dụng</text>
  <text x="452" y="217" font-family="{FONT}" font-size="8.9" font-weight="700" fill="#991B1B">★ Bẫy trắc nghiệm số 1: Tràng An là DI SẢN HỖN HỢP duy nhất ở VN &amp; ĐNA!</text>
</svg>"""
    write_svg("unesco_vietnam_9_disan.svg", svg)


if __name__ == "__main__":
    gen_matrix_weight_chart()
    gen_timeline_strategy()
    gen_bai1_diagram()
    gen_bai2_diagram()
    gen_bai3_diagram()
    gen_unesco_9_disan()
    print("All 6 vector SVG diagrams generated successfully.")
