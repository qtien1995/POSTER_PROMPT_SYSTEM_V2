# GOOGLE FLOW / IMAGEN 3 BATCH PRODUCTION SYSTEM
## MASTER PROMPT VẠN NĂNG & DATASET TỰ ĐỘNG HÓA TẠO 31 ẢNH HÀNG LOẠT

- **Hệ thống:** POSTER STUDIO & MASTER PROMPT SYSTEM V2.5
- **Công cụ đích:** Google Flow (Vertex AI Prompt Flow / Imagen 3 Batch Prediction / ComfyUI Flow)
- **Cố vấn tài chính chính thức:** Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268
- **Chữ ký cố vấn:** "Tiến"
- **Tỷ lệ khung hình:** 3:4

---

## I. 1 MASTER PROMPT TEMPLATE VẠN NĂNG (DÙNG CHO GOOGLE FLOW VARIABLE INJECTION)

Nếu sử dụng tính năng **Prompt Variables (Tham số hóa tự động)** trong Google Flow / Vertex AI, bạn chỉ cần nhập duy nhất mẫu Prompt sau vào khối Prompt Node:

```text
A commercial luxury financial poster in {{STYLE_DNA}} aesthetic, 3:4 aspect ratio.
Foreground & Hero Subject: {{HERO_VISUAL}}
Environment & Atmosphere: {{ENVIRONMENT}}
Lighting Physics & Color Science: {{LIGHTING_AND_PALETTE}}
Material Shaders & Textures: {{MATERIALITY}}
Composition & Hierarchy: Swiss graphic design layout, 40% intentional negative space reserved for typography at top and bottom. Edge-to-edge tack-sharp 85mm prime lens perspective.
On-Image Exact Vietnamese Typography (Render exactly and only these strings):
- Primary Headline at upper negative space: "{{HEADLINE}}"
- Secondary Subheadline: "{{SUBTITLE}}"
{{OPTIONAL_LABELS}}
- Advisor Signature System at lower negative space: Delicate handwritten cursive signature "Tiến" in deep emerald ink, positioned directly above the single-line contact block: "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268"
Negative Constraints: No floating coins, no neon glowing shields, no plastic gloss, no 3D cartoon characters, no unauthorized watermarks, no extra gibberish text. High-end commercial graphic design finish.
```

---

## II. DANH SÁCH 31 MASTER PROMPTS ĐỘC LẬP (COPY HÀNG LOẠT VÀO GOOGLE FLOW RUNNER)

Nếu bạn chạy trực tiếp từng prompt trong danh sách hàng loạt (Batch Execution List), đây là toàn bộ 31 prompt chuẩn công nghiệp đã được điền sẵn đầy đủ 100% dữ liệu:

### [1/31] Style 01: MANULIFE_CLEAN
```text
A commercial luxury financial poster in Manulife Clean Corporate minimalism aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A sleek minimalist cylindrical podium in matte off-white ceramic elevating a faceted emerald green geometric emblem. Environment & Atmosphere: Clean architectural studio with warm ivory textured walls (#F8F6F0) and soft subtle light-gray backdrop. Lighting Physics & Color Science: Soft diffused studio lighting with gentle ground contact shadow; Deep Pine Green (#0B3B24), Emerald (#1B6B48), Warm Ivory (#F8F6F0). Material Shaders: Matte ceramic, brushed emerald lacquer. Composition: Symmetrical balanced layout with 40% negative space. On-Image Exact Vietnamese Typography: Primary Headline: "NỀN TẢNG VỮNG CHẮC"; Secondary Subheadline: "Bảo vệ tài chính & Tích lũy có kỷ luật"; Signature block: Handwritten cursive signature "Tiến" in emerald ink and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268". Negative Constraints: No floating coins, no neon glowing shields, no plastic gloss. Edge-to-edge tack-sharp 85mm prime lens perspective.
```

### [2/31] Style 02: INFORMATION_INFOGRAPHIC
```text
A commercial luxury financial poster in Swiss Architectural Infographics aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A precision-crafted 3D isometric hexagonal column divided into three distinct strata: top emerald green layer labeled '1. Y TẾ TOÀN DIỆN', middle deep pine green layer labeled '2. BẢO VỆ THU NHẬP', and foundational brushed champagne gold layer labeled '3. TÍCH LŨY TƯƠNG LAI'. Environment & Atmosphere: Pure warm ivory archival paper surface (#FBF9F4) with delicate tactile texture. Lighting & Color: Soft directional studio light; Emerald Green (#1B6B48), Deep Pine (#0B3B24), Champagne Gold (#E5C378). On-Image Exact Vietnamese Typography: Headline: "CẤU TRÚC BẢO VỆ TOÀN DIỆN"; Subheadline: "3 Lớp tài sản vững chãi cho gia đình"; Badges: "1. Y TẾ TOÀN DIỆN", "2. BẢO VỆ THU NHẬP", "3. TÍCH LŨY TƯƠNG LAI"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [3/31] Style 03: VISUAL_METAPHOR
```text
A commercial luxury financial poster in Visual Metaphor Quiet Luxury aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A monumental honed white Carrara marble column, elegantly spiraled with a sculpted matte emerald green ribbon, firmly supporting an illuminated architectural glass greenhouse roof casting warm light downwards. Environment & Atmosphere: Architectural studio with subtle split tone backdrop in deep pine green and soft ivory. Lighting & Color: Honed marble white, deep pine green (#0B3B24), glowing warm incandescent light (2700K). Directional 45-degree cinematic key light. On-Image Exact Vietnamese Typography: Headline: "TRỤ CỘT KHI NÀO CẦN ĐIỂM TỰA?"; Subheadline: "Bảo toàn nguồn thu nhập cho gia đình"; Signature: Handwritten signature "Tiến" in emerald ink and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [4/31] Style 04: HUMAN_STORY
```text
A commercial luxury financial poster in Authentic Human Story Editorial aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A caring Vietnamese father kneeling gently to guide his smiling toddler daughter as she takes joyful first steps in a sun-drenched modern living room. Environment & Atmosphere: Warm contemporary home with light oak wooden floors, green potted monstera plants, soft linen curtains. Lighting & Optics: Natural morning window daylight, authentic organic film grain, authentic skin textures without plastic retouching. 50mm f/2.0 portrait prime. On-Image Exact Vietnamese Typography: Headline: "VÌ NHỮNG BƯỚC ĐI ĐẦU TIÊN CỦA CON"; Subheadline: "Kế hoạch học vấn và bảo vệ trọn vẹn"; Signature: Handwritten signature "Tiến" in pine green ink and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [5/31] Style 05: EDITORIAL_MAGAZINE
```text
A commercial luxury financial poster in Bloomberg Businessweek and The New Yorker editorial aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A masterfully carved geometric emerald crystal vase resting on a seamless warm ivory floor, refracting sunlight into gentle green and amber caustics. Environment: Minimalist gallery space with 50% breathing room. Palette: Rich Ivory (#F5F3E9), Emerald Glass (#00A758), Jet Black (#111111). On-Image Exact Vietnamese Typography: Headline: "TỰ DO TÀI CHÍNH BẮT ĐẦU TỪ KỶ LUẬT"; Subheadline: "Chiến lược quản trị rủi ro & gia sản"; Bottom right credit: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [6/31] Style 06: PREMIUM_WEALTH
```text
A commercial luxury financial poster in Private Wealth Management Quiet Luxury aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A deep forest green handcrafted leather portfolio binder embossed with an ornate gold family tree crest and an emerald stone inlay, paired with a champagne gold fountain pen on polished black Marquina marble. Environment: Warm walnut wood-paneled executive study with blurred background. Lighting: Directional cinematic lighting, shallow depth of field. On-Image Exact Vietnamese Typography: Headline: "GIA SẢN TRƯỜNG TỒN"; Subheadline: "Hoạch định di sản và hưu trí an nhàn"; Signature: Handwritten signature "Tiến" in gold ink and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [7/31] Style 07: DATA_VISUALIZATION
```text
A commercial luxury financial poster in Swiss Financial Data Visualization aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: Massive elegant serif typography '100% THU NHẬP' rendered in deep pine green dominating the upper center, directly integrated above a minimalist ascending bar chart demonstrating steady income continuity. Environment: Clean warm ivory background (#F7F5EE) with delicate architectural baseline grid. On-Image Exact Vietnamese Typography: Headline: "BẢO TOÀN 100% THU NHẬP"; Subheadline: "Dữ liệu chi trả và tốc độ bù đắp dòng tiền"; Metric: "100% THU NHẬP"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [8/31] Style 08: SOCIAL_MEDIA_HOOK
```text
A commercial luxury financial poster in High-Conversion Social Media Hook aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A minimalist frosted glass hourglass suspended mid-frame: fine golden sand flows from the top bulb, but upon settling in the bottom chamber, it crystallizes into dense, lustrous emerald geometric shield plates. Environment: Gradient studio backdrop from deep pine green to warm ivory. On-Image Exact Vietnamese Typography: Headline: "TIỀN MẤT CÓ THỂ KIẾM LẠI. THỜI GIAN THÌ KHÔNG."; Subheadline: "Bắt đầu tích lũy sớm trước khi quá muộn"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [9/31] Style 09: SCENARIO_COMPARISON
```text
A commercial luxury financial poster in Split Screen Scenario Comparison aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: Symmetrical vertical split layout: Left side in muted stormy slate tones shows a torn umbrella struggling in rain labeled 'CHƯA CÓ DỰ PHÒNG'; Right side in warm golden sunlight shows a solid emerald architectural canopy sheltering a serene family silhouette labeled 'CÓ KẾ HOẠCH BẢO VỆ'. On-Image Exact Vietnamese Typography: Headline: "CHỌN AN TÂM HAY CHỌN RỦI RO?"; Subheadline: "Hai tương lai tài chính trước biến cố"; Badges: "CHƯA CÓ DỰ PHÒNG", "CÓ KẾ HOẠCH BẢO VỆ"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [10/31] Style 10: EDUCATIONAL_ILLUSTRATION
```text
A commercial luxury financial poster in Scandinavian Educational Vector Illustration aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: In refined 2D vector line-art on warm art paper, a father and mother lovingly water a vibrant emerald green sapling whose upper branches curve gracefully into an architectural portal holding a university diploma. Environment: Warm ivory matte paper background (#FBF9F4) with soft sage green botanical accents. On-Image Exact Vietnamese Typography: Headline: "GIEO HẠT HÔM NAY, VỮNG BƯỚC NGÀY MAI"; Subheadline: "Giải pháp tích lũy giáo dục an tâm cho cha mẹ"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [11/31] Style 11: ANATOMICAL_BODY_MAP
```text
A commercial luxury financial poster in Medical Infographics Anatomical aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A minimalist profile silhouette of human anatomy rendered in translucent frosted optic glass, with delicate luminous callout pins and thin hairline vectors connecting to the brain, heart, lungs, and liver zones, indicating multi-stage early-to-late coverage. Environment: Clean dark pine green and deep slate backdrop with subtle medical coordinate gridlines. On-Image Exact Vietnamese Typography: Headline: "LÁ CHẮN SỨC KHỎE ĐA TẦNG"; Subheadline: "Bảo vệ chuyên sâu 134 bệnh lý nghiêm trọng qua các giai đoạn"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [12/31] Style 12: MANULIFE_PREMIUM_METAPHOR
```text
A commercial luxury financial poster in Flagship Manulife Premium Metaphor Quiet Luxury aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: In the center of an expansive minimalist architectural rotunda, a monumental fluted Carrara marble pedestal supports a flawless, internally lit emerald gemstone. A majestic curved canopy of smoked frosted glass arches overhead, sheltering the gem. Lighting: 45-degree volumetric sunlight, soft shadows across brushed terrazzo floors. On-Image Exact Vietnamese Typography: Headline: "BẢO CHỨNG BÌNH AN CHO GIA ĐÌNH"; Subheadline: "Giải pháp bảo vệ tài chính chuẩn mực Manulife"; Signature: Handwritten signature "Tiến" in emerald ink and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [13/31] Style 13: CLINICAL_INFORMATION_DESIGN
```text
A commercial luxury financial poster in Swiss Healthcare Clinical Information Design aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A premium brushed titanium medical card with emerald lacquer trim resting gently on an ultra-clean frosted glass surface, accompanied by subtle embossed medical cross symbols and minimalist hospital network badges. Palette: Clinical Crisp White (#FFFFFF), Medical Emerald (#00A758), Frosted Glass Ice Blue. On-Image Exact Vietnamese Typography: Headline: "CHĂM SÓC Y TẾ TOÀN CẦU"; Subheadline: "Bảo lãnh viện phí trực tiếp tại các bệnh viện hàng đầu"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [14/31] Style 14: FINANCIAL_ARCHITECTURE
```text
A commercial luxury financial poster in Architectural Model Photography aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A monolithic triangular building cross-section made of reinforced architectural concrete, Carrara marble, and polished brass: the massive bedrock basement is labeled 'MÓNG BẢO VỆ', the middle residential core is labeled 'THÂN TÍCH LŨY', and the glowing glass penthouse needle is labeled 'ĐỈNH ĐẦU TƯ'. On-Image Exact Vietnamese Typography: Headline: "KIẾN TRÚC TÀI CHÍNH BỀN VỮNG"; Subheadline: "Xây móng bảo vệ trước khi xây đỉnh tăng trưởng"; Badges: "MÓNG BẢO VỆ", "THÂN TÍCH LŨY", "ĐỈNH ĐẦU TƯ"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [15/31] Style 15: DOCUMENTARY_EDITORIAL
```text
A commercial luxury financial poster in Authentic Photojournalism Documentary aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: In a modest, cozy Vietnamese home, an empathetic financial advisor respectfully hands over an official Manulife claim settlement envelope to an emotional mother; hands gently touch, expressing deep trust and heartfelt gratitude. Lighting & Optics: Warm authentic living family room, natural window daylight, subtle 35mm film grain, muted warm tones. On-Image Exact Vietnamese Typography: Headline: "LỜI HỨA ĐƯỢC GIỮ VẸN NGUYÊN"; Subheadline: "Đồng hành cùng khách hàng qua những thời khắc khó khăn nhất"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [16/31] Style 16: CONCEPTUAL_EDITORIAL
```text
A commercial luxury financial poster in Conceptual Editorial Fine Art aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: A simple, slender silhouette of a father walking peacefully in a sunlit minimalist room. His cast shadow onto the clean ivory wall transforms into an immense, gentle giant carrying the entire family house safely upon his shoulders. Environment: Minimalist gallery space with pure warm ivory tones and extensive negative space. On-Image Exact Vietnamese Typography: Headline: "GIÁ TRỊ CỦA BẠN LÀ BAO NHIÊU?"; Subheadline: "Bạn chính là cỗ máy in tiền quan trọng nhất của gia đình"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [17/31] Style 17: EDITORIAL_COMIC_TIMELINE
```text
A commercial luxury financial poster in The New Yorker / FT Weekend 2D Comic Strip aesthetic, 3:4 aspect ratio. Foreground & Hero Subject: Clean 2D vector line-art character progressing from left to right along a timeline path on warm ivory paper (#FBF9F4): 1) 'ĐỘC THÂN' (carefree with backpack), 2) 'KẾT HÔN' (holding wedding flowers), 3) 'CÓ CON' (carrying baby), 4) 'MUA NHÀ' (carrying moving box), 5) 'TRẢ NỢ' (bent under a heavy backpack labeled NỢ). Each has a thought bubble making excuses. At the far right stands a dashed signpost: 'VẪN CHƯA DƯ'. On-Image Exact Vietnamese Typography: Headline: "ĐỢI DƯ RỒI MỚI MUA?"; Subheadline: "Đời sống rất giỏi tiêu hết phần \"dư\" đó trước khi bạn kịp nhận ra."; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

---

### [18/31] Pattern 01: BODY_MAP
```text
A commercial luxury financial poster using the Body Map visual pattern, 3:4 aspect ratio. Foreground & Hero Subject: A semi-transparent 3D frosted glass human silhouette standing in profile on a dark forest green backdrop. Clean luminous callout pins with hairline vectors connect to the brain, heart, lungs, and digestive system, each marked with crisp white badges. On-Image Exact Vietnamese Typography: Headline: "ĐỊNH VỊ RỦI RO, BẢO TOÀN SỨC KHỎE"; Subheadline: "Bảo vệ chi tiết từng hệ cơ quan trọng yếu trước biến cố"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [19/31] Pattern 02: PROTECTION_LAYERS
```text
A commercial luxury financial poster using the Protection Layers concentric pattern, 3:4 aspect ratio. Foreground & Hero Subject: Three concentric architectural rings sculpted from brushed emerald titanium, frosted crystal, and champagne gold metal, securely shielding a miniature glowing porcelain house at the very center. Soft warm caustic reflections. On-Image Exact Vietnamese Typography: Headline: "3 TẦNG KHIÊN BẢO VỆ GIA ĐÌNH"; Subheadline: "Y tế toàn diện • Thu nhập trụ cột • Tích lũy hưu trí"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [20/31] Pattern 03: FINANCIAL_FLOW
```text
A commercial luxury financial poster with the Financial Flow pattern, 3:4 aspect ratio. Foreground & Hero Subject: An elegant 3D sculptural river of liquid gold and emerald streams flowing smoothly across a honed marble terrain, splitting gracefully into three designated reservoirs labeled 'QUỸ BẢO VỆ', 'QUỸ TÍCH LŨY', and 'QUỸ DỰ PHÒNG'. On-Image Exact Vietnamese Typography: Headline: "DÒNG CHẢY TÀI CHÍNH THÔNG MINH"; Subheadline: "Điều phối dòng tiền từ thu nhập đến bảo vệ và gia tăng tài sản"; Badges: "QUỸ BẢO VỆ", "QUỸ TÍCH LŨY", "QUỸ DỰ PHÒNG"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [21/31] Pattern 04: TIMELINE_JOURNEY
```text
A commercial luxury financial poster using the Timeline / Journey visual pattern, 3:4 aspect ratio. Foreground & Hero Subject: A graceful curved geometric path in emerald green traversing upwards across textured warm ivory paper. Along the path stand 3 architectural milestone plinths marked with life ambitions: '18 TUỔI ĐẠI HỌC', '30 TUỔI AN CƯ', '55 TUỔI HƯU TRÍ'. On-Image Exact Vietnamese Typography: Headline: "LỘ TRÌNH 30 NĂM AN TÂM TÀI CHÍNH"; Subheadline: "Từng cột mốc cuộc đời đều có nguồn tài chính sẵn sàng"; Plinths: "18 TUỔI ĐẠI HỌC", "30 TUỔI AN CƯ", "55 TUỔI HƯU TRÍ"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [22/31] Pattern 05: COMIC_WALKTHROUGH
```text
A commercial luxury financial poster in narrative life-stages comic walkthrough pattern, 3:4 aspect ratio. Foreground & Hero Subject: Multi-panel 2D vector comic illustration depicting an everyday worker navigating career growth, wedding expenses, childcare, and mortgage payments, accompanied by humorous slice-of-life thought bubbles. On-Image Exact Vietnamese Typography: Headline: "HÀNH TRÌNH CUỘC ĐỜI & NHỮNG LỰA CHỌN"; Subheadline: "Mỗi giai đoạn sống cần một điểm tựa tài chính tương ứng"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [23/31] Pattern 06: BEFORE_AFTER
```text
A commercial luxury financial poster in high-contrast Before / After pattern, 3:4 aspect ratio. Foreground & Hero Subject: Symmetrical split screen layout: Left side shows an anxious figure at a cluttered desk piled with medical bills in dark stormy tones labeled 'TRƯỚC: BẤT AN & BỊ ĐỘNG'. Right side shows a relaxed, smiling family in a serene sunlit living room with an organized emerald green financial binder labeled 'SAU: VỮNG TÂM & CHỦ ĐỘNG'. On-Image Exact Vietnamese Typography: Headline: "TRƯỚC & SAU KHI CÓ ĐIỂM TỰA"; Subheadline: "Sự khác biệt giữa nỗi lo vô hình và sự chủ động trọn vẹn"; Badges: "TRƯỚC: BẤT AN & BỊ ĐỘNG", "SAU: VỮNG TÂM & CHỦ ĐỘNG"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [24/31] Pattern 07: HERO_NUMBERS
```text
A commercial luxury financial poster in bold Hero Numbers pattern, 3:4 aspect ratio. Foreground & Hero Subject: A massive sculptural 3D typography monument of '1.000.000.000 ĐỒNG' carved from brushed emerald green metal and polished champagne gold, standing prominently on a clean warm ivory podium. On-Image Exact Vietnamese Typography: Headline: "QUYỀN LỢI BẢO VỆ TỐI ĐA"; Subheadline: "Hạn mức bảo vệ sẵn sàng cho ngày giông bão"; Hero Number: "1.000.000.000 ĐỒNG"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [25/31] Pattern 08: EDITORIAL_QUESTION
```text
A commercial luxury financial poster in literary editorial question pattern, 3:4 aspect ratio. Foreground & Hero Subject: 50% generous breathing room on warm textured ivory art paper. In the lower third, a lone empty executive desk chair sits quietly under a dramatic focused circular spotlight. On-Image Exact Vietnamese Typography: Headline: "AI SẼ THAY BẠN ĐI LÀM VÀO NGÀY MAI?"; Subheadline: "Bảo hiểm không làm mất đi rủi ro, nhưng bù đắp toàn bộ thiệt hại tài chính."; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [26/31] Pattern 09: DASHBOARD
```text
A commercial luxury financial poster in modern Apple-style Bento Grid dashboard pattern, 3:4 aspect ratio. Foreground & Hero Subject: An Apple-inspired minimalist Bento grid of rounded cards in frosted emerald glass and matte ivory, displaying key metric widgets: 'QUỸ DỰ PHÒNG: 6 THÁNG THU NHẬP', 'HẠN MỨC Y TẾ: 2 TỶ/NĂM', 'QUỸ HỌC VẤN: 100% HOÀN TẤT'. On-Image Exact Vietnamese Typography: Headline: "BẢNG ĐIỀU KHIỂN TÀI CHÍNH GIA ĐÌNH"; Subheadline: "Quản trị rủi ro và tài sản theo chuẩn mực hiện đại"; Badges: "QUỸ DỰ PHÒNG: 6 THÁNG THU NHẬP", "HẠN MỨC Y TẾ: 2 TỶ/NĂM", "QUỸ HỌC VẤN: 100% HOÀN TẤT"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [27/31] Pattern 10: PYRAMID_LADDER
```text
A commercial luxury financial poster in financial pyramid ladder pattern, 3:4 aspect ratio. Foreground & Hero Subject: An architectural stepped pyramid made of polished Carrara marble and brass accents rising steadily to a sharp apex. The massive bedrock base is labeled 'BẢO VỆ & DỰ PHÒNG', the middle terrace is 'TÍCH LŨY MỤC TIÊU', and the pinnacle is 'ĐẦU TƯ TĂNG TRƯỞNG'. On-Image Exact Vietnamese Typography: Headline: "THÁP TÀI SẢN BỀN VỮNG"; Subheadline: "Không thể xây đỉnh đầu tư trên một nền móng bảo vệ rỗng"; Steps: "BẢO VỆ & DỰ PHÒNG", "TÍCH LŨY MỤC TIÊU", "ĐẦU TƯ TĂNG TRƯỞNG"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [28/31] Pattern 11: PROTECTION_FLOWER
```text
A commercial luxury financial poster in Protection Flower origami lotus pattern, 3:4 aspect ratio. Foreground & Hero Subject: A mesmerizing geometric origami lotus flower with five symmetrical petals sculpted from translucent emerald green glass and frosted jade paper, resting on a warm ivory architectural surface. The five petals carry delicate minimalist labels: 'Y TẾ', 'BỆNH LÝ', 'TAI NẠN', 'THU NHẬP', 'HƯU TRÍ'. Soft warm caustic reflections. On-Image Exact Vietnamese Typography: Headline: "HOA BẢO VỆ TOÀN DIỆN"; Subheadline: "Che chở vẹn tròn mọi khía cạnh sức khỏe & cuộc sống"; Petals: "Y TẾ", "BỆNH LÝ", "TAI NẠN", "THU NHẬP", "HƯU TRÍ"; Signature: Handwritten signature "Tiến" in emerald ink and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [29/31] Pattern 12: WEALTH_TREE
```text
A commercial luxury financial poster in botanical Wealth Tree pattern, 3:4 aspect ratio. Foreground & Hero Subject: An ancient bonsai tree sculpted from emerald jade and bronze. The deep underground roots exposed through clear glass terrain are labeled 'QUỸ BẢO VỆ & DỰ PHÒNG', while the lush green canopy bears golden fruits labeled 'TÀI SẢN & DI SẢN'. On-Image Exact Vietnamese Typography: Headline: "RỄ CÓ CHẮC, CÂY MỚI BỀN"; Subheadline: "Bảo vệ là bộ rễ nuôi dưỡng tán cây tài sản gia đình"; Labels: "QUỸ BẢO VỆ & DỰ PHÒNG", "TÀI SẢN & DI SẢN"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [30/31] Pattern 13: STRUCTURAL_METAPHOR
```text
A commercial luxury financial poster in architectural structural metaphor pattern, 3:4 aspect ratio. Foreground & Hero Subject: A low-angle perspective of a monumental cable-stayed bridge built from white marble and green steel tension cables, spanning across a deep misty ravine. The massive foundation pillar is steadfastly anchored into solid bedrock. On-Image Exact Vietnamese Typography: Headline: "NHỊP CẦU VƯỢT GIÔNG BÃO"; Subheadline: "Điểm tựa chịu lực giúp gia đình vững vàng bước tiếp"; Signature: Handwritten signature "Tiến" in green ink and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```

### [31/31] Pattern 14: ASSET_SHIELDING
```text
A commercial luxury financial poster in sophisticated asset shielding pattern, 3:4 aspect ratio. Foreground & Hero Subject: In a serene minimalist architectural courtyard, an elegant sweeping curved wall of honed white Carrara marble gently shields a glowing, warm candlelight flame from strong passing winds. Absolutely no glowing neon shields, no floating coins. On-Image Exact Vietnamese Typography: Headline: "LÁ CHẮN VÔ HÌNH, BẢO TOÀN TỔ ẤM"; Subheadline: "Bảo vệ tài sản gia đình bằng giải pháp tài chính chuẩn mực"; Signature: Handwritten signature "Tiến" and "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
```
