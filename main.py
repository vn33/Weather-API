from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/translator")
def translator():
    return render_template("translator.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# @app.route("/api/v1/<word>")
# def info(word):
#     df = pd.read_csv("dictionary.csv")
#     definition = df.loc[df['word'] == word]['definition'].squeeze()
#     return {
#         "definition": definition,
#         "word": word
#     }


if __name__ == "__main__":
    app.run(debug=True)


