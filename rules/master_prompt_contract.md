# Master Prompt Contract

A final output is valid only when it is **ONE coherent production master prompt** for the requested poster/image.

## Mandatory blocks
The master prompt should contain these sections in one prompt:

1. `ROLE & OBJECTIVE`
2. `CORE MESSAGE`
3. `VISUAL THESIS`
4. `HERO VISUAL`
5. `SUBJECT + ACTION + RELATIONSHIPS`
6. `ENVIRONMENT / SCENE`
7. `VISUAL METAPHOR` when relevant
8. `COMPOSITION & HIERARCHY`
9. `STYLE / VISUAL DNA`
10. `PALETTE / LIGHTING / MATERIAL` as relevant
11. `ON-IMAGE COPY`
12. `TEXT HIERARCHY`
13. `TEXT PLACEMENT`
14. `SIGNATURE SYSTEM`
15. `ALLOWED_TEXT`
16. `NEGATIVE CONSTRAINTS`
17. `TECHNICAL`
18. `ACCURACY LOCK`

Do not split these into separate prompts.

## Nghiêm Cấm Chia Nhỏ Prompt Theo Từng Nền Tảng (No Multi-Platform Split Prompts)
- **TUYỆT ĐỐI KHÔNG** chia nhỏ hoặc xuất thêm mục "Bộ Prompt Tối Ưu Từng Nền Tảng" (Midjourney, FLUX, DALL-E/ChatGPT, Flow...).
- Hệ thống chỉ xuất **DUY NHẤT 1 MASTER PRODUCTION PROMPT TOÀN NĂNG** (đầy đủ 18 khối chuẩn), tương thích trực tiếp cho mọi engine AI mà không cần phải phân mảnh hay cắt xén nội dung.

## Copy is part of the design
The prompt must explicitly state the exact text that should appear inside the artwork.
Include only copy that contributes to the communication goal.

If source content is too long:
- keep the core meaning;
- compress into poster-readable copy;
- use hierarchy instead of paragraphs;
- prefer one strong headline and a small amount of supporting text;
- do not shrink text merely to fit everything.

If the user explicitly provides exact wording and asks to preserve it, preserve it verbatim.

## Subject/action lock
Never describe only a subject noun. Lock the important action and relationships.
Example fields:
- who is present;
- who holds/touches/looks at what;
- what object belongs to or connects to what;
- where a transformation begins and ends;
- what must remain physically continuous.

## Composition rule
One poster should normally have:
- one core message;
- one dominant focal point;
- clear eye path;
- intentional negative space;
- readable text zones.

## ALLOWED_TEXT rule
List every exact rendered string, including Signature System strings.
Then explicitly state:
`Render exactly and only the ALLOWED_TEXT strings. Do not add any other letters, numbers, labels, logos, pseudo-text, watermark, instruction text, or placeholder text.`

Do not place design instructions inside ALLOWED_TEXT.

## Exact Vietnamese text reality
Image models may misspell Vietnamese. The prompt must still request exact text. If the returned render contains text errors, repair via returned-image feedback; do not weaken the intended copy just because the renderer may fail.

## Negative constraints
Use negatives to protect the concept, not to create a huge generic blacklist. Include only likely failure modes for that design plus the core anti-AI constraints.

## Standalone rule
The final master prompt must make sense if copied alone into an image generator. Do not write `same as above`, `use previous style`, or depend on hidden context.
