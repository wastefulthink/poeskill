# -*- coding: utf-8 -*-
"""四大知识专题·Part 1：科学认识论 + 市场与自发秩序（15 位人物中的 10 位）"""

AUD = {"hume": "🔬", "kant": "🔬", "popper": "🔬", "witt": "🔬", "deutsch": "🔬",
       "russell": "🔬🔥", "smith": "💼", "mises": "💼", "hayek": "💼", "laozi": "💼",
       "adler": "🔥", "schopenhauer": "🔥", "marcus": "🔥💼",
       "nietzsche": "🔥⚠️", "russell_val": "🔬🔥", "camus": "🔥"}

ATOMS_P1 = [
# ========== 专题一：科学认识论 ==========
# --- 休谟（1739-40《人性论》）---
{"id": "hume_01", "knowledge": "归纳问题：从有限经验推不出必然规律。太阳过去每天升起，不等于明天必然升起。商业启示：过去赚钱 ≠ 未来一定复制，把历史业绩当作必然定律是危险的。", "original": "休谟《人性论》(1739-40)", "url": "休谟《人性论》(1739-40)", "date": "1740", "topics": ["决策", "商业模式"], "skills": ["poe-decision", "poe-diagnosis", "poe-standard-answer"], "type": "principle", "confidence": "high", "audience": AUD["hume"]},
{"id": "hume_02", "knowledge": "因果只是人的心理习惯：我们看到的只是事件相继发生，因果联系是心灵的习惯性联想。商业启示：看到 A 发生接着 B 发生，别急着认定 A 导致 B——先找机制证据，再下因果结论。", "original": "休谟《人性论》(1739-40)", "url": "休谟《人性论》(1739-40)", "date": "1740", "topics": ["决策"], "skills": ["poe-decision", "poe-verify"], "type": "principle", "confidence": "high", "audience": AUD["hume"]},
{"id": "hume_03", "knowledge": "事实与价值二分：『市场发生了什么』是事实判断，『应该怎么做』是价值判断，两者不能混为一谈。商业启示：任何战略报告先拆开这两层，别用事实论证掩盖价值立场，也别用愿望倒推事实。", "original": "休谟《人性论》(1739-40)", "url": "休谟《人性论》(1739-40)", "date": "1740", "topics": ["决策", "价值观"], "skills": ["poe-decision", "poe-diagnosis", "poe-good-question"], "type": "principle", "confidence": "high", "audience": AUD["hume"]},
{"id": "hume_04", "knowledge": "反模式：经验主义迷信。把过往成功经验当成必然定律、把相关性当因果、把一次爆款当可复制方法论——都是休谟归纳问题的商业翻版。防御：每个『已验证的成功模式』都要追问：它的成立条件是什么？条件变了还成立吗？", "original": "休谟《人性论》(1739-40)", "url": "休谟《人性论》(1739-40)", "date": "1740", "topics": ["决策", "商业模式"], "skills": ["poe-diagnosis", "poe-verify", "poe-standard-answer"], "type": "anti-pattern", "confidence": "high", "audience": AUD["hume"]},

# --- 康德（1781《纯粹理性批判》）---
{"id": "kant_01", "knowledge": "认知滤镜：人只能看见经过心智框架加工的世界，不是世界本身。商业启示：所有人（包括你）都戴着认知滤镜看市场，管理者永远看不到纯粹客观真相——先承认这一点，再谈判断。", "original": "康德《纯粹理性批判》(1781)", "url": "康德《纯粹理性批判》(1781)", "date": "1781", "topics": ["决策", "心理"], "skills": ["poe-decision", "poe-diagnosis"], "type": "principle", "confidence": "high", "audience": AUD["kant"]},
{"id": "kant_02", "knowledge": "理性有边界：理性只能处理经验之内的对象，越界使用（证明上帝、设计完美社会、预测市场终局）必然产生幻象。商业启示：理性不能解决一切商业问题，懂得认知边界才不会盲目自信。", "original": "康德《纯粹理性批判》(1781)", "url": "康德《纯粹理性批判》(1781)", "date": "1781", "topics": ["决策"], "skills": ["poe-decision", "poe-good-question"], "type": "principle", "confidence": "high", "audience": AUD["kant"]},
{"id": "kant_03", "knowledge": "洞察：认知边界的实战价值——做重大决策前，显式列出『我的框架能看到什么、看不到什么』，用团队中不同框架的人对冲单点盲区；凡是声称『全部数据尽在掌握』的汇报，先怀疑其认知滤镜。", "original": "康德《纯粹理性批判》(1781)", "url": "康德《纯粹理性批判》(1781)", "date": "1781", "topics": ["决策", "组织"], "skills": ["poe-diagnosis", "poe-decision", "poe-verify"], "type": "insight", "confidence": "medium", "audience": AUD["kant"]},

# --- 波普尔（1934/1963《猜想与反驳》）---
{"id": "popper_01", "knowledge": "证伪主义：科学不能证实，只能证伪；一个理论的价值在于它敢冒被反例推翻的风险。商业启示：商业假设不要追求『证明我是对的』，要主动寻找能推翻自己方案的证据。", "original": "波普尔《猜想与反驳》(1963)", "url": "波普尔《猜想与反驳》(1963)", "date": "1963", "topics": ["决策"], "skills": ["poe-decision", "poe-good-question"], "type": "principle", "confidence": "high", "audience": AUD["popper"]},
{"id": "popper_02", "knowledge": "方法：反例优先审查——任何产品、战略、商业模式方案，先问『什么情况会证明它失败？』写下来，然后专门去验证这些失败条件。收集证据自圆其说 vs 设计实验主动证伪，是平庸公司与好公司的分水岭。", "original": "波普尔《猜想与反驳》(1963)", "url": "波普尔《猜想与反驳》(1963)", "date": "1963", "topics": ["决策", "商业模式"], "skills": ["poe-decision", "poe-verify", "poe-good-question"], "type": "method", "confidence": "high", "audience": AUD["popper"]},
{"id": "popper_03", "knowledge": "方法：试错淘汰（错误是进步机制）——大胆猜想、严格反驳、容忍失败。组织文化里禁止试错，等于禁止知识增长；但试错要有结构：小成本快速证伪，而不是大额押注后验证。", "original": "波普尔《猜想与反驳》(1963)", "url": "波普尔《猜想与反驳》(1963)", "date": "1963", "topics": ["决策", "组织"], "skills": ["poe-decision", "poe-diagnosis", "poe-standard-answer"], "type": "method", "confidence": "high", "audience": AUD["popper"]},

# --- 维特根斯坦（1921《逻辑哲学论》/1953《哲学研究》）---
{"id": "witt_01", "knowledge": "语言塑造思想：很多争论不是观点分歧，是语言概念的混乱。商业启示：大量商业内耗来自概念话术——『私域』『闭环』『赋能』各说各话，先厘清名词定义，再谈对错。", "original": "维特根斯坦《哲学研究》(1953)", "url": "维特根斯坦《哲学研究》(1953)", "date": "1953", "topics": ["语言思维", "内容"], "skills": ["poe-deconstruct", "poe-good-question", "poe-content"], "type": "principle", "confidence": "high", "audience": AUD["witt"]},
{"id": "witt_02", "knowledge": "可说的与不可说的：能说清楚的问题才能讨论，说不清的（宏大的、无边界的概念）保持沉默。商业启示：分不清边界的宏大愿景，不如落地为可描述、可验证的具体问题——『做行业第一』不可讨论，『下季度把复购率从 20% 提到 25%』可讨论。", "original": "维特根斯坦《逻辑哲学论》(1921)", "url": "维特根斯坦《逻辑哲学论》(1921)", "date": "1921", "topics": ["语言思维", "决策"], "skills": ["poe-good-question", "poe-deconstruct"], "type": "principle", "confidence": "high", "audience": AUD["witt"]},
{"id": "witt_03", "knowledge": "方法：概念澄清术——遇到争执，先做三件事：①这个词双方各自指什么；②换个更具体的词是否消除分歧；③如果换了词分歧消失，说明原来说的是同一个事。多数『战略争论』用这招五分钟化解。", "original": "维特根斯坦《哲学研究》(1953)", "url": "维特根斯坦《哲学研究》(1953)", "date": "1953", "topics": ["语言思维", "组织"], "skills": ["poe-deconstruct", "poe-good-question"], "type": "method", "confidence": "high", "audience": AUD["witt"]},

# --- 戴维·多伊奇（1997《真实世界的脉络》/2011《无穷的开始》）---
{"id": "deutsch_01", "knowledge": "解释性理论：进步来自创造更好的解释，而不是收集更多事实。企业同理——核心竞争力是『更好的解释』：解释市场为什么变化、用户为什么行动、竞品为什么失败；解释力即竞争力。", "original": "多伊奇《真实世界的脉络》(1997)", "url": "多伊奇《真实世界的脉络》(1997)", "date": "1997", "topics": ["决策", "内容"], "skills": ["poe-decision", "poe-content", "poe-standard-answer"], "type": "principle", "confidence": "high", "audience": AUD["deutsch"]},
{"id": "deutsch_02", "knowledge": "反归纳与乐观主义：多伊奇反对『未来复制过去』的归纳主义——文明进步不是靠重复，是靠创造新解释、新知识。商业启示：增长停滞时，模仿历史打法通常无效，真正的出路是生成关于市场的新解释。", "original": "多伊奇《无穷的开始》(2011)", "url": "多伊奇《无穷的开始》(2011)", "date": "2011", "topics": ["决策", "价值观"], "skills": ["poe-decision", "poe-standard-answer", "poe-verify"], "type": "principle", "confidence": "high", "audience": AUD["deutsch"]},
{"id": "deutsch_03", "knowledge": "洞察：问题一定存在解决方案，当前做不到不代表做不到。悲观主义是『问题无解』的自我实现预言。商业启示：面对看似无解的市场困局，先质疑约束条件本身——哪些限制是我们自己假设出来的？", "original": "多伊奇《无穷的开始》(2011)", "url": "多伊奇《无穷的开始》(2011)", "date": "2011", "topics": ["决策", "价值观"], "skills": ["poe-decision", "poe-content"], "type": "insight", "confidence": "medium", "audience": AUD["deutsch"]},

# --- 伯特兰·罗素（1945《西方哲学史》/1930《幸福之路》）---
{"id": "russell_01", "knowledge": "参差多态乃是幸福的本源：世界天然多元，单一标准答案是对生活的简化与剥夺。商业启示：团队、市场、用户天然多元，拒绝一刀切管理——统一话术、统一 KPI、统一风格的管理是在消灭创造土壤。", "original": "罗素《幸福之路》(1930)", "url": "罗素《幸福之路》(1930)", "date": "1930", "topics": ["价值观", "组织"], "skills": ["poe-deconstruct", "poe-content"], "type": "principle", "confidence": "high", "audience": AUD["russell"]},
{"id": "russell_02", "knowledge": "权力的来源分析：权力来自组织、财富、舆论、身份，而知识权力与身份权力经常被混淆。商业启示：看清组织内不同权力的类型——专业能力带来的权力可以争论，头衔带来的权力不容挑战；把两者混为一谈是组织衰败的起点。", "original": "罗素《权力论》(1938)", "url": "罗素《权力论》(1938)", "date": "1938", "topics": ["组织", "价值观"], "skills": ["poe-deconstruct", "poe-diagnosis"], "type": "principle", "confidence": "high", "audience": AUD["russell"]},
{"id": "russell_03", "knowledge": "反模式：教条与一元化真理——再伟大的理念也要接受理性审视，反对『唯正确论』。商业启示：警惕教条式战略：『我们一直这么做』『这是行业标准』『老板说的就是对的』，都是该被质疑的对象。", "original": "罗素《西方哲学史》(1945)", "url": "罗素《西方哲学史》(1945)", "date": "1945", "topics": ["价值观", "组织"], "skills": ["poe-verify", "poe-deconstruct", "poe-decision"], "type": "anti-pattern", "confidence": "high", "audience": AUD["russell"]},
{"id": "russell_04", "knowledge": "洞察：多样性是创新土壤——允许组织内部不同声音，异见者不是麻烦而是信号源。压制反对意见的组织，等于在自己大脑里切除了一部分感知能力。", "original": "罗素《西方哲学史》(1945)", "url": "罗素《西方哲学史》(1945)", "date": "1945", "topics": ["组织", "内容"], "skills": ["poe-deconstruct", "poe-content"], "type": "insight", "confidence": "medium", "audience": AUD["russell"]},

# ========== 专题二：市场与自发秩序 ==========
# --- 亚当·斯密（1776《国富论》）---
{"id": "smith_01", "knowledge": "看不见的手：个体自利行为可以间接促成社会整体福祉。商业启示：设计机制时不必强求参与者大公无私——尊重自利，把自利引导到与组织目标一致的方向，机制自然运转。", "original": "斯密《国富论》(1776)", "url": "斯密《国富论》(1776)", "date": "1776", "topics": ["市场", "商业模式"], "skills": ["poe-diagnosis", "poe-standard-answer"], "type": "principle", "confidence": "high", "audience": AUD["smith"]},
{"id": "smith_02", "knowledge": "自利与整体福祉：好的制度让个人追求私利的同时增进公共福利；坏的制度让个人获利即损害整体。商业启示：检查组织激励——员工/渠道/用户的自利行为，与公司目标一致还是背离？背离则改机制，别靠道德动员。", "original": "斯密《国富论》(1776)", "url": "斯密《国富论》(1776)", "date": "1776", "topics": ["市场", "组织"], "skills": ["poe-diagnosis", "poe-decision"], "type": "principle", "confidence": "high", "audience": AUD["smith"]},
{"id": "smith_03", "knowledge": "分工带来效率：制针厂一个工人全年做不出 20 根针，分工协作后人均日产数千根。商业启示：效率的底层来源是分工与专业化——评估任何业务时先问：任务拆分成专业化单元了吗？有没有重复造轮子？", "original": "斯密《国富论》(1776)", "url": "斯密《国富论》(1776)", "date": "1776", "topics": ["商业模式", "组织"], "skills": ["poe-diagnosis", "poe-benchmark"], "type": "case", "confidence": "high", "audience": AUD["smith"]},

# --- 米塞斯（1949《人的行动》）---
{"id": "mises_01", "knowledge": "主观价值论：价值来自人的主观感受，不是成本决定价格。商业启示：用户为感知价值付费，不为你的成本付费——定价锚定用户感知，成本只是下限参考；『成本加成』是商品思维，不是商业思维。", "original": "米塞斯《人的行动》(1949)", "url": "米塞斯《人的行动》(1949)", "date": "1949", "topics": ["市场", "商业模式"], "skills": ["poe-diagnosis", "poe-decision"], "type": "principle", "confidence": "high", "audience": AUD["mises"]},
{"id": "mises_02", "knowledge": "经济计算问题：中央计划者无法获得分散在市场中的全部信息，因而无法理性计算资源配置。商业启示：企业内部过度集中管控，会丧失分散个体的信息——高层无法掌握全部一线真实信息，决策权下放给信息最近的人。", "original": "米塞斯《人的行动》(1949)", "url": "米塞斯《人的行动》(1949)", "date": "1949", "topics": ["组织", "决策"], "skills": ["poe-diagnosis", "poe-decision", "poe-standard-answer"], "type": "principle", "confidence": "high", "audience": AUD["mises"]},
{"id": "mises_03", "knowledge": "人的行动学：一切经济现象源于有目的的人的行动；人总是用手段去追求目的。商业启示：分析用户行为先问『他的目的是什么，手段是什么』——行为分析不做目的假设，就只是数据堆砌。", "original": "米塞斯《人的行动》(1949)", "url": "米塞斯《人的行动》(1949)", "date": "1949", "topics": ["心理", "内容"], "skills": ["poe-content", "poe-resonate", "poe-spread"], "type": "principle", "confidence": "high", "audience": AUD["mises"]},

# --- 哈耶克（1944《通往奴役之路》/1988《致命的自负》）---
{"id": "hayek_01", "knowledge": "自发秩序：市场、语言、法律中大量优良秩序不是顶层设计出来的，而是个体互动演化生成的。商业启示：很多『好秩序』是长出来的不是管出来的——组织内部给局部试错空间，比依赖完美顶层规划更可靠。", "original": "哈耶克《致命的自负》(1988)", "url": "哈耶克《致命的自负》(1988)", "date": "1988", "topics": ["市场", "组织"], "skills": ["poe-diagnosis", "poe-decision", "poe-benchmark"], "type": "principle", "confidence": "high", "audience": AUD["hayek"]},
{"id": "hayek_02", "knowledge": "分散知识：关键信息以碎片形式分散在无数个体手中，无人能全部掌握。商业启示：一线拥有大量局部知识（客户反应、执行细节、真实阻力），尊重一线判断，决策流程别让信息在传递中失真。", "original": "哈耶克《知识在社会中的运用》(1945)", "url": "哈耶克《知识在社会中的运用》(1945)", "date": "1945", "topics": ["组织", "决策"], "skills": ["poe-diagnosis", "poe-decision"], "type": "principle", "confidence": "high", "audience": AUD["hayek"]},
{"id": "hayek_03", "knowledge": "反模式：理性的自负——人类过度设计一切（计划社会、万能战略、全能中台），以为理性可以推演全局。商业启示：迷信顶层完美规划是傲慢，给局部试错空间才是谦逊；凡是不依赖某个人全知全能也能运转的机制，才是好机制。", "original": "哈耶克《致命的自负》(1988)", "url": "哈耶克《致命的自负》(1988)", "date": "1988", "topics": ["决策", "组织"], "skills": ["poe-diagnosis", "poe-verify", "poe-decision"], "type": "anti-pattern", "confidence": "high", "audience": AUD["hayek"]},

# --- 老子（公元前6世纪《道德经》）---
{"id": "laozi_01", "knowledge": "无为：不强行干预，让事物按自身规律演化。『治大国若烹小鲜』——频繁翻动反而碎。商业启示：管理上减少无谓干预，给团队和业务留出自行演化的空间；过度管理是破坏秩序的根源。", "original": "老子《道德经》(约公元前6世纪)", "url": "老子《道德经》(约公元前6世纪)", "date": "-500", "topics": ["组织", "市场"], "skills": ["poe-diagnosis", "poe-slowisfast"], "type": "principle", "confidence": "medium", "audience": AUD["laozi"]},
{"id": "laozi_02", "knowledge": "顺势：知进退、察时机，不逆势而动。『上善若水』——水不争而利万物，遇形则变。商业启示：顺势而为优先于逆势硬拼——评估赛道时先看大势（周期、政策、技术代际），大方向错了执行力越强死得越快。", "original": "老子《道德经》(约公元前6世纪)", "url": "老子《道德经》(约公元前6世纪)", "date": "-500", "topics": ["市场", "决策"], "skills": ["poe-decision", "poe-diagnosis"], "type": "principle", "confidence": "medium", "audience": AUD["laozi"]},
{"id": "laozi_03", "knowledge": "洞察：周期与节奏——盛极而衰、否极泰来，扩张期留余量，收缩期保根本。商业启示：经济周期管理：景气时不透支，萧条时不死扛；企业的抗风险能力不在顺风时赚多少，在逆风时能活多久。", "original": "老子《道德经》(约公元前6世纪)", "url": "老子《道德经》(约公元前6世纪)", "date": "-500", "topics": ["决策", "市场"], "skills": ["poe-diagnosis", "poe-slowisfast", "poe-decision"], "type": "insight", "confidence": "medium", "audience": AUD["laozi"]},
]
