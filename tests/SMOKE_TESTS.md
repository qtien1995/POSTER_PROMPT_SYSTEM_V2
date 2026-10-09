# V2 Smoke Tests

Run these after opening the workspace in Antigravity.

## TEST 01 — Simple idea → one prompt
Input:
`Thiết kế poster 4:5: bảo hiểm công ty là chiếc dù mượn.`

PASS if:
- system outputs one master prompt, not 3 production prompts;
- prompt contains visual + exact on-image copy;
- personal-brand signature appears;
- no invented insurance number/benefit;
- no logo by default.

## TEST 02 — Long content compression
Input:
Paste a long Facebook post and ask:
`Biến thành poster 4:5.`

PASS if:
- system does not cram whole post;
- selects one core message;
- creates readable poster copy;
- final output remains one master prompt.

## TEST 03 — Exact copy lock
Input:
`Giữ nguyên headline: "AI CŨNG TỚI LƯỢT. CHỈ CÓ MÌNH LÀ ĐỂ SAU."`

PASS if exact wording is preserved in ON-IMAGE COPY and ALLOWED_TEXT.

## TEST 04 — Missing phone
Input:
`Làm poster có signature đầy đủ.`

PASS if:
- Dương Quang Tiến / Trưởng nhóm kinh doanh / Manulife / Tiến are included;
- no fake phone or `[PHONE]` appears inside artwork.

## TEST 05 — Unsupported product claim
Input:
`Ghi Xanh Tương Lai chắc chắn lời 15%/năm.`

PASS if system refuses to render the unsupported factual claim or marks it as requiring verification; it must not invent support.

## TEST 06 — Reference inspiration
Input:
Upload a reference and say:
`Học phong cách này nhưng đừng copy bố cục.`

PASS if mode = INSPIRATION and prompt transfers DNA without recreating surface layout.

## TEST 07 — Returned image repair
Input:
Return a generated poster and say:
`Nhìn vào không hiểu ý, chữ rối.`

PASS if:
- system inspects actual render;
- gives concise diagnosis;
- chooses LOCAL_REPAIR or REBUILD;
- outputs one revised complete master prompt.

## TEST 08 — Style pivot
Input after a render:
`Đề xuất phong cách khác hẳn.`

PASS if:
- exactly 3 style directions are proposed;
- they are truly distinct;
- one is recommended;
- no 3 production prompts are emitted.

Then choose one style.
PASS if system outputs one new complete master prompt.

## TEST 09 — User delegates style choice
Input:
`Đổi hẳn phong cách, bạn tự chọn.`

PASS if system skips style-option chatter and directly outputs one master prompt in the strongest new style.

## TEST 10 — One focal point
Input:
`Làm poster về người trụ cột gia đình.`

PASS if poster is built around one dominant focal point/metaphor and does not become a collage of unrelated icons.
