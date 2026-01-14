from flask import Flask, jsonify
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import random

app = Flask(__name__)
TZ = ZoneInfo("Asia/Ho_Chi_Minh")

def get_time_window():
    now = datetime.now(TZ)

    window_minute = (now.minute // 20) * 20
    start = now.replace(minute=window_minute, second=0, microsecond=0)
    end = start + timedelta(minutes=20)

    return start, end, now

def tinh_du_lieu():
    start, end, now = get_time_window()

    # vòng cố định theo khung
    seed = int(start.timestamp())
    random.seed(seed)
    vong = random.randint(50, 200)

    # độ tin cậy tăng dần
    if now >= end:
        do_tin_cay = 100
    else:
        total = (end - start).total_seconds()
        passed = (now - start).total_seconds()
        do_tin_cay = round(15 + (passed / total) * 85)

    return {
        "Game": "Quyết Chiến",
        "Thoi_Gian": f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}",
        "Vong": vong,
        "Do_Tin_Cay": f"{do_tin_cay}%",
        "Server_Time": now.strftime("%H:%M")  # để debug
    }

@app.route("/api/nohu")
def nohu():
    return jsonify(tinh_du_lieu())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
