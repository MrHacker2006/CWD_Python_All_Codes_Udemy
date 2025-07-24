from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def hello_world():
    print(request.method) # It will tell which type of method is used(GET or POST)
    print(request.form)  # It will return an immutable dict
    if(request.method == "POST"):
        with open("File.txt", "w") as f:
            f.write(f"The name of the user is {request.form['Name']} and the email of the user is {request.form['Email']}")
        return render_template("contact.html")
    else:
         return render_template("contact.html")

app.run(debug=True)