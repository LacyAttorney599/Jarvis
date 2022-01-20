import sys
import discord
from discord.ext import commands


TOKEN = ''
f = open("TOKEN", "r")
TOKEN = f.read()


if TOKEN == '' :
    sys.exit("Token non défini")

client = discord.Client()

@client.event
async def on_ready():
    print("Your Bot is Ready !") 

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'bonjour':
        await message.channel.send(f' Salut, {message.author.display_name} Je ne veux pas parler à Jason !')
        return

# client = commands.Bot(command_prefix = "!", description = "Bot de Clement")

# @client.command()
# async def dire(ctx, *message):
#     await ctx.send(" ".join(message))

# @client.command()
# async def traduire_chinese(ctx, *text):
#  Caractere_chinois = "????????????????Q????V??Y?"
#  Texte_chinois = []
#  for word in text:
#         for char in word:
#              if char.isalpha():
#                     index = ord(char) - ord("a")
#                     transformed = Caractere_chinois[index]
#                     Texte_chinois.append(transformed)
#              else:
#                     Texte_chinois.append(char)
#                     Texte_chinois.append(" ")
#                     await ctx.send("".join(Texte_chinois)) 

client.run(TOKEN)