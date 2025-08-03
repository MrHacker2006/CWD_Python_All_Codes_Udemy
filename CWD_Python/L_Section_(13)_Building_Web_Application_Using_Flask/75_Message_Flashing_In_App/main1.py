from flask import Flask , render_template, flash

app = Flask(__name__)

app.secret_key = "gkdlfldjfoajor39" # If we try to run it without this key, it will give error

@app.route('/')
def hello_world():
    return render_template("index1.html")

@app.route('/logout')
def logout():
    flash("You have been logged out!", "sucess")
    return render_template("index1.html")

app.run(debug=True)