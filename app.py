from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "550255f5f7deaee4349ec80327f8b1e5"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form["city"]

        complete_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)

        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }

        elif response.status_code == 404:
            error = "City not found"
        elif response.status_code == 401:
            error = "Invalid API key"
        else:
            error = "Something went wrong"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)