from flask import Flask, request, send_file, logging

app = Flask(__name__)

@app.route("/tracker.png")
def track():
    try:
        ip = request.remote_addr
        user_agent = request.headers.get("User-Agent")
        referrer = request.referrer or "No Referrer"

        app.logger.info(f"Visitor IP: {ip}, User-Agent: {user_agent}, Referrer: {referrer}")

        # Ensure "tracker.png" exists in your project directory
        return send_file("tracker.png", mimetype="image/png")

    except Exception as e:
        app.logger.error(f"Error serving tracker.png: {str(e)}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
