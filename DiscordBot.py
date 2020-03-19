import discord.ext.commands 
from discord.ext.commands import Bot
import wikipedia

token = 'bot_token_here'

client = discord.Client()
bot = Bot(command_prefix='$') 

@client.event
async def on_message(message):

    if message.content == '$hello':
        await message.channel.send("Hello!")

    if message.content == "$shrug":
        await message.channel.send('¯\_(ツ)_/¯')
    
    if message.content == "$how are you?" != -1:
        await message.channel.send("Great!")
       
    if message.content == "$who are you?" != -1:
        await message.channel.send("I am a bot, but consider me your friend!")
    
    if message.content == "$thank you" != -1:
        await message.channel.send("Happy to help, as always!") 
        
    if message.content == "$what do you eat?" != -1:
            await message.channel.send("Loads of data!")

    if message.content == "$search" != -1:
            search = message.content 
            return_content = wikipedia.summary(search, sentences = 5)
            await message.channel.send(return_content)
            
    if message.content == "$users" != -1:
            id = client.get_guild(689260912200122383)
            await message.channel.send("# of Members are {}".format(id.member_count))
            
    if message.content == "$server" != -1:
            ch = client.get_guild(689260912200122383)
            await message.channel.send("The server name is " + str(ch))
 
    if message.content == "$channel" != -1:
            ch = message.channel
            await message.channel.send("This message was sent to the " + str(ch) + " channel") 

    if message.content == "$names" != -1:
            await message.channel.send(str(client.users))
            
    if message.content == "$terminate" != -1:
            await message.channel.send("The bot will be terminated..")
            client.logout()   
                                   
client.run(token)