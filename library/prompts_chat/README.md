# KHO TRÍ TUỆ CỘNG ĐỒNG PROMPTS.CHAT (AI PROMPTS COMMUNITY) — LOCAL ENGINE

> Nguồn chính thức: [prompts.chat - AI Prompts Community](https://prompts.chat/) / [f/prompts.chat trên GitHub](https://github.com/f/prompts.chat)  
> Tác giả sáng lập: Fatih Kadir Akın (@f)  
> Giấy phép mở: **CC0 1.0 Universal (Public Domain)**  
> Quy mô dữ liệu: **2,435 Prompts & Personas cộng đồng tinh tuyển**, 173k+ GitHub Stars, Top #1 Dataset trên Hugging Face.

---

## 1. Mục Đích Tích Hợp Vào Poster Studio V3.0

Hệ sinh thái `POSTER STUDIO & MASTER PROMPT SYSTEM V3.0` tích hợp toàn bộ kho tri thức `prompts.chat` trực tiếp vào workspace offline nhằm đạt được 4 mục tiêu đột phá:

1. **Local Intelligence Hub (Hoạt Động Offline 100%):** Lưu trữ trọn vẹn 2,435 prompts tại [`library/prompts_chat/prompts_community.json`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/prompts_community.json) và [`library/prompts_chat/prompts.csv`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/prompts.csv), tra cứu siêu tốc bằng CLI [`scripts/prompts_chat_tool.py`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/scripts/prompts_chat_tool.py) mà không cần mạng Internet.
2. **Cầu Nối Chuyển Hóa Sang 18-Block Master Prompt:** Bộ chuyển đổi thích ứng (`adapt`) cho phép lấy bất kỳ ý tưởng hoặc persona nào từ cộng đồng và biên dịch chuẩn hóa thành 1 Master Production Prompt 18 khối đạt chuẩn công nghiệp.
3. **Cải Tiến Hệ Thống Bằng 3 Kỹ Thuật Đỉnh Cao:**
   - **Mô Hình Chú Ý Thị Giác & Eye-Tracking (Cognitive Science):** Kế thừa từ prompt `Predictive Eye Tracking Heatmap Generator` của Nielsen Norman Group & Gestalt, bổ sung quy chuẩn kiểm soát điểm rơi ánh nhìn tại [`rules/visual_hierarchy_eyeflow.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/visual_hierarchy_eyeflow.md).
   - **Bộ Lọc Khử Nhiễu Ký Tự AI (Anti-Visual-Noise Filter):** Kế thừa từ prompt `Removing visual noise in the neural network's response`, loại bỏ triệt để rác ký tự, bracket thừa và token lặp vô nghĩa.
   - **Bộ 10 Công Thức Tiêu Đề Đột Phá (High-Converting Headline Formulas):** Kế thừa từ prompt `Landing page copywriting` & `Advertiser`, hệ thống hóa tại [`rules/headline_copywriting_formulas.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/headline_copywriting_formulas.md).
4. **Bổ Sung 3 Phong Cách Nghệ Thuật Mới Vào Hệ Thống V3.0:**
   - [`STYLE_024_ART_DECO_VINTAGE_TRAVEL_POSTER`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_024_ART_DECO_VINTAGE_TRAVEL_POSTER.md)
   - [`STYLE_025_EXPLODED_VIEW_TECHNICAL_INFOGRAPHIC`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_025_EXPLODED_VIEW_TECHNICAL_INFOGRAPHIC.md)
   - [`STYLE_026_WHIMSICAL_3D_ISOMETRIC_MINIATURE_DIORAMA`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_026_WHIMSICAL_3D_ISOMETRIC_MINIATURE_DIORAMA.md)

---

## 2. Cấu Trúc Thư Mục & Tài Nguyên

- [`prompts_community.json`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/prompts_community.json): Cơ sở dữ liệu JSON đầy đủ của 2,435 prompts (gồm các trường: `id`, `act`, `prompt`, `type`, `for_devs`, `contributor`).
- [`prompts.csv`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/prompts.csv): Bản sao raw CSV 6.8MB đồng bộ từ kho upstream của Fatih Kadir Akın.
- [`CURATED_CREATIVE_PROMPTS.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/CURATED_CREATIVE_PROMPTS.md): Tuyển tập 30+ prompt xuất sắc nhất dành riêng cho mỹ thuật, poster đồ họa, copywriting và kỹ nghệ prompt.
- [`scripts/prompts_chat_tool.py`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/scripts/prompts_chat_tool.py): Công cụ CLI tương tác dòng lệnh để tra cứu, hiển thị và tự động chuyển đổi sang Master Prompt.

---

## 3. Hướng Dẫn Sử Dụng Công Cụ CLI (`prompts_chat_tool.py`)

### Xem thống kê dữ liệu
```bash
python scripts/prompts_chat_tool.py stats
```

### Tìm kiếm prompt theo từ khóa hoặc loại hình
```bash
# Tìm kiếm từ khóa "poster"
python scripts/prompts_chat_tool.py search "poster"

# Tìm kiếm prompt ảnh (IMAGE)
python scripts/prompts_chat_tool.py search "3d" --type IMAGE

# Tìm kiếm prompt cấu trúc (STRUCTURED)
python scripts/prompts_chat_tool.py search "infographic" --type STRUCTURED
```

### Hiển thị chi tiết nội dung prompt
```bash
# Xem theo tên Act
python scripts/prompts_chat_tool.py show "Travel Poster"

# Xem theo ID
python scripts/prompts_chat_tool.py show 293
```

### Xem danh sách tuyển tập tuyển chọn (Curated)
```bash
python scripts/prompts_chat_tool.py list-curated
```

### Tự động chuyển đổi sang 18-Block Master Production Prompt
```bash
python scripts/prompts_chat_tool.py adapt "Travel Poster" --topic "Bảo an gia đình đón bình minh 2026" --headline "BÌNH YÊN TRƯỚC MỌI BẾN ĐỖ"
```

---

## 4. Tôn Trọng Bản Quyền & Nguồn Gốc

Kho dữ liệu này được bảo chứng bởi cộng đồng mã nguồn mở toàn cầu dưới giấy phép **CC0 1.0 Universal**. Khi tái sử dụng các prompt tiêu biểu trong các nghiên cứu hoặc sản phẩm thương mại, hệ thống ghi nhận đóng góp của tác giả gốc tại mục metadata (ví dụ: `@f`, `@recep`, `@ilkerulusoy`, `@semihkislar`, `@serkanozcan`, `@cipeberre`, `@iamcanturk`).
