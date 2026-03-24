import discord
import os
from mcstatus import JavaServer
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()
server = JavaServer.lookup(os.getenv("SERVER_NAME"))

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.slash_command(name="hello", description="Hello World!")
async def hello(ctx):
    await ctx.respond(f"hello {ctx.author.name}!")

@bot.slash_command(name="check", description="This is to check how many the people are connected to the server")
async def check(ctx):
    try:
        status = server.status()
        players = status.players.online
        await ctx.respond(f"there are {players} people in the server.")
    except:
        print("The server is offline or unreachable.")


def main():
    token = os.getenv("DISCORD_TOKEN")
    bot.run(token)

if __name__ == "__main__":
    main()
