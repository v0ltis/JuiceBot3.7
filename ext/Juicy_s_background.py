import discord
from discord.ext import commands, tasks
import asyncio

from itertools import cycle

from __main__ import Consts

class Background_Tasks(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		help_msg = discord.Activity(name='{}help'.format(Consts.commands_prefix),type=discord.ActivityType.watching)
		guild_msg = discord.Activity(name='to {} servers'.format(len(self.bot.guilds)),type=discord.ActivityType.listening)
		site_msg = discord.Activity(name='juicebot.github.io'.format(Consts.commands_prefix),type=discord.ActivityType.watching)
		ver_msg = discord.Activity(name=" in version {}".format(Consts.version),type=discord.ActivityType.playing)
		self.status = cycle([site_msg,help_msg,guild_msg,ver_msg])
		
		self.change_status.start()
	

	@tasks.loop(seconds=5)
	async def change_status(self):
		await self.bot.change_presence(activity=next(self.status))

