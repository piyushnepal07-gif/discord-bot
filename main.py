import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
import time

while True:
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        print("🔁 Restarting in 5 seconds...")
        time.sleep(5)

