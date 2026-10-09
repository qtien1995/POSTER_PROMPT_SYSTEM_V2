# Production Platform Adapters V2.5

The Master Production Prompt is written in universal English so it can be deployed directly across all top-tier AI generation platforms with targeted optimization.

---

## 1. ChatGPT Images 2.5 Adapter (Sunburst & Flare)
- **Tối ưu hóa:** ChatGPT Images 2.5 vượt trội về hiểu ngữ cảnh tự nhiên, duy trì phong cách qua các lần chỉnh sửa (multi-turn consistency) và bảo toàn đặc trưng của ảnh tham chiếu.
- **Cấu trúc lệnh:**
  - Nêu rõ vai trò của ảnh mẫu: *"Learn the visual DNA, lighting physics, and graphic design architecture from [Reference Image], but generate a new scene featuring [New Subject]."*
  - Khóa vùng chữ (Text Lock): Ghi rõ câu chữ tiếng Việt đặt trong ngoặc kép với vị trí cụ thể (Headline at top negative space, secondary copy at bottom-left).
  - Yêu cầu render kiểu thiết kế đồ họa thương mại cao cấp (commercial graphic design poster with sharp typography).

---

## 2. FLUX.1 Pro Adapter
- **Tối ưu hóa:** FLUX.1 Pro có khả năng render chữ (typography) và tái tạo chất liệu thực tế (materiality) cực kỳ xuất sắc.
- **Cấu trúc lệnh:**
  - Sử dụng văn phong mô tả tự nhiên, giàu chi tiết vật lý (lighting Kelvin, camera focal length, surface texture).
  - Tách bạch rõ giữa khối hình ảnh mô tả và khối chữ cần in: `The image features the bold, crisp text "TIÊU ĐỀ" rendered cleanly in modern sans-serif typography across the upper third.`
  - Thêm chữ ký: `In the lower right corner, elegant subtle handwritten signature "Tiến" followed by the line "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268".`

---

## 3. Midjourney v6 / v7 Adapter
- **Tối ưu hóa:** Midjourney mạnh về tính thẩm mỹ, nghệ thuật điện ảnh (cinematic quality) và chi tiết ánh sáng.
- **Cấu trúc tham số:**
  - Thêm đuôi tham số bắt buộc: `--ar 4:5 --style raw --v 6.1`
  - Nếu dùng ảnh tham chiếu làm style: Sử dụng tham số `--sref [URL]` kết hợp `--sw 100` (hoặc `--sw 200` nếu muốn áp chặt DNA phong cách).
  - Khóa text tiếng Việt bằng cách đặt chuỗi chữ trong dấu ngoặc kép `"..."`.

---

## 4. Google Flow / Imagen 3 Adapter
- **Tối ưu hóa:** Rất mạnh về bố cục không gian, chi tiết điện ảnh và độ tương phản tự nhiên.
- **Cấu trúc lệnh:**
  - Mô tả theo cấu trúc phân tầng rõ ràng: Chủ thể chính (Foreground/Hero) → Hậu cảnh (Environment) → Hướng chiếu sáng (Lighting) → Tông màu và chất liệu (Color & Material) → Không gian âm và vị trí văn bản.
