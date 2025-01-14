# Weather App

This is a simple graphical weather application built using Python's `tkinter` module. The application retrieves real-time weather data using the OpenWeatherMap API and displays information about the current weather conditions, including temperature, humidity, wind speed, and more.

## Features

- **Real-time Weather Data**: Fetches weather information for any city in the world using the OpenWeatherMap API.
- **Interactive UI**: User-friendly interface to enter a city name and retrieve weather details.
- **Time and Day Display**: Continuously updates and displays the current time and day.
- **Error Handling**: Provides user-friendly error messages for invalid city names or issues with the API.

## Requirements

To run this application, you'll need the following:

- Python 3.x
- The following Python packages:
  - `tkinter`
  - `requests`
  - `python-dotenv`

You also need an API key from [OpenWeatherMap](https://openweathermap.org/api). Create a free account and generate an API key.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AlPhA2AB/Weather_App_Desktop__OasisInfobyte_Task_3.git
   cd Weather_App_Desktop__OasisInfobyte_Task_3
   ```

2. **Install Dependencies**
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup API Key**
   Create a `.env` file in the project directory and add your OpenWeatherMap API key:
   ```
   api_key=YOUR_API_KEY
   ```

4. **Run the Application**
   Execute the script to start the application:
   ```bash
   python script.py
   ```

## Usage

1. Open the application by running the script.
2. Enter the name of a city in the input field.
3. Click the **GET WEATHER** button to fetch and display the weather details.
4. The current time and day are updated automatically every second.

## Application Interface

- **Input Field**: Enter the city name for which you want weather information.
- **GET WEATHER Button**: Fetches the weather data for the entered city.
- **Weather Information Panel**: Displays details such as temperature, humidity, wind speed, and weather description.
- **Time and Day Panel**: Displays the current time and day.

## Example

Here is how the output look:

```
City: London
Weather: light rain
Temperature: 15.67°C
Humidity: 77%
Wind speed: 4.5m/s

TIME: 14:35:18
DAY: Monday
```

## Project Structure

```
Weather_App_Desktop__OasisInfobyte_Task_3/
|── script.py          # Main application script
|── .env               # Environment file to store API key
|── requirements.txt  # Python dependencies
|── README.md          # Project documentation
```

## Notes

- Ensure you have a stable internet connection for the API requests.
- If the API key is invalid or the city name is incorrect, an error message will be displayed.

## Future Improvements

- Add support for displaying extended weather forecasts.
- Integrate a map feature to visualize weather conditions.
- Support for multiple languages.
- Add a dark mode for the application interface.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your requirements.

# Developer Info
[Ayon Biswas](https://www.linkedin.com/in/ayon-biswas-61a595268)
