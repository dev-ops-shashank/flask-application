# app.py
from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime


app = Flask(__name__)

# Simple in-memory storage
tasks = []


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task():
    task = {
        "id": len(tasks) + 1,
        "title": request.form["title"],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    return redirect(url_for("index"))


@app.route("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)