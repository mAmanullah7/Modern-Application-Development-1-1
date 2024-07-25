
# from flask import Flask, request
# import sys
# app = Flask(__name__)

# @app.route('/home', methods=[sys.argv[1]])
# def my_func():
#     if request.method == 'GET':
#         return "<h1>Hello from App Development</h1>"
#     elif request.method == 'POST':
#         return "<h1>Hello from POST</h1>"
#     else:
#         return "<h1>Please enter a valid HTTP method</h1>"

# app.run(debug=True)


from flask import Flask, request
import sys
app = Flask(__name__)

@app.route('/home', methods=sys.argv)
def my_func():
    if request.method == 'GET':
        return f"Hello from {sys.argv[1]} method"
    elif request.method == 'POST':
        return f"Hello from {sys.argv[2]} method"
    else:
        return "please enter a valid HTTP method"

app.run(debug=True)

# curl -X POST http://127.0.0.1:5000/home?



# from flask import Flask, request
# import sys

# app = Flask(__name__)

# @app.route('/home', methods=[sys.argv[1]])
# def my_func():
#     if request.method == 'GET':
#         return "<h1>Hello from App Development</h1>"
#     elif request.method == 'POST':
#         return "<h1>Hello from POST</h1>"
#     else:
#         return "<h1>Please enter a valid HTTP method</h1>"

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask
# from flask import render_template
# from flask import request

# app = Flask(__name__)

# @app.route("/hello", methods=["GET", "POST"])

# def Hello_world():
#     if request.method == "GET":
#         return render_template("details.html")
    
#     elif request.method == "POST":
#         username = request.form["name"]
#         return render_template("display.html", name=username)
    
#     else:
#         print("Error Chek")


# if __name__ == '__main__':
#     app.debug=True
#     app.run()