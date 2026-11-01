# 风格模板：液态流动 Liquid Motion

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
液态流动 Liquid Motion

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML WebGL2 fragment shader: 2D SDF metaballs (smooth-min) + fake 3D lighting from field gradient normals, text SDF for the logo
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「液态创世」Liquid logo genesis — glossy, organic, high energy.
- Deep plum ground; glossy candy liquid (hot orange → pink → violet) with specular highlights and fresnel rim so it reads like thick 3D liquid, not flat blobs.
- 0–2s: droplets fall and splash with squash on landing; 2–4s: blobs merge via metaball fusion — stretched necks, snap, 2–3 frame rebound; secondary droplets follow 2–3 frames late;
- 4–6s: a big liquid wave floods across the frame as a transition (wavy front with 3–5 phase-offset bulges);
- 6–8.5s: the liquid coalesces into a wordmark (e.g. "FLUX") — text SDF blended with the metaballs;
- 8.5–10s: a last drip falls from the logo and ripples; hold.
Ease: flung, never uniform (cubic-bezier(0.22,1,0.36,1)).
Sound: bubbly gloops, pour, splash, drip, deep bass swell under a glossy synth bed.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
图形像液体一样流动、拉丝、滴落、融合：转场是一泼颜料漫过屏幕，logo 从一滴液体聚合成形。有机、解压、高能量，广泛用于音乐视频、食品饮料广告和转场包装。
视觉特征 波浪边缘转场, 拉丝与滴落, metaball融合, 次级液滴跟随, 有机曲线永不直线
关键技法 液态转场：遮罩路径手 K 波浪形前沿扫过画面，前沿加 3~5 个错相位的凸起
metaball 融合的通用伪造法：高斯模糊(20px+) → 提高对比度阈值（AE 用 Levels 收紧、Web 用 feColorMatrix alpha 阈值），两球靠近即自动'粘连'
拉丝-断裂-回弹：主形离开时留一条细颈，断裂瞬间两端各回弹 2~3 帧
缓动前快后慢 cubic-bezier(0.22,1,0.36,1)，液体只会被'甩'出去不会匀速
次级液滴延迟主体 2~3 帧跟随（follow-through），落地做扁平化 squash
```
