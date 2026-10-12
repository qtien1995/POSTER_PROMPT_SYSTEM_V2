# Final Completeness Gate & QA Checklist V3.0 (Master Release)

Every poster design or master prompt must pass this gate before delivery.  
Source authority: `rules/qa_completeness_gate.md` & [`rules/visual_hierarchy_eyeflow.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/visual_hierarchy_eyeflow.md).

---

## 1. 8-Point Final Completeness Gate

1. **VISUAL:** Chủ thể chính (focal point) có nổi bật không? Ý niệm thị giác (metaphor/hero) có phục vụ thông điệp không? Tôn vinh chất liệu thủ công thật, loại bỏ hoàn toàn người mẫu da nhựa CGI (*plastic skin*).
2. **MESSAGE:** Poster có truyền tải duy nhất một thông điệp cốt lõi trong 1–2 giây đầu tiên không? Headline có ứng dụng các công thức tiêu đề đột phá ([`rules/headline_copywriting_formulas.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/headline_copywriting_formulas.md)) để đạt sức hút dừng lướt (*stopping power*) không?
3. **TYPOGRAPHY & HIERARCHY:** Bố cục chữ có phân tầng rõ rệt (Headline $\rightarrow$ Subhead $\rightarrow$ Detail/Badge) không? Phông chữ có sắc nét, cao cấp chuẩn editorial graphic design không? Bộ dấu tiếng Việt đã được bảo vệ toàn vẹn (*Diacritical Guard*) chưa?
4. **ADVISOR SIGNATURE SYSTEM:** Đã tích hợp đầy đủ chữ ký viết tay **"Tiến"** và khối thông tin **Dương Quang Tiến • Trưởng nhóm kinh doanh Manulife • 0935 074 268** vào negative space chưa? *(Tuyệt đối không dựng box thô kệch chia cắt trang)*.
5. **ACCURACY & COMPLIANCE:** Mọi con số, quyền lợi hoặc điều kiện có đúng với tài liệu chính thức không? Có bị biến "minh họa" thành "cam kết" không?
6. **MOBILE READABILITY (Thumbnail Test):** Khi thu nhỏ về kích thước màn hình điện thoại (khoảng 3–4 cm), headline và focal point có đọc/hiểu được ngay trong 3 giây không?
7. **TECHNICAL INTEGRITY:** Tỷ lệ khung hình đúng (4:5 / 1:1 / 9:16); không lỗi giải phẫu (ngón tay, khuôn mặt), không bị bóng nhựa rẻ tiền.
8. **VISUAL ATTENTION & EYE-FLOW (Cognitive Heatmap Check):** Đạt chuẩn kiểm tra luồng mắt tự nhiên (Z-Pattern hoặc Circular Orbit), mỏ neo tương phản cao nhất nằm đúng vị trí Hero/Headline, và duy trì tối thiểu 35–45% vùng âm bản thanh sạch (*negative space buffer*).

---

## 2. Thumbnail Test (Kiểm tra hiển thị di động)
Thu nhỏ ảnh về kích thước mobile:
- Headline còn đọc được rõ ràng không?
- Chủ thể trung tâm còn nổi bật không?
- Khối chữ ký cá nhân có đặt đúng vị trí, không đè lên hình ảnh chính không?
- Nếu quá dày chữ: Lập tức cô đọng câu chữ hoặc chuyển sang định dạng Carousel nhiều trang.

---

## 3. Anti-AI Artifact Checklist
Quét nhanh các lỗi thường gặp của AI:
- Bàn tay và ngón tay thừa/thiếu;
- Mắt hoặc nét mặt bị biến dạng;
- Đồ vật bị hòa lẫn hoặc dính vào nhau phi vật lý;
- Chữ tiếng Việt bị mất dấu hoặc xuất hiện ký tự rác;
- Hiện tượng nhựa hóa (*plastic look*) hoặc vầng sáng neon (*glow*) quá mức.

---

## 4. Anti-Visual-Noise Filter (Chuẩn prompts.chat)
Thanh lọc toàn bộ rác ký tự và token dư thừa khỏi Master Prompt và ảnh đồ họa:
- **Loại bỏ triệt để ký tự rác:** Không để lọt các ký tự dịch vụ (░, ═, │, ■, >>>, ###, [bracket thừa]);
- **Khử lặp từ ngữ:** Loại bỏ các đoạn lặp dòng, lặp từ, hoặc các khối tiêu đề bị nhân bản phi lý;
- **Bảo toàn ngữ nghĩa:** Chỉ giữ lại các token mang ý niệm thị giác thuần khiết, cô đọng và có trọng lượng tạo hình mạnh nhất.
