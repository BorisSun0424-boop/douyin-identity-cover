# Image-generation prompt checklist

Use this checklist to write a task-specific prompt. Replace every bracketed field.

## Identity

> Use reference image 1 as the identity master for the same real person. Preserve [face shape / glasses / hairstyle / distinguishing features], but do not preserve the source head angle. Rebuild the complete visible upper body for the new pose; no pasted face, no face swap seam, no identity beautification.

## Coherent action

> Camera is [eye level / slightly low / slightly high]. Torso turns [direction and approximate amount]. Shoulders, neck, head, jaw, and gaze follow the same action. Head turns only [amount] relative to torso. [Hand] performs [specific action] toward [specific evidence]. The other hand [natural resting action]. Hands and neck are anatomically normal.

## Variation

> Clothing is [specific new outfit]. This cover must differ from the previous cover in [camera angle, gesture, clothing, evidence placement]. Keep the same identity, not the same pose.

## Evidence

> Reference image 2 is [real product/background evidence]. Preserve its recognizable structure and place it [location]. Show [one specific control, result, or artifact] clearly. Do not invent claims, numbers, or logos that are not supported.

## Exact title

> Render exactly these lines with no substitutions, omissions, or extra words:
> [line 1]
> [line 2]
> [line 3]

> Use bold Chinese sans-serif, white with dark outline; emphasize only [keyword] in [accent]. Keep it inside the centered 3:4 safe area and off the face.

## Output and negatives

> 9:16 vertical Douyin cover. All key content remains visible after centered 3:4 crop. No watermark, bottom captions, platform chrome, extra readable labels, twisted neck, mismatched head and torso, distorted glasses, fused fingers, duplicated limbs, or two unrelated devices.

## Revision rule

If the first result fails anatomy, start again from the identity master and evidence with a simpler pose. If only text fails, preserve the accepted visual and replace text with a deterministic renderer.

