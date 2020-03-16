import discord

token = "Njg4ODI4NjY2NTQ4OTc3NzM3.Xm7TRA.QTCmbv3W1pTGi9KQOhr4xPY0tSQ"
client = discord.Client()

@client.event
async def on_message(message):
 if message.content.find("!hello") != -1:
      await message.channel.send("Hello!")

client.run(token)