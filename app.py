from flask import Flask, request, jsonify
import secrets
import string

app = Flask(__name__)

# Temporary in-memory storage
url_store = {}


def generate_short_code(length=6):
    """Generate a random 6-character short code."""
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(secrets.choice(characters) for _ in range(length))

        if code not in url_store:
            return code


@app.route("/shorten", methods=["POST"])
def shorten_url():
    """Create a short code for a long URL."""

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({
            "error": "Please provide a URL"
        }), 400

    original_url = data["url"]

    if not isinstance(original_url, str) or not original_url.startswith(
        ("http://", "https://")
    ):
        return jsonify({
            "error": "URL must start with http:// or https://"
        }), 400

    short_code = generate_short_code()

    url_store[short_code] = original_url

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}",
        "original_url": original_url
    }), 201


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)