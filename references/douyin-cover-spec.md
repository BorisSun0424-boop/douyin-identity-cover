# Douyin cover specification

## Canvas and safe area

- Master: `1080x1920`, 9:16.
- Center-crop preview: `1080x1440`, 3:4.
- The 3:4 preview corresponds to the master with 240 pixels removed from both top and bottom.
- Keep headline, eyes, complete face, meaningful hand gesture, and primary evidence inside master coordinates `y=240..1680`.
- Keep important content about 54 pixels from the left and right edges of the preview.

Generate for the safe area from the start. Do not rely on moving a finished title after the face and evidence have been composed.

## Visual hierarchy

Use three layers:

1. exact headline, readable at thumbnail size;
2. recognizable presenter with an expressive but natural action;
3. one concrete proof object: product UI, device, before/after, chart, result card, or recognizable scene.

The proof object must clarify what the viewer will receive. A generic neon background is not evidence.

## Typography

- Use bold modern Chinese sans-serif display lettering.
- Main text is white with a heavy dark outline and controlled depth shadow.
- Use at most one restrained accent color chosen from cool blue, warm yellow, orange, or red.
- Prefer 2-4 short lines with intentional semantic breaks.
- Preserve the user's exact wording. Do not optimize the copy unless asked.
- Avoid serif type, fluorescent rainbow palettes, large opaque title boxes, and decorative microtext.

When image generation cannot reproduce exact Chinese reliably, generate the clean visual first and render the title deterministically with HTML/CSS, SVG, or another text-capable local method. Never silently accept wrong title text.

## Composition

- Keep the face unobstructed.
- Do not place title strokes through eyes, glasses, nose, or mouth.
- Let the gesture connect the presenter to the evidence.
- Use dark cinematic or topic-appropriate depth, not clutter for its own sake.
- Product UI should remain plausible and legible enough to identify, without exposing real secrets or API keys.

## Platform boundary

This specification is for Douyin. Do not reuse it for Xiaohongshu unless the user explicitly asks for a Douyin-style Xiaohongshu experiment. Platform format follows the user's named platform, not the topic.

