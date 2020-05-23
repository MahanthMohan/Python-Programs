import requests  #A python module to send requests to an API and collect data
import tkinter as tk
root = tk.Tk()

city = input("Enter the city name: ")
request_url = 'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={}'.format(city)
# This is the link that has two attributes: Your api id and the location request
return_data = requests.get(request_url).json()
relevant_data = return_data['main']
Current_temp = 'The Current temperature is ' + str(int((relevant_data['temp']) - 273)) + " degrees Celsius"
Maximum_temp = 'The Maximum temperature is ' + str(int(relevant_data['temp_max'] - 273)) + " degrees Celsius"
Minimum_temp = 'The Minimum temperature is ' + str(int(relevant_data['temp_min'] - 273)) + " degrees Celsius"
Humidity = 'The Humidity is ' + str((relevant_data['humidity']))
# Displays the json weather data in form of an integer
def DisplayWeather():
    CL.place(x = '600', y = '125')
    WL1.place(x = '600', y = '210')
    WL2.place(x = '600', y = '285')
    WL3.place(x = '600', y = '360')
    WL4.place(x = '600', y = '435')
# A method that places the labels onto the canvas
Canvas = tk.Canvas(root, height = '1080', width = '1920')
Canvas.pack()
# Creates a canvas
CL = tk.Label(root, text = "Today's weather for the city of {}: ".format(city))
WL1 = tk.Label(root, text = Current_temp)
WL2 = tk.Label(root, text = Maximum_temp)
WL3 = tk.Label(root, text = Minimum_temp)
WL4 = tk.Label(root, text = Humidity)
# Labels that display the parsed json text
WeatherButton = tk.Button(root, text = "Display Weather", command = DisplayWeather)
WeatherButton.pack()
WeatherButton.place(relx = '0.45', rely = '0.8', height = '55', width = '125')
# A button to display weather, which is done by calling the command DisplayWeather
tk.mainloop()
# Closes the execution of tkinter
