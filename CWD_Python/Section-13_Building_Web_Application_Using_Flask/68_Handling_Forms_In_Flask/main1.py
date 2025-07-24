from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def hello_world():
    print(request.method) # It will tell which type of method is used(GET or POST)
    print(request.form)  # It will return an immutable dict
    return render_template("contact.html")

app.run(debug=True)