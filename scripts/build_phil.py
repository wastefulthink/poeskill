# -*- coding: utf-8 -*-
"""构建 poeskill 四大知识专题库：powers_poe.jsonl + 12 个哲学知识包 + 哲学概念词典"""
import json, os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from powers_phil_p1 import POWERS_P1
from powers_phil_p2 import POWERS_P2
from powers_phil_p3 import POWERS_P3
from powers_phil_p4 import POWERS_P4
from powers_phil_p5 import POWERS_P5
from powers_phil_p6 import POWERS_P6

POWERS = POWERS_P1 + POWERS_P2 + POWERS_P3 + POWERS_P4 + POWERS_P5 + POWERS_P6
OUT = r"C:/Users/Administrator/WorkBuddy/2026-08-14-14-39-44/poeskill-repo/knowledge"

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
os.makedirs(f"{OUT}/powers", exist_ok=True)
with open(f"{OUT}/powers/powers_poe.jsonl", "w", encoding="utf-8") as f:
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
os.makedirs(f"{OUT}/skill-packs", exist_ok=True)
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
    with open(f"{OUT}/skill-packs/{skill}_pack.md", "w", encoding="utf-8") as f:
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
    ("逆向思维", "munger", "先想怎么失败，再避免失败，比正面求成更可靠", "决策/风险"),
    ("能力圈", "munger", "只在真懂的领域下注，边界比大小重要", "决策/战略"),
    ("激励超级反应", "munger", "行为几乎全由激励驱动，设计激励先问所有人会做什么", "组织/激励"),
    ("双系统思维", "kahneman", "快直觉与慢推理并存，重大决策必须唤醒慢系统", "决策"),
    ("锚定效应", "kahneman", "先出现的数字扭曲后续判断，先设理性锚", "谈判/定价"),
    ("损失厌恶", "kahneman", "失去的痛苦约为同等获得的快乐两倍", "心理/定价"),
    ("峰终定律", "kahneman", "体验记忆由峰值与结尾决定", "产品/体验"),
    ("事前验尸", "kahneman", "决策前假设已失败并倒推原因，暴露盲点", "决策/风险"),
    ("心理账户", "thaler", "钱按来源用途分账户，定价要理解用户账户", "定价/心理"),
    ("助推", "thaler", "默认选项就是决策，设计默认值优于发通知", "机制设计"),
    ("沉没成本谬误", "thaler", "已投入的不该影响未来决策，止损靠纪律", "决策"),
    ("黑天鹅", "taleb", "罕见高冲击事件主导历史，别按平均值规划生死", "风险"),
    ("反脆弱", "taleb", "设计冗余与可逆选项，让波动成为养分", "风险/战略"),
    ("杠铃策略", "taleb", "极度保守＋极度冒险，放弃中庸", "决策"),
    ("幸存者偏差", "taleb", "只看活下来的样本会高估成功概率", "认知/对标"),
    ("目标管理", "drucker", "先定义成果再分配资源，目标模糊则执行浪费", "组织/管理"),
    ("顾客决定企业", "drucker", "企业目的是创造顾客，利润是结果不是目的", "商业模式"),
    ("五力模型", "porter", "行业吸引力由五种力量决定，力量越强利润越薄", "战略/诊断"),
    ("战略即取舍", "porter", "无取舍无战略，运营效益不等于战略", "战略"),
    ("有限理性", "simon", "信息算力有限，追求满意而非最优", "决策"),
    ("交易成本", "coase", "企业因市场交易成本而存在，降摩擦即生意", "商业模式"),
    ("第一性原理", "feynman", "从基本原理推导，不依赖类比与惯例", "决策/创新"),
    ("费曼技巧", "feynman", "讲不清就是没真懂，用教检验理解", "学习"),
    ("红皇后效应", "darwin", "必须不断奔跑才能留在原地，维持即衰退", "战略/市场"),
    ("生态位", "darwin", "占据独特位置，同质竞争是生态位缺失", "战略/市场"),
    ("创造性破坏", "schumpeter", "创新摧毁旧结构，领先地位永远是暂时的", "创新/市场"),
    ("企业家精神", "schumpeter", "新组合的执行者，创新五形态不只有新技术", "创新"),
    ("动物精神", "keynes", "投资决策受情绪与血性驱动，市场不理性", "市场/心理"),
    ("选美理论", "keynes", "市场猜别人会选谁，共识的共识决定价格", "市场/传播"),
    ("反身性", "soros", "认知改变现实，现实改变认知，正反馈成泡沫", "市场/风险"),
    ("易错性", "soros", "认知天生有缺陷，判断留可逆余量", "认知/决策"),
    ("战略转折点", "grove", "10倍速变化出现时，不转身就会被甩下", "战略/危机"),
    ("只有偏执狂才能生存", "grove", "成功滋生自满，自满招致毁灭", "战略/心态"),
    ("黄金中道", "aristotle", "美德是两极之间的适度，管理同理", "决策/价值观"),
    ("修辞三要素", "aristotle", "人格＋情感＋逻辑，三者合力才说服", "内容/传播"),
    ("思想自由市场", "mill", "异见是发现真理的机制，消灭异见等于灭校准", "组织/决策"),
    ("伤害原则", "mill", "自由止于伤害他人，自由与责任一体两面", "价值观"),
    ("理性化与铁笼", "weber", "工具理性极致化会抽干意义，留低效空间", "组织/价值观"),
    ("卡里斯玛权威", "weber", "魅力型领导无法制度化传承，人走茶凉", "组织/管理"),
    ("信息熵", "shannon", "信息量等于不确定性减少，不减少不确定的是噪声", "信息/决策"),
    ("图灵测试", "turing", "以行为判定智能，用户只认可观察的结果", "产品/认知"),
    ("四假象说", "bacon", "部落/洞穴/市场/剧场四类偏见源，先自查再判断", "认知/决策"),
    ("归纳法", "bacon", "知识从经验中来，决策回到一手数据", "决策/认知"),
    ("方法论怀疑", "descartes", "怀疑一切可怀疑的，直到找到确定基点", "决策/认知"),
    ("分割问题", "descartes", "拆到最小单元每个都可行动，拆解粒度定执行力", "决策/组织"),
    ("举证责任", "dennett", "谁断言谁举证，无证据只是意见不是结论", "决策/认知"),
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
with open(f"{OUT}/philosophy-glossary.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"哲学概念词典已生成（{len(CONCEPTS)} 词）")
print("全部完成")
