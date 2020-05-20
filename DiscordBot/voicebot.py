import discord
import youtube_dl
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

@bot.command()
async def play(ctx, url):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    player.start()
    
bot.run(get_token())