# 倪海厦人纪·中医辨证知识系统

> **人纪** = 倪海厦中医教学体系，涵盖伤寒论、金匮要略、针灸、神农本草、黄帝内经等12门课程的完整知识库。

🇨🇳 中文说明 | [English Version](README.md)

## 内容概览

**56个引用文件（8.7MB）**，覆盖12门课程：

| 模块 | 内容 | 大小 |
|:----|:----|:----:|
| 伤寒论 | 全文索引（1.3MB）+笔记+精华 | 六经辨证体系 |
| 金匮要略 | 全文索引（1MB）+笔记 | 杂病方证 |
| 针灸 | 全文索引（843KB）+精华笔记 | 经络穴位刺法 |
| 神农本草 | 全文索引（1.2MB）+精华笔记 | 365味中药 |
| 黄帝内经 | 全文索引（1.6MB）+精华笔记 | 中医理论基础 |
| 方剂 | 全文索引（873KB）| 经方方证对照 |
| 临床案例 | 医案+截图证据 | 倪师实际病案 |
| 八纲辨证 | 课程摘要+截图 | 表里寒热虚实阴阳 |
| 扶阳论坛 | 课程摘要+截图 | 扶阳理论 |
| 易筋经 | 课程摘要+截图 | 养生功法 |
| 天纪-人纪关联 | 关联图谱 | 命理与中医的交叉 |

## 三种使用方式

### 1. Hermes Skill（推荐）

如果你在用 [Hermes Agent](https://hermes-agent.nousresearch.com)，把 `nihaisha-renji` 目录放到 `~/.hermes/skills/` 下即可。

触发方式：提到"倪海厦"或描述症状时自动加载。

### 2. MCP Server

在任何支持MCP的客户端（Claude Desktop、VS Code、Cursor等）中配置：

```json
{
  "mcpServers": {
    "nihaisha-renji": {
      "command": "python3",
      "args": ["绝对路径/nihaisha-renji/api_server.py"],
      "env": {
        "PORT": "8833"
      }
    }
  }
}
```

调用示例：
```
query_renji(symptom="桂枝汤", top_k=5)
```

### 3. REST API

```bash
# 查询中医知识
curl -X POST http://localhost:8833/api/query \
  -H "Content-Type: application/json" \
  -d '{"symptom":"桂枝汤","top_k":5}'

# 健康检查
curl http://localhost:8833/health
```

## 快速启动

```bash
# 1. 安装依赖
pip install fastapi uvicorn

# 2. 启动服务
cd nihaisha-renji
python3 -m uvicorn api_server:app --host 0.0.0.0 --port 8833

# 3. 测试
curl -X POST http://localhost:8833/api/query \
  -H "Content-Type: application/json" \
  -d '{"symptom":"桂枝汤","top_k":3}'
```

## 知识图谱

系统包含课程间关联图谱（`references/knowledge-graph.md`），覆盖：
- 同一方剂在伤寒论/金匮/临床案例中的分布
- 同一症状在不同六经中的表现差异
- 药物在不同方剂中的配伍变化

## 天纪↔人纪关联

本系统与天纪系统存在双向关联（`references/tianji-renji-link.md`）：
- **命宫→脏腑：** 紫微斗数十二宫对应人体脏腑
- **星性→体质：** 十四主星对应先天体质倾向
- **化忌→养生：** 化忌宫位提示薄弱脏腑养护方向

## 安全声明

> ⚠️ 本系统为倪海厦课程的**学习辅助工具**。所有输出均基于课程原文整理。
> **不构成医疗诊断、不替代执业医师、不是处方或治疗建议。**
> 如有健康问题，请务必咨询执业医师。

## 相关项目

- [nihaisha-tianji](https://github.com/jonhnsonzz/nihaisha-tianji) — 倪海厦天纪：易经·紫微斗数·命理风水

## 许可

仅供学习研究使用。内容版权归属原课程。
