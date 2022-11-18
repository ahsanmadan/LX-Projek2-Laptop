import requests
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:asan@cluster0.hmhssac.mongodb.net/?retryWrites=true&w=majority")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/detail/<keyword>")
def detail(keyword):
    return render_template("detail.html",word = keyword)

@app.route("/api/simpan", methods = ["POST"])
def simpan():
    return jsonify({'result': 'success', 'msg': 'Kata Tersimpan'})

@app.route("/api/hapus", methods = ["POST"])
def hapus():
    return jsonify({'result': 'success', 'msg': 'Kata telah di hapus'})
    

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000,debug=True)