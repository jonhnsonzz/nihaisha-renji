<div align="center">

# nihaisha

**把倪海厦中医课程整理成可检索、可追溯、有安全边界的 Agent Skill。**

Claude Code / Codex / OpenClaw Skill。装进 agent 后，可以用自然语言按症状、方剂、穴位、课程模块、课次或板书截图检索倪海厦课程资料，输出学习型辨证梳理、方证/穴位/药性对比、逐课复习计划和截图证据索引。

[![GitHub stars](https://img.shields.io/github/stars/JuneYaooo/nihaisha-tcm?style=flat)](https://github.com/JuneYaooo/nihaisha-tcm/stargazers)
[![Skill](https://img.shields.io/badge/Agent-Skill-orange.svg)](./SKILL.md)
[![TCM](https://img.shields.io/badge/TCM-%E5%80%AA%E6%B5%B7%E5%8E%A6-green.svg)](./references/index.md)
[![Course](https://img.shields.io/badge/course-multi--module-blue.svg)](./references/index.md)

**English** → [docs/README.en.md](./docs/README.en.md)

</div>

---

## 课程蒸馏方法

本项目的课程蒸馏方法来自作者维护的 [lineage-skill](https://github.com/JuneYaooo/lineage-skill)：把高密度课程材料整理成可溯源、可迁移、可产出的 Agent Skill。

## 能做什么

- **白话问题入口**：把"感冒怕冷""手脚冷""拉肚子""睡不着"等普通表达转成课程里的分水岭问题。
- **多课程检索**：覆盖伤寒论、金匮要略、仲景心法、临床案例、八纲辨证、扶阳论坛、易筋经、梁冬对话、斯坦福演讲、天纪、黄帝内经、神农本草、针灸课程，以及讲稿笔记、汉唐中医、诊疗日志、电子书和音频合集索引。
- **六经与方证导航**：按六经、症状、方剂和传变逻辑整理《伤寒论》核心内容。
- **穴位与药性学习**：可检索针灸经络穴位、配穴思路，以及神农本草课程里的药性、剂型、配伍与单味药线索。
- **逐课复习**：按课程模块和课次整理主题地图、关键词和适合复习的问题。
- **截图证据**：已接入 2986 条截图证据索引，对应图片均已压缩为仓库内 WebP，可按方名、穴位、课次、病机、术数关键词或时间点检索。
- **安全边界**：默认作为课程学习与中医理论整理，不做个人诊断、处方或剂量指导。

## 适合哪些场景

| 场景 | 适合程度 | 说明 |
| --- | --- | --- |
| 学习倪海厦课程 | 很适合 | 从课程模块、课次、主题、截图证据几个入口复习。 |
| 查某个方的课程方证 | 很适合 | 可返回症状群、病机层次、相关方和禁忌提醒。 |
| 查针灸、经络、穴位 | 很适合 | 可按穴位、经络、配穴场景和实操截图检索。 |
| 查本草药性或内经理论 | 适合 | 可进入神农本草、黄帝内经模块做课程学习整理。 |
| 用白话提问 | 很适合 | 先转成辨证分水岭，再进入课程术语。 |
| 找板书、PPT 或实操截图 | 适合 | 用 `scripts/search_screenshots.py` 跨模块检索截图索引。 |
| 整理学习笔记 | 适合 | 可生成可追加到 references 的 Markdown。 |
| 真实病情用药决策 | 不适合 | 本 skill 不提供个人诊断、处方、剂量或自我用药建议。 |

## 课程模块

| 模块 | 文本资料 | 截图证据 |
| --- | --- | --- |
| 伤寒论 | references/shanghanlun.md, references/lesson-map.md | screenshot-evidence.md 649 张 |
| 金匮要略 | references/jingui.md | jingui-screenshot-evidence.md 656 张 |
| 仲景心法 | references/zhongjing-xinfa.md | zhongjing-xinfa-screenshot-evidence.md 68 张 |
| 临床案例/倪师医案 | references/clinical-cases.md | clinical-cases-screenshot-evidence.md 88 张 |
| 八纲辨证 | references/bagang.md | bagang-screenshot-evidence.md 33 张 |
| 扶阳论坛 | references/fuyang.md | fuyang-screenshot-evidence.md 37 张 |
| 易筋经 | references/yijinjing.md | yijinjing-screenshot-evidence.md 28 张 |
| 梁冬对话倪师 | references/liangdong.md | - |
| 斯坦福大学演讲 | references/stanford.md | - |
| 天纪 | references/tianji.md | tianji-screenshot-evidence.md 527 张 |
| 黄帝内经 | references/huangdi.md | huangdi-screenshot-evidence.md 272 张 |
| 神农本草 | references/bencao.md | bencao-screenshot-evidence.md 127 张 |
| 针灸课程 | references/acupuncture.md | acupuncture-screenshot-evidence.md 501 张 |

## 安装

### 方式一：让 AI 自己装

```text
帮我安装 nihaisha skill：https://github.com/JuneYaooo/nihaisha-tcm
```

### 方式二：手动安装

```bash
git clone git@github.com:JuneYaooo/nihaisha-tcm.git
cd nihaisha-tcm
bash install_as_skill.sh --target codex
```

## 安全说明

本项目用于倪海厦课程学习、资料检索和中医理论整理，不用于医疗诊断或个体化治疗。

## 版权与用途说明

本项目仅作个人学习、资料整理与技术交流使用，不作商业用途。

## 当前覆盖

- 已整理并接入截图图片：针灸课程、黄帝内经课程、神农本草课程、伤寒论课程、金匮要略课程、仲景心法传讲、人纪之临床案例、人纪之八纲辨证、扶阳论坛、倪师易筋经、倪海厦天纪。
- 已整理文字资料：文字笔记、汉唐中医、诊疗日志、电子书合集、音频合集。
- 待扩展：梁冬对话、斯坦福演讲、其他资料。
