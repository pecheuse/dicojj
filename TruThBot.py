import discord
from discord.ext import commands
import asyncio
import requests
import random
from bs4 import BeautifulSoup
client = discord.Client()
bot = commands.Bot(command_prefix='$')
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
    game = discord.Game("test")
    await bot.change_presence(status=discord.Status.online, activity=game)
@bot.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content[0:4] == "$검색 ":
        messagesplit = message.content.split(" ")
        messagesplit = ''.join(messagesplit[1:])
        webpage = requests.get("https://www.google.com/search?q="+str(messagesplit)+"&hl=ko&tbm=isch")
        soup = BeautifulSoup(webpage.text, "html.parser")
        img = soup.find_all('img')
        img2=img[2]
        img_src=img2.get('src')
        embed = discord.Embed(title=message.content[4:]+":",
                              description="https://www.google.com/search?q="+str(messagesplit)+"&hl=ko&tbm=isch",
                              color=0x383b38)
        embed.set_footer(
            icon_url="https://www.google.com/search?q="+str(messagesplit)+"&hl=ko&tbm=isch")
        embed.set_image(url=img_src)
        await message.channel.send(embed=embed)
    if message.content.startswith("$tr "):
         embed = discord.Embed(title="수린:", description=str(YES3) + str(id) + str(YES4) + str(message.content[3:]) + str(YES5), color=0x383b38)
         await message.channel.send(embed=embed)

    if message.content.startswith("$비밀"):
        await message.channel.purge(limit=1)
        embed = discord.Embed(title="비밀 메시지 입니다.", description=message.content[3:], color=0x383b38)
        await message.channel.send("누군가가 비밀 메세지를 입력 했습니다.", embed=embed)
        # await bot.send_message(message.channel, "https://www.google.com/search?q=")
    if message.content.startswith("$표현 "):
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
        await message.channel.send(embed=embed)
    if message.content.startswith("$명령어"):
        embed = discord.Embed(description= "$봇 <내용> (대화 기능)\n$tr <내용> (내용 강조)\n$검색 <내용> (이미지 검색)\n$비밀 <내용> (비밀 메시지)\n$표현 <내용> (이모티콘으로 영어,숫자표시)\n$투표 <(내용)/투표)> (투표)\n$랜덤 <1번/2번/3번/4번...> (랜덤 추첨)", color=0x383b38)
        await message.channel.send(embed=embed)
    if message.content.startswith("$랜덤"):
        select = message.content[4:].split("/")
        select2 = random.choice(select)
        embed = discord.Embed(description="선정:"+select2, color=0x383b38)
        await message.channel.send(embed=embed)
    """if message.content.startswith("Tnick "):
        if message.content[6:9] == 'add':
            write = open('./nickname.txt', 'a+')
            write.write(YES3+id+">:"+message.content[10:]+"\n")
            write.close()
            await message.channel.send(message.channel, 'Done!')
        if message.content[6:10] == 'list':
            read = open('./nickname.txt', 'r')
            await message.channel.send(message.channel, read.read())
            read.close() """
    if message.content[0:4] == "$계산 ":
        splitphase = message.content.split(" ")
        first1 = int(splitphase[1])
        second2 = splitphase[2]
        third3 = int(splitphase[3])
        result2 = 0
        if second2 == "*":
            result2 = first1 * third3
        elif second2 == "/":
            result2 = first1 / third3
        elif second2 == "+":
            result2 = first1 + third3
        elif second2 == "-":
            result2 = first1 - third3
        await message.channel.send(result2)
    if message.content[0:5] == "$계산기 ":
        splitphase = message.content.split(" ")
        result3 = int(splitphase[1])

        for i in range(len(splitphase)):
            if i == 0 or i == 1:
                pass
            elif splitphase[i] != "*" and splitphase[i]!="+"and splitphase[i]!= "/"and splitphase[i]!= "-":
                pass
            elif splitphase[i] == "*":
                result3 *= int(splitphase[i+1])
            elif splitphase[i] == "+":
                result3 += int(splitphase[i+1])
            elif splitphase[i] == "-":
                result3 -= int(splitphase[i+1])
            elif splitphase[i] == "/":
                result3 /= int(splitphase[i+1])
        await message.channel.send("계산은 앞에서부터 뒤로 계산합니다. 계산순서무시")
        await message.channel.send(result3)
    if message.content[0:4] == "$삭제 ":
        split4 = message.content.split(" ")
        split4 = int(split4[1])
        await message.channel.purge(limit=split4)
    if message.content[0:4] == "$도배 ":
        split5 = message.content.split(" ")
        split6 = int(split5[1])
        split7 = ' '.join(split5[2:])
        for i in range(split6):
            if i <= 10:
                await message.channel.send(split7)
    if message.author.id == 669851548414640131:
        embed = discord.Embed(title="o3983은 발언권 없어짐", description=message.content,
                              color=0x383b38)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.delete()
        await message.channel.send(embed = embed)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)

