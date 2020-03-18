import discord.ext.commands 
from discord.ext.commands import Bot

token = 'Bot_token_here'

client = discord.Client()
bot = Bot(command_prefix='$') 

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")

    if message.content.startswith("$shrug"):
        await message.channel.send('¯\_(ツ)_/¯')
    
    if message.content.find("$How are you?") != -1:
        await message.channel.send("Great!")
       
    if message.content.find("$Who are you?") != -1:
        await message.channel.send("I am a bot, but consider me your friend!")
    
    if message.content.find("$Thank you") != -1:
        await message.channel.send("Happy to help, as always!") 

client.run(token)