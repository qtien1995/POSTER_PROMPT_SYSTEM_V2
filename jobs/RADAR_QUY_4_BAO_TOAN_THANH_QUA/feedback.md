# FEEDBACK & REPAIR AUDIT: RADAR QUÝ 4 POSTER (V1 -> V2 -> V3 -> V4)
**Ngày ghi nhận:** 02/10/2026  
**Lịch sử ảnh render:**
- V1: [`user_render_v1.png`](file:///d:/POSTER_PROMPT_SYSTEM_V2/jobs/RADAR_QUY_4_BAO_TOAN_THANH_QUA/user_render_v1.png) — Lỗi 1 font phẳng, thiếu điểm nhấn.
- V2: [`user_render_v2.png`](file:///d:/POSTER_PROMPT_SYSTEM_V2/jobs/RADAR_QUY_4_BAO_TOAN_THANH_QUA/user_render_v2.png) — Tiêu đề Didot + 3D Gold rất đẹp, nhưng chữ ký "Tiến" trôi nổi đơn độc giữa đáy, mất thông tin.
- V3: [`user_render_v3.png`](file:///d:/POSTER_PROMPT_SYSTEM_V2/jobs/RADAR_QUY_4_BAO_TOAN_THANH_QUA/user_render_v3.png) — Bị lỗi layout: đường kẻ ngang dài cắt đôi chân trang, chữ ký "Tiến" một nơi còn dòng thông tin dàn trải hết mép trang một nẻo ("lạc quẻ"); phụ đề bị trùng lặp text với badge.

---

## 1. SO SÁNH V3 EXPECTED VS OBSERVED

| Tiêu chí | EXPECTED (Kỳ vọng) | OBSERVED (Thực tế ảnh V3) | Đánh giá |
| :--- | :--- | :--- | :--- |
| **Headline & 3D Visual** | Tiêu đề Didot + 3D Champagne Gold Embossed, đền đá Carrara tròn, mầm cây ánh vàng. | Tiếp tục duy trì đẳng cấp rất cao, sắc nét, sang trọng. | **ĐẠT XUẤT SẮC (10/10)** |
| **Dòng phụ (Subheadline)** | `Đừng để một biến cố sức khỏe bất ngờ xóa sạch nỗ lực cả năm`. | Bị AI render trùng lặp câu của Badge trên cùng: "Kế hoạch bảo vệ Quý 4 • Nền tảng An Tâm". | **LỖI LẶP CHỮ (Cần sửa)** |
| **Khối Chữ Ký Nhận Diện** | Chung 1 cụm thống nhất (Cohesive Stack): Chữ ký "Tiến", Tên, Chức danh, SĐT đi liền với nhau thành 1 khối danh thiếp sang trọng. | Bị tách làm 2 phần rời rạc: Một đường kẻ ngang dài hết trang, "Tiến" nằm góc phải bên trên, dòng text kéo dài từ mép trái sang mép phải bên dưới. **Chữ ký bị lạc quẻ hoàn toàn!** | **CHƯA ĐẠT LAYOUT (Cần sửa gấp)** |

---

## 2. QUY CHUẨN THIẾT KẾ KHỐI NHẬN DIỆN MỚI (THE COHESIVE IDENTITY STACK)
Gom toàn bộ 4 yếu tố thành **1 CỤM THỐNG NHẤT DUY NHẤT**, căn chỉnh thẳng hàng:
```
           / Tiến /          ◄── [Chữ ký tay nghệ thuật]
       Dương Quang Tiến      ◄── [Họ và tên - Font Swiss Semi-bold]
    Trưởng nhóm kinh doanh   ◄── [Chức danh]
           Manulife          ◄── [Tổ chức]
         0935 074 268        ◄── [Số điện thoại chính thức]
```
- **Xóa bỏ triệt để:** Đường kẻ ngang dài hết khổ giấy.
- **Xóa bỏ triệt để:** Dòng chữ kéo dài từ mép trái sang mép phải.
