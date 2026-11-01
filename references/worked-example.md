# 端到端示例：从需求到生成提示词

一个最小的完整走查，示范三件事：**怎么选风格**、**Creative seed 重写到什么程度**、**哪些内容逐字保留**。
生成正式提示词时，除 seed 外的段落一律从骨架与模板复制，不要仿写本示例的行文。

## 1. 用户需求（输入）

> 给我们的咖啡品牌「醒山」做一支 10 秒竖屏动画，投小红书，气质清爽高级一点。
> 屏幕文案就用品牌名"醒山"，加一句"一杯山醒来"。

信息盘点：品牌名 ✓、文案 ✓、时长 10s ✓、画幅竖屏 ✓、平台 ✓、气质 ✓——无关键缺失，不追问，直接推进。

## 2. 选风格（决策过程）

- 咖啡 = 饮料 → catalog 命中「高端产品质感片」行：首选 04 3D 渲染系，但它是重路线（需 Blender）；
- 执行环境未知 → 按 Step 1 规则默认轻量路线；
- 液体质感天然贴合咖啡 + 需要结尾 logo 揭示 → **主推 07 液态流动**（WebGL，轻量）；
- 备选：12 玻璃拟态（更"高级"但饮食感弱）、04（确认有 Blender 时的更优解）。

## 3. 重写后的 Creative seed（核心产出）

对照 07 模板的 seed 基因逐条落位（缓动只被"甩"、细颈断裂回弹、次级液滴延迟跟随、结尾聚合成 wordmark），
并按竖屏要求写明构图逻辑：

```text
# Creative seed
「醒山 · 一杯山醒来」Morning-coffee liquid genesis for a specialty coffee brand, vertical social cut.
- 1080×1920 portrait composition: one tall central column of motion, generous negative space above and below.
- 0.0–0.5s HOOK: a single glossy amber droplet falls through cream-white space and SPLATS flat (squash on
  landing) — instantly readable liquid physics, never a static open.
- 0.5–3.0s: droplets stream down the central column, merging via metaball fusion — stretched necks, snap,
  2–3 frame rebound; secondary drips follow 2–3 frames late; latte-caramel tones swirl into the amber.
- 3.0–5.5s: a big liquid wave floods DOWNWARD across the frame as a transition (wavy front with 3–5
  phase-offset bulges), revealing a minimal cup silhouette line.
- 5.5–8.0s HERO: the liquid coalesces into a steaming cup that tips and pours one last drop; the drop
  becomes the 醒山 wordmark (text SDF blended with the metaballs), tagline 一杯山醒来 fades up beneath it.
- 8.0–10.0s: wordmark settles with living micro-motion; a last drip falls and ripples once; hold.
- Palette 4 colours: espresso brown #3B2A20, caramel #C68B4E, cream #F5EDE0, fresh green accent #7FA65A.
- Ease: flung, never uniform (cubic-bezier(0.22,1,0.36,1)).
Sound: warm lo-fi bossa ~90 BPM; bubbly gloops, pour, splash, drip synced to the frame; soft chime on the
wordmark landing.
```

导演自主权段（You are the director: you may change…）原样保留在其后，不得改写。

## 4. 拼装清单

| 段落 | 处理 |
|---|---|
| 开头角色段 | 骨架第 1 块逐字（时长 10s，无需改 `10-second` 字样） |
| `# Style` | 07 模板逐字 |
| `# Output (fixed)` | 改数值：`1080×1920, 30 fps, exactly 10.000 s (300 frames)`，`(fixed)` 标签保留 |
| `# Suggested technical route` | 07 模板逐字 |
| `# Creative seed` | 上文重写版 |
| 导演自主权段 | 07 模板逐字 |
| `# Signature features…` | 07 模板逐字 |
| `# How to work` 至结尾 | 骨架第 3 块逐字 |

## 5. 交付前

机械项校验：

```bash
python3 scripts/check_prompt.py out/prompt-xingshan-07.md --template styles/templates/07-liquid.md
```

再按 SKILL.md Step 4 清单人工判断节拍创意质量，然后按 Step 5 的字面结构交付三部分。
