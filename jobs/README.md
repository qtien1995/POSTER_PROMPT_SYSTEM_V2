# Thư Mục Quản Lý Dự Án (Jobs Management Standard V3.0)

Thư mục `jobs/` được dành riêng cho các dự án và chiến dịch thiết kế thực tế của khách hàng / tư vấn viên.

---

## 1. Cấu Trúc Bắt Buộc Của Một Dự Án (Standard Job Folder Structure)
Mỗi dự án phải được tổ chức thành một thư mục độc lập với cấu trúc tinh gọn:

```
jobs/<PROJECT_NAME>/
  brief.md           # Đề bài, mục tiêu chiến dịch, thông điệp cốt lõi & copy chuẩn
  state.yaml         # Trạng thái dự án, phong cách, tỷ lệ, phiên bản, thông tin cố vấn
  MASTER_PROMPT.md   # Tệp Master Production Prompt chính thức duy nhất (hoặc theo bộ frame)
  <render_images>    # Các tệp ảnh được tạo trực tiếp (.jpg, .png)
```

---

## 2. Quy Tắc Nghiêm Cấm (Anti-Pollution Rules)
- **Nghiêm cấm để file lộn xộn ở thư mục gốc `jobs/`:** Tuyệt đối không lưu các file prompt tổng hợp (omnibus), file benchmark test, dataset JSON hay thư mục phong cách cũ ở thư mục gốc `jobs/`.
- Mọi tài liệu nghiên cứu, benchmark, catalog cũ phải được lưu trữ trong `library/archive/` hoặc `tests/`.
- Không tạo nhiều file prompt trùng lặp tên; nếu có nhiều phiên bản thử nghiệm, hãy lưu trữ vào thư mục con `archive/` bên trong job đó.

---

## 3. Các Dự Án Hoạt Động Hiện Tại
- `jobs/AO_TUONG_BHYT_THE_TU/` — Bộ poster thức tỉnh "Ảo tưởng BHYT & Thẻ từ"
- `jobs/AO_TUONG_BHYT_THE_TU_STYLE_COMIC/` — Phiên bản Tranh truyện tự sự Comic
- `jobs/BAT_THU_MON_GHI_BAN_LAM_PHAT/` — Chiến dịch "Bát phở 80k & Thủ môn ghi bàn"
- `jobs/BAY_THANH_KHOAN_SO_DO/` — Bộ poster "Bẫy thanh khoản sổ đỏ & Đất nền"
- `jobs/BHYT_5_NAM_CHI_PHI_CHIM/` — Chiến dịch "BHYT 5 năm & Chi phí chìm viện phí"
- `jobs/LA_CHAN_XANH/` — Chiến dịch "Lá Chắn Xanh — Bảo vệ bệnh hiểm nghèo"
- `jobs/PINTEREST_STYLE_019_LIFESTYLE_ECOSYSTEM/` — Dự án Hệ sinh thái tiện ích đô thị 5 phút
- `jobs/RADAR_QUY_4_BAO_TOAN_THANH_QUA/` — Poster "Radar Quý 4 — Bảo toàn thành quả"
- `jobs/song_khoe_moi_ngay_2024/` — Bộ 4 thẻ bảo lãnh viện phí "Sống Khỏe Mỗi Ngày 2024"
- `jobs/VUNG_BUOC_QUA_SONG_GIO/` — Poster "Vững bước qua sóng gió cuộc đời"
- `jobs/XANH_PHU_QUY/` — Dự án "Xanh Phú Quý — Bảo tồn & phát triển tài sản VIP"
