import os
import logging
from flask import Flask, request, send_file

app = Flask(__name__)

# Configure logging explicitly
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[logging.StreamHandler()])

# Get absolute path of tracker.png
TRACKER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tracker.png")

@app.route("/tracker.png")
def track():
    try:
        # Try to get the real visitor's IP
        forwarded_for = request.headers.get("X-Forwarded-For", "")
        real_ip = forwarded_for.split(",")[0].strip() if forwarded_for else request.remote_addr
        
        user_agent = request.headers.get("User-Agent", "Unknown")
        referrer = request.referrer or "No Referrer"

        # Print visitor details to logs
        logging.info(f"📌 Visitor IP: {real_ip}, User-Agent: {user_agent}, Referrer: {referrer}")

        return send_file(TRACKER_PATH, mimetype="image/png")

    except Exception as e:
        logging.error(f"❌ Error serving tracker.png: {str(e)}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)
