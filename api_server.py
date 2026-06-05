"""倪海厦中医辨证查询API — 数据广场端口8833"""
import subprocess, os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="倪海厦中医辨证查询API")

class Query(BaseModel):
    symptom: str
    top_k: int = 5

@app.post("/api/query")
def diagnose(q: Query):
    symptom = q.symptom.strip()
    if not symptom:
        return {"code": 400, "message": "请输入症状/方剂/穴位关键词"}
    nihaisha_dir = os.path.expanduser("~/.hermes/skills/nihaisha-renji/references")
    results = []
    if os.path.exists(nihaisha_dir):
        try:
            out = subprocess.run(["grep", "-ril", symptom, nihaisha_dir], capture_output=True, text=True, timeout=15)
            matched = [f for f in out.stdout.strip().split("\n") if f.strip()][:q.top_k]
            for fname in matched:
                basename = os.path.basename(fname).replace(".md","")
                try:
                    prev = subprocess.run(["grep", "-i", symptom, fname], capture_output=True, text=True, timeout=5)
                    lines = [l.strip() for l in prev.stdout.split("\n") if l.strip()][:3]
                except:
                    lines = []
                results.append({"module": basename, "match_count": len(lines), "preview": lines})
        except Exception as e:
            return {"code": 500, "message": str(e)}
    return {"code": 0, "data": {"query": symptom, "total": len(results), "results": results}, "disclaimer": "仅限中医学研究用途，不提供诊断处方"}

@app.get("/health")
def health():
    return {"status": "ok", "service": "nihaisha-api"}
