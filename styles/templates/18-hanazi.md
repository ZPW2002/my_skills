# 风格模板：综艺花字 Variety Show Kinetic Captions (Hanazi)

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
综艺花字 Variety Show Kinetic Captions (Hanazi)

# Output (fixed)
- 1080×1920, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML DOM/SVG: multi-layer text-stroke 花字 components + spring pops + SVG burst/sweat/sparkle decorations over a pet-vlog footage layer (CC0 photos with Ken Burns + handheld shake + punch-ins)
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「萌宠综艺感 vlog」综艺花字 in its native habitat — reactive captions over a pet vlog.
- Base layer that feels like footage: CC0/PD cat or dog photos from /assets/images with slow Ken Burns, subtle handheld shake, snap punch-in zooms on 'moments' (you may also build a stylised scene if photos look weak).
- 花字 moments synced to beats: title "今日份快乐" (fill gradient + thick white stroke + coloured outer stroke + drop shadow, rounded heavy font), "？？？" bouncing question marks, "震惊!!" inside a radial 爆炸框 with speed lines + 放射线 flash, "（小声）" small aside, "绝绝子" with sparkles, sweat drops, a "猫主子认证" stamp.
- Motion: pop 0 → 1.15 → 1.0 in ~8 frames, per-character bounce with 2-frame stagger, slight rotation, gentle wiggle while holding; appear 2–3 frames after the audio/visual moment. High-saturation pink/yellow/cyan with white strokes.
Sound: bouncy variety-show bed (pizzicato/bass/claps) + boing, pop, ding, slide whistle, record scratch on '？？？'.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
源自电视综艺后期的情绪化装饰字幕：多层描边圆体字带弹性入场，跟随人物情绪变色变形，配打击音效。现已下沉为 vlog、萌宠、访谈、搞笑二创的通用包装语言，剪映内置大量花字模板，B 站也有免费花字样式包流通。
视觉特征 多层描边圆体/胖体字, 高饱和撞色+白边+投影, 弹性 pop 入场, 配合音效出现, 手绘装饰符号（爆炸框/汗滴/闪光）
关键技法 字体三层结构：填充色+粗白描边+彩色外描边/投影（CSS 可用多层 text-shadow 或 SVG stroke 模拟）
入场 overshoot：scale 0→1.15→1.0（约 8 帧），或逐字弹跳错帧 2 帧
情绪匹配：吐槽用歪斜手写体、惊讶用放射线爆炸框、尴尬用汗滴符号
出现时机对齐笑点/音效，比语音晚 2~3 帧更自然
长时间驻留花字加轻微 wiggle 保持活性
```
