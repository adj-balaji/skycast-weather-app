# 🌤️ SkyCast – Weather Forecast Web App

## 🚀 Overview

**SkyCast** is a simple and elegant web application that provides real-time weather information for any city using the OpenWeatherMap API.

It allows users to:

* Search for a city
* View live weather data
* Get key environmental details instantly

---

## 🎯 Objective

To build a lightweight web application that fetches and displays real-time weather data using external APIs.

---

## ⚙️ Features

* 🌍 Search weather by city name
* 🌡️ Temperature display (°C)
* 💧 Humidity levels
* 🌬️ Wind speed
* 🌪️ Atmospheric pressure
* 🌤️ Weather description
* ❌ Error handling (invalid city/API issues)

---

## 🧠 Tech Stack

### 🔹 Backend

* Python (Flask)

### 🔹 Frontend

* HTML
* CSS

### 🔹 API

* OpenWeatherMap API

---

## 🏗️ Project Architecture

```id="sky1"
User Input (City)
        ↓
Flask Backend
        ↓
OpenWeather API Request
        ↓
JSON Response Processing
        ↓
Render HTML Template
```

---

## 📂 Project Structure

```id="sky2"
SkyCast/
│
├── app.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── requirements.txt
├── README.md
```

---

## ▶️ Installation

```bash id="sky3"
git clone https://github.com/adj-balaji/skycast-weather-app.git
cd skycast-weather-app
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash id="sky4"
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔑 API Setup

* Get your API key from OpenWeatherMap
* Replace in `app.py`:

```python id="sky5"
API_KEY = "your_api_key_here"
```

---

## 📡 How It Works

### 🔹 1. User Input

* User enters city name

### 🔹 2. API Call

* Flask sends request to OpenWeather API

👉 Implementation: 

---

### 🔹 3. Data Processing

* Extract:

  * Temperature
  * Humidity
  * Wind speed
  * Description

---

### 🔹 4. UI Rendering

* Data passed to HTML template

👉 Template: 

---

### 🔹 5. Styling

* Clean UI using CSS

👉 Styles: 

---

## 📊 Example Output

* City: Chennai
* Temperature: 32°C
* Humidity: 70%
* Wind Speed: 5 m/s

---

## ⚠️ Limitations

* Requires internet connection
* Depends on API availability
* No forecast (only current weather)

---

## 🚀 Future Enhancements

* 🌦️ 5-day weather forecast
* 📍 Auto-detect location
* 🌙 Dark mode UI
* 📊 Weather charts
* 📱 Mobile responsive design

---

## 👨‍💻 Author

**BALAJI A D J**
GitHub: https://github.com/adj-balaji

---

## ⭐ Give a star if you like this project!
