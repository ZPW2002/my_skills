#!/usr/bin/env python3
"""机械项校验：生成的 MG 提示词是否符合通用骨架与所选风格模板（SKILL.md Step 4）。

用法：
    python3 scripts/check_prompt.py <生成的提示词文件> --template styles/templates/<编号>.md

检查项：
  - 章节完整性（10 个必需标题 + 开头角色段）
  - Output 规格：分辨率 / fps / 时长 / 帧数自洽（帧数 = 时长 × fps）
  - 开头段 "ONE <N>-second" 与 Output 时长一致
  - 与模板逐字一致：Style、Suggested technical route、Signature features、导演自主权段
  - 与骨架逐字一致：开头角色段（时长字样归一化后）、# How to work 起的通用尾部段
  - 时长档位：> 30 s 必须声明章节结构（references/chapter-mode.md）
  - seed 密度：占全文比例 ≤ 35%（超 25% 警告）、微指令每拍密度、短片的单一 HOOK
  - 一致性 lint：禁令与用法互斥（如「禁光晕」又要求发光）、「镜头不停」与多处定格冲突、
    未定义的量词 N、seed 色板数量与 Signature 配色约束冲突
  - Creative seed：节拍时间覆盖（HOOK ≤ 0.5s、结尾 ≈ 总时长）、色板 hex（< 3 时警告）、Sound 行存在
  - 全文无 AI 助手/工具产品名

阈值依据：15 份原版 10 秒提示词的 seed 占比中位数 14%、最高 21%，故上限取 35%（留余量后仍能
识别"brief 写成成片"的产物）。

退出码：0 = 通过（可含警告）；1 = 存在 FAIL。
"""

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "# Style",
    "# Output (fixed)",
    "# Suggested technical route",
    "# Creative seed",
    "# Signature features and key techniques",
    "# How to work",
    "# Rules",
    "# Craft checklist",
    "# Before you deliver, score yourself honestly",
    "# Deliver",
]

AGENT_NAMES = re.compile(
    r"\b(zcode|claude|codex|copilot|gemini|chatgpt|openai|windsurf|anthropic|deepseek|kimi|manus)\b",
    re.I,
)

FENCE_RE = re.compile(r"```text\n(.*?)\n```", re.S)
OUTPUT_RE = re.compile(r"exactly\s+(\d+(?:\.\d+)?)\s*s\s*\((\d+)\s*frames\)", re.I)
FPS_RE = re.compile(r"(\d+)\s*fps", re.I)
RES_RE = re.compile(r"(\d{3,4})\s*×\s*(\d{3,4})")
BEAT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*[–—-]\s*(\d+(?:\.\d+)?)\s*s\b")
HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")


def load_prompt_text(path: Path) -> str:
    """提示词文件：优先取第一个 ```text 围栏块，否则视为纯文本。"""
    text = path.read_text(encoding="utf-8")
    m = FENCE_RE.search(text)
    return m.group(1).strip("\n") if m else text.strip("\n")


def load_template_text(path: Path) -> str:
    return FENCE_RE.search(path.read_text(encoding="utf-8")).group(1).strip("\n")


def skeleton_blocks(path: Path):
    """骨架文件的前两个 ```text 块：（开头角色段, 通用尾部段）。"""
    blocks = [b.strip("\n") for b in FENCE_RE.findall(path.read_text(encoding="utf-8"))]
    opening = next(b for b in blocks if b.startswith("You are the director,"))
    tail = next(b for b in blocks if b.startswith("# How to work"))
    return opening, tail


def section_of(prompt: str, heading_prefix: str) -> str:
    """取某个顶级 '# ' 标题到下一个顶级标题之间的正文。"""
    pattern = re.compile(
        r"(?ms)^# " + re.escape(heading_prefix) + r".*?$\n(.*?)(?=^# |\Z)")
    m = pattern.search(prompt)
    return m.group(1).strip() if m else ""


def seed_of(prompt: str) -> str:
    return section_of(prompt, "Creative seed")


def norm_duration_token(text: str, seconds: float) -> str:
    """把开头段里的时长字样归一化为 'ONE <N>-second'，便于跨时长比较。"""
    label = f"{int(seconds)}-second" if float(seconds).is_integer() else f"{seconds:g}-second"
    return re.sub(r"ONE\s+[\d.]+-second", f"ONE {label}", text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("prompt", type=Path, help="生成的提示词文件（纯文本或含 ```text 围栏）")
    ap.add_argument("--template", required=True, type=Path, help="所用风格模板文件")
    ap.add_argument("--skeleton", type=Path, default=None,
                    help="骨架文件（默认取本脚本同级 ../references/prompt-skeleton.md）")
    args = ap.parse_args()

    skel_path = args.skeleton or (Path(__file__).resolve().parent.parent / "references" / "prompt-skeleton.md")
    prompt = load_prompt_text(args.prompt)
    template = load_template_text(args.template)
    skel_opening, skel_tail = skeleton_blocks(skel_path)

    results = []  # (level, message)

    def fail(msg): results.append(("FAIL", msg))
    def warn(msg): results.append(("WARN", msg))
    def ok(msg):   results.append(("OK", msg))

    # ---- 章节完整性（标题允许带括号后缀，如 "(the result is judged against these)"）----
    for h in REQUIRED_SECTIONS:
        (ok if re.search(r"(?m)^" + re.escape(h) + r"(?![\w-])", prompt) else fail)(f"章节 {h}")
    if not prompt.lstrip().startswith("You are the director,"):
        fail("开头角色段缺失（应以 'You are the director,' 开始）")
    else:
        ok("开头角色段存在")

    # ---- Output 规格 ----
    out_sec = section_of(prompt, "Output (fixed)")
    m_dur, m_fps, m_res = OUTPUT_RE.search(out_sec), FPS_RE.search(out_sec), RES_RE.search(out_sec)
    duration = fps = None
    if not (m_dur and m_fps and m_res):
        fail("Output 规格不完整（需要 'exactly <N> s (<F> frames)'、'<N> fps'、'<W>×<H>'）")
    else:
        duration, frames = float(m_dur.group(1)), int(m_dur.group(2))
        fps = int(m_fps.group(1))
        expect = round(duration * fps)
        if abs(frames - expect) <= 1:
            ok(f"帧数自洽：{duration}s × {fps}fps ≈ {frames} frames")
        else:
            fail(f"帧数不自洽：{duration}s × {fps}fps 应为 {expect}，实际 {frames}")
        ok(f"分辨率 {m_res.group(1)}×{m_res.group(2)} @ {fps} fps, {duration}s")

    # ---- 开头段：时长字样 + 与骨架逐字（归一化后） ----
    pre = prompt.split("# ", 1)[0].strip()
    if duration is not None:
        if f"ONE {int(duration)}-second" in pre or f"ONE {duration:g}-second" in pre:
            ok(f"开头段时长字样与 Output 一致（{duration:g}s）")
        else:
            fail(f"开头段缺少 'ONE {duration:g}-second'（时长改动需同步开头段字样）")
    if norm_duration_token(pre, duration or 10) == norm_duration_token(skel_opening, duration or 10):
        ok("开头角色段与骨架逐字一致（时长字样归一化后）")
    else:
        fail("开头角色段被改写（应逐字保留，仅时长字样可变）")

    # ---- 与模板逐字一致的段落 ----
    t_style = section_of(template, "Style")
    t_route = section_of(template, "Suggested technical route")
    t_sig = section_of(template, "Signature features")
    p_style = section_of(prompt, "Style")
    p_route = section_of(prompt, "Suggested technical route")
    p_sig = section_of(prompt, "Signature features")
    for name, a, b in [("Style", t_style, p_style),
                       ("Suggested technical route", t_route, p_route),
                       ("Signature features", t_sig, p_sig)]:
        (ok if a == b else fail)(f"{name} 与模板逐字一致")

    # 导演自主权段
    t_dir = re.search(r"You are the director: you may change.*?(?=\n# |\Z)", template, re.S)
    p_dir = re.search(r"You are the director: you may change.*?(?=\n# |\Z)", prompt, re.S)
    if t_dir and p_dir and t_dir.group(0).strip() == p_dir.group(0).strip():
        ok("导演自主权段与模板逐字一致")
    else:
        fail("导演自主权段缺失或被改写（应逐字保留在 Creative seed 之后）")

    # ---- 通用尾部段 ----
    p_tail = prompt[prompt.index("# How to work"):].strip() if "# How to work" in prompt else ""
    (ok if p_tail == skel_tail.strip() else fail)("通用尾部段（# How to work 起）与骨架逐字一致")

    # ---- 时长档位：> 30 s 必须走章节模式 ----
    LONG_FORM_SEC = 30
    is_long = duration is not None and duration > LONG_FORM_SEC
    if is_long:
        has_heading = bool(re.search(r"(?im)^#\s*CHAPTERS|\[LOCK\]\s*(?:CHAPTERS|章节)", seed_of(prompt)))
        chapter_lines = set(re.findall(
            r"(?im)^[-*\s]*\d{1,2}\s*[·.]?[^\n]{0,60}?\d+(?:\.\d+)?\s*[–-]\s*(\d+(?:\.\d+)?)\s*s",
            seed_of(prompt)))
        mentions = len(re.findall(r"(?i)chapter|章节", seed_of(prompt)))
        if has_heading or len(chapter_lines) >= 2 or mentions >= 2:
            ok(f"长片（{duration:g}s > {LONG_FORM_SEC}s）已声明章节结构")
        else:
            fail(f"时长 {duration:g}s 超过 {LONG_FORM_SEC}s 但未声明章节结构——"
                 "应按 references/chapter-mode.md 用 [LOCK] CHAPTERS 每章 10–20s 组织，"
                 "否则只能逐拍写死")

    # ---- Creative seed ----
    seed = seed_of(prompt)
    if seed:
        beats = [(float(a), float(b)) for a, b in BEAT_RE.findall(seed)]
        if not beats:
            warn("Creative seed 未检测到 'X–Ys' 秒级节拍（散文式 seed 可接受，请人工确认节拍感）")
        else:
            starts, ends = [b[0] for b in beats], [b[1] for b in beats]
            if min(starts) <= 0.5:
                ok(f"HOOK 及时：首个节拍始于 {min(starts)}s")
            else:
                fail(f"HOOK 过晚：首个节拍始于 {min(starts)}s（应 ≤ 0.5s）")

            # 三层 seed 只写 1 个样板拍，覆盖由 IDEA/CHAPTERS 承担，不做覆盖判定
            if len(beats) >= 3:
                if duration is not None:
                    if max(ends) >= duration - 1.5:
                        ok(f"节拍覆盖到结尾：最后节拍止于 {max(ends)}s / 总时长 {duration:g}s")
                    else:
                        fail(f"节拍未覆盖结尾：最后节拍止于 {max(ends)}s，总时长 {duration:g}s")
            else:
                ok(f"节拍 {len(beats)} 处（样板拍模式：覆盖由 IDEA/CHAPTERS 承担，不判覆盖）")

            # 多 HOOK：短片只应有单钩子（长片的每章钩子由章节模式接管）
            if not is_long:
                n_hook = len(re.findall(r"\bHOOK\b", seed))
                if n_hook >= 3:
                    warn(f"HOOK 标记 {n_hook} 处——'a hook in the first 0.5 s' 要求单一钩子；"
                         "多段 HOOK 会把开场判断稀释成清单核对")
                elif n_hook:
                    ok(f"HOOK 标记 {n_hook} 处")

        hexes = set(h.upper() for h in HEX_RE.findall(seed))
        if len(hexes) >= 3:
            ok(f"色板 hex：{len(hexes)} 个")
        else:
            warn(f"色板 hex 少于 3 个（当前 {len(hexes)}）——规范建议 3–6 个具体 hex；"
                 "若色彩已用文字具体描述（如原版 02 线条动画）可接受，请人工确认")
        if re.search(r"(?m)^[-*\s]*Sound\s*[:：]", seed):
            ok("Sound 行存在")
        else:
            fail("缺少 Sound 行（音乐风格 + BPM + 关键音效）")

        # ---- seed 密度：brief 还是成片？ ----
        ratio = len(seed) / max(len(prompt), 1)
        if ratio > 0.35:
            fail(f"seed 占全文 {ratio:.0%}（上限 35%）——brief 已膨胀成完成版 treatment，"
                 "执行者没有创作余量。保留 IDEA/SURFACE 与 1 个样板拍，"
                 "其余逐拍微指令移入 [FREE]")
        elif ratio > 0.25:
            warn(f"seed 占全文 {ratio:.0%}（建议 ≤25%）——检查是否把执行决策写死")
        else:
            ok(f"seed 占比 {ratio:.0%}（≤25%，brief 尺度）")

        micro = re.findall(r"\d+\s*(?:frames?|帧|px)|\d+(?:\.\d+)?%|cubic-bezier\(", seed)
        if len(beats) >= 3:
            per = len(micro) / len(beats)
            lvl = fail if per > 1.5 else (warn if per > 0.8 else ok)
            lvl(f"微指令密度 {per:.2f}/拍（{len(micro)} 处 / {len(beats)} 拍；建议 ≤0.8——"
                "帧数、像素、百分比应给判断标准而非逐个数值）")
        elif len(micro) > 8:
            warn(f"微指令 {len(micro)} 处（无秒级节拍时建议 ≤8）")
        else:
            ok(f"微指令 {len(micro)} 处")

        # ---- 一致性 lint ----
        prohib = re.search(r"禁[^。\n]{0,6}(?:光晕|发光|辉光|渐变)|no glow|never glow", seed)
        if prohib:
            outside = [m.start() for m in re.finditer(r"glow|发光|光晕|辉光", seed)
                       if not prohib.start() <= m.start() < prohib.end()]
            if outside:
                fail(f"自相矛盾：声明「{prohib.group(0)}」却在别处要求发光 {len(outside)} 处")
            else:
                ok("发光禁令无冲突")

        cont = re.search(r"never stops?|no cut|一镜到底|连续运镜|continuous camera|one continuous shot", seed, re.I)
        n_freeze = len(re.findall(r"freeze|定格|静止", seed, re.I))
        if cont and n_freeze >= 2:
            warn(f"措辞冲突：「{cont.group(0)}」与 {n_freeze} 处定格/冻结并存——"
                 "章卡定格若是有意的，改写为「不切黑场，章卡处短定格」以免执行者反复权衡")

        m_pal = re.search(r"[Pp]alette\s+(\d+)\s+colou?rs?", seed)
        m_sig_pal = re.search(r"克制配色[（(]\s*(\d+)\s*[~–-]\s*(\d+)\s*色", p_sig)
        if m_pal and m_sig_pal:
            n_seed, lo, hi = int(m_pal.group(1)), int(m_sig_pal.group(1)), int(m_sig_pal.group(2))
            if n_seed > hi:
                fail(f"违反 Signature：seed 用 {n_seed} 色，该风格要求「克制配色（{lo}~{hi} 色）」")
            else:
                ok(f"色板数量合规（{n_seed} ≤ {hi}）")

        if re.search(r"\bN\s+(?:identical|stack|layers?|层|blocks?|copies)", seed):
            warn("检测到未定义量词 N（如 'stack of N identical …'）——执行者无法确定数量；"
                 "给出具体值，或明确写「由执行者决定并在报告中说明」")
    else:
        fail("Creative seed 段为空")

    # ---- 产品名残留 ----
    hits = sorted(set(m.group(0) for m in AGENT_NAMES.finditer(prompt)))
    if hits:
        fail(f"检测到 AI 助手/工具产品名残留：{', '.join(hits)}")
    else:
        ok("无 AI 助手/工具产品名残留")

    # ---- 输出 ----
    icon = {"OK": "✓", "WARN": "▲", "FAIL": "✗"}
    for level, msg in results:
        print(f"{icon[level]} [{level}] {msg}")
    n_fail = sum(1 for l, _ in results if l == "FAIL")
    n_warn = sum(1 for l, _ in results if l == "WARN")
    verdict = "FAIL" if n_fail else "PASS"
    print(f"\n{verdict}: {len(results)} 项检查，{n_fail} FAIL，{n_warn} WARN")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
