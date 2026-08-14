# -*- coding: utf-8 -*-
"""扩展批次 P6：认知科学思想家（平克/丹尼特）+ 现有 15 位思想家加深"""

POWERS_P6 = [
# ---------- 史蒂芬·平克 ----------
{"id":"pinker_01","knowledge":"语言本能：语言能力是人类先天的认知模块。商业启示：理解用户先理解他们的语言习惯——文案、命名、沟通方式顺应语言直觉，别用反直觉的表达。","original":"史蒂芬·平克《语言本能》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"1994","topics":["认知","内容"],"skills":["poe-content","poe-deconstruct","poe-ai-check"],"type":"principle","confidence":"high","audience":"🔬"},
{"id":"pinker_02","knowledge":"心智是计算系统：思维是符号与规则的计算过程。商业启示：把『用户怎么想』建模成输入-规则-输出，模型化理解才能规模化优化产品。","original":"史蒂芬·平克《心智如何工作》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"1997","topics":["认知","产品"],"skills":["poe-diagnosis","poe-deconstruct","poe-good-question"],"type":"principle","confidence":"medium","audience":"🔬"},
{"id":"pinker_03","knowledge":"暴力在下降：数据表明人类暴力长期持续下降。商业启示：直觉感受的趋势（『世风日下』）常与数据相反，重要判断以长期数据为准，别被短期情绪叙事带偏。","original":"史蒂芬·平克《人性中的善良天使》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"2011","topics":["认知","市场"],"skills":["poe-verify","poe-standard-answer","poe-ai-check"],"type":"insight","confidence":"medium","audience":"⚠️🔬"},
{"id":"pinker_04","knowledge":"风格感：清楚的写作是清晰思考的外在表现。商业启示：写不清往往是没想清，要求团队把方案写清楚本身就是强制思考。","original":"史蒂芬·平克《风格感觉》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"2014","topics":["内容","认知"],"skills":["poe-content","poe-ai-check","poe-good-question"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"pinker_05","knowledge":"贝叶斯理性：理性判断=先验×新证据的更新。商业启示：做判断先写清先验概率，再问『新信息改变了多少』，避免只盯着最新热点事件。","original":"史蒂芬·平克《理性》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"2021","topics":["决策","认知"],"skills":["poe-decision","poe-verify","poe-good-question"],"type":"method","confidence":"high","audience":"🔬💼"},
{"id":"pinker_06","knowledge":"人性共通性：不同文化的人共享基本心理机制。商业启示：跨国、跨平台做产品，底层需求共通，表层偏好不同——先抓住共通的人性，再做本地化。","original":"史蒂芬·平克《白板》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"2002","topics":["市场","产品"],"skills":["poe-diagnosis","poe-benchmark","poe-resonate"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"pinker_07","knowledge":"道德直觉先于道德推理：人先有对错直觉，再找理由辩护。商业启示：品牌与危机沟通要顺应道德直觉（诚实、公平、尊重），事后讲道理补救效果有限。","original":"史蒂芬·平克《白板》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"2002","topics":["心理","内容"],"skills":["poe-resonate","poe-content","poe-content-risk-check"],"type":"principle","confidence":"medium","audience":"💼"},
{"id":"pinker_08","knowledge":"进步主义证据：用数据衡量进步，而非叙事。商业启示：评价趋势、策略、团队用『可对比的长期数据』，故事讲得再好也不能替代指标。","original":"史蒂芬·平克《当下的启蒙》","url":"https://zh.wikipedia.org/wiki/史蒂芬·平克","date":"2018","topics":["决策","认知"],"skills":["poe-verify","poe-decision","poe-standard-answer"],"type":"principle","confidence":"high","audience":"🔬💼"},

# ---------- 丹尼尔·丹尼特 ----------
{"id":"dennett_01","knowledge":"意向立场：把复杂系统当作『有理性的主体』来预测其行为。商业启示：分析用户、竞品、对手时，用『他想要什么、会怎么选』的意向立场预测，比研究其内部细节更高效。","original":"丹尼尔·丹尼特《意向立场》","url":"https://zh.wikipedia.org/wiki/丹尼尔·丹尼特","date":"1987","topics":["认知","决策"],"skills":["poe-benchmark","poe-decision","poe-standard-answer"],"type":"method","confidence":"high","audience":"🔬💼"},
{"id":"dennett_02","knowledge":"设计立场与物理立场：预测系统可以用物理规律，也可以用设计意图。商业启示：分析一个业务，先试『物理立场』（成本、约束），再试『设计立场』（它被设计来干嘛），最后才用意向立场。","original":"丹尼尔·丹尼特《意向立场》","url":"https://zh.wikipedia.org/wiki/丹尼尔·丹尼特","date":"1987","topics":["认知","决策"],"skills":["poe-deconstruct","poe-diagnosis","poe-decision"],"type":"method","confidence":"high","audience":"🔬💼"},
{"id":"dennett_03","knowledge":"举证责任：谁断言谁举证，断言方必须给出可检验的证据。商业启示：『我觉得市场会接受』这类断言，提出者负责拿证据，否则只是意见不是结论。","original":"丹尼尔·丹尼特（批判性思维）","url":"https://zh.wikipedia.org/wiki/丹尼尔·丹尼特","date":"1995","topics":["决策","认知"],"skills":["poe-verify","poe-ai-check","poe-good-question"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"dennett_04","knowledge":"危险的观念：好的观念会自我传播、自我繁殖。商业启示：做传播与品牌，内容本身要有『观念的种子』——让人想转述、想引用，传播是观念属性的结果。","original":"丹尼尔·丹尼特《达尔文的危险思想》","url":"https://zh.wikipedia.org/wiki/丹尼尔·丹尼特","date":"1995","topics":["传播","内容"],"skills":["poe-spread","poe-content","poe-resonate"],"type":"insight","confidence":"high","audience":"🔬💼"},
{"id":"dennett_05","knowledge":"多草稿模型：意识是多个平行过程的竞争结果，没有单一『自我』。商业启示：组织决策也是多草稿竞争——别只让一个方案自嗨，同时推几个候选再择优。","original":"丹尼尔·丹尼特《意识的解释》","url":"https://zh.wikipedia.org/wiki/丹尼尔·丹尼特","date":"1991","topics":["认知","决策"],"skills":["poe-decision","poe-chatroom","poe-good-question"],"type":"insight","confidence":"medium","audience":"🔬"},
{"id":"dennett_06","knowledge":"乐观主义方法论：复杂问题都能拆解成可处理的小问题。商业启示：『不可能』常常只是『还没拆开』，把大目标拆到可行动粒度再判断可行性。","original":"丹尼尔·丹尼特（方法论）","url":"https://zh.wikipedia.org/wiki/丹尼尔·丹尼特","date":"1991","topics":["决策","心态"],"skills":["poe-goal","poe-good-question","poe-action"],"type":"principle","confidence":"high","audience":"🔬💼"},

# ---------- 休谟（加深） ----------
{"id":"hume_05","knowledge":"温和怀疑主义：知识有边界，但边界内可以实用地生活。商业启示：别因『什么都不能确定』而停止行动，确定不了的用试错与缓冲带处理。","original":"大卫·休谟《人类理解研究》","url":"https://zh.wikipedia.org/wiki/大卫·休谟","date":"1748","topics":["决策","认知"],"skills":["poe-decision","poe-verify","poe-action"],"type":"principle","confidence":"high","audience":"🔬"},
{"id":"hume_06","knowledge":"理性是激情的奴隶：理性服务于情感与欲望。商业启示：说服先动情绪再讲逻辑，理性论证是给已动情的人递台阶。","original":"大卫·休谟《人性论》","url":"https://zh.wikipedia.org/wiki/大卫·休谟","date":"1740","topics":["心理","内容"],"skills":["poe-content","poe-resonate","poe-hook"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"hume_07","knowledge":"习惯是人生指南：多数行动靠习惯而非推理。商业启示：用户的行为习惯比理性分析更顽固，改变用户行为优先『顺应习惯』而非『教育用户』。","original":"大卫·休谟《人类理解研究》","url":"https://zh.wikipedia.org/wiki/大卫·休谟","date":"1748","topics":["心理","产品"],"skills":["poe-diagnosis","poe-content","poe-resonate"],"type":"principle","confidence":"high","audience":"💼"},

# ---------- 康德（加深） ----------
{"id":"kant_04","knowledge":"人是目的不是手段：人不能被当作纯工具使用。商业启示：把员工、用户当达成目的的工具，短期得利、长期失去信任，尊重人是可持续经营的前提。","original":"伊曼努尔·康德《道德形而上学奠基》","url":"https://zh.wikipedia.org/wiki/伊曼努尔·康德","date":"1785","topics":["价值观","组织"],"skills":["poe-diagnosis","poe-goal","poe-decision"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"kant_05","knowledge":"绝对命令：只按你能愿意它成为普遍法则的准则行动。商业启示：决策前问『如果所有人（含竞品）都这么做，世界会怎样』，这一问过滤掉大量短期主义。","original":"伊曼努尔·康德《道德形而上学奠基》","url":"https://zh.wikipedia.org/wiki/伊曼努尔·康德","date":"1785","topics":["价值观","决策"],"skills":["poe-decision","poe-verify","poe-content-risk-check"],"type":"principle","confidence":"medium","audience":"💼"},
{"id":"kant_06","knowledge":"先验框架：没有框架我们无法理解任何经验。商业启示：任何数据都需要解释框架才成为信息，汇报时先声明框架再摆数据，否则数字可以讲出相反故事。","original":"伊曼努尔·康德《纯粹理性批判》","url":"https://zh.wikipedia.org/wiki/伊曼努尔·康德","date":"1781","topics":["认知","决策"],"skills":["poe-ai-check","poe-deconstruct","poe-verify"],"type":"principle","confidence":"high","audience":"🔬💼"},

# ---------- 波普尔（加深） ----------
{"id":"popper_04","knowledge":"批判理性主义：理性不是证明对，而是接受被批评与修正。商业启示：建立『欢迎被推翻』的会议文化，方案被推翻是进步，不是面子损失。","original":"卡尔·波普尔《猜想与反驳》","url":"https://zh.wikipedia.org/wiki/卡尔·波普尔","date":"1963","topics":["决策","组织"],"skills":["poe-verify","poe-decision","poe-chatroom"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"popper_05","knowledge":"渐进工程：社会改良要小步试错，反对整体蓝图。商业启示：变革用试点-验证-推广的节奏，一次推全量高风险改革是赌博。","original":"卡尔·波普尔《开放社会及其敌人》","url":"https://zh.wikipedia.org/wiki/卡尔·波普尔","date":"1945","topics":["决策","组织"],"skills":["poe-slowisfast","poe-goal","poe-decision"],"type":"method","confidence":"high","audience":"💼"},
{"id":"popper_06","knowledge":"开放社会：容忍批评与多元的社会更有适应力。商业启示：组织的开放度决定信息质量，允许质疑的组织比一言堂更能纠错。","original":"卡尔·波普尔《开放社会及其敌人》","url":"https://zh.wikipedia.org/wiki/卡尔·波普尔","date":"1945","topics":["组织","价值观"],"skills":["poe-diagnosis","poe-verify","poe-decision"],"type":"principle","confidence":"high","audience":"🔬💼"},

# ---------- 维特根斯坦（加深） ----------
{"id":"witt_04","knowledge":"语言游戏：词的意义在于使用情境。商业启示：同样的词在不同部门含义不同，跨团队协作先对齐『这个词在我们这里指什么』。","original":"路德维希·维特根斯坦《哲学研究》","url":"https://zh.wikipedia.org/wiki/路德维希·维特根斯坦","date":"1953","topics":["语言思维","组织"],"skills":["poe-deconstruct","poe-good-question","poe-ai-check"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"witt_05","knowledge":"私人语言不可能：独自确认的标准不是标准。商业启示：『我觉得质量没问题』不是可验证标准，定义可共同观察的验收标准，否则沟通全靠默契。","original":"路德维希·维特根斯坦《哲学研究》","url":"https://zh.wikipedia.org/wiki/路德维希·维特根斯坦","date":"1953","topics":["语言思维","组织"],"skills":["poe-goal","poe-deconstruct","poe-good-question"],"type":"principle","confidence":"high","audience":"🔬💼"},

# ---------- 多伊奇（加深） ----------
{"id":"deutsch_04","knowledge":"好的解释：科学知识是对世界的解释，而非预测机器的输出。商业启示：真正理解业务=能给出『为什么』的机制解释，只会报数的团队没有理解。","original":"戴维·多伊奇《真实世界的脉络》","url":"https://zh.wikipedia.org/wiki/戴维·多伊奇","date":"1997","topics":["认知","决策"],"skills":["poe-deconstruct","poe-diagnosis","poe-good-question"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"deutsch_05","knowledge":"乐观主义：所有问题原则上都可解，只要找到好的解释。商业启示：遇到僵局先别认命，问题无解往往是因为解释框架错了，换解释再试。","original":"戴维·多伊奇《无穷的开始》","url":"https://zh.wikipedia.org/wiki/戴维·多伊奇","date":"2011","topics":["心态","创新"],"skills":["poe-action","poe-good-question","poe-standard-answer"],"type":"principle","confidence":"high","audience":"🔬💼"},

# ---------- 斯密（加深） ----------
{"id":"smith_04","knowledge":"道德情感：同情共感是人类道德的基础。商业启示：品牌与组织要有共情能力，只算利益账的组织会失去人心，人心账最终会回到利益账。","original":"亚当·斯密《道德情操论》","url":"https://zh.wikipedia.org/wiki/亚当·斯密","date":"1759","topics":["价值观","组织"],"skills":["poe-resonate","poe-diagnosis","poe-content"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"smith_05","knowledge":"市场教会合作：交换让陌生人学会互利。商业启示：把团队内部也当『市场』——跨部门协作设计成双方获利的交换，比命令与情感绑架更持久。","original":"亚当·斯密《国富论》","url":"https://zh.wikipedia.org/wiki/亚当·斯密","date":"1776","topics":["市场","组织"],"skills":["poe-diagnosis","poe-standard-answer","poe-decision"],"type":"insight","confidence":"medium","audience":"💼"},
{"id":"smith_06","knowledge":"正义的制度：正义是社会的支柱，仁慈是装饰。商业启示：管理靠制度而非指望仁慈，把关键行为写成规则与底线，靠人情维持的秩序会塌。","original":"亚当·斯密《道德情操论》","url":"https://zh.wikipedia.org/wiki/亚当·斯密","date":"1759","topics":["机制设计","组织"],"skills":["poe-diagnosis","poe-decision","poe-goal"],"type":"principle","confidence":"high","audience":"💼"},

# ---------- 米塞斯（加深） ----------
{"id":"mises_04","knowledge":"行动学：人的行动总是追求目标、克服障碍。商业启示：分析员工与用户行为先问『他在追求什么目标』，行为异常往往是目标错位而非人品问题。","original":"路德维希·冯·米塞斯《人的行动》","url":"https://zh.wikipedia.org/wiki/路德维希·冯·米塞斯","date":"1949","topics":["决策","组织"],"skills":["poe-action","poe-diagnosis","poe-good-question"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"mises_05","knowledge":"企业家利润：利润来自发现别人没看见的套利机会。商业启示：超额利润的合法来源是信息差与洞察差，持续问『别人没看见什么』。","original":"路德维希·冯·米塞斯《人的行动》","url":"https://zh.wikipedia.org/wiki/路德维希·冯·米塞斯","date":"1949","topics":["商业模式","创新"],"skills":["poe-standard-answer","poe-benchmark","poe-diagnosis"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"mises_06","knowledge":"时间偏好：人天然偏好现在多于未来。商业启示：让用户『现在就要』（即时价值、立刻见效）比画未来大饼有效，产品设计先给当下回报。","original":"路德维希·冯·米塞斯《人的行动》","url":"https://zh.wikipedia.org/wiki/路德维希·冯·米塞斯","date":"1949","topics":["心理","产品"],"skills":["poe-content","poe-resonate","poe-diagnosis"],"type":"principle","confidence":"high","audience":"💼"},

# ---------- 哈耶克（加深） ----------
{"id":"hayek_04","knowledge":"知识分工：没有任何人拥有全部知识。商业启示：别迷信『最懂的人』，把决策权下放给掌握相关局部知识的人，中央集权必然信息失真。","original":"弗里德里希·哈耶克《知识在社会中的运用》","url":"https://zh.wikipedia.org/wiki/弗里德里希·哈耶克","date":"1945","topics":["组织","决策"],"skills":["poe-diagnosis","poe-decision","poe-knowledge"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"hayek_05","knowledge":"竞争作为发现程序：竞争的价值在于发现未知的更好方案。商业启示：内部赛马、A/B 测试、多方案并行都是『发现程序』，别用一次规划代替持续竞争。","original":"弗里德里希·哈耶克《竞争的含义》","url":"https://zh.wikipedia.org/wiki/弗里德里希·哈耶克","date":"1948","topics":["市场","创新"],"skills":["poe-standard-answer","poe-decision","poe-benchmark"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"hayek_06","knowledge":"规则优于命令：一般性规则比具体指令更能适应变化。商业启示：给团队定原则与底线（规则），别事事下指令，规则治下的组织才有自组织能力。","original":"弗里德里希·哈耶克《法律、立法与自由》","url":"https://zh.wikipedia.org/wiki/弗里德里希·哈耶克","date":"1973","topics":["机制设计","组织"],"skills":["poe-diagnosis","poe-goal","poe-decision"],"type":"principle","confidence":"high","audience":"💼"},

# ---------- 老子（加深） ----------
{"id":"laozi_04","knowledge":"上善若水：柔韧比刚强更能持久。商业启示：应对强势对手与硬碰硬的下策不同，灵活、绕行、顺势的策略成本更低、存活更久。","original":"老子《道德经》","url":"https://zh.wikipedia.org/wiki/道德经","date":"公元前400","topics":["战略","心态"],"skills":["poe-standard-answer","poe-decision","poe-slowisfast"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"laozi_05","knowledge":"知止不殆：知道何时停止才不危险。商业启示：扩张、烧钱、加功能都有临界点，懂得收手与止损的组织活得比贪大的久。","original":"老子《道德经》","url":"https://zh.wikipedia.org/wiki/道德经","date":"公元前400","topics":["决策","心态"],"skills":["poe-decision","poe-slowisfast","poe-goal"],"type":"principle","confidence":"high","audience":"💼"},

# ---------- 阿德勒（加深） ----------
{"id":"adler_05","knowledge":"生活风格：人早年形成的应对模式贯穿一生。商业启示：团队的『习惯性反应』（遇事先甩锅、先报喜）也是组织早年形成的风格，改行为先改风格。","original":"阿尔弗雷德·阿德勒《自卑与超越》","url":"https://zh.wikipedia.org/wiki/阿尔弗雷德·阿德勒","date":"1931","topics":["心理","组织"],"skills":["poe-action","poe-diagnosis","poe-goal"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"adler_06","knowledge":"自卑与超越：自卑感是成长的动力而非缺陷。商业启示：承认差距（自卑）才能驱动改进（超越），团队里『我们还不够好』的紧迫感是进步的燃料。","original":"阿尔弗雷德·阿德勒《自卑与超越》","url":"https://zh.wikipedia.org/wiki/阿尔弗雷德·阿德勒","date":"1931","topics":["心理","激励"],"skills":["poe-action","poe-goal","poe-slowisfast"],"type":"principle","confidence":"high","audience":"💼"},
{"id":"adler_07","knowledge":"横向关系：平等对话而非上下施压。商业启示：把『我命令你』改成『我们一起决定』，横向关系的团队信息流动更顺畅、决策质量更高。","original":"阿尔弗雷德·阿德勒（个体心理学）","url":"https://zh.wikipedia.org/wiki/阿尔弗雷德·阿德勒","date":"1931","topics":["组织","沟通"],"skills":["poe-action","poe-diagnosis","poe-good-question"],"type":"principle","confidence":"medium","audience":"💼"},

# ---------- 叔本华（加深） ----------
{"id":"schopenhauer_04","knowledge":"生命意志：欲望满足即无聊，不满足即痛苦。商业启示：理解用户『满足后又空虚』的循环，做产品或内容要么持续提供新意义，要么帮用户跳出循环。","original":"阿图尔·叔本华《作为意志和表象的世界》","url":"https://zh.wikipedia.org/wiki/阿图尔·叔本华","date":"1818","topics":["心理","产品"],"skills":["poe-resonate","poe-diagnosis","poe-content"],"type":"principle","confidence":"medium","audience":"⚠️💼"},
{"id":"schopenhauer_05","knowledge":"独处与内在丰富：能从独处中获益的人内在丰富。商业启示：深度工作、独立思考是稀缺能力，给团队留不被打扰的时间，别用会议填满一切。","original":"阿图尔·叔本华《人生的智慧》","url":"https://zh.wikipedia.org/wiki/阿图尔·叔本华","date":"1851","topics":["心态","组织"],"skills":["poe-slowisfast","poe-action","poe-goal"],"type":"principle","confidence":"medium","audience":"💼"},

# ---------- 马可·奥勒留（加深） ----------
{"id":"marcus_04","knowledge":"专注当下：不为过去悔恨、不为未来焦虑，只做此刻该做之事。商业启示：复盘与规划之外，执行期只处理当下，身心合一是效率与心态的底层。","original":"马可·奥勒留《沉思录》","url":"https://zh.wikipedia.org/wiki/马可·奥勒留","date":"180","topics":["心态","决策"],"skills":["poe-action","poe-slowisfast","poe-goal"],"type":"principle","confidence":"high","audience":"🔥💼"},
{"id":"marcus_05","knowledge":"美德即行动：不做空谈，以行动定义自己。商业启示：价值观要以行为检验——看一个组织信什么，别看它的墙贴，看它发钱、开人、排优先级时怎么选。","original":"马可·奥勒留《沉思录》","url":"https://zh.wikipedia.org/wiki/马可·奥勒留","date":"180","topics":["价值观","组织"],"skills":["poe-diagnosis","poe-goal","poe-decision"],"type":"principle","confidence":"high","audience":"💼"},

# ---------- 尼采（加深） ----------
{"id":"nietzsche_04","knowledge":"永恒轮回：如果一切将无限重演，你此刻的选择就是永恒的选择。商业启示：把每个重要决策当作会永远重播的选择，『做了十年后还愿意重复吗』过滤冲动。","original":"弗里德里希·尼采《快乐的科学》","url":"https://zh.wikipedia.org/wiki/弗里德里希·尼采","date":"1882","topics":["心态","决策"],"skills":["poe-decision","poe-slowisfast","poe-goal"],"type":"principle","confidence":"low","audience":"⚠️🔥"},
{"id":"nietzsche_05","knowledge":"自我超越：人是要被超越的存在，成为你自己。商业启示：组织的天花板是自我设限，持续挑战『我们只能做到这样』的信念，超越从打破自我定义开始。","original":"弗里德里希·尼采《查拉图斯特拉如是说》","url":"https://zh.wikipedia.org/wiki/弗里德里希·尼采","date":"1883","topics":["心态","价值观"],"skills":["poe-goal","poe-action","poe-slowisfast"],"type":"principle","confidence":"low","audience":"⚠️🔥"},

# ---------- 加缪（加深） ----------
{"id":"camus_04","knowledge":"西西弗斯：把重复的推石劳动变成反抗与意义。商业启示：枯燥的日常工作是多数人的宿命，给重复劳动注入意义感（用户价值、成长叙事）是管理者的必修课。","original":"阿尔贝·加缪《西西弗神话》","url":"https://zh.wikipedia.org/wiki/阿尔贝·加缪","date":"1942","topics":["心态","激励"],"skills":["poe-action","poe-goal","poe-content"],"type":"principle","confidence":"high","audience":"🔥💼"},
{"id":"camus_05","knowledge":"反抗：不接受不合理的既定命运。商业启示：对行业惯例、市场共识保持『反抗式审视』，默认接受现状的组织放弃了改写规则的权利。","original":"阿尔贝·加缪《反抗者》","url":"https://zh.wikipedia.org/wiki/阿尔贝·加缪","date":"1951","topics":["创新","价值观"],"skills":["poe-standard-answer","poe-deconstruct","poe-goal"],"type":"principle","confidence":"medium","audience":"🔥💼"},

# ---------- 罗素（加深） ----------
{"id":"russell_05","knowledge":"避免教条：对确定性保持警惕，教条是认知的坟墓。商业启示：『绝对正确』的信念会让组织失去校准能力，给结论留修正空间。","original":"伯特兰·罗素《西方哲学史》","url":"https://zh.wikipedia.org/wiki/伯特兰·罗素","date":"1945","topics":["认知","心态"],"skills":["poe-verify","poe-deconstruct","poe-decision"],"type":"principle","confidence":"high","audience":"🔬💼"},
{"id":"russell_06","knowledge":"无知之乐：承认并拥抱自己的无知，好奇心由此而生。商业启示：『我不知道』的提问比『我知道』的断言更有价值，鼓励提问的组织学习更快。","original":"伯特兰·罗素《幸福之路》","url":"https://zh.wikipedia.org/wiki/伯特兰·罗素","date":"1930","topics":["学习","心态"],"skills":["poe-learning","poe-good-question","poe-goal"],"type":"principle","confidence":"high","audience":"🔬🔥"},
]
