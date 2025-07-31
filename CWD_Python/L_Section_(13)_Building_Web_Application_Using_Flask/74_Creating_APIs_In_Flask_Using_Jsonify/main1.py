from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def json():
    marks = {
        "Saurabh": 89,
        "Raghav": 56,
        "Shaurya": 77,
        "Shaskank": 89,
        "Hariom": 69
    }
    return jsonify(marks)

app.run(debug=True)