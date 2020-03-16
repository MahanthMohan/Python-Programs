import discord
import requests 
import wikipedia

token = "Discord_bot_key"
client = discord.Client()

@client.event
async def bot_responses(message):
 if message.content.find("!hello") != -1:
      await message.channel.send("Hello!")

 elif message.content.find("!How are you") != -1:
      await message.channel.send("Great!")
       
 elif message.content.find("!Who are you?") != -1:
      await message.channel.send("I am a bot, but consider me your friend!")
    
 elif message.content.find("!How is the weather?") != -1:
       API_URL = 'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb'
       request_url = 'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={}'.format("Cupertino")
       return_data = requests.get(request_url).json()
       relevant_data = return_data['main']
       description = relevant_data['description']
       current_temp = 'and the Current temperature is ' + str(int((relevant_data['temp']) - 273)) + " degrees Celsius"
       await message.channel.send("The weather in Cupertino is " + current_temp)
 
 elif message.content.find("!Thank you") != -1:
       await message.channel.send("Happy to help, as always!") 
 
 elif message.content.find("!Search") != -1:
       await message.channel.send(wikipedia.summary("Android", sentences = 4))
        
client.run(token)