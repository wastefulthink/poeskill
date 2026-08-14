# -*- coding: utf-8 -*-
"""四大知识专题·Part 2：人性与个体动机 + 价值与精神哲学"""

ATOMS_P2 = [
# ========== 专题三：人性与个体动机 ==========
# --- 阿德勒（1931《自卑与超越》）---
{"id": "adler_01", "knowledge": "目的论：人的行为不是被过去（创伤、性格）决定，而是被当下目标牵引——先有目的，再为它寻找理由。商业启示：员工很多『性格问题』其实是目的驱动的行为：迟到可能是逃离压力的目的，不是懒。别贴标签，先找行为在服务什么目的。", "original": "阿德勒《自卑与超越》(1931)", "url": "阿德勒《自卑与超越》(1931)", "date": "1931", "topics": ["心理", "组织"], "skills": ["poe-action", "poe-resonate", "poe-content"], "type": "principle", "confidence": "medium", "audience": "🔥"},
{"id": "adler_02", "knowledge": "追求优越感：人天然追求『变得更好』的向上冲动；自卑感是正常起点，关键在于把它转化为建设性努力还是掩盖性借口。商业启示：管理者看见个体内心的优越感诉求——给进步以可见反馈，比单纯加薪更能激活长期动力。", "original": "阿德勒《自卑与超越》(1931)", "url": "阿德勒《自卑与超越》(1931)", "date": "1931", "topics": ["心理", "组织"], "skills": ["poe-action", "poe-resonate"], "type": "principle", "confidence": "medium", "audience": "🔥"},
{"id": "adler_03", "knowledge": "共同体感觉：健康的自我是在为共同体贡献中获得的——人需要归属感与贡献感。商业启示：构建团队共同体，而非单纯奖惩——让成员感到『我的贡献被看见、我在共同体中有位置』，是激励的底层结构。", "original": "阿德勒《自卑与超越》(1931)", "url": "阿德勒《自卑与超越》(1931)", "date": "1931", "topics": ["组织", "心理"], "skills": ["poe-action", "poe-spread", "poe-content"], "type": "principle", "confidence": "medium", "audience": "🔥"},
{"id": "adler_04", "knowledge": "洞察：所有烦恼都来自人际关系——阿德勒把人的心理困境归结为关系问题而非孤立缺陷。商业启示：团队矛盾的本质多是人际关系矛盾，先处理关系再谈对错；组织冲突解决的第一刀，永远是『人-人』而非『事-事』。", "original": "阿德勒《被讨厌的勇气》思想源头(1931)", "url": "阿德勒《自卑与超越》(1931)", "date": "1931", "topics": ["心理", "组织"], "skills": ["poe-action", "poe-resonate"], "type": "insight", "confidence": "medium", "audience": "🔥"},

# --- 叔本华（1818《作为意志和表象的世界》）---
{"id": "schopenhauer_01", "knowledge": "意志为本：世界底层是永不停歇的欲望之流（意志），理智只是它的工具。商业启示：理解欲望驱动人性——用户购买、员工奋斗、创业者冒险，底层都是欲望；营销就是与欲望对话，而不是与理性对话。", "original": "叔本华《作为意志和表象的世界》(1818)", "url": "叔本华《作为意志和表象的世界》(1818)", "date": "1818", "topics": ["心理", "内容"], "skills": ["poe-resonate", "poe-spread", "poe-content"], "type": "principle", "confidence": "medium", "audience": "🔥"},
{"id": "schopenhauer_02", "knowledge": "欲望带来痛苦：欲望不满足则痛苦，满足则空虚，人生如钟摆在两端摆动。商业启示：创业者的欲望管理——把『必须成功』的执念降级为『做成此事值得一试』，反而减少决策扭曲与焦虑瘫痪。", "original": "叔本华《作为意志和表象的世界》(1818)", "url": "叔本华《作为意志和表象的世界》(1818)", "date": "1818", "topics": ["心理", "决策"], "skills": ["poe-action", "poe-resonate"], "type": "principle", "confidence": "medium", "audience": "🔥"},
{"id": "schopenhauer_03", "knowledge": "方法：预期管理——降低对他人与环境的过高期待，管理预期以对抗焦虑。商业启示：对合作方、员工、市场回报设定『预期区间』而非单点期望：最好的结果值得庆祝，最差的结果提前备好预案，焦虑源于把期望当成承诺。", "original": "叔本华《人生的智慧》(1851)", "url": "叔本华《人生的智慧》(1851)", "date": "1851", "topics": ["心理", "决策"], "skills": ["poe-action", "poe-decision"], "type": "method", "confidence": "medium", "audience": "🔥"},

# --- 马可·奥勒留（约170-180《沉思录》）---
{"id": "marcus_01", "knowledge": "控制二分法：分清什么是可控的、什么不可控，只对可控部分负责。『我们的力量无法控制一切，但能控制自己的判断与行动。』商业启示：危机决策第一原则——把问题拆成可控/不可控两栏，把全部精力放在可控栏。", "original": "马可·奥勒留《沉思录》(约170-180)", "url": "马可·奥勒留《沉思录》(约170-180)", "date": "180", "topics": ["心理", "决策"], "skills": ["poe-action", "poe-decision", "poe-slowisfast"], "type": "principle", "confidence": "high", "audience": "🔥💼"},
{"id": "marcus_02", "knowledge": "逆境自律：障碍不是阻碍，是练习场——『阻碍行动的反而推动行动』。商业启示：逆风时决策者的心态建设：把危机当作成本最低的压测，每一次被迫收缩都在暴露平时看不见的脆弱点，修复它就是增长。", "original": "马可·奥勒留《沉思录》(约170-180)", "url": "马可·奥勒留《沉思录》(约170-180)", "date": "180", "topics": ["心理", "决策"], "skills": ["poe-action", "poe-standard-answer"], "type": "principle", "confidence": "high", "audience": "🔥💼"},
{"id": "marcus_03", "knowledge": "向内自省：每日检视自己的判断与行为，不指责外界。商业启示：高管自我管理——复盘会上先问『我哪部分判断错了』，再问外部因素；向内归因的团队复盘效率远高于向外归因的追责会。", "original": "马可·奥勒留《沉思录》(约170-180)", "url": "马可·奥勒留《沉思录》(约170-180)", "date": "180", "topics": ["心理", "组织"], "skills": ["poe-action", "poe-decision"], "type": "insight", "confidence": "medium", "audience": "🔥💼"},

# ========== 专题四：价值与精神哲学（选择性参考） ==========
# --- 尼采（1883-85《查拉图斯特拉如是说》）---
{"id": "nietzsche_01", "knowledge": "重估一切价值：上帝已死——传统价值体系失效后，人必须自己为价值立法。商业启示：商业世界需要重估世俗既定价值，敢于打破行业旧范式——『行业惯例』『别人都这么做』恰恰是最该被重估的对象。", "original": "尼采《查拉图斯特拉如是说》(1883-85)", "url": "尼采《查拉图斯特拉如是说》(1883-85)", "date": "1885", "topics": ["价值观", "内容"], "skills": ["poe-content", "poe-standard-answer", "poe-deconstruct"], "type": "principle", "confidence": "medium", "audience": "🔥⚠️"},
{"id": "nietzsche_02", "knowledge": "权力意志：生命本质是扩张与自我超越的意志，不是求生存而是求更强。商业启示：强者的扩张冲动——创业者的意志力是稀缺资产，但要注意：尼采的『权力意志』极易被误读为不择手段的扩张，参考时必须用理性做节制（见罗素对冲条目）。", "original": "尼采《查拉图斯特拉如是说》(1883-85)", "url": "尼采《查拉图斯特拉如是说》(1883-85)", "date": "1885", "topics": ["价值观"], "skills": ["poe-content", "poe-verify"], "type": "principle", "confidence": "medium", "audience": "🔥⚠️"},
{"id": "nietzsche_03", "knowledge": "反模式：奴隶道德与道德绑架——弱者以『善良』为名规训强者，把平庸包装成美德。商业启示：警惕弱者道德绑架强者：『你都这么成功了凭什么不帮我』『赚钱就是不道德』——但反向同样危险，不可全盘接纳尼采，他是最容易断章取义的思想家，务必对照罗素/康德使用。", "original": "尼采《道德的谱系》(1887)", "url": "尼采《道德的谱系》(1887)", "date": "1887", "topics": ["价值观", "组织"], "skills": ["poe-verify", "poe-content"], "type": "anti-pattern", "confidence": "medium", "audience": "🔥⚠️"},

# --- 罗素·对冲尼采（1930《幸福之路》/1945《西方哲学史》）---
{"id": "russell_val_01", "knowledge": "理性节制：激情需要理性约束，个人自由以他人同等自由为边界。商业启示：创业者的强大意志不能变成无边界的扩张冲动——对市场、对竞对、对员工，权力都必须设界；没有节制的强者意志是组织灾难的开始。", "original": "罗素《幸福之路》(1930)", "url": "罗素《幸福之路》(1930)", "date": "1930", "topics": ["价值观", "组织"], "skills": ["poe-content", "poe-verify"], "type": "principle", "confidence": "high", "audience": "🔬🔥"},
{"id": "russell_val_02", "knowledge": "洞察：幸福来自多元欲望的平衡，而非单一欲望的无限满足——罗素与尼采的平衡点：强者精神值得肯定，但自我实现不能以他人自由为代价。商业启示：把权力意志当唯一信条的公司会走向自我毁灭，用理性做节制才是长期主义。", "original": "罗素《幸福之路》(1930)", "url": "罗素《幸福之路》(1930)", "date": "1930", "topics": ["价值观"], "skills": ["poe-verify", "poe-standard-answer"], "type": "insight", "confidence": "high", "audience": "🔬🔥"},

# --- 加缪（1942《西西弗神话》）---
{"id": "camus_01", "knowledge": "荒诞：世界本身没有预设意义，人却本能地追求意义——冲突即荒诞。商业启示：不确定性时代，商业本身没有预设意义；承认『没有标准答案』不是消极，是看清现实的第一步。", "original": "加缪《西西弗神话》(1942)", "url": "加缪《西西弗神话》(1942)", "date": "1942", "topics": ["价值观", "内容"], "skills": ["poe-content", "poe-standard-answer"], "type": "principle", "confidence": "medium", "audience": "🔥"},
{"id": "camus_02", "knowledge": "自我创造意义：在无先天意义的世界里，意义是人行动创造出来的。『应当想象西西弗是幸福的』——推石上山这个动作本身就有意义。商业启示：创业的『意义』不是被赋予的，是在持续行动中被创造出来的——先行动，意义在后面追你。", "original": "加缪《西西弗神话》(1942)", "url": "加缪《西西弗神话》(1942)", "date": "1942", "topics": ["价值观", "内容"], "skills": ["poe-content", "poe-action"], "type": "principle", "confidence": "medium", "audience": "🔥"},
{"id": "camus_03", "knowledge": "洞察：接纳困境继续行动——荒诞不是放弃的理由，而是清醒的前提；反抗荒诞的方式就是带着清醒继续生活。商业启示：逆境中最好的策略不是等意义明朗再行动，而是在行动中重建意义——接纳困境，继续推石头。", "original": "加缪《西西弗神话》(1942)", "url": "加缪《西西弗神话》(1942)", "date": "1942", "topics": ["价值观", "决策"], "skills": ["poe-content", "poe-action", "poe-standard-answer"], "type": "insight", "confidence": "medium", "audience": "🔥"},
]
