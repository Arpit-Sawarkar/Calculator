from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    display = ""

    if request.method == "POST":
        display = request.form.get("display")
        btn = request.form.get("btn")

        if btn == "AC":
            display = ""

        elif btn == "BACK":
            display = display[:-1]

        elif btn == "=":
            try:
                display = str(eval(display))
            except:
                display = "Error"

        else:
            display = display + btn

    return render_template("index.html", display=display)


if __name__ == "__main__":
    app.run(debug=True)
