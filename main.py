import sys
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/graph")
def graph():
    return render_template("graph.html")

@app.route("/resources.html")
def resources():
    return render_template("resources.html")

@app.route("/regents.html")
def regents():
    return render_template("regents.html")

@app.route("/java")
def java():
    return render_template("java.html")




if __name__ == "__main__":
    app.run(debug=True)

# print(sys.executable)
# print(sys.version)