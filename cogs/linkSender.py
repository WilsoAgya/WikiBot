from nextcord.ext import commands
from .linkGetter import wikiFile

class wikiLink(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    print("Test file loaded!")

  @commands.command()
  async def wiki(self, ctx):
    link = await wikiFile.wikiLinkFunction(self, ctx)
    await ctx.send(f"You have recieved a link {link}")
  
def setup(bot):
  bot.add_cog(wikiLink(bot))