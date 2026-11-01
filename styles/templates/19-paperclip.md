# 风格模板：粗描边贴纸人科普 MG（回形针/林超风格） Bold-outline Sticker Explainer MG (PaperClip / Lin Chao style)

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
粗描边贴纸人科普 MG（回形针/林超风格） Bold-outline Sticker Explainer MG (PaperClip / Lin Chao style)

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: one huge canvas (e.g. 6000×3000 px) with a camera transform (long eases), SVG charts, photo stickers with 10px white outline
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「回形针式硬核科普」The PaperClip-style knowledge-video look: sticker-ized photos + flat icons + precise charts on a giant canvas with continuous camera moves.
- Topic (write your own tight copy), e.g. 「一部手机里，藏着多少种元素？」.
- Calm blue-grey/off-white canvas (#E9EEF2 + slate), 2–3 colours + one accent (e.g. #FF5A36); equal-weight sans typography, strict alignment.
- One continuous camera path: sticker phone photo (white 10px outline, soft shadow) → exploded-parts stickers with leader-line labels → periodic-table grid where element tiles light up → bar chart grows with count-up "70+" → world map with supply routes drawing → pull out to a bold typographic title card in the 回形针 manner (heavy sans, huge number, small caption).
- Every beat introduces a new visual element; charts are exact (bars to scale, numbers consistent).
Sound: clean tech-explainer bed, UI clicks, ticking during count-up, soft whoosh on camera moves.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
回形针 PaperClip 带火的知识区标准包装：实拍图片抠图后加粗白描边变成『贴纸』，与扁平图标、数据图表一起铺在大画布上，镜头平移缩放串联信息点；林超等财经/跨学科 UP 主将其与手写板书、公式卡片结合。至今仍是硬核科普、财经知识区、企业宣传片的主流范式。
视觉特征 照片贴纸化（粗白描边）, 蓝灰/米白冷静底色, 扁平图标+精确数据图表, 大画布镜头平移缩放, 信息密度极高的节拍化叙事
关键技法 素材照片抠图 + 8~12px 白描边统一质感，消除图片来源差异
超宽大画布布局，摄像机层做平移/缩放（ease 长曲线），一镜串多个信息点
图表动效：柱状图生长、数字滚动计数、路径描边生长
解说词逐句驱动画面元素入场，语速快、每句必有新视觉元素
克制配色（2~3 色）+ 等线字体，保持『严肃感』
```
