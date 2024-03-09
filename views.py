from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/identification")
def identification():
    return render_template("identification.html")

if __name__ == "__main__":
    app.run(debug=True)