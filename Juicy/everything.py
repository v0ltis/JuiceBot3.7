import discord
from discord.ext import commands

from ext import bot_moderator_ids

class everything_in_a_class(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def answer(self,ctx,receiver : int, *, message : str):
		if ctx.author.id in bot_moderator_ids:
			user = self.bot.get_user(receiver)
			if user.dm_channel != None:
				await user.dm_channel.send(message+'\n'+f"<@{ctx.author.id}>")
			else:
				await user.create_dm()
				await user.dm_channel.send(message+'\n'+f"<@{ctx.author.id}>")