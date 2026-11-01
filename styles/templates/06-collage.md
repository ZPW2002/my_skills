# 风格模板：拼贴剪贴 Collage / Cutout Animation

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
拼贴剪贴 Collage / Cutout Animation

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: DOM/Canvas with PNG cutouts from /assets/images (rembg), SVG/CSS white-edge + halftone filters; stepped 12 fps (render 30 fps, hold motion on 12 fps grid)
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「脑洞拼贴」Surreal Dada/Monty-Python cutout collage in a modern editorial magazine finish.
- Newsprint/kraft paper ground; a public-domain Victorian portrait cutout with rough white scissor edge + halftone; the top of the head FLIPS OPEN like a lid (Terry Gilliam homage) revealing deep space (NASA PD imagery) from which flowers, birds, planets, pointing hands and a vintage rocket spill out.
- Jaw/mouth on a separate cut flaps with the sound; hands slap elements onto the page; torn-paper strips; bold constructivist red/black diagonal typography (e.g. "THE MIND IS A COLLAGE" / 脑洞大开).
- Motion on 12 fps (even 6 fps for some holds) with ±2px hand-placement jitter; paper-flip / torn-paper transition to the end card.
Sound: vinyl crackle, jazzy boom-bap bed, paper rustles, scissors snips, slaps and a comic 'pop' when the lid opens.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
把老照片、报纸、手撕纸片剪出来重新拼装的复古超现实风格，源头是 Monty Python 和苏联构成主义海报。人物头身比例失衡、嘴巴单独开合、半调网点纹理是标志。近年与'杂志风'合流，成为音乐类、街头潮流类短视频的高频风格。
视觉特征 照片剪影白描边, 半调网点, 报纸纹理, 比例失衡的超现实拼装, 定格式抽帧运动
关键技法 素材处理：人物/物件抠图后加 2~4px 白描边（剪刀剪出来的感觉）+ 半调 halftone 滤镜
关节动画：锚点设在肩/肘/颌，做 puppet 式分段旋转，嘴巴用两三张替换帧开合
刻意降帧：主体运动 12fps 甚至 6fps（stop-motion 感），位置加 ±2px 随机抖动模拟手摆
图层结构：背景纸纹 → 大形色块 → 照片剪影 → 手写涂鸦/胶带贴纸 → 颗粒调整层
转场用'手把元素拍上来'或整页翻纸
```
