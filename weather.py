import requests  #A python module to send requests to an API and collect data
import tkinter as tk

root = tk.Tk()

# A method that collects the user location from the GUI
def getWeather():
   location = e.get()
   request_url = 'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={}'.format(location)
   return_data = requests.get(request_url).json()
   temp_data = return_data['main']['temp']
   temp = 'The temperature is ' + str(int(temp_data - 273)) + " degrees Celsius"
   weather_data = str(return_data['weather']).split(",")[2].replace('description":"','')
   description = weather_data.replace("'","")
   CL = tk.Label(root, text = "Weather in {}: ".format(location))
   WL1 = tk.Label(root, text = "-->" + description)
   WL2 = tk.Label(root, text = "--> " + temp)
   CL.place(x = '220', y = '270')
   WL1.place(x = '225', y = '300')
   WL2.place(x = '225', y = '330')


# Creates a canvas
Canvas = tk.Canvas(root, height = '562.5', width = '750', relief = 'raised')
Canvas.pack()

MainLabel = tk.Label(root, text = "Get Weather Data")
MainLabel.config(font=("montserrat", 16))
MainLabel.place(x = '260', y = '50')
City = tk.Label(root, text = "Your City/Location:")
City.place(x = '281.25', y = '100')
e = tk.Entry(root)
Canvas.create_window('332.5', '135', window = e)

WeatherButton = tk.Button(root, text = "Display Weather", command = getWeather)
WeatherButton.pack()
WeatherButton.place(x = '270', y = '170', height = '45', width = '125')

tk.mainloop()
# Closes the execution of tkinter
