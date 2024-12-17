from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature = 23

    return {"Station": station,
            "date": date,
            "temperature": temperature}

# this makes sure it only executes when executing directly
if __name__ == "__main__":
    app.run(debug=True, port=5001)
