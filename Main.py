import os
import discord
import random
from replit import db
import math
#from alive_pls import keep_alive

invalid_msg = ['Invalid input','Sir, why you do that?','Some thing went so wrong','Check your input pls','Put trash in the recycle bin pls','404 not found .-.']


client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} say hello to your server,o/".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.author)
    msg = message.content
    msg.strip()
    if msg.startswith('/sayhi'):
        await message.channel.send('Hello!')

    if msg.startswith('$host'):
        phong = random.randint(100,999)
        if not "so phong" in db.keys():
           db["so phong"] = []
        while (str(phong) in db["so phong"]):
          phong = random.randint(100,999)
        db["so phong"] += [phong]
        #db[str(phong)] = [message.author]
        await message.channel.send("Phòng " + str(phong) + " đã được tạo bởi " + f"""{message.author.mention} """ + ". Sử dụng /join để tham gia và dùng /list để xem thành viên")

    if msg.startswith("$list"):
      for s in db["so phong"]:
        await message.channel.send(str(s) + "\n")

    if msg.startswith('/helpme'):
      await message.channel.send(file=discord.File('help.txt'))

##keep_alive()
TOKEN = os.environ['botToken']
client.run(TOKEN)
