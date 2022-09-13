from nextcord.ext import commands

class wikiFile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("Bot file loaded!")

    async def wikiLinkFunction(self, ctx):
        wikiFile.wikiLinkVariable = "https://www.google.com"
        return wikiFile.wikiLinkVariable

def setup(bot):
    bot.add_cog(wikiFile(bot))
