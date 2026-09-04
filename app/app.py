import os

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health_check():
    try:
        check_database()

        return jsonify({
            "status": "healthy",
            "service": "devops-learning",
            "environment": os.getenv("APP_ENV", "unknown"),
            "database": "connected"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "service": "devops-learning",
            "environment": os.getenv("APP_ENV", "unknown"),
            "database": "disconnected",
            "error": str(e)
        }), 503


def check_database():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "devopsdb"),
        user=os.getenv("DB_USER", "devops"),
        password=os.getenv("DB_PASSWORD", "devops_password")
    )

    connection.close()

    return True


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
