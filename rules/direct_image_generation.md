# Direct Image Generation Rule

This rule defines how the system directly synthesizes visual posters using the built-in `generate_image` tool.

---

## 1. When to Trigger Direct Image Generation
- **`HYBRID` Mode (Default):** Always generate the direct image AND output the Master Production Prompt.
- **`DIRECT_IMAGE` Mode:** When user explicitly asks to "tạo ảnh", "vẽ ảnh", "render ảnh", "làm hình này".
- If the user explicitly asks for "chỉ prompt" or "prompt only", skip image generation and output prompt only.

---

## 2. Tool Invocation Contract
When calling `generate_image`:
- **`Prompt`**: Must be a high-density, descriptive prompt optimized for AI image rendering.
  - State the subject, environment, lighting, color palette, camera angle, and artistic style clearly.
  - Explicitly include instructions for graphic design elements, negative space, and on-image Vietnamese typography.
  - Instruct the model to render crisp, editorial-quality typography for the headline, subhead, and signature.
- **`ImageName`**: Lowercase with underscores, 2-3 words (e.g., `poster_xanh_uoc_mo`, `manulife_wealth_metaphor`, `advisor_tien_editorial`).
- **`AspectRatio`**: Chuẩn hóa theo bảng ánh xạ thông minh (Smart Aspect Ratio Mapping):
  - Khi yêu cầu `'4:5'` (Chuẩn Facebook / Instagram Feed): Trong lệnh gọi `generate_image`, **tự động ánh xạ sang `'3:4'`** (tỷ lệ gần nhất được hỗ trợ bởi tool API để tránh lỗi), trong khi trong Master Production Prompt cung cấp cho người dùng vẫn giữ nguyên `'4:5'` (hoặc `--ar 4:5`) cho Midjourney/FLUX.
  - Khi yêu cầu `'1:1'`: Sử dụng `'1:1'` (Square Feed / Carousel).
  - Khi yêu cầu `'9:16'`: Sử dụng `'9:16'` (Story / Reels / TikTok).
  - Khi yêu cầu `'16:9'`: Sử dụng `'16:9'` (Landscape / Web Banner / Youtube).
  - Các tỷ lệ khác được hỗ trợ trực tiếp bởi API: `'2:3'`, `'3:2'`, `'4:3'`.
- **`ImagePaths`**: When learning DNA from a reference image in the workspace or artifact directory, pass up to 3 image file paths in `ImagePaths` to guide visual generation.

---

## 3. Integrated Typography & Graphic Design Standard (ChatGPT Images 2.5 Quality)
Direct image generation must not look like an empty stock photo. It must look like a **finished commercial graphic design artwork**:
1. **Headline Zone:** High-contrast, sharp typography integrated into dedicated negative space.
2. **Subhead & Value Proposition:** Subtle, readable secondary text block.
3. **Identity & Signature:** Subtle handwritten mark "Tiến" and professional line: "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".
4. **Graphic Flourishes:** Clean minimal badges, subtle framing hairline borders, metric callouts if relevant.

---

## 4. Multi-Turn Iteration & Repair
When the generated image has flaws:
- Use `ImagePaths` with the generated image path and specify precise edit instructions in `Prompt`.
- Focus fixes on typography alignment, facial features, or lighting adjustments.

---

## 5. Mandatory Clickable Link Rule (Bắt buộc trả link trực tiếp)
Every time an image is generated:
1. Organize and copy the file into the project folder (`d:/POSTER_PROMPT_SYSTEM_V2/jobs/<PROJECT_NAME>/`).
2. Always output direct, clickable GitHub-style markdown links with `file:///` and forward slashes (`/`) so the user can immediately click to open and view the high-resolution image in their viewer.
