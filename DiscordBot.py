import discord.ext.commands 
from discord.ext.commands import Bot
import wikipedia

token = 'bot_token_here'

client = discord.Client()
bot = Bot(command_prefix='$') 

@client.event
async def on_message(message):

    if message.content.find("$hello") != -1:
        await message.channel.send("Hello!")

    if message.content.find("$shrug") != -1:
        await message.channel.send('¯\_(ツ)_/¯')
    
    if message.content.find("$how are you?") != -1:
        await message.channel.send("Great!")
       
    if message.content.find("$who are you?") != -1:
        await message.channel.send("I am a bot, but consider me your friend!")
    
    if message.content.find("$thank you") != -1:
        await message.channel.send("Happy to help, as always!") 
        
    if message.content.find("$what do you eat?") != -1:
            await message.channel.send("Loads of data!")

    if message.content.find("$search") != -1:
            search = message.content
            splitted_search = search.split(" ")
            query = splitted_search[1] 
            return_content = wikipedia.summary(query, sentences = 3)
            await message.channel.send(return_content)
            
    if message.content.find("$users") != -1:
            id = client.get_guild(689260912200122383)
            await message.channel.send("# of Members are {}".format(id.member_count))
            
    if message.content.find("$server") != -1:
            ch = client.get_guild(689260912200122383)
            await message.channel.send("The server name is " + str(ch))
 
    if message.content.find("$channel") != -1:
            ch = message.channel
            await message.channel.send("This message was sent to the " + str(ch) + " channel") 

    if message.content.find("$names") != -1:
            await message.channel.send(str(client.users))
            
    if message.content.find("$author") != -1:
            author = message.author
            await message.channel.send("the author of this message is " + str(author))
                                            
client.run(token)