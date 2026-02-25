from flask import Flask, render_template, request
app = Flask(__name__)


def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mult(a, b):
    c = a * b
    return c

def div(a, b):
    c = a / b
    return c


@app.route("/")
def start_index():
    return render_template("index.html")
@app.route("/welcome")
def welcome():
    return "Welcome"
@app.route("/calculator") #mapping connects url request to python program
@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        ans = int(request.form.get("op"))

        if ans == 1:
            result = add(num1, num2)
        elif ans == 2:
            result = sub(num1, num2)
        elif ans == 3:
            result = mult(num1, num2)
        elif ans == 4:
            result = div(num1, num2)
        else:
            result = "Invalid option"

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)


app.run(host = "0.0.0.0", port=5050)