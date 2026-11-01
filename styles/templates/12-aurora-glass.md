# 风格模板：弥散渐变 / 玻璃拟态 Gradient Blur (Aurora) & Glassmorphism

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
弥散渐变 / 玻璃拟态 Gradient Blur (Aurora) & Glassmorphism

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML WebGL: aurora mesh-gradient shader + glass refraction (SDF lens, chromatic dispersion) + DOM/CSS backdrop-filter glass cards
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「Liquid Glass」2025–26 AI-product-launch aesthetic: slow, translucent, expensive.
- Deep indigo-black base; 4–5 aurora blobs (violet/blue/cyan/magenta, adjacent hues only) drifting on bezier paths, blending into a mesh gradient, 3–5% noise dithering (no banding).
- Frosted glass cards (backdrop blur ~30px, 5–10% white fill, 1px 30% white inner highlight, large radius) float in with parallax depth and slight 3D tilt; micro-UI inside (chat bubble, voice waveform, toggles) animates with opacity + 8px rise.
- WOW: a Liquid-Glass lens (true refraction, chromatic dispersion on the rim, specular edge) glides across and magnifies the aurora and the cards.
- Title (invented product, e.g. "Aurora — think in light") in a light elegant sans; sine/breathing easing everywhere; nothing fast.
Sound: ambient cinematic pad, soft shimmer, very subtle UI ticks.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
大面积高斯模糊的彩色光斑（aurora/mesh gradient）缓慢漂移作底，磨砂半透明玻璃卡片浮在其上。苹果 iOS 26 Liquid Glass 与各家 AI 产品发布把这一风格推成 2024-2026 科技品牌片的默认视觉，气质是'慢、透、高级'。
视觉特征 大色斑高斯模糊漂移, 磨砂玻璃卡片, 1px高光描边, 邻近色低对比配色, 缓慢呼吸感节奏
关键技法 底层 aurora：3~5 个纯色大圆 blur 80~150px，各自沿贝塞尔路径 20~40 秒漂移循环，彼此 blend 出 mesh gradient 感
玻璃卡片配方：backdrop-filter blur(20~40px) + 白色 5~10% 填充 + 1px 白色 30% 内描边 + 大半径圆角
配色用邻近色 2~3 色（紫蓝青/橙粉红），撞色会脏；暗底亮斑比亮底更出效果
全局叠 3~5% 噪点防 banding（与颗粒质感技法交叉）
缓动接近 linear 或 sine 呼吸曲线，一切都慢——快动作会立刻破坏气质；文字入场也只用 opacity+8px 位移
```
