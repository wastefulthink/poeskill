# -*- coding: utf-8 -*-
"""构建 poeskill 四大知识专题库：powers_poe.jsonl + 12 个哲学知识包 + 哲学概念词典"""
import json, os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from powers_phil_p1 import POWERS_P1
from powers_phil_p2 import POWERS_P2

POWERS = POWERS_P1 + POWERS_P2
OUT = r"C:/Users/Administrator/WorkBuddy/2026-08-14-14-39-44/poeskill-知识库"

# ---------- 校验 ----------
ids = [a["id"] for a in POWERS]
assert len(ids) == len(set(ids)), "id 重复"
for a in POWERS:
    req = {"id","knowledge","original","url","date","topics","skills","type","confidence"}
    assert req.issubset(set(a)), f"缺字段: {a['id']}"
    assert a["confidence"] in ("high","medium","low")
    assert a["type"] in ("principle","method","case","anti-pattern","insight","tool")
    assert isinstance(a["skills"], list) and a["skills"], f"skills 为空: {a['id']}"
print(f"能量总数: {len(POWERS)}，校验通过")

# ---------- 输出 jsonl（注入语言字段，支持 i18n）----------
os.makedirs(f"{OUT}/能量库", exist_ok=True)
with open(f"{OUT}/能量库/powers_poe.jsonl", "w", encoding="utf-8") as f:
    for a in POWERS:
        p = dict(a)
        p["language"] = "zh-CN"   # 源语言标记；翻译版请复制条目并改 language + knowledge
        f.write(json.dumps(p, ensure_ascii=False) + "\n")
print("powers_poe.jsonl 已生成")

# ---------- 知识包 ----------
PACK_META = {
    "poe-diagnosis": ("商业模式与市场诊断", "斯密/米塞斯/哈耶克/休谟/康德/波普尔"),
    "poe-decision": ("科学决策方法", "波普尔/休谟/康德/多伊奇/马可·奥勒留/老子"),
    "poe-good-question": ("提问与问题澄清", "维特根斯坦/波普尔/康德"),
    "poe-deconstruct": ("概念拆解与语言澄清", "维特根斯坦/罗素"),
    "poe-content": ("内容与表达哲学", "罗素/尼采/加缪/叔本华/阿德勒"),
    "poe-action": ("行动与动机", "阿德勒/叔本华/马可·奥勒留/加缪"),
    "poe-standard-answer": ("历史规律与商业案例", "斯密/哈耶克/多伊奇/尼采/加缪"),
    "poe-verify": ("批判核查", "波普尔/休谟/罗素/尼采(反例)"),
    "poe-benchmark": ("对标与竞争参照", "斯密/哈耶克/米塞斯"),
    "poe-resonate": ("共鸣与人性洞察", "叔本华/阿德勒"),
    "poe-spread": ("传播心理", "阿德勒/叔本华/米塞斯"),
    "poe-slowisfast": ("长期主义与节奏", "老子/马可·奥勒留"),
}
os.makedirs(f"{OUT}/Skill知识包", exist_ok=True)
for skill, (title, src) in PACK_META.items():
    sel = [a for a in POWERS if skill in a["skills"]]
    lines = []
    lines.append(f"# {skill}：{title}（哲学知识包）")
    lines.append("")
    lines.append(f"> 来源：{src} | 共 {len(sel)} 个能量单元 | 四大知识专题（科学认识论·市场自发秩序·人性动机·价值哲学）")
    lines.append("")
    lines.append("> 语言：zh-CN（源语言）。翻译版请复制本包并按 i18n 规范翻译 knowledge 字段。")
    lines.append("> 受众标注：🔬科学家高偏好 ｜ 🔥大众高流量 ｜ 💼商业圈层高频 ｜ ⚠️需选择性参考，谨防断章取义")
    lines.append("")
    for a in sel:
        lines.append(f"## {a['id']} {a.get('audience','')}")
        lines.append("")
        lines.append(f"- **思想核心与商业启示**：{a['knowledge']}")
        lines.append(f"- **出处**：{a['original']}")
        lines.append(f"- **类型**：{a['type']} ｜ **置信度**：{a['confidence']}")
        lines.append("")
    with open(f"{OUT}/Skill知识包/{skill}_哲学知识包.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"知识包 {skill}: {len(sel)} 条")
print("知识包全部生成")

# ---------- 哲学概念词典 ----------
CONCEPTS = [
    ("归纳问题", "hume", "从有限经验推不出必然规律，过去成功≠未来复制", "决策"),
    ("因果是心理习惯", "hume", "A 后发生 B 不等于 A 导致 B，先找机制证据", "决策"),
    ("事实-价值二分", "hume", "市场发生了什么（事实）≠ 应该怎么做（价值）", "战略"),
    ("认知滤镜", "kant", "人只能看见心智框架加工后的世界，管理者看不到纯客观真相", "决策"),
    ("理性有边界", "kant", "理性不能解决一切商业问题，懂边界才不盲目自信", "决策"),
    ("证伪主义", "popper", "商业假设要主动找推翻自己的证据，而非自圆其说", "决策/战略"),
    ("反例优先", "popper", "先问『什么情况会证明它失败』，再投入资源", "产品/战略"),
    ("语言塑造思想", "witt", "商业内耗多来自概念混乱，先厘清定义再辩论", "组织/沟通"),
    ("可说的与不可说的", "witt", "分不清边界的宏大愿景，不如落地为可验证的具体问题", "目标管理"),
    ("解释性理论", "deutsch", "企业核心竞争力是更好的解释：市场为什么变、用户为什么动", "战略"),
    ("反归纳乐观主义", "deutsch", "增长停滞时模仿历史打法通常无效，出路是创造新解释", "增长"),
    ("参差多态", "russell", "拒绝一刀切管理，多元是创新土壤", "组织"),
    ("权力类型", "russell", "区分专业知识权力与身份权力，混同是组织衰败起点", "组织"),
    ("看不见的手", "smith", "尊重自利，把自利引导到与组织目标一致的方向", "机制设计"),
    ("分工效率", "smith", "效率底层来源是分工与专业化，先问任务拆透没有", "运营"),
    ("主观价值论", "mises", "用户为感知价值付费，不为你的成本付费", "定价"),
    ("经济计算问题", "mises", "过度集中管控丧失一线信息，决策权下放给信息最近的人", "组织"),
    ("自发秩序", "hayek", "好秩序是长出来的不是管出来的，给局部试错空间", "组织/市场"),
    ("分散知识", "hayek", "一线拥有大量局部知识，别让信息在传递中失真", "组织"),
    ("理性的自负", "hayek", "反模式：迷信顶层完美规划是傲慢", "战略"),
    ("无为", "laozi", "过度管理是破坏秩序的根源，减少无谓干预", "管理"),
    ("顺势", "laozi", "大方向错了执行力越强死得越快，先看大势", "战略"),
    ("目的论", "adler", "员工行为是目的驱动不是性格缺陷，先找行为服务的目", "管理/激励"),
    ("优越感诉求", "adler", "给进步以可见反馈，比单纯加薪更能激活长期动力", "激励"),
    ("共同体感觉", "adler", "让成员感到贡献被看见，是激励的底层结构", "团队"),
    ("欲望与痛苦", "schopenhauer", "把『必须成功』降级为『值得一试』，减少决策扭曲", "心态"),
    ("预期管理", "schopenhauer", "设定预期区间而非单点期望，焦虑源于期望当承诺", "心态"),
    ("控制二分法", "marcus", "危机决策：拆可控/不可控两栏，精力全放可控栏", "危机管理"),
    ("逆境自律", "marcus", "危机是最低成本的压测，暴露脆弱点修复即增长", "危机管理"),
    ("重估价值", "nietzsche", "⚠️ 行业惯例最该被重估，但极易断章取义，需对照罗素", "创新"),
    ("权力意志", "nietzsche", "⚠️ 强者扩张冲动需理性节制，不可全盘接纳", "价值观"),
    ("理性节制", "russell", "对尼采的对冲：权力必须有边界，强者尊重他人自由", "价值观"),
    ("荒诞与创造意义", "camus", "商业无预设意义，意义在持续行动中被创造", "价值观/逆境"),
    ("接纳困境继续行动", "camus", "先行动，意义在后面追你", "逆境"),
]
lines = []
lines.append("# 哲学概念词典（poeskill）")
lines.append("")
lines.append("> 由 powers_poe.jsonl 提炼的高频概念 → 出处人物 → 一句话核心 → 商业场景。")
lines.append("")
for name, person, core, scene in CONCEPTS:
    lines.append(f"### {name}（{person}）")
    lines.append(f"- 核心：{core}")
    lines.append(f"- 商业场景：{scene}")
    lines.append("")
with open(f"{OUT}/哲学概念词典.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"哲学概念词典已生成（{len(CONCEPTS)} 词）")
print("全部完成")
