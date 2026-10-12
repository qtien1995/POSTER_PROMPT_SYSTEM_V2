# Changelog

## V3.1 (prompts.chat Integration & Community Intelligence Engine)
- **Tích Hợp Kho Tri Thức prompts.chat (2,435 Prompts):** Tải và lập chỉ mục toàn bộ cơ sở dữ liệu từ [prompts.chat - AI Prompts Community](https://prompts.chat/) (173k+ Stars, CC0 1.0 Universal) lưu trữ ngoại tuyến tại [`library/prompts_chat/prompts_community.json`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/prompts_community.json) và [`library/prompts_chat/prompts.csv`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/prompts.csv).
- **Bộ Công Cụ CLI prompts.chat Tool:** Xây dựng [`scripts/prompts_chat_tool.py`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/scripts/prompts_chat_tool.py) hỗ trợ lệnh `stats`, `search`, `show`, `adapt` (tự động biên dịch mọi prompt cộng đồng sang chuẩn Master Prompt 18 khối), và `list-curated`.
- **Cẩm Nang Sáng Tạo Tinh Tuyển:** Biên soạn [`library/prompts_chat/CURATED_CREATIVE_PROMPTS.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/prompts_chat/CURATED_CREATIVE_PROMPTS.md) phân loại 20+ prompt có giá trị ứng dụng cao nhất về poster đồ họa, copywriting, prompt engineering và nhiếp ảnh.
- **Hệ Thống Kiểm Soát Điểm Rơi Thị Giác & Eye-Flow:** Kế thừa từ prompt `Predictive Eye Tracking Heatmap Generator`, ban hành [`rules/visual_hierarchy_eyeflow.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/visual_hierarchy_eyeflow.md) áp dụng nguyên tắc Nielsen Norman Group & Gestalt, đo lường nhiệt độ chú ý và quỹ đạo Z-pattern.
- **Bộ 10 Công Thức Tiêu Đề Đột Phá:** Kế thừa từ prompt `Landing page copywriting` & `Advertiser`, ban hành [`rules/headline_copywriting_formulas.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/headline_copywriting_formulas.md) chuẩn hóa tiêu đề poster BHNT/tài chính.
- **Bộ Lọc Khử Nhiễu Token AI (Anti-Visual-Noise Filter):** Tích hợp kỹ thuật loại bỏ rác ký tự (░, ═, │, ###, bracket thừa) vào [`rules/qa_completeness_gate.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/qa_completeness_gate.md) và [`rules/master_prompt_contract.md`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/rules/master_prompt_contract.md).
- **Bổ Sung 3 Phong Cách Nghệ Thuật Mới:**
  - [`STYLE_024_ART_DECO_VINTAGE_TRAVEL_POSTER`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_024_ART_DECO_VINTAGE_TRAVEL_POSTER.md)
  - [`STYLE_025_EXPLODED_VIEW_TECHNICAL_INFOGRAPHIC`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_025_EXPLODED_VIEW_TECHNICAL_INFOGRAPHIC.md)
  - [`STYLE_026_WHIMSICAL_3D_ISOMETRIC_MINIATURE_DIORAMA`](file:///d:/AI/POSTER_PROMPT_SYSTEM_V2/library/styles/STYLE_026_WHIMSICAL_3D_ISOMETRIC_MINIATURE_DIORAMA.md)
- **Thiết Lập Chế Độ Vận Hành Mặc Định PROMPT_ONLY:** Điều chỉnh luồng sản xuất mặc định: Thảo luận, chốt nội dung, phong cách và chọn phương án (PA) $\rightarrow$ Viết DUY NHẤT 1 Master Production Prompt 18 khối để người dùng tự kiểm thử. Chỉ kích hoạt công cụ `generate_image` khi người dùng có yêu cầu tạo ảnh rõ ràng.

## V3.0 (Master Release & Full System Optimization)
- **Hợp Nhất Phong Cách & Triệt Tiêu Trùng Lặp:** Loại bỏ hoàn toàn file nhân bản vô ích (`STYLE_010`), tích hợp sâu 6 tầng Visual DNA từ `library/dna/` vào từng thẻ phong cách chính thức trong `library/styles/` (`STYLE_009`, `STYLE_017`, `STYLE_018`, `STYLE_019`, `STYLE_020`, `STYLE_021`, `STYLE_022`, và bổ sung `STYLE_023`). Quy hoạch rõ ràng: `library/dna/` là nơi tiếp nhận bản trích xuất thô khi có ảnh tham chiếu mới.
- **Quy Hoạch & Dọn Sạch Thư Mục `jobs/`:** Di chuyển toàn bộ file benchmark, catalog cũ, omnibus prompt và dataset (`14_VISUAL_PATTERNS`, `17_CORE_STYLES`, `ART_CENTRIC_TEST_PROMPTS`, `BENCHMARK_11_PILLARS`, `OMNIBUS_MASTER_PROMPT...`) ra khỏi thư mục gốc `jobs/` sang `library/archive/` và `tests/`. Chuẩn hóa dự án `song_khoe_moi_ngay_2024` về 1 tệp `MASTER_PROMPT.md` hoàn chỉnh kèm `brief.md` và `state.yaml`.
- **Đồng Bộ Luồng Vận Hành One-Best-Direction:** Khóa chặt quy tắc mặc định tự động chọn 1 hướng thiết kế mạnh nhất để ra sản phẩm hoàn thiện ngay (ảnh + master prompt), tối ưu tốc độ, triệt tiêu việc bắt duyệt 3 concept qua lại; chỉ kích hoạt đề xuất 3 styles khi người dùng yêu cầu rõ ràng.
- **Đồng Bộ Typography & Cụm Chữ Ký Chuẩn:** Thống nhất toàn diện 11 công thức phối font giữa `rules/typography_system.md` và `MASTER_FONT_CATALOG.md`. Chuẩn hóa sơ đồ chữ ký khối 4 tầng thống nhất (`The 4-Tier Cohesive Stack`), nghiêm cấm đường kẻ ngang chia cắt trang.
- **Ánh Xạ Tỷ Lệ Ảnh Thông Minh:** Bổ sung cơ chế tự động ánh xạ tỷ lệ `4:5` sang `'3:4'` khi gọi công cụ `generate_image` để tương thích hoàn hảo với API engine, đồng thời giữ nguyên `4:5` trong prompt ngoài cho Midjourney / FLUX.
- **Tái Tạo MANIFEST.txt Toàn Diện:** Cập nhật lại toàn bộ danh mục tài nguyên thực tế trong toàn bộ không gian làm việc.

## V2.6 (System Streamlining & 10 Master Design Pillars Consolidation)
- **10 Master Design Pillars:** Rà soát và tinh tuyển toàn diện từ 19 phong cách phân mảnh xuống **10 Trụ Cột Thiết Kế Tinh Tuyển** ([MASTER_10_STYLES_CATALOG.md](file:///d:/POSTER_PROMPT_SYSTEM_V2/library/styles/MASTER_10_STYLES_CATALOG.md)), loại bỏ 100% sự trùng lặp và phân tán.
- **Vietnamese Heritage & Royal Art Pillar (Pillar 09):** Nâng cấp toàn diện với 5 tuyệt phẩm văn hóa truyền thống Việt Nam: Phù điêu gỗ lụa đỏ satin, Tranh cắt giấy dân gian Âm Sắc, Tranh huyền tích Thần Thoại, Thơ trăng Thăng Long viên mãn, Khắc kim hoàng gia Cải Lương ([DNA_VIETNAMESE_HERITAGE_COLLECTION.md](file:///d:/POSTER_PROMPT_SYSTEM_V2/library/dna/DNA_VIETNAMESE_HERITAGE_COLLECTION.md)).
- **Lifestyle Ecosystem Infographic Pillar (Pillar 10):** Chuẩn hóa mô hình đô thị thông minh 5 phút & vòng tròn tiện ích sống gia đình từ ảnh mẫu FIATO Airport City ([DNA_019_LIFESTYLE_ECOSYSTEM_INFOGRAPHIC.md](file:///d:/POSTER_PROMPT_SYSTEM_V2/library/dna/DNA_019_LIFESTYLE_ECOSYSTEM_INFOGRAPHIC.md)).
- **Strict Prohibition on Multi-Platform Prompts:** Khóa chặt nguyên tắc chỉ xuất duy nhất 1 Master Production Prompt toàn năng, nghiêm cấm phân mảnh prompt theo từng nền tảng.
- **Style Router Synchronization:** Đồng bộ hóa bộ định tuyến phong cách (`rules/style_router.md`) bám sát chuẩn 10 Master Pillars.

## V2.5 (Comprehensive Upgrade — Direct Image Generation & 99% Visual DNA Cloning)
- **Direct Image Generation Engine:** Integrated `generate_image` tool directly into the production workflow, allowing immediate image generation alongside master prompts.
- **Tri-Mode Operational Switch:** Added `HYBRID` (generate image + prompt), `DIRECT_IMAGE` (image only), and `PROMPT_ONLY` (prompt only).
- **99% Visual DNA Cloning & Transfer Engine:** Added deep 6-layer reverse-engineering (Composition, Lighting, Color science, Materiality/Shaders, Optics, Integrated Typography) to clone 99% aesthetic fidelity from any reference image.
- **OpenAI ChatGPT Images 2.5 Benchmark:** Enforced integrated graphic design and typography architecture—rendering on-image headlines, subheads, metric tags, and advisor signature with crisp editorial graphic quality.
- **Advisor Signature & Identity Integration:** Locked official identity from source document: `Dương Quang Tiến`, `Trưởng nhóm kinh doanh`, `Manulife`, phone `0935 074 268`, handwritten signature `"Tiến"`.
- **Complete Style & Pattern Expansion:** Expanded from 10 to 16 core Style Families and 13 Visual Patterns from Master Core v1.2.
- **Full Insurance Compliance & Accuracy Engine:** Added rigorous Fact Lock, Guaranteed vs Illustrative classification, Headline Safety, and Soft CTA rules.
- **Platform Adapters:** Added platform-specific directives for ChatGPT Images 2.5, FLUX.1 Pro, Midjourney v6/v7, and Google Flow / Imagen 3.
- **Completeness & Artifact QA Gate:** Formalized 7-point completeness checklist, mobile thumbnail 3-second test, and anti-AI artifact detection.

## V2.0
- Replaced default 3-concept + approval workflow with direct one-best-direction workflow.
- Final output is one complete master prompt by default.
- Made on-image copy mandatory in final poster prompt.
- Added exact ALLOWED_TEXT whitelist contract.
- Rebuilt Signature System with handwritten mark + professional identity + optional confirmed contact.
- Added returned-image repair loop with LOCAL_REPAIR vs REBUILD.
- Added explicit style-pivot flow: 3 style proposals, then one master prompt.
- Distilled reference DNA and fact-lock rules into active lightweight modules.
- Added smoke-test suite for Antigravity.
