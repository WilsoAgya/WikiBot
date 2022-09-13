import nextcord
import os
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.command(name="Hi")
async def SendMessage(ctx):
    await ctx.send("HELLO")

@bot.event
async def on_ready():
   print(f"Logged in as:{bot.user.name}")

for filename in os.listdir('./cogs'): #Every file in the cogs folder.
    if filename.endswith('.py'): #Checks if the file is a python file.
        bot.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':     
  bot.run(os.environ['BOTTOKEN'])