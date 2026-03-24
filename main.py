import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.slash_command(name="hello", description="Hello World!")
async def hello(ctx):
    await ctx.respond(f"hello {ctx.author.name}!")

def main():
    token = os.getenv("DISCORD_TOKEN")
    bot.run()

if __name__ == "__main__":
    main()
