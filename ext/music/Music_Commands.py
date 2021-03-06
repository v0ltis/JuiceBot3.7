import discord
from discord.ext import commands

from __main__ import Consts

import os,youtube_dl
import concurrent,asyncio

import new_play_command as play_command

class Music_Commands_Class(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.music_info_per_guild = {}

	@commands.command()
	async def pause(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.pause()
	
	@commands.command()
	async def resume(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.pause()
	
	@commands.command()
	async def pause(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.pause()

	@commands.command()
	async def skip(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.stop()

	async def stop(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.stop()
		self.music_info_per_guild[ctx.guild.id]['stoped'] = True

	@commands.command(name='stop')
	async def stop_command(self,ctx):
		await self.stop(ctx)
	
	async def join(self,ctx):
		lang_test_results = await self.bot.what_language(ctx)
		if ctx.author.voice != None:
			voice_channel = ctx.author.voice.channel
			await voice_channel.connect()
			return voice_channel
		else:
			await ctx.send('[Music] '+Trad.join[lang_test_results[1]][0],delete_after=5)
			return False

	@commands.command(name='join')
	async def join_command(self,ctx):
		await self.join(ctx)
	
	async def leave(self,ctx):
		lang_test_results = await self.bot.what_language(ctx)
		voice_clients = self.bot.voice_clients

		voice = discord.utils.get(voice_clients, guild=ctx.guild)

		if voice != None:
			await voice.disconnect()
		else:
			voices_in_channel = ctx.author.voice
			if voices_in_channel != None:
				voice_channel = voices_in_channel.channel
				if self.bot.user.id in [x.id for x in voice_channel.members]:
					try:
						await self.stop(ctx)
					except:
						pass
					await self.join(ctx)
					await self.leave(ctx)
					for track in os.listdir(Consts.music_location):
						if track.startswith(str(ctx.guild.id)):
							await os.remove(track)
			else:
				return False

	@commands.command(name='leave')
	async def leave_command(self,ctx):
		await self.leave(ctx)

	@commands.command()
	async def play(self,ctx,*,url):
		try:
			await self.join(ctx)
		except:
			pass
		await play_command.play(self,ctx,url)
