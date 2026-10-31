---
name: douyin-identity-cover
description: Create or revise Douyin covers from one real-person identity photo, generating coherent new camera angles, poses, clothing, and topic-specific product evidence while preserving identity and a verified 9:16-to-3:4-safe layout. Use for presenter-led Chinese Douyin cover requests; do not use for Xiaohongshu covers or generic posters without a presenter.
---

# Douyin Identity Cover

Turn one supplied portrait into a repeatable presenter identity system, not a pasted-face template. Preserve who the person is while rebuilding the whole visible body for each cover.

## Inputs

Require:

- one clear identity-master photo supplied or explicitly selected by the user;
- the exact cover title;
- a topic, product, interface, or result that the cover must visibly prove.

If the user has not supplied the identity photo, ask for it. If no product image exists, create one plausible visual anchor from the topic, but do not present invented UI or metrics as a real screenshot.

## Workflow

1. Inspect the identity master before generation. Treat facial identity as the invariant; do not copy its original head angle into every cover.
2. Read [references/identity-and-pose.md](references/identity-and-pose.md) before choosing a new pose, camera angle, expression, clothing, or gesture.
3. Read [references/douyin-cover-spec.md](references/douyin-cover-spec.md) before composing the title and product evidence.
4. Choose one clear action that explains the topic. Define the torso direction first, then derive shoulder line, neck, head rotation, gaze, jaw, and hand action from it.
5. Generate a fresh coherent upper body with the built-in image-generation tool. Include the identity master and any real product/background evidence as separate references. Use [references/prompt-template.md](references/prompt-template.md) as a checklist, not as text to copy blindly.
6. Validate in this order:
   - face-neck-shoulder anatomy and hand integrity;
   - recognizable identity without waxy beautification or identity drift;
   - exact Chinese title with no missing, duplicated, or substituted characters;
   - visible product/result evidence relevant to the title;
   - centered 3:4 crop safety.
7. If anatomy is wrong, discard that generation and regenerate from the original identity master plus evidence. Do not repair a pasted face or twisted neck by repeatedly editing the broken image.
8. Normalize the accepted image with `scripts/prepare_cover.py`, then visually inspect both the 9:16 master and 3:4 preview before delivery.

## Output contract

Deliver both:

- `1080x1920` 9:16 PNG master;
- `1080x1440` centered 3:4 crop preview.

Keep the exact title, complete face, meaningful gesture, and primary evidence inside the preview. State which image is the master and which is the crop check.

## Revision discipline

When the user requests a targeted revision, change only the named variable unless the existing anatomy fails. A title change must not silently change identity, clothing, pose, or evidence. An anatomy failure permits a full pose regeneration because local face replacement would preserve the defect.

## Diversity across a series

When prior covers are available, vary at least three of these between adjacent covers: camera angle, torso direction, gesture, clothing silhouette, expression, prop, background depth, and evidence placement. Keep the face recognizable, but do not repeat the same frontal crop and pointing pose by default.
