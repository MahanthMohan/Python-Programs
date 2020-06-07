import requests  #A python module to send requests to an API and collect data
import tkinter as tk

root = tk.Tk()

# A method that places the labels onto the canvas
def DisplayWeather():
    CL.place(x = '600', y = '125')
    WL1.place(x = '600', y = '160')
    WL2.place(x = '600', y = '245')

# A method that collects the user location from the GUI
def getLocation():
   City = tk.Label(root, text="City")
   City.place(x = '600', y = '90')
   e = tk.Entry(root)
   location = str(e.get())
   return location

# Creates a canvas
Canvas = tk.Canvas(root, height = '1080', width = '1920')
Canvas.pack()

# A button to display weather, which is done by calling the command DisplayWeather
WeatherButton = tk.Button(root, text = "Display Weather", command = DisplayWeather)
WeatherButton.pack()
WeatherButton.place(relx = '0.45', rely = '0.8', height = '55', width = '125')

city = getLocation()
request_url = 'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={}'.format(city)
# This is the link that has two attributes: Your api id and the location request

# Displays the json weather data in form of an integer
return_data = requests.get(request_url).json()
temp_data = return_data['main']['temp']
weather_data = return_data['weather']['description']
Current_temp = 'The Current temperature is ' + str(int(temp_data - 273)) + " degrees Celsius"


CL = tk.Label(root, text = "Today's weather for the city of {}: ".format(city))
WL1 = tk.Label(root, text = Current_temp)
WL2 = tk.Label(root, text = temp_data)
# Labels that display the parsed json text

tk.mainloop()
# Closes the execution of tkinter
