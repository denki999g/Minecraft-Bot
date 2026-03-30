import discord
import os
from mcstatus import JavaServer
from dotenv import load_dotenv
import exchange_rate

load_dotenv()
bot = discord.Bot()
server = JavaServer.lookup(os.getenv("SERVER_NAME"))

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.slash_command(name="hello", description="Hello World!")
async def hello(ctx):
    await ctx.respond(f"hello {ctx.author.name}!")

# We need requests library for this one.
@bot.slash_command(name="usd", description="This is to check the exchange rate between USD and KRW (how much 1 USD is worth in Korean won).")
async def usd_to_krw(ctx):
    usd_to_krw_dict = exchange_rate.get_usd_to_krw_dict()
    er_date = usd_to_krw_dict["date"]
    er_value = usd_to_krw_dict["rates"]["KRW"]
    await ctx.respond(
        f"Date: {er_date}\n"
        f"1 USD = {er_value} KRW")

@bot.slash_command(name="check", description="This is to check how many the people are connected to the server")
async def check(ctx):
    try:
        status = server.status()
        playerCount = status.players.online
        players = status.players.sample
        playerNames = [player.name for player in players]

        if playerCount == 0:
            await ctx.respond(f"there is no one in the server.")
        elif playerCount == 1:
            await ctx.respond(
                f"there is one person in the server.\n"
                f"player : {", ".join(playerNames)}")
        else:
            await ctx.respond(
                f"there are {players} people in the server.\n"
                f"players : {", ".join(playerNames)}")
    except:
        await ctx.respond("The server is offline or unreachable.")
        print("The server is offline or unreachable.")

@bot.slash_command(name="version", description="This is to check the java server version and the mod version")
async def version(ctx):
    try:
        status = server.status()
        modName, modVersion = status.raw.get("betterStatus").values()
        serverVersion = status.version.name
        await ctx.respond("" \
            f"Server version : {serverVersion}\n"
            f"Mod name : {modName}\n"
            f"Mod version : {modVersion}\n")
    except:
        await ctx.respond("The server is offline or unreachable.")
        print("The server is offline or unreachable.")

def main():
    token = os.getenv("DISCORD_TOKEN")
    bot.run(token)

if __name__ == "__main__":
    main()
