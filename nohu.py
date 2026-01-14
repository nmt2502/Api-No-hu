from flask import Flask, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

def tinh_du_lieu():
    now = datetime.now()
    future = now + timedelta(minutes=15)

    rounded_minute = ((future.minute + 4) // 5) * 5
    if rounded_minute >= 60:
        future = future.replace(hour=future.hour + 1, minute=0)
    else:
        future = future.replace(minute=rounded_minute)

    start_time = future
    end_time = start_time + timedelta(minutes=20)

    seed = int(start_time.timestamp())
    random.seed(seed)
    vong = random.randint(50, 200)

    if now <= start_time:
        do_tin_cay = 15
    elif now >= end_time:
        do_tin_cay = 100
    else:
        total = (end_time - start_time).total_seconds()
        passed = (now - start_time).total_seconds()
        do_tin_cay = round(15 + (passed / total) * 85)

    return {
        "Game": "Quyết Chiến",
        "Thoi_Gian": f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}",
        "Vong": vong,
        "Do_Tin_Cay": f"{do_tin_cay}%"
    }

@app.route("/api/nohu", methods=["GET"])
def nohu():
    return jsonify(tinh_du_lieu())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
