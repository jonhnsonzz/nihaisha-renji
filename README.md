# Ni Haixia Renji — TCM Diagnosis Knowledge System

> **人纪 (Renji)** = The Human Realm — Ni Haixia's complete TCM (Traditional Chinese Medicine) curriculum knowledge base.

倪海厦人纪·中医辨证知识系统 — 伤寒论、金匮要略、针灸、神农本草、黄帝内经等12门课程完整知识库。

## What's Inside

**56 reference files (8.7 MB)** covering 12 courses:

| Module | Files | Size |
|--------|-------|------|
| Shang Han Lun (伤寒论) | Full text index (1.3MB) + notes + essence | Course on the Cold Damage |
| Jin Gui Yao Lue (金匮要略) | Full text index (1MB) + notes | Essential Prescriptions from the Golden Cabinet |
| Acupuncture (针灸) | Full text index (843KB) + notes + essence | Meridians, acupoints, needling |
| Shen Nong Ben Cao (神农本草) | Full text index (1.2MB) + notes + essence | Herbal medicine |
| Huang Di Nei Jing (黄帝内经) | Full text index (1.6MB) + notes + essence | Yellow Emperor's Inner Canon |
| Fang Ji (方剂) | Full index (873KB) | Formula patterns |
| Clinical Cases (临床案例) | Cases + evidence screenshots | Ni's actual clinical records |
| Ba Gang (八纲辨证) | Summary + screenshots | Eight-principle pattern identification |
| Fu Yang (扶阳论坛) | Summary + screenshots | Yang-supporting forum |
| Yi Jin Jing (易筋经) | Summary + screenshots | Tendon-changing classic |
| Tianji-Renji Link | Cross-reference map | Relationship between Tianji & Renji |

## Three Ways to Use

### 1. Hermes Skill

If you use [Hermes Agent](https://hermes-agent.nousresearch.com):

```bash
# The skill is already in ~/.hermes/skills/nihaisha-renji/
# Just load it:
# Trigger: mention "倪海厦" or TCM symptoms
```

### 2. MCP Server

Configure in your MCP-compatible client (Claude Desktop, VS Code, Cursor, etc.):

```json
{
  "mcpServers": {
    "nihaisha-renji": {
      "command": "python3",
      "args": ["/path/to/nihaisha-renji/api_server.py"],
      "env": {
        "PORT": "8833"
      }
    }
  }
}
```

Then call:
```
query_renji(symptom="桂枝汤", top_k=5)
```

### 3. REST API

```bash
# Query TCM knowledge
curl -X POST http://localhost:8833/api/query \
  -H "Content-Type: application/json" \
  -d '{"symptom":"桂枝汤","top_k":5}'

# Health check
curl http://localhost:8833/health
```

## Quick Start

```bash
# 1. Install API server
pip install fastapi uvicorn

# 2. Start server
cd nihaisha-renji
python3 -m uvicorn api_server:app --host 0.0.0.0 --port 8833

# 3. Test it
curl -X POST http://localhost:8833/api/query \
  -H "Content-Type: application/json" \
  -d '{"symptom":"桂枝汤","top_k":3}'
```

## Safety Notice

> ⚠️ This system is an **educational tool** for studying Ni Haixia's TCM curriculum. All outputs are based on course materials for learning purposes only. **Does NOT constitute medical diagnosis, prescription, or treatment advice.** Consult a licensed physician for health issues.

## Related Projects

- [nihaisha-tianji](https://github.com/jonhnsonzz/nihaisha-tianji) — Ni Haixia Tianji: I-Ching & Ziwei Doushu knowledge system

## License

Educational use. Content copyright belongs to the original course materials. This project is a study tool for organizing and retrieving course content.
