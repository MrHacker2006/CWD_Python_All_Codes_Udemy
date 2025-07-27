from flask import Flask , render_template

app = Flask(__name__ , static_url_path="/assets") # This is how you can change static url path 

@app.route('/')
def hello_world():
    return render_template("index.html")

app.run(debug=True)