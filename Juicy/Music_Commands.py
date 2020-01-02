import discord
from discord.ext import commands,tasks

from __main__ import Consts,Trad#old lines

from opts import opt
from ext import opt_trad

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
			if x.endswith('.mp3') or x.endswith('.webm'):
				os.remove(Consts.music_location+x)
		print("Music reseted succesfully !")

	@tasks.loop(seconds=1)
	async def auto_leave(self):
		for voice in self.bot.voice_clients:
			if self.bot.auto_leave_for_guild[voice.guild.id]:
				await voice.disconnect()

	@commands.command()
	async def pause(self,ctx):
		print("Paused")
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
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		voice.stop()
		self.music_info_per_guild[ctx.guild.id]['stoped'] = True

	@commands.command(name='stop')
	async def stop_command(self,ctx):
		await self.stop(ctx)
	
	async def join(self,ctx):
		try:
			lang_test_results = await self.bot.what_language(ctx)
			if ctx.author.voice != None:
				print("join way 1")
				voice_channel = ctx.author.voice.channel
				voice_client = await voice_channel.connect(timeout=5)
				print("return")
				return voice_client
			else:
				print("join way 2")
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
		print(await self.leave(ctx))

	@commands.command()
	async def play(self,ctx,*,url):
		print("Play rec")
		await self.join(ctx)
		print("Play command received !")
		#self.bot.auto_leave_for_guild[ctx.guild.id] = False

		#removing old files
		try:
			for x in os.listdir(Consts.music_location):
				if x.startswith(str(ctx.guild.id)):
					os.remove(Consts.music_location+x)
		except PermissionError:
			#print("Trying to delete song file, but it's being played")
			await ctx.send('[Music] '+"ERROR: Music playing")
			return False

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
		async def download(self,url,optns):
			if not self.music_info_per_guild[ctx.guild.id]['is_playlist']:
				with youtube_dl.YoutubeDL(optns) as ydl:
						info = ydl.extract_info(url)
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

		task_download = asyncio.create_task(download(self,url,ytdl_optns))
		task_play = asyncio.create_task(playing(self,ctx,url))
		task_message = asyncio.create_task(messaging(self,ctx))
		print("lets play some music")
		await asyncio.gather(task_play,task_download,task_message)
