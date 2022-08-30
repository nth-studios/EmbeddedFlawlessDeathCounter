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
    # print("-----------")
    # print("")
    # print("Welcome to the flawless embed terminal!")
    # print("")
    # print("Enter the name for player 1:")
    # players.append(input())
    # print("Enter the name for player 2:")
    # players.append(input())
    # print("Enter the name for player 3:")
    # players.append(input())
    # print("Enter the name for player 4:")
    # players.append(input())
    # print("Enter the name for player 5:")
    # players.append(input())
    # print("Enter the name for player 6:")
    # players.append(input())
    # embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
    # embed2 = await ctx.send(embed=embedVar)


@bot.command()
async def flawless(ctx):
    print("-----------")
    print("")
    print("Welcome to the flawless embed terminal!")
    print("")
    print("Enter the name for player 1:")
    players.append(input())
    deaths.append(0)
    print("Enter the name for player 2:")
    players.append(input())
    deaths.append(0)
    print("Enter the name for player 3:")
    players.append(input())
    deaths.append(0)
    print("Enter the name for player 4:")
    players.append(input())
    deaths.append(0)
    print("Enter the name for player 5:")
    players.append(input())
    deaths.append(0)
    print("Enter the name for player 6:")
    players.append(input())
    deaths.append(0)
    embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
    for i in range(len(players)):
        embedVar.add_field(name=players[i], value=deaths[i], inline=False)
    embed2 = await ctx.send(embed=embedVar)

    while(True):
        num = input()
        deaths[num-1] += 1
        embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
        for i in range(len(players)):
            embedVar.add_field(name=players[i], value=deaths[i], inline=False)
        await embed2.edit(embed=embedVar)


# @bot.command()
# async def new(ctx, player: str):
#     num = len(players)+1
#     players.append(player + " (" + str(num) + ")")
#     deaths.append(0);
#     embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
#     for i in range(len(players)):
#         embedVar.add_field(name=players[i], value=deaths[i], inline=False)
#     await ctx.send(embed=embedVar)
#
# @bot.command()
# async def death(ctx, num: int):
#     if(num<len(players)+1):
#         deaths[num-1] += 1
#         embedVar = discord.Embed(title="Flawless Raid", description="Death Counter", color=0x00ff00)
#         for i in range(len(players)):
#             embedVar.add_field(name=players[i], value=deaths[i], inline=False)
#         await ctx.send(embed=embedVar)



bot.run("token")

