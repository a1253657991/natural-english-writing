# natural-english-writing

帮你写、改、翻译和检查专业英文、学术英文。目标是让懂行的读者（包括语言学家）读起来，觉得这是一个具体的人写给他们看的，而不是通用的 AI 腔。

它不追 AI 检测率，也不靠换词。换词往往把句子改得拗口，而语言学家对这种拗口最敏感。

A Claude skill for drafting, revising, translating and auditing professional and academic English, so that expert readers (including linguists) read it as the work of a specific writer addressing them, not as generic LLM prose. It does not chase detector scores and does not swap words.

## 它怎么工作

| 阶段 | 做什么 | 为什么 |
|---|---|---|
| 1. 确认需求 | 每次使用都先做。先读完你给的材料，再分轮提问，问题数量不设上限，每题附理由和推荐默认值；问到没有歧义为止，写成需求简报（brief）给你确认 | 坏结果多半来自猜错了读者、文体或目的 |
| 2. 内容清单 | 把要表达的每个论点列出来，标明来源和强度；缺的标 `[NEED]` 再问你；长文先定大纲 | 防止内容跑偏、编造细节，以及套用对称模板 |
| 3. 定文体 | 有范文就提炼范文的语域特征，没有就用 `references/genres.md` 里的文体画像 | 照真实文体写，比"写得像人"可靠 |
| 4. 起草 | 只给正面的写作原则（具体、立场、信息流、术语一致等），不给禁用词表 | 禁用词表会引出被禁的词（Antislop 2026） |
| 5. 检查 | 这时才加载 `references/patterns.md`，按模式逐条标出问题，改法是重写、具体化或删掉，不是换同义词 | 只修症状没用，要修的是原因 |
| 6. 核对交付 | 逐条核对忠实度、矫枉过正、语域统一、残留模式和需求要求；然后交付正文和中文改动说明 | 不新增事实，不改变论点强度 |

四种模式：从要点写作、修改你的英文稿、中文稿转英文、只检查不重写。

## 安装

**Claude Code**（本机或其他电脑）：

```bash
git clone https://github.com/a1253657991/natural-english-writing ~/.claude/skills/natural-english-writing
```

**claude.ai 网页版**：把 `SKILL.md` 和 `references/` 打成 zip，在设置的 Skills 里上传。也可以把 `SKILL.md` 的内容贴进 Project instructions。

**其他 agent**（Codex、Cursor、OpenCode 等）：放到它们的 skills 目录下，或者把 `SKILL.md` 当系统提示用。

## 使用

在 Claude Code 里输入 `/natural-english-writing`，或者直接说"帮我把这段写成英文 / 改一下 / 看看有没有 AI 味"，它会自动触发。

可以一起提供的材料：你的要点或草稿、读者是谁、一段目标期刊或机构的范文、作业要求或评分标准。没给的，它会问。

## 更新与维护

```bash
cd ~/.claude/skills/natural-english-writing
git pull                     # 拿最新版
python3 scripts/check.py     # 改完以后自检
```

维护规则：

- `SKILL.md` 每次使用都会整篇读入，控制在 2,200 词以内（由 `scripts/check.py` 检查）。细节放进 `references/`，并注明在哪个阶段读。
- 新增模式前，先在 `docs/research-notes.md` 写明依据，并确认现有条目没有覆盖它。编号按组（A–G）连续。
- 改了行为就同步更新 `SKILL.md` 里 `metadata.version` 和 `CHANGELOG.md` 的版本号，两处保持一致。
- `evals/` 里是测试用例，改完可以用 `claude plugin eval .` 重新跑一遍。

## 设计依据

详见 [`docs/research-notes.md`](docs/research-notes.md)。主要包括：

- Reinhart et al. 2025（PNAS）：分词从句、名词化、并列、被动的语料对比数据。
- Jiang & Hyland 2025–2026：ChatGPT 作文的立场、元话语、词束特征。
- Herbold et al. 2023、Shaib et al. 2024/2025、Kobak et al. 2025、Juzek & Ward 2025。
- Russell et al. 2025（ACL）：经常用 LLM 的人靠什么认出 AI 文本，哪些线索不可靠。
- Casal & Kessler 2023：语言学家判断短摘要的正确率只有 38.9%。
- Paech et al. 2026（Antislop）：在 prompt 里禁词效果有限。
- Wikipedia: Signs of AI writing；Williams & Bizup《Style》；Swales；Hyland。

## 与 blader/humanizer 的关系

这个 skill 借鉴了 [blader/humanizer](https://github.com/blader/humanizer)（MIT，Siqi Chen）：

- 解释框架：模型默认做最宽泛的选择；
- 强 / 弱信号分级；
- 不准新增事实；
- 以样本为准；
- 一批模式的分类。

不同的地方：

- 加了需求确认、内容清单和文体画像；
- 能从要点写作，也能中译英；
- 不一律改主动语态，因为模型本来就是被动句偏少；
- 不全禁 em dash；
- 加了立场校准和矫枉过正检查；
- 只面向专业和学术文体，不往文本里加作者没给的观点。

逐条对比见 `docs/research-notes.md` 第 4 节。

## License

MIT. 改编自 blader/humanizer 的部分，同样保留其 MIT 版权声明，见 `LICENSE`。
