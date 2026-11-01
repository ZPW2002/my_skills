# 风格模板：扁平矢量动画 Flat / Vector 2D Motion Graphics

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
扁平矢量动画 Flat / Vector 2D Motion Graphics

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG + GSAP (CustomEase/CustomBounce/MorphSVG); motion blur mb=4 for fast moves
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「一镜到底的扁平世界」One-continuous-shot brand explainer, the canonical Motion-Ocean/Google-explainer form, pushed to showreel polish.
- 0.0–1.2s HOOK: empty bold color field; a single saturated circle drops in with the three-phase anticipation → stretch → squash → overshoot → settle. Immediately readable craft.
- 1.2–3.0s: the circle becomes the sun; a flat city pops up building-by-building with 2–4 frame stagger (each with its own mini overshoot), clouds slide, birds flap.
- 3.0–5.5s: camera pushes into one window → a geometric character at a desk (limb rig with anchor rotations, head bob, blink) reacts; phone pings.
- 5.5–8.0s: the notification bubble expands to fill the frame as a SHAPE WIPE transition; inside, icons burst in a choreographed rhythm (bar chart grows, check mark draws, heart pops, coin flips).
- 8.0–10.0s: element-driven transition — everything collapses/flies into a logo lockup for an invented brand (e.g. "Popwise") + tagline, elastic settle, 1s hold with micro-motion.
Rules: one hero moves at a time; squash&stretch ~10%; secondary action & follow-through; element-driven transitions (an object flies out and carries the cut); strictly flat (no gradients), bold 5–6 color palette (e.g. ultramarine #2B2BFF, coral #FF5A4E, sunflower #FFC62B, mint #2EE6A8, cream #FFF6E9, ink #151433).
Sound: upbeat future-bass/pop ~120 BPM; pop/boing/whoosh on each entry, synced to the frame.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
MG 动画最主流的基本盘风格，源自 Google Material/企业解释视频（explainer）传统。纯色几何化的人物与场景、无描边或极简描边、大色块撞色，一切元素都是矢量形状。常见于 SaaS 产品宣传、科普解说、企业年报视频。
视觉特征 纯色大色块, 几何化角色, 无渐变或极少渐变, 干净留白, 高饱和品牌色板, 元素弹性入退场
关键技法 AE Shape Layer + 父子级 null 控制层级，人物四肢用锚点旋转做 rig
弹性缓动是灵魂：overshoot 用 cubic-bezier(0.34,1.56,0.64,1) 或 AE 里 70~85% influence 的贝塞尔手柄；入场'预备-冲出-回弹'三段式
元素错峰入场（stagger 2~4 帧），同一时刻只让一个主体动
30fps 居多；位移动画带 10% 左右 squash&stretch 增加弹性
转场常用色块擦除（shape wipe）或元素飞出带动整场切换
```
