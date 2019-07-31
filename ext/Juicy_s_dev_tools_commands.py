import asyncio
import discord
from discord.ext import commands

from __main__ import Consts

class Dev_Tools_Commands(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def clear(self,ctx,channel_id : int,limit=None):
		await ctx.message.delete()
		if ctx.author.id in Consts.admins:
			await ctx.send(content="You're an admin let's clear this channel !",delete_after=5)
			channel = self.bot.get_channel(channel_id)
			if limit == None:
				async for x in channel.history(oldest_first=False):
					await x.delete()
			else:
				async for x in channel.history(oldest_first=False,limit=int(limit)+1):
					await x.delete()
			await ctx.send(content="Finished",delete_after=5)
		else:
			await ctx.send(content="You're not an admin i won't clear this channel.",delete_after=5)

	@commands.command()
	async def get_str_emoji(self,ctx,*,emoji):
		emoji_found = None
		await ctx.send("```{}```".format(emoji))

	@commands.command()
	async def close(self,ctx):
		if ctx.author.id in Consts.admins:
			await self.bot.change_presence(status=discord.Status.dnd)
			self.bot.clear()
			await self.bot.close()
