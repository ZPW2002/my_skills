# 风格模板：线条动画 Line Art / Line Animation

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
线条动画 Line Art / Line Animation

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG paths + stroke-dashoffset (getTotalLength) + GSAP; a virtual camera that follows the pen tip
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「一笔画」One-line narrative for a luxury / architecture brand — the whole film is ONE continuous line.
- Deep midnight ground (#0B1320 or near-black) + a single champagne-gold line (#E9D7A5), constant ~3px, round caps, a softly glowing pen tip that leads the draw.
- Story (continuous path, the tail of each figure is the start of the next): a seed → sprouts into a sapling → branches become the structural lines of a building → the building outline extends into a skyline/horizon → the horizon line lifts and loops into a monogram logo → LINE-TO-FILL moment (logo fills with gold from its anchor) → thin letter-spaced serif wordmark (e.g. "ATELIER LINEA") fades up.
- Draw speed eases into corners (cubic-bezier(0.65,0,0.35,1)); the virtual camera drifts/pushes to keep the tip in frame, then dollies out at the end to reveal the whole drawing composed as a poster; older line segments dim to ~35% as the camera moves on.
Sound: minimal felt piano + soft string swell; a pen-on-paper whisper whose loudness follows tip speed; delicate chime on the fill.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
以单色细线为唯一造型语言，线条自我描绘（draw-on）、延伸、转折并变形为下一个图形，一笔连成整支片子。极简高级感强，常见于奢侈品、金融、建筑类品牌片和 logo 动画。
视觉特征 等宽细线, 单色或双色, 大量负空间, 线条连续生长, 线面转换瞬间
关键技法 核心是 stroke 描绘：AE 用 Trim Paths 0→100%，Web 端用 SVG stroke-dasharray/dashoffset
线宽全片恒定（2~4px），转角处让描绘速度略减速，用 easeInOut cubic-bezier(0.65,0,0.35,1)
'一笔画'叙事：上一图形的尾线即下一图形的起线，路径提前在 Illustrator 里连好
线转面：描完轮廓后用同路径的 fill 从锚点扩展填充
配合微小的端点圆头（round cap）与路径抖动可增加手绘感
```
