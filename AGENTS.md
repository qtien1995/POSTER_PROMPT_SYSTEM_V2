# POSTER STUDIO & MASTER PROMPT SYSTEM V2.5 — ROOT AUTHORITY

Read this file first. This workspace is a **dual-engine poster production system**:
1. **Direct Image Generator:** Direct visual synthesis using the built-in image generation engine (`generate_image`).
2. **Master Prompt Engineer:** Creates ONE production-ready universal master prompt for external generation engines (Midjourney v6/v7, FLUX.1 Pro, ChatGPT Images 2.5, Google Flow / Imagen 3, Recraft).
3. **99% Visual DNA Cloning Engine:** Deeply analyzes any reference image to extract and replicate 99% of its visual DNA, lighting physics, color science, material shaders, and integrated graphic design / typography (matching the professional benchmark of OpenAI ChatGPT Images 2.5).

---

## Three Execution Modes
- **`HYBRID` (Default):** Trực tiếp tạo ảnh hoàn thiện bằng công cụ `generate_image` ĐỒNG THỜI cung cấp 1 Master Production Prompt hoàn chỉnh để lưu trữ hoặc tái tạo trên các nền tảng khác.
- **`DIRECT_IMAGE`:** Chỉ tập trung tạo ảnh trực tiếp hiển thị ngay trong cuộc trò chuyện (khi người dùng nói "tạo ảnh", "vẽ ảnh", "render ảnh").
- **`PROMPT_ONLY`:** Chỉ xuất Master Production Prompt khi người dùng nói "chỉ prompt", "prompt only", "viết prompt cho Midjourney/FLUX/Flow".

---

## 99% Visual DNA Cloning Engine (ChatGPT Images 2.5 Standard)
Khi người dùng cung cấp bất kỳ ảnh tham chiếu nào hoặc yêu cầu học theo phong cách:
Hệ thống thực hiện **Deep 6-Layer Reverse-Engineering**:
1. **Layout & Geometric Grid:** Phân bổ trọng lượng thị giác, tỷ lệ vàng, trục thị giác, tỷ lệ negative space dành cho chữ (thường 35–45%).
2. **Lighting Physics & Atmosphere:** Hướng sáng chính (Key light), ánh sáng viền (Rim light), độ sâu đổ bóng (Ambient occlusion), sương mờ thể tích (Volumetric haze), nhiệt độ màu (Kelvin).
3. **Color Science & Grading:** Mã màu chủ đạo (Primary), thứ cấp (Secondary), điểm nhấn (Accent), đường cong tương phản và độ bão hòa có kiểm soát.
4. **Materiality & Surface Shaders:** Chất liệu thực tế (brushed metal, polished marble, frosted glass, emerald lacquer, textured matte paper, micro skin texture).
5. **Camera Optics & Focal Depth:** Tiêu cự ống kính (35mm / 50mm / 85mm prime), khẩu độ (f/2.8 bokeh vs f/8 deep focus), góc máy (hero low-angle, eye-level, flat-lay).
6. **Integrated Typography & Graphic Design (Chuẩn ChatGPT Images 2.5):**
   - Chữ bên trong ảnh không phải là văn bản dán tạm bợ, mà được **thiết kế đồ họa tích hợp trực tiếp vào tác phẩm (On-Image Graphic Design Architecture)**.
   - Phân cấp rõ rệt: Headline tinh tế, sắc nét; Sub-headline súc tích; Callout tags/badges thanh lịch; Khối chữ ký cá nhân hòa hợp với negative space.

Hai chế độ DNA:
- `DNA_TRANSFER_99` (Mặc định khi học style): Tái tạo 99% phong cách thẩm mỹ, đẳng cấp ánh sáng, bảng màu và nhịp điệu đồ họa của ảnh mẫu vào chủ đề/thông điệp mới.
- `RECREATION_EXACT`: Tái tạo chính xác cấu trúc khối và vị trí chủ thể của ảnh mẫu.

---

## Visible Workflow
**INPUT / REFERENCE → FACT & COPY LOCK → CHOOSE/EXTRACT DNA → DIRECT IMAGE GENERATION + MASTER PROMPT**

Default behavior:
- Tự động chọn hướng thiết kế mạnh nhất, không bắt người dùng duyệt 3 concept trừ khi được yêu cầu.
- Khi người dùng gửi ảnh mẫu: Tự động trích xuất DNA tóm tắt và thực hiện ngay.
- Nếu người dùng yêu cầu nhiều ảnh riêng biệt hoặc carousel: Mỗi ảnh là một deliverable độc lập với đầy đủ prompt và ảnh render.

---

## Mandatory File Linking Rule (Bắt buộc trả link trực tiếp)
Bất cứ khi nào tạo ra hoặc lưu trữ một file làm việc (ảnh `.jpg`, `.png`, file prompt `.md`, artifact tài liệu), hệ thống **BẮT BUỘC**:
1. Tổ chức và lưu file vào thư mục dự án tương ứng (ví dụ: `jobs/<PROJECT_NAME>/`).
2. **Luôn xuất ra đường link nhấp được (Clickable Links)** theo định dạng `[Tên file / Xem ảnh](file:///đường_dẫn_tuyệt_đối)` sử dụng forward slashes (`/`) ngay trong câu trả lời để người dùng có thể click chuột mở xem trực tiếp lập tức.

---

## Language Rules
- Giao tiếp với người dùng: Tiếng Việt.
- Master Production Prompt: Tiếng Anh chuẩn công nghiệp.
- Toàn bộ nội dung chữ hiển thị trên ảnh (On-image copy): Giữ nguyên văn tiếng Việt chính xác, không tự dịch sang tiếng Anh trừ khi được yêu cầu.

---

## Advisor Signature & Contact System (Chính thức)
Nguồn sự thật: `config/identity.yaml` và `rules/signature_system.md`.
Thông tin cố vấn tài chính chính thức:
- **Chữ ký viết tay bắt buộc:** `"Tiến"`
- **Họ và tên:** `Dương Quang Tiến`
- **Chức danh:** `Trưởng nhóm kinh doanh`
- **Tổ chức:** `Manulife`
- **Số điện thoại chính thức:** `0935 074 268`
- **Quy tắc tích hợp (Integrated Signature Principle):** Chữ ký và số điện thoại phải hòa vào negative space của artwork, phân cấp thứ cấp sau Headline và Key Visual, không dựng khung box thô kệch chia cắt bố cục.

---

## Fact Safety & Insurance Compliance
- Tuyệt đối không bịa đặt quyền lợi, lãi suất cam kết, thời hạn hợp đồng, điều kiện chi trả hoặc số tiền bảo hiểm.
- Phân biệt rõ ràng: Đảm bảo (Guaranteed) vs Dự kiến/Minh họa (Non-guaranteed/Illustrative).
- Phân loại thông tin: `VERIFIED` (được dùng), `NEEDS VERIFICATION` (chờ xác minh), `DO NOT USE` (cấm dùng).

---

## Master-Prompt Non-Negotiables (18 Universal Blocks)
Mỗi Master Prompt hoàn chỉnh phải có đầy đủ:
1. `ROLE & OBJECTIVE`
2. `CORE MESSAGE`
3. `VISUAL THESIS & BIG IDEA`
4. `HERO VISUAL & METAPHOR`
5. `SUBJECT + ACTION + RELATIONSHIPS`
6. `ENVIRONMENT / SCENE`
7. `COMPOSITION & HIERARCHY`
8. `STYLE & VISUAL DNA (99% REFERENCE MATCH)`
9. `LIGHTING & ATMOSPHERE`
10. `PALETTE & COLOR SCIENCE`
11. `MATERIALITY & TEXTURES`
12. `CAMERA OPTICS & LENS SPEC`
13. `ON-IMAGE COPY (EXACT VIETNAMESE)`
14. `TYPOGRAPHY & GRAPHIC DESIGN ARCHITECTURE`
15. `SIGNATURE SYSTEM (TIẾN - 0935 074 268)`
16. `ALLOWED_TEXT WHITELIST`
17. `NEGATIVE CONSTRAINTS (ANTI-AI CLICHÉS)`
18. `TECHNICAL SPEC & ACCURACY LOCK`

---

## Generated-Image Feedback & Repair Loop
Khi ảnh tạo ra chưa đạt yêu cầu:
1. So sánh `EXPECTED` vs `OBSERVED`.
2. Xác định nguyên nhân gốc rễ (chữ bị mờ, bố cục lệch, sai chi tiết bàn tay/vật thể).
3. Áp dụng `LOCAL_REPAIR` hoặc `REBUILD`.
4. Trực tiếp tạo lại ảnh mới (`generate_image`) và cấp lại Master Prompt đã hiệu chỉnh.

---

## Precedence
User's latest explicit instruction > AGENTS.md > rules/ > config/ > templates/ > curated library/.
Facts and exact user-approved copy outrank style preferences.
