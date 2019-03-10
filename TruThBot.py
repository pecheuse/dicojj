import discord
from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup as bs
client = discord.Client()
bot = commands.Bot(command_prefix='T')
import os
YES = "네,"
YES2 = "너"
YES3 = "<@"
YES4 = ">님이\""
YES5 = "\"라고 말하였습니다."
@bot.event
async def on_ready():
    print("로그인")
    print(bot.user.name)
    print(bot.user.id)
    print("------------------")
    await bot.change_presence(game=discord.Game(name="수린이 입니다. -_-", type=1))
@bot.event
async def on_message(message):
    if message.content.startswith("봇 "):
        if message.content[-1] == "?":
            if message.content[2] == "나":
                embed = discord.Embed(title="수린:", description= YES + YES2+message.content[3:-1], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="수린:", description= YES + message.content[2:-1], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
        else:
            if message.content[2]== "나":
                embed = discord.Embed(title="수린:", description= YES + YES2+message.content[3:-1], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="수린:", description= YES+message.content[2:], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
    id = message.author.id
    if message.content.startswith("tr "):
         embed = discord.Embed(title="수린:", description=YES3 + id + YES4 + message.content[3:] + YES5, color=0x383b38)
         await bot.send_message(message.channel, embed=embed)
    if "검색" == message.content.split(" ")[0]:
        group = message.content.split(" ")[1]
        search = requests.get("https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group)
        bp = bs(search.text, "html.parser")
        img = bp.find_all('img')
        img2=img[2]
        img_src=img2.get('src')
        embed = discord.Embed(title="수린:", description= "https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group, color=0x383b38)
        embed.set_footer(icon_url="https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group)
        embed.set_image(url=img_src)
        await bot.send_message(message.channel, embed=embed)
        del group, search, bp, img, embed
    if message.content.startswith("비밀"):
        await bot.delete_message(message)
        embed = discord.Embed(title="비밀 메시지 입니다.", description=message.content[2:], color=0x383b38)
        await bot.send_message(message.channel, embed=embed)
        # await bot.send_message(message.channel, "https://www.google.com/search?q=")
    if message.content.startswith("T표현 "):
        AA = message.content[4:]
        AA2 = AA.upper()
        A = AA2.replace('A', ":regional_indicator_a:")
        B = A.replace('B', ":regional_indicator_b:")
        CC = B.replace('C', ":regional_indicator_c:")
        DD = CC.replace('D', ":regional_indicator_d:")
        EE = DD.replace('E', ":regional_indicator_e:")
        FF = EE.replace('F', ":regional_indicator_f:")
        GG = FF.replace('G', ":regional_indicator_g:")
        HH = GG.replace('H', ":regional_indicator_h:")
        II = HH.replace('I', ":regional_indicator_i:")
        JJ = II.replace('J', ":regional_indicator_j:")
        KK = JJ.replace('K', ":regional_indicator_k:")
        LL = KK.replace('L', ":regional_indicator_l:")
        MM = LL.replace('M', ":regional_indicator_m:")
        NN = MM.replace('N', ":regional_indicator_n:")
        OO = NN.replace('O', ":regional_indicator_o:")
        PP = OO.replace('P', ":regional_indicator_p:")
        QQ = PP.replace('Q', ":regional_indicator_q:")
        RR = QQ.replace('R', ":regional_indicator_r:")
        SSS = RR.replace('S', ":regional_indicator_s:")
        TT = SSS.replace('T', ":regional_indicator_t:")
        UU = TT.replace('U', ":regional_indicator_u:")
        VV = UU.replace('V', ":regional_indicator_v:")
        WW = VV.replace('W', ":regional_indicator_w:")
        XX = WW.replace('X', ":regional_indicator_x:")
        YY = XX.replace('Y', ":regional_indicator_y:")
        ZZ = YY.replace('Z', ":regional_indicator_z:")
        Z0 = ZZ.replace('0', ":zero:")
        Z1 = Z0.replace('1', ':one:')
        Z2 = Z1.replace('2', ':two:')
        Z3 = Z2.replace('3', ':three:')
        Z4 = Z3.replace('4', ':four:')
        Z5 = Z4.replace('5', ':five:')
        Z6 = Z5.replace('6', ':six:')
        Z7 = Z6.replace('7', ':seven:')
        Z8 = Z7.replace('8', ':eight:')
        Z9 = Z8.replace('9', ':nine:')
        embed = discord.Embed(description=Z9, color=0x383b38)
        await bot.send_message(message.channel, embed=embed)
    if message.content.startswith("T명령어"):
        embed = bot.send_message(message.channel, "봇 <내용> (대화 기능)\ntr <내용> (내용 강조)\n검색 <내용> (이미지 검색)\n비밀 <내용> (비밀 메시지)\nT표현 <내용> (이모티콘으로 영어,숫자표시)")
        await bot.send_message(message.channel, embed=embed)
    if message.content.startswith("T투표"):
        async def quickpoll(self, ctx, question, *options: str):
            if len(options) <= 1:
                await self.bot.say('You need more than one option to make a poll!')
                return
            if len(options) > 10:
                await self.bot.say('You cannot make a poll for more than 10 things!')
                return

            if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
                reactions = ['✅', '❌']
            else:
                reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
            description = []
            for x, option in enumerate(options):
                description += '\n {} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description))
            react_message = await self.bot.say(embed=embed)
            for reaction in reactions[:len(options)]:
                await self.bot.add_reaction(react_message, reaction)
            embed.set_footer(text='Poll ID: {}'.format(react_message.id))
            await self.bot.edit_message(react_message, embed=embed)
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
