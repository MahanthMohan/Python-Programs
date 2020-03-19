import discord.ext.commands 
from discord.ext.commands import Bot
import wikipedia

token = 'Njg5MjYxMjk0NTIzNzc3MDgz.XnLqnw.UvWvBzl_1Tq3by9qNHZKuPwEUXw'

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
            bruh = search.split(" ")
            query = bruh[1] 
            return_content = wikipedia.summary(query)
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
            
    if message.content == "$author" != -1:
            author = message.author
            await message.channel.send("the author of this message is " + str(author))
                                            
client.run(token)