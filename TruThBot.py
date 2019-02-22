import discord
from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup as bs
client = discord.Client()
bot = commands.Bot(command_prefix='T')
import os
@bot.event
async def on_ready():
    print("로그인")
    print(bot.user.name)
    print(bot.user.id)
    print("------------------")
    await bot.change_presence(game=discord.Game(name="수린이 입니다. -_-", type=1))
@bot.event
async def on_message(message):
    if message.content.startswith("봇"):
        if message.content[-1] == "?":
            await bot.send_message(message.channel, "네," + message.content[1:-1])
        else:
            await bot.send_message(message.channel, "네,"+message.content[1:])
    id = message.author.id
    if message.content.startswith("tr"):
         await bot.send_message(message.channel, "<@" + id + ">님이\"" + message.content[3:] + "\"라고 말하였습니다.")
    if "검색" == message.content.split(" ")[0]:
        group = message.content.split(" ")[1]
        search = requests.get("https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group)
        bp = bs(search.text, "html.parser")
        img = bp.find_all("img")

        await bot.send_message(message.channel, img[11]['src'])

        del group, search, bp, img
    if message.content.startswith("비밀"):
        await bot.delete_message(message)
        await bot.send_message(message.channel, message.content[2:])
        # await bot.send_message(message.channel, "https://www.google.com/search?q=")
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
