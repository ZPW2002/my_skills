# 风格模板：复古系（80s Synthwave / Y2K 千禧） Retro: 80s Synthwave / VHS / Y2K

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
复古系（80s Synthwave / Y2K 千禧） Retro: 80s Synthwave / VHS / Y2K

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML WebGL (perspective grid, sun, mountains shader) + canvas chrome text + CSS/SVG glow; VHS pass
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「OUTRUN 1986」The quintessential 80s synthwave title sequence.
- Starry night, striped retro sun (horizontal band cut-outs, magenta→orange→yellow), wireframe mountains, palm silhouettes, neon magenta/cyan perspective grid rushing toward the camera.
- 0–1s: VHS tracking noise + 'PLAY ▶' OSD; 1–4s: camera flies low over the grid, sun rises; 4–6s: CHROME title (e.g. "NEON DRIVE", multi-stop metallic gradient, bevel highlight, star glint sweeping across) SLAMS in with a lens flare; 6–7.5s: pink neon script word (e.g. "Midnight") writes on like a neon tube with flicker; 7.5–10s: sustained ride, subtle VHS chroma bleed/scanlines, end on the hero frame.
- Double glow (tight ~4px + wide ~30px), deep purple sky gradient.
Sound: synthwave — gated-reverb snare, arpeggiated saw bass, lush pads, big chord + crash on the title slam.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
对特定年代媒介美学的整体引用：80s synthwave 是霓虹网格+日落渐变+镀铬字；VHS 是扫描线+色偏+磁带噪声；Y2K 千禧风是液态镀铬金属、酸性绿紫、拟物系统窗口和低保真 3D。近两年 Y2K 在音乐视频与潮流品牌片中强势回潮，B站模板市场大量供应'酸性镀铬'素材。
视觉特征 霓虹辉光, 透视网格地平线, 扫描线与RGB色偏, 镀铬金属字, 酸性配色, 拟物窗口UI
关键技法 synthwave 三件套：透视网格滚动（一点透视 grid + 纵向位移循环）、日落多层渐变球、双层辉光（内层紧 4px 高亮+外层散 30px 低透明）
VHS 做旧链：RGB split（红蓝通道各偏 1~2px）→ 扫描线（2px 间隔 10% 黑条）→ 波浪扭曲抖动（每秒 1~2 次随机 glitch 抽帧）→ 4:3 圆角遮罩
Y2K 镀铬字：极高对比的多段金属渐变 + bevel 高光 + 环境映射感反光，配 lens flare
Y2K 运动语言：弹窗式 pop 出现、光标点击、窗口拖拽，界面拟物即动画叙事
帧率故意不稳：关键段落抽帧到 15fps 或倒放 2 帧制造磁带卡顿
```
