
from flask import Flask
from threading import Thread
import requests
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

def run():
    # اقرأ المنفذ من متغير PORT المُعيّن أو استخدم 5000 كافتراضي
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()

def self_ping():
    url = os.environ.get("RENDER_URL")  # أو ضع هنا رابط خدمتك على Render
    while True:
        try:
            requests.get(url)
            print("Self-ping succeeded")
        except Exception:
            print("Self-ping failed")
        time.sleep(60 * 3)

if __name__ == "__main__":
    keep_alive()
    Thread(target=self_ping, daemon=True).start()
