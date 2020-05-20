import discord
from discord.ext import commands

def get_token():
    f = open("token.txt", "r")
    token = f.read().replace("bot_token: ","")
    return token

bot = commands.Bot(command_prefix = '$')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(get_token())