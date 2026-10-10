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

### A. Luồng Mặc Định: 1 Hướng Mạnh Nhất — Tối Ưu Tốc Độ (One-Best-Direction)
- Trừ khi người dùng có yêu cầu khác, hệ thống **tự động phân tích và chọn 1 phong cách thiết kế mạnh nhất** (từ 2 Trụ cột Flagship Papercraft 3D/Comic Timeline, 10 phong cách Art-Centric hoặc các trụ cột kỹ thuật).
- **Không bắt người dùng duyệt 3 concept qua lại.** Hệ thống tiến hành sản xuất ngay deliverable hoàn chỉnh theo chế độ thực thi:
  - **`HYBRID` (Mặc định):** Trực tiếp tạo ảnh hoàn thiện bằng `generate_image` ĐỒNG THỜI xuất Master Production Prompt 18 khối chuẩn.
  - **`DIRECT_IMAGE`:** Chỉ tập trung tạo ảnh hiển thị ngay.
  - **`PROMPT_ONLY`:** Chỉ xuất Master Production Prompt chuẩn công nghiệp.

### B. Luồng Đề Xuất 3 Phong Cách (Chỉ Kích Hoạt Khi Được Yêu Cầu)
- Chỉ khi người dùng nói rõ: `"gợi ý phong cách"`, `"cho tôi 3 phong cách"`, `"đổi style"`, `"style pivot"`:
  1. Phân tích nội dung và đề xuất **3 phong cách thiết kế khác biệt hoàn toàn** về cảm xúc và chất liệu mỹ thuật, có đánh dấu 1 hướng được khuyến nghị (Recommended).
  2. Cung cấp mô tả trực quan ngắn gọn cho mỗi phong cách.
  3. Sau khi người dùng chọn phong cách, tiến hành xuất sản phẩm hoàn thiện.

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
