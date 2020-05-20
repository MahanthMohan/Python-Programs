import discord
from discord.ext import commands
import wikipedia
import requests
import random
import json

def get_token():
    f = open("token.txt", "r")
    token = f.read().replace("bot_token: ","")
    return token

def responses(response_number):
    with open("intents.json") as file:
        intents = json.load(file)['intents']
        response_list = intents[response_number]['responses']
        leng = len(response_list)
        response = str(response_list[random.randint(0,leng)])
        return response

bot = commands.Bot(command_prefix='$')

@bot.event
async def member_join(member):
        for channel in member.server.channels:
                await bot.send_message("Welcome to the server {}".format(member.mention))

@bot.event
async def on_message(message):
    if message.content.find("$help") != -1:
        await message.channel.send("The prefix is $")
        await message.channel.send("Common commands include Hello, Shrug, Search, Channel, and Users")

    if message.content.find("$hello") != -1:
        await message.channel.send(responses(1))

    if message.content.find("$say") != -1:
            content = message.content
            callPhrase = "$say "
            return_content = content.partition(callPhrase)[2]
            await message.channel.send(return_content)

    if message.content.find("$shrug") != -1:
        await message.channel.send('¯\_(ツ)_/¯')

    if message.content.find("$how are you?") != -1:
        await message.channel.send(responses(2))

    if message.content.find("$who are you?") != -1:
        await message.channel.send(responses(3))

    if message.content.find("$thank you") != -1:
        await message.channel.send(responses(4))

    if message.content.find("$what do you eat?") != -1:
        await message.channel.send(responses(5))

    if message.content.find("$search") != -1:
            search = message.content
            callPhrase = "$search "
            query = search.partition(callPhrase)[2]
            return_content = wikipedia.summary(query, sentences = 5)
            await message.channel.send(return_content)

    if message.content.find("$users") != -1:
            id = bot.get_guild(ctx.message.server)
            await message.channel.send("# of Members are {}".format(id.member_count))

    if message.content.find("$server") != -1:
            ch = bot.get_guild(ctx.message.server)
            await message.channel.send("The server name is " + str(ch))

    if message.content.find("$channel") != -1:
            ch = message.channel
            await message.channel.send("This message was sent to the " + str(ch) + " channel")

    if message.content.find("$author") != -1:
            author = message.author
            await message.channel.send("the author of this message is " + str(author))

    if message.content.find("$translate") != -1:
            content = message.content
            callPhrase = "$translate "
            query = content.partition(callPhrase)[2]
            request_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200510T203759Z.c32fdda6ccace388.761b8b4cbfa468781df5a3b117f3eccb0407f241&text={}&lang=en&format=plain".format(query)
            return_data = requests.get(request_URL).json()
            translated_text = return_data['text']
            await message.channel.send(translated_text[0])

    if message.content.find("$weather") != -1:
        content = message.content
        callPhrase = "$weather "
        city = content.partition(callPhrase)[2]
        request_url = 'http://api.openweathermap.org/data/2.5/weather?appid=a82ce5d667628af3985ec52d8a1a91eb&q={}'.format(city)
        return_data = requests.get(request_url).json()
        relevant_data = return_data['main']
        Current_temp = 'The Current temperature is ' + str(int((relevant_data['temp']) - 273)) + " degrees Celsius"
        Maximum_temp = 'The Maximum temperature is ' + str(int(relevant_data['temp_max'] - 273)) + " degrees Celsius"
        Minimum_temp = 'The Minimum temperature is ' + str(int(relevant_data['temp_min'] - 273)) + " degrees Celsius"
        await message.channel.send(Current_temp)
        await message.channel.send(Maximum_temp)
        await message.channel.send(Minimum_temp)

    if message.content.find("$purge") != -1:
        content = str(message.content)
        content_list = content.split(" ")
        amount = int(content_list[1])
        await message.channel.purge(limit = amount, bulk = amount)

    if message.content.find("$terminate") != -1:
            await message.channel.send("***The bot was terminated***")
            await bot.close() 

bot.run(get_token())
