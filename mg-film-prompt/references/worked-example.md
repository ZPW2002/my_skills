# 端到端示例：从需求到生成提示词

一个最小的完整走查，示范三件事：**怎么选风格**、**三层 seed 写到什么程度算够**、**哪些内容逐字保留**。
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

只写 `[LOCK]` 与 1 个 `[REGISTER]` 样板拍，其余交给执行者。这段约 890 字符，约占全文 15%——
和原版 15 份提示词（中位数 14%、最高 21%）同一量级，这才叫 brief。

```text
# Creative seed
「醒山 · 一杯山醒来」Morning-coffee liquid genesis for a specialty coffee brand, vertical social cut.

[LOCK] IDEA
- 论点：一杯好咖啡的"醒来"是液体自己长出来的形状，不是被摆出来的。
- 论证脊柱：一滴 → 汇聚成流 → 漫过画面 → 聚成杯与字。
- 不变量：结尾 wordmark 的轮廓完全由同一条液体流动路径聚合而成（无硬切、无二次建模）。

[LOCK] SURFACE
- 色板：espresso #3B2A20、caramel #C68B4E、cream #F5EDE0、leaf #7FA65A（4 色，贴合 07 的邻近色规则）。
- 字体 / 质感：细体无衬线，字距舒展；液体全程高光 + fresnel 边缘，读作厚液体而非平面色块。
- 构图：1080×1920 竖向，运动集中在中央单列，上下留大负空间；所有生长沿竖向展开。
- Sound：lo-fi bossa 约 90 BPM；gloop / pour / splash / drip 拟音，wordmark 落定时一声轻铃。

[REGISTER] 样板拍
- 0.0–1.2s HOOK: 琥珀色液滴自上方落入米白空间，砸落时 squash 扁平化——单主体、单一动作、
  高光锐利；全片其余节拍照此密度组织。

[FREE] 其余节拍、液滴次级跟随、缓动曲线、转场机制——由执行者设计，在交付报告中说明选择理由。
```

对照 07 模板的 seed 基因逐条落位：缓动只被"甩"、细颈断裂回弹、次级液滴延迟跟随、结尾聚合成 wordmark——
这些写在模板的 Signature features 里，**逐字保留**，不进 seed。

## 4. 拼装清单

| 段落 | 处理 |
|---|---|
| 开头角色段 | 骨架第 1 块逐字（时长 10s，无需改 `10-second` 字样） |
| `# Style` | 07 模板逐字 |
| `# Output (fixed)` | 改数值：`1080×1920, 30 fps, exactly 10.000 s (300 frames)`，`(fixed)` 标签保留 |
| `# Suggested technical route` | 07 模板逐字 |
| `# Creative seed` | 上文三层版 |
| 导演自主权段 | 07 模板逐字 |
| `# Signature features…` | 07 模板逐字 |
| `# How to work` 至结尾 | 骨架第 3 块逐字 |

## 5. 交付前

机械项校验：

```bash
python3 scripts/check_prompt.py out/prompt-xingshan-07.md --template styles/templates/07-liquid.md
```

预期全绿。再按 SKILL.md Step 4 清单判断"论点是否立得住、样板拍够不够好"，然后按 Step 5 的字面结构交付三部分。

## 6. 如果这支片要 60 秒怎么办

不要把这 10 秒的节拍表拉长四倍——读 `references/chapter-mode.md`，改用 `[LOCK] CHAPTERS`：
每章 10–20 秒、各写一句章任务与收尾形态，全片只留一个 HERO。章内怎么做，仍然是执行者的活。
