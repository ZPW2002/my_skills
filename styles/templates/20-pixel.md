# 风格模板：像素风 Pixel Art / 8-bit

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
像素风 Pixel Art / 8-bit

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML Canvas at 320×180 internal resolution, integer-scaled ×6 with nearest-neighbour; sprites authored as pixel arrays in code; limited palette
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「像素冒险 PIXEL QUEST」A retro side-scroller title/attract sequence.
- Internal 320×180, ×6 nearest-neighbour; limited palette (PICO-8-like 16–32 colours) with dithered sky gradient; 3–4 parallax layers (sky, far mountains, mid forest/city, near ground tiles) moving by whole pixels.
- Hero sprite (hand-authored 16×16–24×24, 6–8 frame run cycle at ~10–12 fps) runs, jumps, collects coins (sparkle), bops a slime; the palette shifts day → sunset; a treasure chest opens with a light burst.
- Dialogue box with pixel CJK font typing 「欢迎来到像素世界！」; chunky pixel logo "PIXEL QUEST" drops in with shine sweep; optional CRT pass (scanlines, slight barrel, phosphor glow) that doesn't blur pixels into mush.
- Strictly: nearest-neighbour, integer pixel positions, stepped timing (no smooth easing on sprites).
Sound: chiptune (pulse lead, triangle bass, noise drums) + jump/coin/chest SFX.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
低分辨率大颗粒像素 + 有限色板 + 低帧率精灵动画的复古游戏美学，在 B 站游戏区（MC、泰拉瑞亚、独立游戏）、8-bit 音乐 MV 和品牌怀旧营销中常见；Aseprite 教程在 B 站有 10 万+ 播放的稳定学习生态。
视觉特征 大颗粒像素与硬边缘, 有限色板(8~32色), 8~12fps 精灵帧动画, 抖动渐变 dithering, CRT 扫描线滤镜
关键技法 Aseprite 绘制精灵表（sprite sheet）+ 序列帧循环（走路 6~8 帧、呼吸 2~4 帧）
缩放必须最近邻插值（CSS image-rendering: pixelated），杜绝抗锯齿糊边
动画用 steps() 阶梯时序而非平滑缓动，保持逐帧感
视差卷轴背景：远中近三层不同速度整像素平移
可选 CRT 后处理：扫描线+桶形畸变+磷光辉光
```
