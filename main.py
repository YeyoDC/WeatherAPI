from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STANAME                                 ', 'STAID']]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    # this will allow to read from any file
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])

    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    temperature = int(temperature)
    return {"Station": station,
            "date": date,
            "temperature": temperature}

# this makes sure it only executes when executing directly
if __name__ == "__main__":
    app.run(debug=True)
