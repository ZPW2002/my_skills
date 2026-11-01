# 风格模板：几何构成 / 包豪斯 Geometric / Bauhaus Motion

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
几何构成 / 包豪斯 Geometric / Bauhaus Motion

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG/Canvas + GSAP on a strict modular grid, beat grid at 120 BPM
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「包豪斯动态海报」Bauhaus 1919 kinetic poster — mechanical, rational, musical.
- Cream paper (#F1E9DA), primaries red #E03C31, yellow #F2B705, blue #1E4FA3, black #111; strict modular grid (e.g. 240px modules); every move is an integer number of modules; every landing on a grid line.
- 120 BPM (0.5 s/beat): each beat a module acts — quarter circles rotate 90° about a corner pivot, semicircles slide one module, triangles flip, squares split; rotation pivots alternate (own centre / corner / frame centre).
- 0–2s grid lines draw & the first red circle lands; 2–6s the composition assembles into a Kandinsky/Bauhaus poster; 6–8s phase-shifted cascade wave across the grid on the drop; 8–10s freeze into a perfect poster with Swiss typography: "BAUHAUS" set vertically in heavy geometric sans + small caps "FORM · FARBE · FUNKTION".
- Easing: power2.inOut or linear — NO overshoot; subtle paper tooth + slight print misregistration allowed.
Sound: minimal techno/click — each flip = a pitched click/blip, kick on quarters.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
圆、三角、矩形在严格网格上做精确的平移、旋转、缩放，三原色+黑白的限定色板，机械理性的秩序美。源自包豪斯与瑞士国际主义平面传统（Adobe 曾与 Bauhaus 档案馆合作 Hidden Treasures 项目），也是动态海报（kinetic poster）的主流语言，与音乐节拍天然合拍。
视觉特征 基础几何形, 红黄蓝黑限定色, 严格网格对齐, 旋转以几何中心为轴, 节拍驱动的模块化运动
关键技法 一切运动锚定网格：位移距离=网格模数整数倍，落点必在网格线上
缓动克制：easeInOutQuad 或干脆匀速，禁用 overshoot——机械感是特征不是缺陷
节拍驱动：每个几何元素在节拍点瞬时出现/翻转，一拍一个动作，类似我们已做的卡点逻辑
旋转轴心玩法：绕自身中心、绕边缘顶点、绕画面中心三种交替制造韵律
生成式变体：Processing/p5.js 用三角函数相位差批量驱动几何阵列（国内动态海报圈主流做法）
```
