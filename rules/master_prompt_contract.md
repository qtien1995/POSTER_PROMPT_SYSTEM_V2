# Quy Chuẩn Bộ Prompt Thực Chiến (Production Prompt Contract V3.1)

Hệ thống chính thức **loại bỏ định dạng prompt 18 khối cồng kềnh**, thay thế bằng **Bộ Prompt Thực Chiến (Mặc định Bộ 4 Ảnh / 4-Frame Carousel Suite)**.

Khi người dùng chốt nội dung, thông điệp và phong cách, hệ thống sẽ viết bộ prompt tương ứng cho 4 ảnh (hoặc số lượng ảnh người dùng yêu cầu) để người dùng tự copy đi kiểm thử trên Midjourney, FLUX, ChatGPT Images 2.5 hoặc Google Flow.

---

## 1. Cấu Trúc Tổng Thể Của Bộ 4 Prompt

Mỗi đợt xuất bản bao gồm 2 phần chính:

### Phần A: Thông Số Visual DNA Đồng Bộ (Shared Visual DNA)
Được nêu ở đầu bộ prompt để đảm bảo cả 4 ảnh có phong cách thẩm mỹ đồng nhất:
- **Phong cách nghệ thuật đã chọn:** (Ví dụ: The New Yorker Comic Timeline, Papercraft 3D, Art Deco Travel, Modern Flat Vector, Kintsugi...).
- **Chất liệu nền & Shaders:** (Giấy Dó ngà sần, vải gấm thêu chỉ vàng, đá cẩm thạch, gốm men rạn...).
- **Bảng màu chấm phá (Color Accents):** Mã màu chủ đạo (Emerald Green `#004D2C`, Ochre Gold `#D4AF37`, Ivory Cream `#FBF9F4`...).
- **Tỷ lệ khung hình đồng bộ:** Mặc định `1:1` vuông (chuẩn Facebook/Instagram Feed) hoặc `4:5` dọc.

### Phần B: Chi Tiết Prompt Cho Từng Khung Hình (Frame 1 → Frame 4)

Mỗi khung hình đảm nhận một mắt xích trong kịch bản tự sự:
- **FRAME 01: THE HOOK & MENTAL MODEL (Dừng lướt & Thức tỉnh)**
- **FRAME 02: THE CONTRAST & BLINDSPOT (Điểm mù & Nghịch lý)**
- **FRAME 03: THE ARCHITECTURE & MATH (Cơ chế bảo vệ & Công thức số liệu)**
- **FRAME 04: THE RESOLUTION & ADVISOR STACK (Đúc kết, Kêu gọi hành động & Chữ ký cố vấn)**

---

## 2. Quy Chuẩn Cấu Trúc Của Từng Prompt Đơn Lẻ

Thay vì 18 khối máy móc, mỗi prompt cho từng frame được cấu trúc tinh gọn theo các trường thông tin sau:

```text
ROLE & OBJECTIVE:
[Thể loại ảnh, mục tiêu dừng lướt và thông điệp cần truyền tải trong frame này.]

VISUAL THESIS & HERO METAPHOR:
[Mô tả cụ thể chủ thể chính, hành động, biểu tượng ẩn dụ và các chi tiết tương tác trong bối cảnh. Tuyệt đối không dùng người mẫu AI da nhựa giả tạo.]

STYLE & MATERIALITY:
[Chất liệu thật, kỹ thuật tạo hình, bề mặt vân giấy/gốm/vải, ánh sáng vật lý.]

COMPOSITION & ASPECT RATIO:
[Tỷ lệ khung hình (1:1 hoặc 4:5). Phân bổ vùng âm bản (negative space 35-45%) dành cho chữ tiếng Việt.]

ON-IMAGE COPY (EXACT VIETNAMESE):
Headline:
"[Tiêu đề chính chuẩn 100% tiếng Việt có dấu]"
Subhead:
"[Dòng phụ hoặc thông số số liệu]"

SIGNATURE & IDENTITY (Bắt buộc ở Frame 4 hoặc góc Frame 1):
Chữ ký viết tay: "Tiến"
Khối thông tin: "Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268"

ALLOWED_TEXT WHITELIST:
[Danh sách chính xác các chuỗi ký tự được phép hiển thị trên ảnh]

NEGATIVE CONSTRAINTS & ANTI-NOISE:
[No plastic CGI skin, no uncanny smiling models, no visual noise symbols (░, ═, ###), no gibberish.]
```

---

## 3. Quy Tắc Chữ Hiển Thị Trên Ảnh (Copy is Part of the Design)
1. **Tiếng Việt 100% có dấu thanh:** Giữ nguyên văn bản tiếng Việt chính xác trong ngoặc kép `""`. Không tự ý dịch sang tiếng Anh.
2. **Súc tích, cô đọng:** Tiêu đề dưới 10 từ để người xem nắm bắt trong 1.5 giây.
3. **Bộ soát lỗi dấu thanh:** Đảm bảo các nguyên âm ghép (`ươ`, `iê`, `oạ`, `uâ`, `ẵ`) hiển thị chuẩn xác.

---

## 4. Khối Nhận Diện Cố Vấn (Advisor Signature)
- Nguồn sự thật: `config/identity.yaml`
- Luôn tích hợp trang nhã vào vùng negative space ở Frame 4 (hoặc góc dưới Frame 1):
  - Chữ ký viết tay: `"Tiến"`
  - Họ và tên: `Dương Quang Tiến`
  - Chức danh & Tổ chức: `Trưởng nhóm kinh doanh Manulife`
  - Hotline chính thức: `0935 074 268`
- **Nghiêm cấm vạch kẻ ngang chia cắt trang.**
