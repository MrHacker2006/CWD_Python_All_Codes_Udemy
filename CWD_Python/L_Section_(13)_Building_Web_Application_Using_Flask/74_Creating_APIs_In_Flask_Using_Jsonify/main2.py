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

    Values = [3 , marks, 5]
    return jsonify(Values)

app.run(debug=True)