''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

import os
import json
import requests
import tkinter as tk
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")

def generate_nairobi_weather():
    city = 'Nairobi'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        response = requests.get(url)
        response.status_code == 200
        data = response.json()
        weather_data = data['main']
        more_data = data['weather'][0]
    except:
        pass
    json_data = json.dumps(weather_data)
    root = tk.Tk()
    root.title("Nairobi Weather Information")
    text = tk.Text(root, height=10, width=30, bg="pink")
    text.pack()
    for k, v in weather_data.items():
        text.insert(tk.END, f"{k}: {v}\n")
    more_button = tk.Button(root, text="More", command=lambda: show_more_data(more_data))
    more_button.pack()
    root.mainloop()

def show_more_data(more_data):
    more_root = tk.Toplevel()
    more_root.title("More Information")
    more_text = tk.Text(more_root, height=10, width=30)
    more_text.pack()
    for k, v in more_data.items():
        more_text.insert(tk.END, f"{k}: {v}\n")

generate_nairobi_weather()
