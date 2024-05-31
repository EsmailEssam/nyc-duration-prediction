from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

# Load model
duration_model = pickle.load(open("models/duration-prediction.sav", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == 'POST':
        passenger_count = float(request.form.get("passenger_count", False))
        trip_distance = float(request.form.get("trip_distance", False))
        PULocationID = float(request.form.get("pull_location_id", False))
        DOLocationID = float(request.form.get("down_location_id", False))
        total_amount = float(request.form.get("total_amount", False))

        test_input = [
            [passenger_count, trip_distance, PULocationID, DOLocationID, total_amount]
        ]

        prediction = round(duration_model.predict(test_input)[0], 2)

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
