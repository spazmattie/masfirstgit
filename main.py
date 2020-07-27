import sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name='MATT', age=16)

if __name__ == "__main__":
    app.run()

# print(sys.executable)
# print(sys.version)