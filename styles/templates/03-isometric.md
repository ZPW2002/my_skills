# 风格模板：等轴 2.5D Isometric / 2.5D

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
等轴 2.5D Isometric / 2.5D

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: Three.js OrthographicCamera at true isometric angle + soft shadows + AO (three/addons postprocessing), or SVG with SSR matrix faces
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「微缩智慧城」An isometric miniature city / data campus that builds itself — the School-of-Motion isometric mograph showpiece.
- True isometric camera (orthographic, 35.264° elevation, 45° azimuth), no perspective, pastel studio palette (lavender ground, mint, peach, sky blue, white) with soft shadows + ambient occlusion so it reads like a premium Dribbble/Behance hero.
- 0–2s: ground tiles flip/drop in as a wave from the centre (tiny bounce each);
- 2–5s: buildings GROW — base lands, walls scaleY from 0 with overshoot, roof caps 2–3 frames later; trees pop; windows light up in sequence;
- 5–8s: life — cars loop along roads, a little train, drones carrying packets, glowing data streams pulse between buildings, a wind turbine spins; camera does parallel slides (no rotation) with 1 : 0.8 : 0.6 parallax layers (foreground clouds);
- 8–10s: pull back to reveal the whole island floating in a pastel void; title card set ON the isometric plane (text skewed into iso space) e.g. "SMART CITY OS".
Sound: bright plucky tech melody (FM marimba/pluck), soft clicks/pops for every tile/building landing, airy whoosh on the pull-back.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
以 30° 等轴测投影展示微缩世界：小城市、办公室切片、数据机房，无灭点、处处等比。信息密度高又不失可爱，是科技公司架构图动画和 App 功能演示的标配。School of Motion 有专门的 isometric mograph 教程系列。
视觉特征 30°等角投影, 无透视灭点, 微缩场景, 楼房生长动画, 平行滑轨式运镜
关键技法 SSR 公式造等轴面：Scale 纵向 86.6% → Shear/skew ±30° → Rotate ∓30°，三个面分别做后拼合
假 3D 靠图层排序：Z 序=画面 y 坐标，物体沿等轴网格移动时保持 2:1 像素斜率
楼房'生长'：底面先落位，立面用 scaleY 从 0 拉起 + 顶面延迟 2~3 帧盖上
运镜是整组平移（无旋转），配合前中后景 1:0.8:0.6 的视差速度
AE 里可用真 3D 图层+正交相机（无透视）偷懒，Motion Design School 的 Isometric Camera 技巧即此路
```
