from asyncore import read
import sys
import random
import discord
from discord.ext import commands

TOKEN = ''
f = open("TOKEN", "r")
TOKEN = f.read()


if TOKEN == '' :
    sys.exit("Token non défini")


bot = commands.Bot(command_prefix='cmd:')

# Montrer dans les logs que le bot est pret 
# 
# 
@bot.event
async def on_ready():
    print("Your Bot is Ready !") 


# La commande de l'affichage des regles cmd:regles
# 
# 
@bot.command()
async def regles(ctx):  
    # éxécuter la commande
    await ctx.send(f"Salut à toi ! Voici les règles du serveur :\n\n  1. Pas d'insultes\n  2. Pas de double comptes\n  3. Pas de spam ")


# ---------- La commande de bienvenue 'cmd:bienvenue @Mention'
# 
# 
@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    # récupérer le pseudo de l'utilisateur
    pseudo = nouveau_membre.mention
    # éxécuter la commande
    await ctx.send(f"Bienvenue sur le serveur {pseudo}! Je suis Jarvis le bot conçu par Clément BLAIZEL, Non je ne suis pas le Jarvis de Tony Stark XD.\n Plus sérieusement ma fonction premiere est d'améliorer l'expérience des utilisateurs du serveur tu peux m'appeler à tout moment avec le préfixe de commande 'cmd:' suivi du nom de la commande que tu souhaite fait la commande 'cmd:help' pour avoir la liste de toutes les commandes que je peux t'afficher.\n N'oublie pas de faire la commande 'cmd:regles' pour connaitre les regles du serveur.\n\n Bonne journée à toi et à plus !" )


# détection de l'erreur 
# 
@bienvenue.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Tu dois faire 'cmd:bienvenue @MentionDeLaPersonne'")

bot.run(TOKEN)
