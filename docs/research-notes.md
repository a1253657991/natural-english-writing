# 研究依据与设计取舍

这份文件给维护者看，运行时不加载。每条研究都写明它在 skill 里落到了哪里。新增或修改规则前，先在这里补上依据。

## 1. 语法与语域特征（语料库语言学）

**Reinhart et al. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. *PNAS* 122. arXiv:2410.16107**

- 用 Biber 的多维特征框架，对比了人写的文本与 GPT-4o、Llama 3 生成的文本。和人类相比，GPT-4o 的用量分别是：
  - 现在分词从句 5.3 倍（指令微调模型普遍在 2–5 倍之间）；
  - 名词化 2.1 倍；
  - 短语并列 1.9 倍；
  - 以 that 从句作主语 2.6 倍；
  - 无施事被动句约 0.5 倍。
- 指令微调模型和人类的差距比基座模型大，而且模型变大以后差距并没有缩小。
- 过度使用的词：camaraderie、tapestry、intricate、underscore、palpable 等。
- **落点**：C1（句尾 -ing 点评）、C2（名词链）、C3（成对 / 三项）、C6（语态要贴合文体）。C6 是本 skill 和 humanizer 的主要分歧：humanizer §11 一律推主动语态，但模型的毛病恰恰是被动句偏少，在学术文本里一律改主动只会更不自然。

**Herbold et al. (2023). AI, write an essay for me. arXiv:2304.14276**

- ChatGPT 论证文和人写的相比：名词化更多、句子更复杂、词汇多样性更高，认知情态标记和情态动词更少。
- **落点**：A4（缺立场）、C2。

**Jiang & Hyland (2025a). Does ChatGPT argue like students? Bundles in argumentative essays. *Applied Linguistics* 46(3).**

- ChatGPT 的三词词束总体更少，但用起来更僵化；名词类、介词类词束更多，主要承担抽象描述和过渡、组织篇章的功能。学生作文的认知立场和作者在场感更强。
- **落点**：B5（靠连接词衔接）、C2、A4。

**Jiang & Hyland (2025b). Rhetorical distinctions: Comparing metadiscourse in essays by ChatGPT and students. *English for Specific Purposes* 79.**

- ChatGPT 作文结构连贯，但互动元话语（hedge、booster、态度标记）显著更少。
- **落点**：A4、A5。这一条修正了一个常见误解：在学术论证文里，AI 的问题主要是"没人称、不表态"，而不是"hedge 太多"。hedge 叠用（A5）主要出现在聊天腔里。

**Jiang & Hyland (2026). Stance in AI and student essays. *Applied Linguistics Review* 17(4).**

- AI 文本的立场表达显著更少、词汇范围更窄、作者在场感更弱。
- **落点**：A4、Phase 4 里"表明作者立场"那一条。

**Jiang & Hyland (2025c). Does ChatGPT write like a student? Engagement markers in argumentative essays. *Written Communication* 42(3).**

- 研究的是读者介入标记。本文件只核对到标题和出处，具体数字没有核对。

**Shaib et al. (2024). Detection and measurement of syntactic templates in generated text. EMNLP. arXiv:2407.00211**

- 用词性序列定义"句法模板"。模型生成模板化文本的比率高于人类；在生物医学文本里差距较小，在影评、新闻里较大。
- **落点**：C5（句形单一）。

## 2. 词汇

**Kobak et al. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Science Advances* 11(27).**

- 分析了 1500 多万篇 PubMed 摘要。delves、showcasing、underscores 等风格词在 LLM 出现后异常增多；据此估计，2024 年至少 13.5% 的摘要经过了 LLM 处理。
- **落点**：D1。

**Juzek & Ward (2025). Why does ChatGPT "delve" so much? COLING. arXiv:2412.11385**（后续：arXiv:2508.01930）

- 没有证据表明是架构或训练数据导致的；结果与"人类反馈学习（RLHF / DPO）偏好某些词"一致。
- **落点**：D1 的解释部分。也说明这些词是偏好学习的副产物，不是"错误"。

**Paech et al. (2026). Antislop. ICLR. arXiv:2510.15061**

- 有些套话在模型输出中的频率是人类文本的 1000 倍以上。在 prompt 里要求"别用这些词"效果有限，还可能适得其反（粉红大象效应）；作者用的是采样回溯和微调。
- **落点**：原则 3，以及"Phase 5 才加载模式清单"这条设计。起草阶段不给禁用词表，只给正面写作原则。

## 3. 人能不能看出来、靠什么看

**Casal & Kessler (2023). Can linguists distinguish between ChatGPT/AI and human writing? *Research Methods in Applied Linguistics*.**

- 72 位语言学期刊审稿人判断研究摘要，正确率只有 38.9%。他们给出的理由听起来合理，但前后不一致。
- **落点**：目标不设成"骗过语言学家"（短文本上他们本来就判断不准），而是达到专家读者对文体、立场、具体性的要求。这也是 skill 不追检测率的理由。

**Russell, Karpinska & Iyyer (2025). People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text. ACL. arXiv:2501.15654**

- 经常用 LLM 写作的人判断 300 篇长篇非虚构文章，5 人多数票只错 1 篇，比大多数检测器都准；改写和"人性化"处理都没有让文本躲过去。
- 他们的线索占比：词汇 53.1%、句式（套路、三项排比）35.9%、语法标点（AI 没有错误）24.8%、原创性（太稳妥、没有意外）23.7%、引语（太正式、和全文同一个腔调、总在段末）22.3%、清晰度（过度解释、塞无关细节）19.5%。
- 不可靠的线索：生僻词、中性语气、非正式语言（o1-Pro 也会用缩写和俚语）。约 31% 的误判理由是词汇，因为人也会写 delve、crucial。
- **落点**：A1、A6、C3、D1 的"别一对一换词"、G1（假口语化没用）。另外，"人类会犯语法错误"虽然是可靠的人类特征，skill 仍然明确不去制造错误（原则 4）：降低质量不在本 skill 的目标之内。

**Shaib et al. (2025). Measuring AI "slop" in text. arXiv:2509.19163**

- 专家对"slop"的判断可以拆成信息效用、信息质量、文风质量三组维度：密度、相关性、事实性、偏见、结构、连贯、语气。
- **落点**：A1、A6，以及 Phase 6 的核对清单。

## 4. 实务指南

**Wikipedia: Signs of AI writing（WikiProject AI Cleanup）**

- 大部分模式的来源。指南本身强调：这些只是"潜在问题的迹象，不是问题本身"，不要只修表面特征。它把 em dash 过多列为"历史特征（2022 至 2026-09）"，说明新模型的标志会变。
- **落点**：原则 3；C7 定为弱信号。

**blader/humanizer v3.1.0（MIT，Siqi Chen）**：https://github.com/blader/humanizer

- 借鉴了：
  - "模型默认做最宽泛的选择"这个解释框架；
  - 强 / 弱信号分级（"weak alone"）；
  - 不准新增事实；
  - 有样本时以样本为准；
  - 改完后专门再查最常残留的几类模式；
  - 多条模式的分类：not X but Y、收尾金句、深刻腔、铺垫、和不存在的人争论、三项排比、分词尾巴、系动词回避、宣传腔、模糊关联、加粗标签、聊天残留、"写给错误读者"。
- 刻意没有照搬的：
  - §8 em dash 全禁：改成按样本或文体指南来，定为弱信号；
  - §10 连字符规则：这是用法指南的偏好，不是 AI 特征，语言学读者未必认同；
  - §11 一律改主动：见 Reinhart，改成 C6；
  - §21 弯引号：在 Word 里没有意义。
  - 另外，humanizer 允许在博客类文体里"加入作者的反应"；本 skill 面向专业文体，改成只用用户给的观点（原则 4）。
- 本 skill 新增的部分：
  - Phase 1 需求确认（问题数量不设上限）；
  - Phase 2 内容清单和大纲确认；
  - Phase 3 文体画像；
  - 从要点写作、中译英两种模式；
  - A4 立场、A5 确定性校准；
  - B6 同义词轮换、B7 信息流、C6 语态；
  - G 组"矫枉过正"检查。

## 5. 写作教学经典（起草原则的来源）

- Joseph M. Williams & Joseph Bizup, *Style: Lessons in Clarity and Grace*：角色作主语、动作作动词；旧信息在前、新信息在后；话题链。→ Phase 4、B7、C2。
- John Swales, *Genre Analysis*（CARS 模型）→ genres.md 里的研究论文部分。
- Ken Hyland, *Metadiscourse*（hedges、boosters、态度标记、自我提及、介入标记）→ A4、A5。
- Allan Bell (1984), audience design → A6，以及 Phase 1 里"读者是谁"放在第一轮问。

## 6. 维护时的判断标准

- 新模式要有依据（研究、指南，或多次实际观察），并先确认现有条目里没有已经覆盖它的。能并进现有条目的，就不新开一条。
- SKILL.md 每次使用都会整篇读入，加内容必须值得。`scripts/check.py` 把它限制在 2,200 词以内。
- 各条模式的强弱，按"一个认真的作者故意这么写的概率"来定。
- 模型更新后，词汇层的特征变化最快，结构层和内容层最稳定。所以 D 组只是辅助，A、B 组才是主体。
