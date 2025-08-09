import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté comme {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTQwMTAxOTY0NDc5MzMyNzY3OA.GsQY83.up-DWlA787FUtPkXzSpCJN18J8rXTCK3ErSRB0")
