# Workflow Chuẩn V3.0 (Quy Trình Tối Ưu Tốc Độ & Sản Xuất Trực Tiếp)

Quy trình sản xuất poster và Master Prompt được chuẩn hóa theo 5 bước tinh gọn, đặt trọng tâm vào Bảo Hiểm Nhân Thọ (BHNT), linh hoạt mở rộng đa ngành, 100% tiếng Việt chuẩn dấu, và **mặc định tự động chọn 1 hướng thiết kế mạnh nhất để ra sản phẩm hoàn thiện ngay lập tức**.

---

## 1. TIẾP NHẬN ĐỀ BÀI (INPUT & DOMAIN LOCK)
- Tiếp nhận tự nhiên: Ý tưởng thô, câu chuyện đời thực, quyền lợi bảo hiểm, thông điệp bán hàng, hoặc ảnh tham chiếu (*reference image*).
- **Trọng tâm ngành:** Ưu tiên số 1 là **Bảo hiểm nhân thọ** (Manulife, bảo vệ gia đình, y tế, hưu trí, học vấn, tích lũy, chuyển giao di sản). Tuy nhiên, sẵn sàng mở rộng sang Bất động sản, Tài chính, Giáo dục, Công nghệ xanh khi có yêu cầu.

---

## 2. KHÓA THÔNG ĐIỆP & SOÁT LỖI DẤU TIẾNG VIỆT 100% (COPY & ORTHOGRAPHY GUARD)
- Giao tiếp và tư duy thiết kế: **100% Tiếng Việt**.
- Xác định thông điệp cốt lõi và nội dung chữ hiển thị trên ảnh (*On-image copy*).
- **Bộ soát lỗi dấu thanh bắt buộc:** Quét toàn bộ các từ tiếng Việt có dấu (`ươ`, `iê`, `oạ`, `uâ`, `ẵ`, dấu hỏi/ngã) để bảo đảm tuyệt đối không sai chính tả, không mất dấu và không bị dịch nhầm sang tiếng Anh trước khi nạp vào prompt.

---

## 3. LỰA CHỌN PHONG CÁCH & XUẤT SẢN PHẨM (STYLE SELECTION & EXECUTION)

### A. Luồng Mặc Định: PROMPT_ONLY (Chốt Nội Dung, Style, PA → Viết Bộ 4 Prompt Để Test)
- **Quy trình chuẩn:**
  1. Thảo luận, chốt nội dung và cốt truyện 4 phân đoạn (Headline, Subhead, thông điệp cốt lõi).
  2. Xác định phong cách mỹ thuật hoặc đưa ra các Phương Án (PA1, PA2, PA3...) để người dùng lựa chọn nếu cần.
  3. Sau khi người dùng **chốt nội dung, style, hoặc chọn PA**, hệ thống tiến hành viết **Bộ Prompt Thực Chiến đồng bộ cho 4 ảnh (Carousel 4 Frames)** để người dùng tự copy đi test trên Midjourney, FLUX, ChatGPT Images 2.5, Google Flow.
  4. **Tuyệt đối KHÔNG tự ý tạo ảnh bằng AI trong luồng mặc định.**

### B. Kích Hoạt Sinh Ảnh AI Trực Tiếp (`generate_image`)
- **CHỈ KHI NÀO** người dùng có yêu cầu rõ ràng:
  - Ví dụ: *"Tạo ảnh"*, *"Vẽ hình này"*, *"Render ảnh cho tôi xem"*, *"Hãy tạo 4 ảnh từ prompt trên"*, hoặc *"Chọn PA1 và vẽ 4 ảnh luôn"*.
  - Lúc đó, hệ thống mới gọi công cụ `generate_image`, lưu file vào thư mục `jobs/<PROJECT>/` và cung cấp đường link nhấp được trực tiếp.

### C. 3 Chế Độ Vận Hành Hệ Thống:
- **`PROMPT_ONLY` (Mặc định):** Xuất Bộ 4 Prompt Thực Chiến sau khi chốt nội dung, style, PA để người dùng tự test.
- **`DIRECT_IMAGE`:** Chỉ tập trung tạo ảnh hiển thị ngay khi người dùng yêu cầu tạo ảnh.
- **`HYBRID`:** Vừa tạo ảnh vừa xuất bộ prompt khi người dùng yêu cầu rõ ràng cả hai.

---

## 4. QUY TẮC LINK NHẤP ĐƯỢC (MANDATORY CLICKABLE FILE LINKING)
Bất cứ khi nào tạo ra file ảnh (`.jpg`, `.png`) hoặc file prompt/brief:
1. Tổ chức và lưu file vào thư mục dự án tương ứng: `jobs/<PROJECT_NAME>/`.
2. **Luôn xuất ra đường link nhấp được (Clickable Links)** theo định dạng `[Tên file / Xem ảnh](file:///đường_dẫn_tuyệt_đối)` sử dụng forward slashes (`/`) ngay trong câu trả lời để người dùng click mở xem trực tiếp lập tức.

---

## 5. CƠ CHẾ TỰ ĐỘNG HỌC & MỞ RỘNG DNA TỪ ẢNH MẪU (AUTO-EXPANDING DNA PIPELINE)
Khi người dùng gửi ảnh mẫu hoặc yêu cầu học style mới:
1. Chạy **Deep 6-Layer Reverse-Engineering** (Bố cục, Ánh sáng, Bảng màu, Chất liệu, Quang học, Typography).
2. Tự động lưu thẻ DNA mới vào `library/dna/DNA_<MÃ_HIỆU>_<TÊN>.md`.
3. Tự động chuẩn hóa và nâng cấp thành Master Style Spec trong `library/styles/STYLE_<MÃ_HIỆU>_<TÊN>.md` và cập nhật vào `library/styles/MASTER_STYLE_SYSTEM_V3.md`.
4. Hệ thống tự mở rộng không giới hạn, liên tục đón nhận xu hướng thẩm mỹ mới.
