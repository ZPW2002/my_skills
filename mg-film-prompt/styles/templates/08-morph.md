# 风格模板：形变动画 Morphing / Shape Morph

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
形变动画 Morphing / Shape Morph

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG + flubber or GSAP MorphSVGPlugin (tune shapeIndex), color-field wipes
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「万物相连」Apple-keynote-grade morph chain: one hero shape continuously becomes 6–8 meaningful icons, on the beat.
- Chain example: coffee cup → (circle) → sun → sunset over sea → gull → paper plane → location pin → heart → invented brand logo "morphe" with wordmark.
- Every A→B goes through a simple intermediate (circle/capsule) with rotation and 10–15% squash&stretch; sub-parts morph in sync (steam → sun rays → waves).
- Background color fields change with each morph (clean color-block wipes); ease cubic-bezier(0.7,0,0.3,1), 3-frame cushions at start/end; no knotting/tangling ever (check every morph mid-point stills).
Sound: rhythmic plucky arpeggio; a pitched whoosh per morph landing on the beat.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
一个图形丝滑连续地变成另一个图形：手机变成地图钉、咖啡杯变成落日。是图形叙事（visual storytelling）的核心语法，苹果发布会动效和高端 explainer 里最见功力的部分。
视觉特征 轮廓连续过渡无跳变, 中介形状桥接, 形变伴随位移旋转, 变形瞬间的挤压拉伸
关键技法 路径对齐是前提：两形状顶点数一致、首顶点方位对应（AE 里重设 first vertex），否则会打结
复杂 A→B 不直接变：先收敛为中介简形（圆/胶囊）再展开，'A→圆→B'两段各 8~12 帧
形变全程叠加 10~15% squash & stretch 与轻微旋转，掩盖插值的机械感
速度曲线中段最快 cubic-bezier(0.7,0,0.3,1)：起止各留 3 帧缓冲
Web 端用 flubber/polymorph 库做最优顶点匹配插值，效果远好于朴素 SMIL
```
