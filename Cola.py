import discord
from discord import Attachment
from discord.ext import commands

from Image_processing import Image_process


client = commands.Bot(command_prefix=".",intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")



@client.command()
async def hello(ctx):
    await ctx.channel.send(f"Hello! {ctx.author.mention}")


@client.command()
async def ping(ctx):

    await ctx.channel.send(f"Pong {round(client.latency*1000)} ms")

@client.command()
async def cc(ctx):

    url='https://cdn.discordapp.com/avatars/595492589826736128/0560c62892e1eaecfbe9323252c85811.webp?size=256'
    
    img = Image_process(USER_NAME='》》• PokemonMaster • 《《',USER_PFP_URL=url,CUR_XP=100,MAX_XP=400) 

    await ctx.channel.send(file=discord.File(fp=img,filename='img.png'))
client.run('secret_token')

