from flask import Flask, render_template, request
from flask.globals import session
from werkzeug.utils import redirect

app= Flask(__name__)
app.secret_key="my secret"

@app.route("/", methods=["GET"])
  
def counter():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route("/destroy_session", methods=["GET"])
def destroySession():
    session.clear()
    return redirect('/')

@app.route("/add2", methods=["GET"])
def addbytwo():
    session["counter"] +=1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)