from flask import Flask
import threading, time
app = Flask(__name__)
log = ["Sistem siap - 5 Karyawan Standby","Modal: Rp 400.000 | Mode PAPER aman"]

def scout():
    while True:
        log.append("Scout: patrol dexscreener - nemu coin baru")
        time.sleep(60)
        if len(log)>50: log.pop(0)

@app.route('/')
def home():
    logs = "<br>".join(log[-20:])
    return f"<body style='background:#0f0f0f;color:#fff;font-family:sans-serif;padding:15px'><h2>🤖 5 Karyawan Solana</h2><p>Modal 400rb | Fee 312 | Mode PAPER</p><div style='background:#1e1e1e;padding:15px;border-radius:15px'>{logs}</div><br><button onclick='location.reload()' style='background:#9945FF;color:white;padding:12px;width:100%;border:none;border-radius:10px'>Refresh Log</button></body>"

threading.Thread(target=scout, daemon=True).start()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
