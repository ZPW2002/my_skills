# 风格模板：赛博朋克 HUD / FUI Cyberpunk HUD / FUI (Fictional UI)

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
赛博朋克 HUD / FUI Cyberpunk HUD / FUI (Fictional UI)

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG/Canvas FUI layers + Three.js wireframe hologram; seeded random data; glow/scanline post pass
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「目标锁定 TARGET ACQUIRED」Cyberpunk HUD / FUI, film-UI grade (Territory Studio-level density & restraint).
- Deep teal-black; cyan #00E5FF linework with orange/red #FF6A00 alert state; hex grid, concentric rotating rings with ticks, radar sweep (conic) with blips, data columns (monospace numbers rolling 3–5 frames then settling), typewriter status lines with cursor, sparkline graphs, a central Three.js wireframe hologram (globe or drone) with scanlines.
- Layered build-up: lines draw on in hierarchical staggered order → data comes alive → a target is found → lock brackets snap 1.4 → 1.0 (fast-out slow-in) → everything flips to alert orange with 'TARGET LOCKED / 目标锁定', coordinates "N31°14′ E121°29′".
- Glow, slight chromatic aberration, scanlines, restrained micro-glitches.
Sound: darksynth pulse + HUD beeps, scan sweeps, ascending lock-on tone, alarm on lock.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
模拟科幻电影/游戏界面的抬头显示包装：青橙霓虹线框、目标锁定框、雷达扫描、数据流小字。在科技数码测评、游戏剪辑（赛博朋克2077、EVA 二创）、军事航天科普和 AI 产品演示中作为『科技感』的默认皮肤，B 站 AE HUD 案例教程播放量达 20 万。
视觉特征 青色/橙色霓虹线框, 目标锁定框与十字准星, 雷达/环形扫描 loop, 等宽小字数据流与打字机文字, 六边形网格与辉光
关键技法 线框生长：SVG stroke-dasharray/dashoffset 描边动画，元素按层级错帧展开
环形雷达：conic-gradient 扫描扇区旋转 loop + 目标点闪烁
数字滚动：随机数快速跳变 3~5 帧后落定真实值；文字打字机 + 光标闪烁
锁定框：四角括号从大到小收缩吸附目标（scale 1.4→1.0 + 快出缓入）
全局外发光（glow）+ 轻微色差 + 扫描线叠加统一质感
```
