# 🏥 倪海厦人纪 · 中医辨证知识系统

<div align="center">

**Ni Haixia Renji — TCM Diagnosis Knowledge System**

[![GitHub stars](https://img.shields.io/github/stars/jonhnsonzz/nihaisha-renji?style=flat-square)](https://github.com/jonhnsonzz/nihaisha-renji)
[![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square)](api_server.py)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-orange?style=flat-square)](SKILL.md)
[![MCP Server](https://img.shields.io/badge/MCP-Server-purple?style=flat-square)](mcp.json)

> 基于倪海厦人纪12门课程（伤寒论、金匮要略、针灸、神农本草、黄帝内经等）的完整知识库。
> **人纪 = 医** — 中医辨证推演系统，56个引用文件，8.7MB知识库。

[English](#) | [中文](#)

</div>

---

## 🌟 Features

- **📖 完整知识库** — 56个引用文件，含全文索引（1.3MB伤寒论、1.2MB神农本草、1MB金匮要略等）
- **🔗 知识图谱** — 课程间实体交叉引用，同一方剂/症状在多门课程中的分布
- **🖼️ 截图证据索引** — 数千张倪师板书/PPT/实操截图索引
- **🔄 天纪-人纪联动** — 命宫→脏腑、星性→体质、化忌→养生（需配合天纪项目）
- **⚡ 三种调用方式** — Hermes Skill / MCP Server / REST API 任选
- **🌐 双语言** — 中英文文档，API响应兼容

## 📦 What's Inside

### 12门课程

| 课程 | 文件 | 全文索引 | 精华笔记 |
|:----|:----|:--------:|:--------:|
| 伤寒论 | `shanghanlun.md` | ✅ 1.3MB | ✅ scan-essence |
| 金匮要略 | `jingui.md` | ✅ 1MB | ✅ |
| 针灸 | `acupuncture.md` | ✅ 843KB | ✅ scan-essence |
| 神农本草 | `bencao.md` | ✅ 1.2MB | ✅ scan-essence (170KB) |
| 黄帝内经 | `huangdi.md` | ✅ 1.6MB (2文件) | ✅ scan-essence |
| 方剂 | `formula-patterns.md` | ✅ 873KB | — |
| 临床案例 | `clinical-cases.md` | — | ✅ |
| 八纲辨证 | `bagang.md` | — | ✅ |
| 扶阳论坛 | `fuyang.md` | — | ✅ |
| 易筋经 | `yijinjing.md` | — | ✅ |
| 仲景心法 | `zhongjing-xinfa.md` | — | ✅ |
| 电子书/音频 | `ebooks.md` | — | ✅ scan-essence |

### 目录结构

```
nihaisha-renji/
├── SKILL.md              # Hermes Agent Skill
├── mcp.json              # MCP Server 配置
├── api_server.py         # REST API 服务
├── references/           # 📚 知识库（56文件，8.7MB）
│   ├── index.md          # 主索引
│   ├── knowledge-graph.md # 知识图谱
│   ├── shanghanlun-full.md # 伤寒论全文索引
│   ├── bencao-full.md     # 神农本草全文索引
│   ├── jingui-full.md     # 金匮要略全文索引
│   ├── fangji-full.md     # 方剂全文索引
│   ├── acupuncture-full.md # 针灸全文索引
│   ├── huangdi-full-*.md  # 黄帝内经全文索引
│   ├── screenshot-evidence.md # 截图证据索引
│   ├── tianji-renji-link.md # 天纪-人纪关联
│   └── ...               # 其余课程资料
├── scripts/              # 搜索工具
│   ├── search_screenshots.py
│   └── build_screenshot_assets.py
├── compiled/             # 古文编译
├── agents/               # Agent配置
├── README.md             # 本文档
└── README_CN.md          # 中文版
```

## 🚀 Quick Start

### Option 1: REST API (最快)

```bash
# 1. 安装依赖
pip install fastapi uvicorn

# 2. 启动服务器
cd nihaisha-renji
python3 -m uvicorn api_server:app --host 0.0.0.0 --port 8833

# 3. 查询知识库
curl -X POST http://localhost:8833/api/query \
  -H "Content-Type: application/json" \
  -d '{"symptom":"桂枝汤","top_k":3}'
```

**示例输出：**
```json
{
  "code": 0,
  "data": {
    "query": "桂枝汤",
    "total": 3,
    "results": [
      {"module": "learning-entry", "match_count": 3, "preview": [...]},
      {"module": "notes-shanghan", "match_count": 3, "preview": [...]},
      {"module": "beginner-questions", "match_count": 1, "preview": [...]}
    ]
  }
}
```

### Option 2: MCP Server

在 Claude Desktop / VS Code / Cursor 等 MCP 客户端中配置：

```json
{
  "mcpServers": {
    "nihaisha-renji": {
      "command": "python3",
      "args": ["/absolute/path/to/nihaisha-renji/api_server.py"],
      "env": {"PORT": "8833"}
    }
  }
}
```

然后 AI 可以直接调用：
```
query_renji(symptom="头痛发热", top_k=5)
```

### Option 3: Hermes Skill

如果你是 [Hermes Agent](https://hermes-agent.nousresearch.com) 用户：

```bash
# 放入 skills 目录
cp -r nihaisha-renji ~/.hermes/skills/nihaisha-renji
# 加载后自动触发
```

## 🔗 Tianji-Renji Connection

本系统与 [nihaisha-tianji](https://github.com/jonhnsonzz/nihaisha-tianji)（天纪·命理风水系统）共享关联知识图谱：

| 天纪 | 人纪对应 | 应用场景 |
|:----|:--------|:---------|
| 命宫星辰 | 先天体质倾向 | 判断易患疾病类型 |
| 疾厄宫 | 对应脏腑疾病 | 结合辨证确定方证 |
| 化忌宫位 | 薄弱脏腑 | 养生重点方向 |
| 阴阳五行 | 八纲辨证基础 | 中医理论哲学根基 |

详见 `references/tianji-renji-link.md`。

## 🩺 Safety Notice

> ⚠️ **重要声明**
> 
> 本系统为倪海厦课程的**学习辅助工具**。所有输出均基于课程原文整理，旨在帮助用户学习和理解倪师的辨证思路。
> 
> ⛑️ **不构成医疗诊断**
> ⛑️ **不替代执业医师**
> ⛑️ **不是处方或治疗建议**
> 
> 如有健康问题，请务必咨询执业医师。

## 📊 Project Stats

- **引用文件**: 56个（含全文索引）
- **总大小**: 8.7 MB
- **课程数量**: 12门
- **截图证据**: 数千张（板書/PPT/实操）
| **API价格**: 开放平台定价
- **代码语言**: Python 3.8+

## 🤝 Contributing

欢迎提交 Issue 或 PR 完善知识库！

1. Fork 本仓库
2. 创建你的分支 (`git checkout -b feature/improvement`)
3. 提交改动 (`git commit -am 'Add improvement'`)
4. 推送 (`git push origin feature/improvement`)
5. 创建 Pull Request

## 📄 License

Educational use only. Content copyright belongs to the original course materials.

## 🙏 Credits

- **倪海厦先生** — 人纪课程的全部知识来源
- **社区贡献者** — 课程资料整理与截图索引构建
- **项目维护者** — 知识系统工程化与API服务

## 📬 Related Projects

- [nihaisha-tianji](https://github.com/jonhnsonzz/nihaisha-tianji) — 倪海厦天纪：易经·紫微斗数·命理风水知识系统
