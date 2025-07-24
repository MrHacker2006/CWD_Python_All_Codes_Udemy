from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Saurabh": 89,
        "Raghav": 56,
        "Shaurya": 77,
        "Shaskank": 89,
        "Hariom": 69
    }
    return render_template("index1.html", marks= marks)

app.run(debug = True)