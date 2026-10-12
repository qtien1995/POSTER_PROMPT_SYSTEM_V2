# TUYỂN TẬP PROMPT SÁNG TẠO ĐỈNH CAO TỪ PROMPTS.CHAT (CURATED CREATIVE SUITE)

Tuyển chọn hơn 20 prompt giá trị nhất từ cộng đồng [prompts.chat](https://prompts.chat/) (tổng 2,435 prompts), được phân nhóm khoa học và đính kèm chỉ dẫn ứng dụng vào **Poster Studio & Master Prompt System V3.0**.

---

## MỤC LỤC NHANH
1. [Nhóm I: Poster & Cấu Trúc Thị Giác (Poster & Visual Architectures)](#nhóm-i-poster--cấu-trúc-thị-giác)
2. [Nhóm II: Khoa Học Thị Giác & Eye-Tracking (Visual Attention & Heatmap)](#nhóm-ii-khoa-học-thị-giác--eye-tracking)
3. [Nhóm III: Copywriting & Tiếp Thị Đỉnh Cao (Direct-Response & Advertising)](#nhóm-iii-copywriting--tiếp-thị-đỉnh-cao)
4. [Nhóm IV: Tối Ưu Prompt & Khử Nhiễu (Prompt Engineering & Noise Removal)](#nhóm-iv-tối-ưu-prompt--khử-nhiễu)
5. [Nhóm V: Nhiếp Ảnh & Sa Bàn Không Gian (Photorealism & 3D Diorama)](#nhóm-v-nhiếp-ảnh--sa-bàn-không-gian)

---

## NHÓM I: POSTER & CẤU TRÚC THỊ GIÁC

### 1. Travel Poster (Tác giả: @recep — Type: STRUCTURED)
- **ID:** 293
- **Đặc trưng:** Phong cách Modern Flat Vector Illustration, mô phỏng đồ họa Adobe Illustrator, đường nét tối giản, mảng màu rực rỡ (turquoise, terracotta, vàng cam, xanh thẳm), chuyển sắc gradient êm dịu, không gian tràn ngập năng lượng lạc quan.
- **Ứng dụng V3.0:** Đã chuẩn hóa thành [`STYLE_024_ART_DECO_VINTAGE_TRAVEL_POSTER`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_024_ART_DECO_VINTAGE_TRAVEL_POSTER.md) cho các poster chủ đề nghỉ hưu an nhàn, du lịch khám phá, tích lũy tương lai.
- **Prompt nguyên bản:**
```json
{
  "style_definition": {
    "art_style": "Modern Flat Vector Illustration",
    "medium": "Digital Vector Art",
    "vibe": "Optimistic, Cheerful, Travel Poster",
    "rendering_engine_simulation": "Adobe Illustrator / Vectorized"
  },
  "visual_parameters": {
    "lines_and_shapes": "Clean sharp lines, simplified geometry, lack of complex textures, rounded organic shapes for trees and clouds.",
    "colors": "High saturation, vibrant palette. Dominant turquoise and cyan for water/sky, warm orange and terracotta for buildings, lush green for vegetation, cream/yellow for clouds.",
    "lighting": "Flat lighting with soft gradients, minimal shadows, bright daylight atmosphere."
  },
  "generation_prompt": "Transform the input photo into a high-quality modern flat vector illustration in the style of a corporate travel poster. The image should feature simplified shapes, clean lines, and a smooth matte finish. Use a vibrant color palette with bright turquoise water, warm orange rooftops, and clear blue skies. The overall mood should be sunlit, modern, and inviting, with minimal textures and soft gradient shading."
}
```

---

### 2. Legebdary Exploded View Prompt (Tác giả: @stiva1979 — Type: STRUCTURED)
- **ID:** 302
- **Đặc trưng:** Sa bàn kỹ thuật 3D CAD cắt lớp bung tỏa (Exploded View), phơi bày các linh kiện và cấu trúc tầng lớp lơ lửng xung quanh thân chính, đường chỉ dẫn mỏng màu trắng (*callout leader lines*), nhãn số tối giản, phông chữ sans-serif tinh xảo, nền studio tối sang trọng.
- **Ứng dụng V3.0:** Đã chuẩn hóa thành [`STYLE_025_EXPLODED_VIEW_TECHNICAL_INFOGRAPHIC`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_025_EXPLODED_VIEW_TECHNICAL_INFOGRAPHIC.md), lý tưởng cho poster bóc tách tháp tài sản cá nhân, cơ cấu quỹ đầu tư liên kết đơn vị, và các tầng bảo vệ hợp đồng BHNT.
- **Prompt nguyên bản:**
```json
{
  "promptDetails": {
    "description": "Ultra-detailed exploded technical infographic of {OBJECT_NAME}, shown in a 3/4 front isometric view. The object is partially transparent and opened, with its key internal and external components separated and floating around the main body in a clean exploded-view layout. Show all major parts typical for {OBJECT_NAME}: outer shell/panels, structural frame, primary electronics/boards, power system/battery, mechanical modules, connectors, and protective shielding. Use thin white callout leader lines and numbered labels in a minimalist sans-serif font. Background: smooth dark gray studio backdrop. Lighting: soft, even, high-end product render lighting with subtle reflections. Style: photoreal 3D CAD render, industrial design concept sheet."
  }
}
```

---

### 3. Floating City Island - Photoreal 4K Poster (Tác giả: @apo-bozdag — Type: IMAGE)
- **ID:** 287
- **Đặc trưng:** Hòn đảo bay tí hon lướt trên tầng mây trắng, địa hình định hình theo bản đồ, bên trên quy tụ công trình biểu tượng, công viên xanh và nhịp sống đô thị, ánh sáng hoàng hôn ấm áp.
- **Ứng dụng V3.0:** Trực quan hóa hệ sinh thái tài chính, poster quy hoạch tài sản gia đình, cộng đồng thịnh vượng.
- **Prompt nguyên bản:**
```text
Design a "floating miniature island" shaped like the ${city:denizli} map/silhouette, gliding above white clouds. On the island, showcase tiny iconic landmarks (like ${landmark:Pamukkale travertine terraces}), lush green parks, miniature modern buildings, and a glowing sunset light casting long, soft shadows. The bottom of the island has exposed rock and earth with hanging vines, floating gently in the sky. Ultra-detailed, cinematic lighting, 4K resolution, architectural diorama style, whimsical yet realistic.
```

---

### 4. Editorial Winter Poster–Style Multi-Panel Collage Generation (Tác giả: @cipeberre — Type: STRUCTURED)
- **ID:** 331
- **Đặc trưng:** Bố cục chia khung đa ô (*multi-panel collage*), tính tự sự thời trang cao cấp, nhịp điệu tương phản giữa đại cảnh và cận cảnh chi tiết, kiểm soát bảng màu chặt chẽ.
- **Ứng dụng V3.0:** Tương thích trực tiếp với phong cách `NARRATIVE_COMIC_TIMELINE` và định dạng Carousel nhiều trang.

---

## NHÓM II: KHOA HỌC THỊ GIÁC & EYE-TRACKING

### 5. Predictive Eye Tracking Heatmap Generator (Tác giả: @ilkerulusoy — Type: STRUCTURED)
- **ID:** 295
- **Đặc trưng:** Mô phỏng chuyển động mắt người dựa trên các nguyên lý khoa học thần kinh thị giác từ **Nielsen Norman Group (NN/g)**, Thuyết tải nhận thức (*Cognitive Load Theory*) và Nguyên tắc Gestalt.
- **Quy tắc cốt lõi:**
  1. *Biological Priority:* Đôi mắt và khuôn mặt người luôn thu hút ánh nhìn tức thì và mạnh nhất.
  2. *High Contrast Visual Anchors:* Điểm có độ tương phản sáng/tối hoặc màu sắc cao nhất sẽ trở thành tiêu điểm cấp 1.
  3. *Reading Path Flow:* Luồng đọc tự nhiên hình chữ Z (Z-pattern) hoặc chữ F (F-pattern).
  4. *Negative Space Buffer:* Vùng không gian thở giúp mắt dừng lại xử lý thông điệp chữ ký và tiêu đề mà không bị quá tải.
- **Ứng dụng V3.0:** Được tích hợp trực tiếp thành cổng kiểm định thị giác tại [`rules/visual_hierarchy_eyeflow.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/visual_hierarchy_eyeflow.md).

---

## NHÓM III: COPYWRITING & TIẾP THỊ ĐỈNH CAO

### 6. Landing Page Copywriting & Headline Framework (Tác giả: @akaszhuai)
- **Nguồn:** `prompts.chat/prompts/cmu1ethy00004gm0ai88cigif_landing-page-copywriting`
- **Đặc trưng:** Hệ thống 10 công thức viết tiêu đề chuyển đổi cao (*High-Converting Headline Formulas*):
  - *Outcome without pain:* Đạt được [kết quả mơ ước] mà không phải chịu [nỗi đau/rủi ro].
  - *Turn input into outcome:* Biến [khoản tích lũy nhỏ mỗi ngày] thành [lá chắn tỷ đồng].
  - *Stop pain - Start pleasure:* Chấm dứt lo âu tài chính — Bắt đầu làm chủ tương lai.
  - *Audience callout:* Giải pháp tài chính chuyên biệt cho [đối tượng khách hàng].
  - *Differentiator:* Gói bảo hiểm duy nhất [điểm độc bản vượt trội].
- **Ứng dụng V3.0:** Đã đúc kết thành hướng dẫn thực hành tại [`rules/headline_copywriting_formulas.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/headline_copywriting_formulas.md).

---

### 7. Creative Branding Strategist & Advertiser (Tác giả: @f)
- **ID:** 12 (Advertiser), 252 (Creative Branding Strategist)
- **Đặc trưng:** Xác định góc định vị cốt lõi (*Core Positioning Hook*), tone giọng thương hiệu đĩnh đạc, biến tính năng khô khan thành giá trị cảm xúc chạm tới khách hàng.

---

## NHÓM IV: TỐI ƯU PROMPT & KHỬ NHIỄU

### 8. Removing Visual Noise in Neural Network's Response (Tác giả: Community)
- **ID:** 358
- **Đặc trưng:** Kỹ thuật loại bỏ triệt để các ký tự rác trang trí (░, ═, │, ■, >>>, ###), loại bỏ các đoạn lặp từ ngữ vô nghĩa, thanh lọc prompt để chỉ giữ lại các token mang ý niệm thị giác thuần khiết và trọng lượng cao nhất.
- **Ứng dụng V3.0:** Nâng cấp khối `NEGATIVE CONSTRAINTS & ANTI-NOISE FILTER` trong Master Prompt Contract 18 khối.

---

### 9. Senior Prompt Engineer Role Guide (Tác giả: Community)
- **ID:** 356
- **Đặc trưng:** Quy trình 4 bước chuẩn mực: Phân tích mục tiêu (Analyze) $\rightarrow$ Thiết kế cấu trúc (Persona, Context, Task, Constraints, Output Format) $\rightarrow$ Xuất mã đóng gói $\rightarrow$ Khuyến nghị chuyên gia.

---

### 10. Chimera AI-Powered Prompt Optimization System (Tác giả: Community)
- **ID:** 407
- **Đặc trưng:** Phương pháp tối ưu hóa prompt đa mô hình (Cross-provider optimization) bảo đảm câu lệnh vận hành nhất quán trên Midjourney, FLUX, ChatGPT Images 2.5 và Google Imagen 3.

---

## NHÓM V: NHIẾP ẢNH & SA BÀN KHÔNG GIAN

### 11. Whimsical 3D Brand Miniatures (Tác giả: @serkanozcan, @f — Type: IMAGE)
- **ID:** 284
- **Đặc trưng:** Mô hình cửa hàng/sa bàn 3D phong cách chibi tí hon, vật liệu nhựa polymer mịn, đèn vàng 3000K ấm cúng hắt ra từ bên trong, tượng người nhỏ nhắn dễ thương, phong cách đồ chơi hộp mù (*blind-box toy*), render Cinema 4D / Octane.
- **Ứng dụng V3.0:** Chuẩn hóa thành [`STYLE_026_WHIMSICAL_3D_ISOMETRIC_MINIATURE_DIORAMA`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_026_WHIMSICAL_3D_ISOMETRIC_MINIATURE_DIORAMA.md) cho các poster bảo vệ gia đình, tích lũy mua nhà, quỹ học vấn trẻ thơ.

---

### 12. Director Variation Grid: One Still, Eight Auteur Re-Shoots (Tác giả: @semihkislar — Type: IMAGE)
- **ID:** 296
- **Đặc trưng:** Lưới 3x3 so sánh 8 phong cách đạo diễn điện ảnh khác nhau xuất phát từ một hình ảnh gốc duy nhất.
- **Ứng dụng V3.0:** Kỹ thuật sinh biến thể đa phong cách cho cùng một thông điệp chiến dịch tiếp thị.

---

### 13. High-End Beauty & Fashion Editorial Specification (Tác giả: @cipeberre — Type: STRUCTURED)
- **ID:** 402, 403
- **Đặc trưng:** Bộ thông số vật lý ống kính 85mm prime f/2.8, ánh sáng studio Profoto softbox, bề mặt kết cấu da thực vi mô (*micro skin texture*), loại bỏ hoàn toàn da nhựa giả tạo.
