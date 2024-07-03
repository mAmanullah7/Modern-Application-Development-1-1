from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods=["GET", "POST"])

def Hello_world():
    if request.method == "GET":
        return render_template("details.html")
    
    elif request.method == "POST":
        username = request.form["name"]
        return render_template("display.html", name=username)
    
    else:
        print("Error Chek")


if __name__ == '__main__':
    app.debug=True
    app.run()