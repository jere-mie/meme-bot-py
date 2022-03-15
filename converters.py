from discord.ext.commands import Converter, Context, BadArgument

class MemeTemplateConverter(Converter):

    async def convert(self, ctx: Context, argument: str) -> str:

        for template in ctx.bot.memesList:
            if template.lower() == argument.lower():
                return template
        
        raise BadArgument("That meme template does not exist!")