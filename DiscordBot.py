import discord.ext.commands 
from discord.ext.commands import Bot
import wikipedia

token = 'bot_token_here'

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
        
    if message.content.find("$What do you eat?") != -1:
            await message.channel.send("Loads of data!")
            
    if message.content.find("$What do you eat?") != -1:
            await message.channel.send("Loads of data!") 

    if message.content.find("$Search") != -1:
            await message.channel.send("Enter the topic: ")
            search = message.content 
            return_content = wikipedia.summary(search, sentences = 5)
            await message.channel.send(return_content)
            
    if message.content.find("$users") != -1:
            id = client.get_guild(689260912200122383)
            await message.channel.send("# of Members are {}".format(id.member_count))
      
            
client.run(token)