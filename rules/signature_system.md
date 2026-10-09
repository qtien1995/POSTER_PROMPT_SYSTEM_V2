# Signature System V2

Signature is a designed identity layer, not a random watermark.
Source of truth: `config/identity.yaml`.

## Components
### A. Handwritten mark — mandatory
Exact text: `Tiến`
- handwritten character;
- subtle;
- legible;
- secondary;
- visually integrated.

### B. Professional identity block
Default personal-brand block:
- `Dương Quang Tiến`
- `Trưởng nhóm kinh doanh`
- `Manulife`

### C. Contact block
Phone may be included only when:
- `config/identity.yaml.phone` contains a confirmed number; or
- the user explicitly supplies a confirmed phone number in the current task.

Never invent or auto-complete a phone number.

## Modes
### `minimal`
Render only handwritten `Tiến`.
Use when the user explicitly wants a very clean editorial poster or minimal signature.

### `personal_brand` — DEFAULT
Render handwritten `Tiến` plus:
- Dương Quang Tiến
- Trưởng nhóm kinh doanh
- Manulife

### `contact`
Render personal-brand mode plus confirmed phone number.
If phone is missing, do not render a placeholder such as `[PHONE]`; fall back to `personal_brand` and state the missing phone outside ALLOWED_TEXT only when necessary.

## Placement & Lockup Architecture (Quy Tắc Cụm Nhận Diện Thống Nhất)
The system integrates signature and contact as a **SINGLE UNIFIED COHESIVE BLOCK (Chung 1 cụm thống nhất)**:

### 1. Cấu trúc xếp tầng 4 dòng bắt buộc (The 4-Tier Cohesive Stack):
Toàn bộ khối nhận diện phải gom lại thành **MỘT CỤM ĐỒNG BỘ DUY NHẤT**, xếp dọc theo thứ tự chặt chẽ:
- **Dòng 1 (Trên cùng cụm):** Chữ ký viết tay nghệ thuật `"Tiến"` (mực xanh ngọc bích hoặc vàng nhũ, mềm mại).
- **Dòng 2:** Họ và Tên: `Dương Quang Tiến` (Font Swiss Sans-serif hoặc Semi-bold, chỉn chu).
- **Dòng 3:** Chức danh & Tổ chức: `Trưởng nhóm kinh doanh Manulife` (Font Regular thanh lịch).
- **Dòng 4:** Số điện thoại: `0935 074 268` (Font Monospace hoặc Clean Sans rõ nét).

### 2. Các điều CẤM TUYỆT ĐỐI:
- **CẤM LẠC QUẺ:** Tuyệt đối không để chữ ký một nơi, còn dòng thông tin bị kéo dài dàn trải từ mép trái sang mép phải.
- **CẤM ĐƯỜNG KẺ CẮT ĐÔI TRANG:** Tuyệt đối không vẽ một đường kẻ ngang dài hết khổ giấy chia cắt poster.
- **CẤM TRƠ TRỌI:** Không để chữ ký đứng lẻ loi một mình không có thông tin đi kèm.

### 3. Vị trí đặt cụm (Cohesive Block Placement):
- Đặt trọn vẹn cả cụm ở **Góc dưới bên phải (Bottom-Right)** hoặc **Góc dưới bên trái (Bottom-Left)**, hoặc **Chính giữa đáy (Bottom-Center)** nhưng cả 4 dòng phải cùng căn chỉnh (căn giữa hoặc căn phải/trái) theo một trục thẳng tắp, tạo thành một chiếc danh thiếp đồ họa cao cấp thu nhỏ, gọn gàng và tinh tế.

## Hierarchy
Typical priority:
1. Hero / primary headline
2. Main supporting message
3. Secondary information
4. Professional identity block
5. Handwritten signature

Signature/identity must never become the focal point unless the user explicitly designs a personal-profile card.

## Text lock
All rendered identity strings must be added to `ALLOWED_TEXT` exactly.
Forbidden:
- invented credentials;
- altered name spelling;
- invented title;
- invented phone;
- fake email/website;
- extra brand claims.

## Logo distinction
The word `Manulife` in the identity block is text, not permission to draw a Manulife logo. Logo remains disabled by default.
