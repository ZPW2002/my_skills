# 风格模板：逐帧手绘 / 线条沸腾 Cel Animation / Frame-by-Frame & Line Boil

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
逐帧手绘 / 线条沸腾 Cel Animation / Frame-by-Frame & Line Boil

# Output (fixed)
- 1920×1080, 24 fps, exactly 10.000 s (240 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML Canvas2D: custom variable-width brush renderer (centreline + pressure → outline polygon), boil = 3–4 jitter variants cycled every 2 frames; paper texture multiply
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「手作魔法」Hand-made frame-by-frame magic, Buck/Giant-Ant hybrid (clean shapes + hand-drawn cel FX), animated on 2s at 24 fps.
- Warm paper ground; ink linework that BOILS (lines redrawn with slight variation every 2 frames); fills slightly off-register like hand colouring.
- Story: a matchstick strikes (SMEAR frame, on 1s for the fast action) → a flame spirit character jumps out, anticipation + squash, dances (on 2s) → it bursts into cel FX: smoke puffs curling, sparks, star bursts, speed lines → the FX re-form into hand-lettered title (e.g. "HAND MADE" or 手作) that keeps boiling on a 1s hold (on 3s for the hold).
- Palette 3–4 colours: ink black, tomato red, sunny yellow, cream paper; paper grain multiply 10–15%.
Sound: playful jazzy pizzicato/xylophone bed + cartoon SFX: strike, fwoosh, pop, poof, sparkle — synced to the frame.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
手绘逐帧或在矢量动画上叠加逐帧质感，标志性特征是 line boil——线条每隔几帧轻微抖动，仿佛画面在'呼吸'。Giant Ant、Buck 等工作室大量使用 cel 元素（烟、水花、速度线）点缀主动画，反数字精致感的核心手段。
视觉特征 线条持续微抖(boil), 一拍二/一拍三节奏, smear拖影帧, 手绘烟火水花点缀, 纸纹底
关键技法 打帧节奏：24fps 下'一拍二'（实际12fps）为主，快动作切'一拍一'，静止镜头'一拍三'
line boil 伪造法：AE 用 Turbulent Displace（数量2~5、大小50）+ 每 2 帧随机化 evolution + Posterize Time 12fps；真 boil 则画 3~4 张微差线稿循环
smear frame：快速位移的中间帧把物体拉长 150%~300% 只保留 1 帧
cel FX 点缀层：烟/水花/闪电用纯手绘逐帧叠在矢量主体上（Buck 式 hybrid）
整体叠纸纹（multiply 10~15%）统一手作气质
```
