# Returned-Image Feedback Loop

Use this only after the user returns an actual generated image.

## Goal
Repair the system at the level that caused the failure, then output one revised full master prompt.

## Audit dimensions
Compare EXPECTED vs OBSERVED on:
- message comprehension;
- focal point;
- visual metaphor;
- subject/action/object relationship;
- composition and eye path;
- text density and hierarchy;
- exact text / spelling;
- style fidelity;
- palette / lighting;
- visual continuity / anatomy / object logic;
- signature system;
- unwanted logos/text/artifacts;
- mobile readability.

## Choose repair mode
### `LOCAL_REPAIR`
Use when the concept is good but execution is wrong.
Examples:
- subject too small;
- text zone crowded;
- wrong camera;
- metaphor connection visually unclear;
- signature too prominent;
- renderer added extra text.

Keep the concept and revise only the necessary specifications, then regenerate a complete master prompt.

### `REBUILD`
Use when the image is technically polished but the underlying idea does not communicate, or the user explicitly rejects the direction.
Rebuild hero visual / metaphor / composition / style as needed.

## Visible response format
Keep diagnosis concise:
- `Lỗi chính:` max 3 high-impact issues.
- `Nguyên nhân prompt:` the likely specification gap.
- `Hướng sửa:` LOCAL_REPAIR or REBUILD.
- Then output **ONE revised complete master prompt**.

Do not output multiple repair prompts.
Do not claim success before a new render is returned.

## Failure → Rule
If the same failure repeats, suggest a candidate reusable rule. Do not auto-promote it globally without testing/approval.
