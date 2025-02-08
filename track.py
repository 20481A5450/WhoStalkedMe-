from flask import Flask, request, send_file
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging to a file
logging.basicConfig(filename="visitors.log", level=logging.INFO, format="%(asctime)s - %(message)s")

@app.route("/tracker.png")
def track():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    referrer = request.referrer  # Captures where the request came from

    # Log visitor details
    logging.info(f"Visitor IP: {ip}, User-Agent: {user_agent}, Referrer: {referrer}")

    # Serve the tracking pixel
    return send_file("tracker.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
