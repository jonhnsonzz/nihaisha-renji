# 🏥 倪海厦人纪 · 中医辨证知识系统

<div align="center">

**基于倪海厦伤寒论、金匮要略、针灸、神农本草、黄帝内经等12门课程的完整知识库**

[![GitHub stars](https://img.shields.io/github/stars/jonhnsonzz/nihaisha-renji?style=flat-square)](https://github.com/jonhnsonzz/nihaisha-renji)
[![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square)](api_server.py)
[![MCP Server](https://img.shields.io/badge/MCP-Server-purple?style=flat-square)](mcp.json)

> **人纪 = 医** — 56个引用文件，8.7MB知识库，支持Hermes Skill / MCP / API三种调用方式

[中文](#) | [English](README.md)

</div>

---

## ✨ 功能特点

- **📖 完整知识库** — 56个引用文件涵盖伤寒论、金匮要略、针灸、神农本草、黄帝内经等12门课程，含全文索引
- **🔗 知识图谱** — `knowledge-graph.md` 记录方剂/症状在多门课程中的交叉引用
- **🖼️ 截图证据索引** — 数千张倪师板書/PPT/实操截图，可精确定位到课次
- **🔄 天纪-人纪联动** — 命宫→脏腑、星性→体质、化忌→养生（需配合天纪项目）
- **⚡ 三种调用方式** — 任选 Hermes Skill / MCP Server / REST API
- **🌐 双语言支持** — 中英文文档齐全

## 📖 12门课程

| 课程 | 全文索引 | 精华笔记 | 
|:----|:--------:|:--------:|
| 伤寒论 | ✅ 1.3MB | ✅ |
| 金匮要略 | ✅ 1MB | — |
| 针灸 | ✅ 843KB | ✅ |
| 神农本草 | ✅ 1.2MB | ✅ (170KB) |
| 黄帝内经 | ✅ 1.6MB | ✅ |
| 方剂 | ✅ 873KB | — |
| 临床案例 | — | ✅ |
| 八纲辨证 | — | ✅ |
| 扶阳论坛 | — | ✅ |
| 易筋经 | — | ✅ |
| 仲景心法 | — | ✅ |
| 电子书/音频 | — | ✅ |

## 🚀 快速开始

### 方式一：REST API（最快）

```bash
# 1. 安装依赖
pip install fastapi uvicorn

# 2. 启动服务
cd nihaisha-renji
python3 -m uvicorn api_server:app --host 0.0.0.0 --port {API_PORT}

# 3. 查询
curl -X POST http://localhost:{API_PORT}/api/query \
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
      {"module": "learning-entry", "match_count": 3, "preview": ["桂枝汤方: 桂枝三两..."]},
      {"module": "notes-shanghan", "match_count": 3, "preview": [...]},
      {"module": "beginner-questions", "match_count": 1, "preview": [...]}
    ]
  }
}
```

### 方式二：MCP Server

在 Claude Desktop、VS Code、Cursor 等中配置：

```json
{
  "mcpServers": {
    "nihaisha-renji": {
      "command": "python3",
      "args": ["/绝对路径/nihaisha-renji/api_server.py"],
      "env": {"PORT": "{API_PORT}"}
    }
  }
}
```

### 方式三：Hermes Skill

```bash
cp -r nihaisha-renji ~/.hermes/skills/nihaisha-renji
# 加载后自动触发
```

## 🔗 天纪↔人纪联动

本系统与 [天纪项目](https://github.com/jonhnsonzz/nihaisha-tianji) 可联动分析：

| 天纪 → | 人纪 → | 应用 |
|:-------|:-------|:-----|
| 命宫星辰 | 先天体质倾向 | 易患疾病类型 |
| 疾厄宫 | 对应脏腑疾病 | 辨证参考 |
| 化忌宫位 | 薄弱脏腑 | 养生方向 |

## ⚠️ 安全声明

本系统为倪海厦课程的**学习辅助工具**。
**不构成医疗诊断、不替代执业医师、不是处方或治疗建议。**

## 📊 项目数据

- **引用文件**: 56个（含全文索引）
- **总大小**: 8.7 MB
- **课程数量**: 12门
| **API价格**: 开放平台定价
- **代码语言**: Python 3.8+

## 🤝 贡献指南

欢迎提交 Issue 或 PR！
1. Fork 本仓库
2. 创建分支 (`git checkout -b feature/improvement`)
3. 提交 (`git commit -am 'Add improvement'`)
4. 推送 (`git push origin feature/improvement`)
5. 创建 Pull Request

## 相关项目

- [nihaisha-tianji](https://github.com/jonhnsonzz/nihaisha-tianji) — 倪海厦天纪：易经/紫微斗数/命理风水
