# FINAL MASTER PROMPT TEMPLATE

Use this as the **single production output**. Do not split into mini-prompts.

```text
ROLE & OBJECTIVE
Create a [asset type] for [platform/use]. The purpose is [objective]. The poster must communicate one clear idea immediately and remain readable on mobile.

CORE MESSAGE
The single message the viewer should understand is:
"[core message]"

VISUAL THESIS
Before reading the supporting text, the viewer should visually understand that [visual meaning].

HERO VISUAL
[Describe the one dominant visual anchor in concrete terms.]

SUBJECT + ACTION + RELATIONSHIPS
[Who/what appears, what each subject is doing, and exactly how important objects/people connect or interact. Lock continuity and ownership/connection where needed.]

ENVIRONMENT / SCENE
[Describe only the environment details that support the message.]

VISUAL METAPHOR
[Explain the metaphor and what each key element represents. Omit this block if the design is intentionally non-metaphorical.]

COMPOSITION & HIERARCHY
[Aspect-ratio-aware layout. State hero position/scale, text zones, negative space, eye path, depth, and what must remain visually dominant.]

STYLE / VISUAL DNA
[One chosen style family, rendering approach, typography mood, shapes/line quality, realism level, and anti-copy intent if a reference is used.]

PALETTE / LIGHTING / MATERIAL
[Specify only what materially affects the result: dominant colors, accent logic, lighting direction/contrast, textures/materials.]

ON-IMAGE COPY
Render the following Vietnamese text exactly as written.

Headline:
"[exact headline]"

Subheadline:
"[exact subheadline if used]"

Supporting copy:
"[exact supporting line 1]"
"[exact supporting line 2]"
[Add only necessary lines.]

CTA / labels:
"[exact text only if needed]"

Professional identity block:
"[exact full name if active]"
"[exact title if active]"
"[exact organization if active]"
"[confirmed phone only if contact mode is active]"

Handwritten signature:
"Tiến"

TEXT HIERARCHY
- [Define headline as primary or define hero vs headline dominance.]
- [Define subheadline/support sizes relative to headline.]
- Professional identity block is small and secondary.
- Handwritten "Tiến" is subtle and does not compete with the message.

TEXT PLACEMENT
[Specify safe text zones and relationship to hero. Preserve negative space. Do not place important text over busy/high-contrast visual areas.]

SIGNATURE SYSTEM
Use [minimal / personal_brand / contact] mode.
Integrate the handwritten "Tiến" naturally into safe negative space. It must be legible, understated, and composition-aware—not a large watermark.
[Describe identity-block placement if active.]

ALLOWED_TEXT — RENDER EXACTLY AND ONLY THESE STRINGS
- "[headline]"
- "[subheadline if used]"
- "[support line 1]"
- "[support line 2]"
- "[CTA/labels if used]"
- "[full name if active]"
- "[title if active]"
- "[organization if active]"
- "[confirmed phone if active]"
- "Tiến"

Render exactly and only the ALLOWED_TEXT strings. Do not add any other letters, numbers, pseudo-text, labels, captions, UI text, instruction text, placeholder text, watermark, fake website, fake phone number, or unauthorized logo.

NEGATIVE CONSTRAINTS
- [Concept-specific failure to avoid]
- [Composition-specific failure to avoid]
- No generic AI-finance clichés unless the concept explicitly requires them.
- No clutter competing with the focal point.
- No unauthorized brand logo.
- No extra rendered text.

TECHNICAL
Aspect ratio: [ratio].
Output intent: [platform].
Prioritize clear mobile readability, clean edges, coherent anatomy/object relationships, strong focal hierarchy, and production-quality finish.

ACCURACY LOCK
Do not invent insurance benefits, financial values, rates, conditions, medical claims, legal claims, product features, contact data, or credentials. Render only facts and copy supplied or verified in the brief/source of truth. Preserve the exact Vietnamese copy above.
```
