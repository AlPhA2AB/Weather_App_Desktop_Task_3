import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dotenv import load_dotenv
import requests
import os
load_dotenv()
api_key =  os.getenv('api_key')
def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def print_weather(data):
    city = data['name']
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    temp_celsius = temp - 273.15
    result = f'City: {city}\nWeather: {weather}\nTemperature: {temp_celsius:.2f}°C\nHumidity: {humidity}%\nWind speed: {wind_speed}m/s'
    return result

def get_weather_info():
    city = city_entry.get()
    data = get_weather(city, api_key)
    if 'message' in data:
        messagebox.showerror('Error', data['message'])
    else:
        weather_info = print_weather(data)
        result_label.config(text=weather_info, justify='left', anchor='w', font=('Helvetica', 10, 'bold'), fg='purple', bg='white')

def update_datetime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_day = now.strftime("%A")
    time_label.config(text=f'TIME: {current_time}', justify='left', anchor='w', font=('Helvetica', 10, 'bold'), fg='green', bg='white')
    day_label.config(text=f'DAY: {current_day}', justify='left', anchor='w', font=('Helvetica', 10, 'bold'), fg='green', bg='white')

root = tk.Tk()
root.title('Weather App')
root.geometry('400x300')  # Set the initial size of the window

# Creating a frame to contain widgets
frame = tk.Frame(root, padx=20, pady=20, bg='white') # Set the background color of the frame to white
frame.pack(expand=True, fill=tk.BOTH)  # Expand to fill the available space

city_label = tk.Label(frame, text='Enter city name:', fg='green', font=('Helvetica', 10, 'bold'), bg='white')
city_label.grid(row=0, column=0, sticky='w', pady=5)

city_entry = tk.Entry(frame, font=('Helvetica', 10, 'bold'), fg='green')
city_entry.grid(row=0, column=1, pady=5)

get_weather_button = tk.Button(frame, text='GET WEATHER', fg='white', bg='green', font=('Helvetica', 10, 'bold'), command=get_weather_info)
get_weather_button.grid(row=1, column=0, columnspan=2, pady=5)


result_label = tk.Label(frame, text='', justify='left', anchor='w', font=('Helvetica', 10, 'bold'), fg='purple', bg='white')
result_label.grid(row=2, column=0, columnspan=2, pady=5)

# Labels to display current time and day
time_label = tk.Label(frame, text='', justify='left', anchor='w', font=('Helvetica', 10, 'bold'), fg='green', bg='white')
time_label.grid(row=3, column=0, columnspan=2, pady=5)

day_label = tk.Label(frame, text='', justify='left', anchor='w', font=('Helvetica', 10, 'bold'), fg='green', bg='white')
day_label.grid(row=4, column=0, columnspan=2, pady=5)

# Update time and day every second
update_datetime()
root.after(1000, update_datetime)

root.mainloop()
