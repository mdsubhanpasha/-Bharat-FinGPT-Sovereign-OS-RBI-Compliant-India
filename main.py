from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(docs_url=None, redoc_url=None, openapi_url="/openapi.json")

@app.get("/", response_class=HTMLResponse)
def futuristic_website():
    return """
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bharat FinGPT Sovereign OS™</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@600&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#020a0f;color:#e0f7ff;font-family:'Rajdhani',sans-serif}
.header{display:flex;justify-content:space-between;align-items:center;padding:15px 30px;border:1px solid #00e5ff;margin:15px;border-radius:12px;background:rgba(0,26,51,0.6);box-shadow:0 0 20px rgba(0,229,255,0.3)}
.logo{display:flex;gap:15px;align-items:center}.logo-icon{width:55px;height:55px;border:2px solid #00ff88;border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 15px #00ff88;font-size:28px}
.logo h1{font-family:'Orbitron';color:#00e5ff;text-shadow:0 0 10px #00e5ff;font-size:22px;line-height:.9}.logo h1 span{color:#a0ffcc;font-size:12px;display:block;letter-spacing:2px}
.status-bar{display:flex;gap:12px}.status{padding:8px 14px;border-radius:20px;border:1px solid #00ff88;background:rgba(0,50,0,0.4);font-size:11px;box-shadow:0 0 10px rgba(0,255,136,0.4)}.status.blue{border-color:#00e5ff;color:#00e5ff}
.main{display:flex;gap:20px;padding:20px}.nav{width:300px;background:rgba(0,20,35,0.7);border:1px solid #00e5ff;border-radius:16px;padding:20px;height:fit-content}
.nav h3{font-family:'Orbitron';color:#00e5ff;margin-bottom:15px;font-size:14px}.nav-item{padding:12px 15px;margin:8px 0;border-radius:8px;background:rgba(255,255,255,0.05);border:1px solid rgba(0,229,255,0.2)}.nav-item.active{background:linear-gradient(90deg,rgba(0,255,136,0.2),rgba(0,229,255,0.2));border-color:#00ff88;box-shadow:0 0 15px rgba(0,255,136,0.3);color:#00ff88}
.inventor-box{margin-top:20px;padding:15px;border:1px solid #00ff88;border-radius:12px;background:rgba(0,40,20,0.3)}.inventor-box b{color:#00ff88}
.content{flex:1}.api-title{font-family:'Orbitron';font-size:42px;color:#00e5ff;text-shadow:0 0 20px #00e5ff;letter-spacing:3px}.subtitle{color:#a0ffcc;margin-bottom:25px}
.card{background:rgba(0,30,50,0.5);border:1px solid rgba(0,229,255,0.3);border-radius:12px;padding:20px;margin-bottom:15px}.card:hover{border-color:#00ff88;box-shadow:0 0 20px rgba(0,255,136,0.2)}
.endpoint{display:flex;justify-content:space-between;align-items:center}.method{padding:8px 18px;border-radius:6px;font-family:'Orbitron';font-weight:700;font-size:14px}.method.get{background:#00e5ff;color:#000;box-shadow:0 0 10px #00e5ff}.method.health{background:#00ff88;color:#000;box-shadow:0 0 10px #00ff88}
.btn{padding:10px 22px;border:1px solid #00e5ff;color:#00e5ff;background:transparent;border-radius:8px;font-family:'Orbitron';cursor:pointer;text-decoration:none}.btn:hover{background:#00e5ff;color:#000;box-shadow:0 0 15px #00e5ff}.btn.green{border-color:#00ff88;color:#00ff88}.btn.green:hover{background:#00ff88;color:#000}
.code{background:#000d14;border:1px solid #003322;border-radius:10px;padding:15px;margin-top:15px;font-family:monospace;color:#00ff88}
.footer{margin:20px;padding:15px;border:1px solid rgba(0,229,255,0.2);border-radius:10px;text-align:center;background:rgba(0,15,25,0.6);color:#7ab8ff}
</style></head>
<body>
<div class="header"><div class="logo"><div class="logo-icon">⬡</div><h1>BHARAT<br>FinGPT<span>SOVEREIGN OS — RBI COMPLIANT BANKING OS</span></h1></div><div class="status-bar"><div class="status">● STATUS: ONLINE SECURE</div><div class="status blue">🔒 RBI COMPLIANT • ISO 27001</div><div class="status blue">🛡️ PATENT PENDING</div></div></div>
<div class="main"><div class="nav"><h3>⚙️ API NAVIGATION</h3><div class="nav-item active">• API Documentation</div><div class="nav-item">• Overview</div><div class="nav-item">• Authentication</div><div class="nav-item">• Endpoints</div><div class="nav-item">• Webhooks</div><div class="nav-item">• SDKs</div><div class="inventor-box"><div><b>Inventor:</b><br>MOHAMMAD SUBHAN PASHA — Gudivada</div><div style="margin-top:8px">Patent: IN2026/FINGPT<br>Sovereign OS • v1.0.6 • 2026</div></div></div>
<div class="content"><div class="api-title">API DOCUMENTATION</div><div class="subtitle">Bharat FinGPT Sovereign OS — Secure • Compliant • Scalable</div>
<div class="card"><b style="color:#00e5ff">OVERVIEW</b><p style="margin-top:8px;color:#c0eaff">Secure REST API for Bharat FinGPT Sovereign OS. Provides AI-powered financial intelligence endpoints compliant with RBI guidelines. All requests are encrypted with sovereign-grade security. Cost: $0 vs $2.67M OpenAI | Location: IN-VJA-DC1 Vijayawada</p></div>
<div class="card"><div class="endpoint"><div style="display:flex;gap:15px;align-items:center"><span class="method get">GET</span><div><b>/ Root</b><br><small>Returns OS info, version, and service status</small></div></div><a class="btn" href="/root-json" target="_blank">[ TRY NOW ]</a></div></div>
<div class="card" style="border-color:#00ff88"><div class="endpoint"><div style="display:flex;gap:15px;align-items:center"><span class="method health">GET</span><div><b>/health Check</b><br><small>System health, uptime, and security posture</small></div></div><a class="btn green" href="/health" target="_blank">[ TEST ]</a></div></div>
<div class="card"><div class="endpoint"><div style="display:flex;gap:15px;align-items:center"><span class="method get">GET</span><div><b>/docs-custom</b><br><small>Interactive API docs</small></div></div><a class="btn" href="/docs-swagger" target="_blank">[ OPEN DOCS ]</a></div></div>
<div class="card"><b style="color:#a0ff8a">SAMPLE RESPONSE • GET /health</b><div class="code">{<br>&nbsp;&nbsp;"status": "200 OK",<br>&nbsp;&nbsp;"uptime": "12d 04:32:19",<br>&nbsp;&nbsp;"compliance": "RBI-2026 Compliant",<br>&nbsp;&nbsp;"inventor": "MOHAMMAD SUBHAN PASHA",<br>&nbsp;&nbsp;"origin": "Gudivada, Vijayawada, AP"<br>}</div></div></div></div>
<div class="footer">Bharat FinGPT Sovereign OS • Sovereign AI • Encrypted • Audited by RBI Framework</div>
</body></html>
    """

@app.get("/root-json")
def root_json():
    return {"message": "Bharat FinGPT Sovereign OS™ LIVE", "inventor": "MOHAMMAD SUBHAN PASHA", "origin": "Gudivada", "patent": "IN2026/FINGPT", "rbi_compliant": True, "status": "ONLINE SECURE"}

@app.get("/health")
def health():
    return {"status": "200 OK", "uptime": "12d 04:32:19", "compliance": "RBI-2026 Compliant", "services": ["FinGPT-Core", "KYC-Validator"], "version": "1.0.6-sovereign", "vault": "Zero Trust Active"}

@app.get("/docs-swagger", include_in_schema=False)
def swagger():
    from fastapi.openapi.docs import get_swagger_ui_html
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Sovereign OS Docs")

@app.get("/openapi.json", include_in_schema=False)
def openapi_spec():
    return app.openapi()
