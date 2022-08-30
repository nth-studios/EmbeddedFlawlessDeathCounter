import keyboard

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
global embed2
players = []
deaths = []

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def flawless(ctx):
    embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
    players = []
    deaths = []
    embed2 = await ctx.send(embed=embedVar)

@bot.command()
async def add(ctx, player: str):
    num = len(players)+1
    players.append(player + " (" + str(num) + ")")
    deaths.append(0);
    embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
    for i in range(len(players)):
        embedVar.add_field(name=players[i], value=deaths[i], inline=True)
    await ctx.send(embed=embedVar)

@bot.command()
async def death(ctx, num: int):
    if(num<len(players)+1):
        deaths[num-1] += 1
        embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
        for i in range(len(players)):
            embedVar.add_field(name=players[i], value=deaths[i], inline=False)
        await ctx.send(embed=embedVar)



bot.run("token")

