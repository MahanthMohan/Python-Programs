import discord
from discord.ext import commands
import wikipedia
import requests
import random
import json

def responses(response_number):
    with open("intents.json") as file:
        intents = json.load(file)['intents']
        response_list = intents[response_number]['responses']
        response = str(response_list[random.randint(0, len(response_list))])
        return response

bot = commands.Bot(command_prefix='$')

@bot.event
async def member_join(member):
        for channel in member.server.channels:
                await bot.send_message(f"Welcome to the server {member.mention}")

@bot.event
async def on_message(message):
    if message.content.find("$help") != -1:
        await message.channel.send("The prefix is $")
        await message.channel.send("Common commands include Hello, Shrug, Search, Translate, Weather, Channel, and Users")

    if message.content.find("$hello") != -1:
        await message.channel.send(responses(0))

    if message.content.find("$say") != -1:
            await message.channel.send(message.content.partition("$say ")[2])

    if message.content.find("$shrug") != -1:
        await message.channel.send('¯\_(ツ)_/¯')

    if message.content.find("$how are you?") != -1:
        await message.channel.send(responses(1))

    if message.content.find("$who are you?") != -1:
        await message.channel.send(responses(2))

    if message.content.find("$thank you") != -1:
        await message.channel.send(responses(3))

    if message.content.find("$what do you eat?") != -1:
        await message.channel.send(responses(4))

    if message.content.find("$search") != -1:
            await message.channel.send(wikipedia.summary(message.content.partition("$search ")[2], sentences = 5))

    if message.content.find("$users") != -1:
            await message.channel.send(f"# of Members are {bot.get_guild(689260912200122383).member_count}")

    if message.content.find("$server") != -1:
            await message.channel.send("The server name is " + str(bot.get_guild(689260912200122383)))

    if message.content.find("$channel") != -1:
            await message.channel.send("This message was sent to the " + str(message.channel) + " channel")

    if message.content.find("$author") != -1:
            await message.channel.send("the author of this message is " + str(message.author))

    if message.content.find("$translate") != -1:
            callPhrase = "$translate "
            query = message.content.partition(callPhrase)[2]
            request_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200510T203759Z.c32fdda6ccace388.761b8b4cbfa468781df5a3b117f3eccb0407f241&text={}&lang=en&format=plain".format(query)
            translated_text = requests.get(request_URL).json()['text'][0]
            await message.channel.send(translated_text)

    if message.content.find("$weather") != -1:
        relevant_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={message.content.partition("$weather ")[2]}').json()['main']
        await message.channel.send('The Current temperature is ' + str(int((relevant_data['temp']) - 273)) + " degrees Celsius")
        await message.channel.send('The Maximum temperature is ' + str(int(relevant_data['temp_max'] - 273)) + " degrees Celsius")
        await message.channel.send('The Minimum temperature is ' + str(int(relevant_data['temp_min'] - 273)) + " degrees Celsius")

    if message.content.find("$purge") != -1:
        await message.channel.purge(limit = int(str(message).content.split(" ")[1]), bulk = int(str(message).content.split(" ")[1]))

    if message.content.find("$terminate") != -1:
            await message.channel.send("***The bot was terminated***")
            await bot.close() 

bot.run('NzExOTg5MTYwNzkzMzQyMDI0.Xv-eDQ.ZLhULGWawqqM9-9lhpMnqxqM9j8')