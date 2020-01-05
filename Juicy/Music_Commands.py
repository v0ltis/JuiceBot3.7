import discord
from discord.ext import commands,tasks

import sys,os

try:
	sys.path.append('./data/')#These lines are temporary while i fully upgrade Juicy (old version)
	import Trad#
except:
	sys.path.append('./Juicy/data/')#These lines are temporary while i fully upgrade Juicy (old version)
	import Trad#

from opts import opt
from ext import data as Consts
from ext import music_trad

import os,youtube_dl
import concurrent,asyncio,time



class Music_Commands_Class(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.music_info_per_guild = {}

	@commands.Cog.listener()
	async def on_ready(self):
		#self.auto_leave.start()
		try:
			files = os.listdir('./Tracks/')
		except FileNotFoundError:
			os.makedirs('./Tracks/')
			files = os.listdir('./Tracks/')
		for x in files:
			if x.endswith('.mp3') or x.endswith('.webm') or x.endswith("m4a"):
				os.remove(Consts.music_location+x)
		#print("Music reseted succesfully !")

	@tasks.loop(seconds=1)
	async def auto_leave(self):
		for voice in self.bot.voice_clients:
			if self.bot.auto_leave_for_guild[voice.guild.id] and self.bot.has_downloaded_the_first_track[voice.guild.id]:
				await voice.disconnect()

	@commands.command()
	async def pause(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.pause()
		opt(ctx.guild,str(ctx.guild.owner.id))
		langue = opt.langue
		await ctx.send(opt_trad.music[langue]["pause"]["successfully"])
	
	@commands.command()
	async def resume(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.resume()
		opt(ctx.guild,str(ctx.guild.owner.id))
		langue = opt.langue
		await ctx.send(opt_trad.music[langue]["resume"]["successfully"])

	@commands.command()
	async def skip(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.stop()

	async def stop(self,ctx):
		def removing_old_files():
			try:
				if self.music_info_per_guild[ctx.guild.id]['stoped']:
					for file in os.listdir("./Tracks"):
						if str(ctx.guild.id) in file:
							os.remove("./Tracks/"+file)
			except:
				removing_old_files()

		print("Stoping")
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.stop()
		self.music_info_per_guild[ctx.guild.id]['stoped'] = True
		self.bot.has_downloaded_the_first_track[ctx.guild.id] = True
		removing_old_files()

	@commands.command(name='stop')
	async def stop_command(self,ctx):
		await self.stop(ctx)
	
	async def join(self,ctx):
		try:
			lang_test_results = await self.bot.what_language(ctx)
			if ctx.author.voice != None:
				voice_channel = ctx.author.voice.channel
				voice_client = await voice_channel.connect(timeout=5)
				return voice_client
			else:
				await ctx.send('[Music] '+Trad.join[lang_test_results[1]][0],delete_after=5)
				return False
		except discord.errors.ClientException:
			pass

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
					#join is needed only for debuging else it is useless
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
	async def var_state(self,ctx):
		msg = str(self.music_info_per_guild),str(self.bot.auto_leave_for_guild),str(self.bot.has_downloaded_the_first_track)
		await ctx.send(msg)

	@commands.command(name="play")
	async def play_cmd(self,ctx,*,url):
		await self.play(ctx,url)

	async def play(self,ctx,url):
		if not ctx.guild.id in self.bot.auto_leave_for_guild.keys():
			self.bot.auto_leave_for_guild[ctx.guild.id] = True
			
		await self.join(ctx)
		#self.bot.auto_leave_for_guild[ctx.guild.id] = False

		#removing old files
		async def music_played():
			#print("Trying to delete song file, but it's being played")
			await ctx.send('[Music] '+"ERROR: Music playing")
			msg = await ctx.send('[Music] '+"Do you want to switch to this track ?")
			await msg.add_reaction("✅")
			await msg.add_reaction("❌")

			def check(reaction, user):
				return str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌' and reaction.message.id == ctx.message.id
			try:
				reaction,user = await self.bot.wait_for("reaction_add", timeout=60.0,check=check)
			except asyncio.TimeoutError:
				return False
			else:
				if str(reaction.emoji) == '❌':
					await ctx.send("[Music] All rights, i won't change the current track.")
				else:
					await ctx.send("[Music] All rights, changing song ...")
					await self.stop(ctx)
					await self.play(ctx,url)

		try:
			for x in os.listdir(Consts.music_location):
				if x.startswith(str(ctx.guild.id)):
					os.remove(Consts.music_location+x)
		except PermissionError:
			print("Error way 1")
			await music_played()
		
		if ctx.guild.id in self.bot.has_downloaded_the_first_track.keys():
			if not self.bot.has_downloaded_the_first_track[ctx.guild.id]:
				print("Error way 2")
				await music_played()

		self.bot.has_downloaded_the_first_track[ctx.guild.id] = False
		await ctx.send('[Music] '+"Getting everything ready now")

		await self.join(ctx)

		#setting ytdl_optns
		ytdl_optns = Consts.ytdl_options
		ytdl_optns['outtmpl'] = Consts.outtmpl.format(ctx.guild.id,1)
		#print(Consts.outtmpl.format(ctx.guild.id,1))
		#setting music info
		self.music_info_per_guild[ctx.guild.id] = {'is_playlist':False,
			'stoped':False,
			'ended':False,
			'download_state':[1,[]],#to download , if download
			'next_message':''
			}

		if 'list' in url:
			self.music_info_per_guild[ctx.guild.id]['is_playlist'] = True
			ytdl_optns['playlist_items'] = str(self.music_info_per_guild[ctx.guild.id]['download_state'][0])

		#audio downloader
		async def download(self,url,optns,guild_id):
			def removing_old_files():
				if self.music_info_per_guild[ctx.guild.id]['stoped']:
					for file in os.listdir("./Tracks"):
						if str(guild_id) in file:
							os.remove("./Tracks/"+file)
			if self.music_info_per_guild[ctx.guild.id]['stoped']:
				removing_old_files()
			if not self.music_info_per_guild[ctx.guild.id]['is_playlist']:
				with youtube_dl.YoutubeDL(optns) as ydl:
					info = ydl.extract_info(url)
				removing_old_files()
			else:
				while not self.music_info_per_guild[ctx.guild.id]['stoped']:
					index = self.music_info_per_guild[ctx.guild.id]['download_state'][0]
					for x in range(index,index+2):
						if not x in self.music_info_per_guild[ctx.guild.id]['download_state'][1]:
							optns['playlist_items'] = str(x)
							optns['outtmpl'] = Consts.outtmpl.format(ctx.guild.id,x)
							#print(optns['outtmpl'])
							if not self.music_info_per_guild[ctx.guild.id]['stoped']:
								with youtube_dl.YoutubeDL(optns) as ydl:
									info = ydl.extract_info(url)
									self.bot.has_downloaded_the_first_track[guild_id] = True
									self.music_info_per_guild[ctx.guild.id]['download_state'][1].append(x)
									if info['entries'] == []:
										self.music_info_per_guild[ctx.guild.id]['stoped'] = True
									else:
										pass
								for y in os.listdir(Consts.music_location):
									if y.startswith(str(ctx.guild.id)+"[{}]".format(x)):
										if '-_' in y:
											youtube_dl_need_up = self.bot.get_channel(606013511629406208)
											await youtube_dl.send('[Music downloader] filename = {}'.format(y))
						await asyncio.sleep(1)
					await asyncio.sleep(1)
				removing_old_files()
		
		#player
		async def messaging(self,ctx):
			while not self.music_info_per_guild[ctx.guild.id]['stoped']:
				message = self.music_info_per_guild[ctx.guild.id]['next_message']
				if message != '':
					await ctx.send('[Music] '+message)
					self.music_info_per_guild[ctx.guild.id]['next_message'] = ''
				await asyncio.sleep(0.5)

		#play function
		async def playing(self,ctx,url):

			#waiting for file
			file_not_find = True
			while file_not_find:
				for x in os.listdir(Consts.music_location):
					if x.startswith(str(ctx.guild.id)):
						file = x
						file_not_find = False
						break
				await asyncio.sleep(1)

			#play
			voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

			self.music_info_per_guild[ctx.guild.id]['stoped'] = False

			#if playlist continue
			def next_track(self):
				if self.music_info_per_guild[ctx.guild.id]['is_playlist'] and not self.music_info_per_guild[ctx.guild.id]['stoped']:				
					#waiting for file
					file_not_find = True
					index = self.music_info_per_guild[ctx.guild.id]['download_state'][0]
					
					while file_not_find:
						for x in os.listdir(Consts.music_location):
							if x.startswith(str(ctx.guild.id)+'[{}]'.format(index)):
								file = x
								file_not_find = False
								break
						time.sleep(1)
					
					title = ''.join(str(x) for x in file.split('-')[1:])
					title = ''.join(str(x) for x in title.split('.')[:-1])
					self.music_info_per_guild[ctx.guild.id]['next_message'] = f'Playing: {title}'

					voice.play(discord.FFmpegPCMAudio(Consts.music_location+file), after=lambda e:next_track(self))
					voice.source = discord.PCMVolumeTransformer(voice.source)
					voice.source.volume = Consts.volume
					
					if not self.music_info_per_guild[ctx.guild.id]['stoped']:
						self.music_info_per_guild[ctx.guild.id]['download_state'][0] += 1
				
				else:
					self.bot.auto_leave_for_guild[ctx.guild.id] = True
					return True
			#print(Consts.music_location+file)
			voice.play(discord.FFmpegPCMAudio(Consts.music_location+file), after=lambda e:next_track(self))

			voice.source = discord.PCMVolumeTransformer(voice.source)
			voice.source.volume = Consts.volume

			#print(file)
			title = ''.join(str(x) for x in file.split('-')[1:])
			#print(title)
			title = ''.join(str(x) for x in title.split('.')[:-1])
			print(title)
			await ctx.send('[Music] '+f'Playing: {title}')

			if self.music_info_per_guild[ctx.guild.id]['is_playlist'] and not self.music_info_per_guild[ctx.guild.id]['stoped']:
				self.music_info_per_guild[ctx.guild.id]['download_state'][0] += 1

		task_download = asyncio.create_task(download(self,url,ytdl_optns,ctx.guild.id))
		task_play = asyncio.create_task(playing(self,ctx,url))
		task_message = asyncio.create_task(messaging(self,ctx))
		print("lets play some music\n")
		await asyncio.gather(task_play,task_download,task_message)
