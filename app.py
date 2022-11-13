from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route("/")
def pratice():
    return render_template("prac.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000,debug=True)