import discord,asyncio
from discord.ext import commands,tasks

from __main__ import Consts

import os

from Music_Commands import Music_Commands_Class

class Music_Event(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		self.auto_leave.start()
		try:
			files = os.listdir('./Tracks/')
		except FileNotFoundError:
			os.makedirs('./Tracks/')
			files = os.listdir('./Tracks/')
		for x in files:
			if x.endswith('.mp3') or x.endswith('.webm'):
				os.remove(Consts.music_location+x)
		print("Music reseted succesfully !")

	@tasks.loop(seconds=1)
	async def auto_leave(self):
		for voice in self.bot.voice_clients:
			if self.bot.auto_leave_for_guild[voice.guild.id]:
				await voice.disconnect()