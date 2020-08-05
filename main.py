from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='', static_folder='')

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

@app.route("/java.html")
def java():
    return render_template("java.html")

@app.route("/mathexams.html")
def math():
    return render_template("mathexams.html")






if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050, debug=True)

# print(sys.executable)
# print(sys.version)