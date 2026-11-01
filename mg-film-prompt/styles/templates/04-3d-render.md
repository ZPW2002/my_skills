# 风格模板：3D 渲染系（C4D/Blender 质感） 3D Render / CGI Motion Design

> 本文件是**风格专属段**（完整提示词的 5 个段落：Style / Output / Suggested technical route / Creative seed / Signature features）。
> 拼装方法与定制规则见 `SKILL.md` 与 `references/prompt-skeleton.md`：
> - `Creative seed` 按用户需求整段重写（故事节拍、色板、声音），其后的「导演自主权」段原样保留；
> - `Style`、`Suggested technical route`、`Signature features` 原样保留，是风格被一眼认出的依据；
> - `Output` 仅在用户要求改画幅/时长/帧率时调整。

```text
# Style
3D 渲染系（C4D/Blender 质感） 3D Render / CGI Motion Design

# Output (fixed)
- 1920×1080, 24 fps, exactly 10.000 s (240 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
Blender 5.1.2 CLI (bpy script → Cycles on Metal GPU with OIDN denoise, or EEVEE if it holds quality) → PNG sequence → ffmpeg; optional HTML overlay pass for typography
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
「Soft & Satisfying」The C4D/Octane pastel product-ident look (Maxon demo-reel vibe): soft candy materials, cloner arrays, physics-feel motion.
- Pastel studio: infinite cyc backdrop, big soft area lights + HDRI (see /assets/hdri), shallow DOF (f/1.8 feel), 24 fps, real motion blur.
- A MoGraph-style cloner field (geometry-nodes grid of glossy rounded pills/spheres) ripples with an effector wave; a hero object — inflated/bevelled 3D wordmark (e.g. "SOFT" or an invented brand) or a glossy jelly logo — drops in, squash-and-stretch jiggle (damped spring), collides with and displaces the cloner field.
- Material trio: SSS gummy (candy pink / peach), glossy plastic (cream / lilac), frosted glass or chrome accent — with AO, soft reflections, subtle subsurface glow.
- Camera: long-tail ease (80% of the move in the first 20%), ends on a clean hero composition held ~1s.
Sound: ASMR-satisfying soft thuds, squishes, bubbly pops, airy cinematic pad; hits frame-synced to impacts.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
Cinema 4D + Redshift/Octane 或 Blender 渲染的实体质感动画：软胶、玻璃、金属、布料，配合克隆阵列和物理模拟。是高端产品片（手机、饮料、球鞋）和品牌 ident 的主流，Maxon 官方 Demo Reel 就是该风格的年度风向标。
视觉特征 PBR真实材质, 浅景深, 柔和棚拍布光, 克隆器阵列, 软体碰撞, 糖果色软胶质感
关键技法 MoGraph 核心：Cloner 克隆器 + Random/Plain Effector 做群体波浪式动画
质感三件套：SSS 次表面散射（软胶感）+ AO + HDRI 三点布光
运动多用长尾 ease：位移曲线前 20% 完成 80% 路程，收尾极慢，配 motion blur
24/25fps 电影帧率 + 浅景深（f/1.8 感）区别于 2D 系的 30fps 利落感
常见结构：产品为轴心，粒子/流体/布料围绕它做物理模拟编排
```
