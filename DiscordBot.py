import discord

token = "Njg4ODI4NjY2NTQ4OTc3NzM3.Xm6w-w.f7JGqmKIQP8rusai5CWuoxeXT3g"
client = discord.Client()

@client.event
async def on_message(message):
 if message.content.find("!hello") != -1:
      await message.channel.send("Hello!")

client.run(token)