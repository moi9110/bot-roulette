import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Permet d'accéder au contenu des messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté comme {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Récupère le token depuis la variable d'environnement
token = os.getenv("MTQwMTAxOTY0NDc5MzMyNzY3OA.GI4WpR.2JWRwuRM8m3MrDjZlH1FZfNMzKTUpyLhDyPW3k")

if token is None:
    print("Erreur : Le token Discord n'est pas défini dans la variable d'environnement 'TOKEN'.")
else:
    bot.run(token)
