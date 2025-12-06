TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1396155255833497660   # your channel ID

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"🎉 Welcome {member.mention} to {member.guild.name}!")
    else:
        print("⚠ Welcome channel not found!")

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
import time

while True:
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        print("🔁 Restarting in 5 seconds...")
        time.sleep(5)
