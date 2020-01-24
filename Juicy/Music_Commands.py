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
from ext import music_trad, music_tags

import os,youtube_dl
import concurrent,asyncio,time



class Music_Commands_Class(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.music_info_per_guild = {}
		self.tasks = {}

	@commands.Cog.listener()
	async def on_disconnect(self):
		for voice in self.bot.voice_clients:
				await voice.disconnect()

	@commands.Cog.listener()
	async def on_ready(self):
		self.auto_leave.start()
		try:
			files = os.listdir('./Tracks/')
		except FileNotFoundError:
			os.makedirs('./Tracks/')
			files = os.listdir('./Tracks/')
		for x in files:
			if x.endswith('.mp3') or x.endswith('.webm') or x.endswith("m4a"):
				os.remove(Consts.music_location+x)
		print("Music reseted succesfully !")
		for voice in self.bot.voice_clients:
			print("Auto leaving ...")
			await voice.disconnect()

	@tasks.loop(seconds=1)
	async def auto_leave(self):
		for voice in self.bot.voice_clients:
			if self.bot.auto_leave_for_guild[voice.guild.id] and (self.music_info_per_guild[voice.guild.id]['has_finished_playing'] or self.music_info_per_guild[voice.guild.id]['stoped']):
				print("Auto leaving ...")
				await voice.disconnect()
	@commands.command()
	async def auto_lv_test(self,ctx):
		for voice in self.bot.voice_clients:
			print(voice)
			if self.bot.auto_leave_for_guild[voice.guild.id] and (self.music_info_per_guild[voice.guild.id]['has_finished_playing'] or self.music_info_per_guild[voice.guild.id]['stoped']):
				print("Auto leaving ...")
				await voice.disconnect()

	@commands.command()
	async def pause(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		langue = self.bot.which_language(ctx)
		if voice.is_connected():
			voice.pause()
			await ctx.send(music_trad[langue]["pause"]["successfully"])
		else:
			await ctx.send(music_trad[langue]["global_error"]["not_connected"])
	
	@commands.command()
	async def resume(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		langue = self.bot.which_language(ctx)
		if voice.is_connected():
			voice.resume()
			await ctx.send(music_trad[langue]["resume"]["successfully"])
		else:
			await ctx.send(music_trad[langue]["global_error"]["not_connected"])

	@commands.command()
	async def skip(self,ctx):
		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		if not self.music_info_per_guild[ctx.guild.id]['is_playlist']:
			await self.stop(ctx)
		voice.stop()

	async def stop(self,ctx):
		def removing_old_files(x):
			try:
				if self.music_info_per_guild[ctx.guild.id]['stoped']:
					for file in os.listdir("./Tracks"):
						if str(ctx.guild.id) in file:
							os.remove("./Tracks/"+file)
			except:
				removing_old_files(x-1)

		voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
		try:
			self.music_info_per_guild[ctx.guild.id]['stoped'] = True
			self.bot.has_downloaded_the_first_track[ctx.guild.id] = True
		except:
			pass

		voice.stop()
		#avoiding errors caused by too many conurrent tasks(bad optimisation)
		for task in self.tasks[ctx.guild.id].values():
			task.cancel()

		removing_old_files(10)

	@commands.command(name='stop')
	async def stop_command(self,ctx):
		await self.stop(ctx)
	
	async def join(self,ctx,cmd=True):#cmd = if the bot call it
		lang_test_results = await self.bot.what_language(ctx)
		langue = self.bot.which_language(ctx)

		if discord.utils.get(self.bot.voice_clients, guild=ctx.guild) == None and cmd:
			voice = ctx.author.voice.channel
			await voice.connect(timeout=5)
		
		elif discord.utils.get(self.bot.voice_clients, guild=ctx.guild) != None and cmd:
			voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
			await voice.move_to(ctx.author.voice.channel)
		
		elif ctx.author.voice != None and cmd:
			voice_channel = ctx.author.voice.channel
			voice_client = await voice_channel.connect(timeout=5)

		elif ctx.author.voice in self.bot.voice_clients:
			await ctx.send(music_trad[langue]["global_error"]["already_connected"])
		
		elif discord.utils.get(self.bot.voice_clients, guild=ctx.guild) != None:
			voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
			await voice.move_to(ctx.author.voice.channel)
			await ctx.send(music_trad[langue]["join"]["movement"])
			return True
		
		elif ctx.author.voice != None:
			voice_channel = ctx.author.voice.channel
			voice_client = await voice_channel.connect(timeout=5)
			await ctx.send(music_trad[langue]["join"]["successfully"])
			return True
		
		else:
			await ctx.send(music_trad[langue]["join"]["failed"])
			await ctx.send('[Music] '+Trad.join[lang_test_results[1]][0],delete_after=5)
			return False

	@commands.command(name='join')
	async def join_command(self,ctx):
		await self.join(ctx,False)
	
	async def leave(self,ctx):
		lang_test_results = await self.bot.what_language(ctx)
		voice_clients = self.bot.voice_clients

		voice = discord.utils.get(voice_clients, guild=ctx.guild)

		if voice != None and not voice.is_playing():
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
			else:
				return False

	@commands.command(name='leave')
	async def leave_command(self,ctx):
		await self.leave(ctx)

	@commands.command()
	async def var_state(self,ctx):
		msg = str(self.music_info_per_guild),str(self.bot.auto_leave_for_guild),str(self.bot.has_downloaded_the_first_track)
		await ctx.send((self.bot.auto_leave_for_guild[ctx.guild.id],self.music_info_per_guild[ctx.guild.id]['has_finished_playing'],self.music_info_per_guild[ctx.guild.id]['stoped']))
	
	@commands.command()
	async def get_dict(self,ctx,*,arg:str):
		'''
		if arg in self.bot.get_vars.keys():
			await ctx.send(self.bot.get_vars[arg])
		else:
			await ctx.send("key does not exist")
		'''
		await ctx.send(self.music_info_per_guild[ctx.guild.id]["index_currently_played"])
		print(str(self.music_info_per_guild[ctx.guild.id])+"\n\n\t")
		print(str(self.music_info_per_guild[ctx.guild.id]["extracted_info"])+"\n\n\t")
		print(str(self.music_info_per_guild[ctx.guild.id]["index_currently_played"])+"\n\n\t")
		await ctx.send(self.music_info_per_guild[ctx.guild.id]["extracted_info"][self.music_info_per_guild[ctx.guild.id]["index_currently_played"]])


	@commands.command(name="play")
	async def play_cmd(self,ctx,*,url):
		await self.play(ctx,url)

	async def play(self,ctx,url):
		if not ctx.guild.id in self.bot.auto_leave_for_guild.keys():
			self.bot.auto_leave_for_guild[ctx.guild.id] = True
		
		langue = self.bot.which_language(ctx)

		#removing old files
		async def music_played():
			#print("Trying to delete song file, but it's being played")
			await ctx.send(music_trad[langue]["global_failed"]["already_playing"])
			msg = await ctx.send(music_trad[langue]["play"]["switching_track"].format(url))
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
					await ctx.send(music_trad[langue]["play"]["not_switching"])
				else:
					await ctx.send(music_trad[langue]["play"]["switching"])
					await self.stop(ctx)
					await asyncio.sleep(1)
					await self.play(ctx,url)

		try:
			for x in os.listdir(Consts.music_location):
				if x.startswith(str(ctx.guild.id)):
					os.remove(Consts.music_location+x)
		except PermissionError:
			await music_played()
		
		if ctx.guild.id in self.bot.has_downloaded_the_first_track.keys():
			if not self.bot.has_downloaded_the_first_track[ctx.guild.id]:
				await music_played()

		self.bot.has_downloaded_the_first_track[ctx.guild.id] = False

		if "youtube" in url or "http" in url or ".com" in url:
			await ctx.send(music_trad[langue]["play"]["receiving_data"].format(url))
		else:
			await ctx.send(music_trad[langue]["play"]["searching"].format(url))

		await self.join(ctx)

		#setting ytdl_optns
		ytdl_optns = Consts.ytdl_options

		ytdl_optns['outtmpl'] = Consts.outtmpl.format(ctx.guild.id,1)

		#setting music info
		self.music_info_per_guild[ctx.guild.id] = {'is_playlist':False,
			'stoped':False,
			'ended':False,
			'download_state':[1,[]],#to download , if download
			'next_message':'',
			'next_embed':None,
			'extracted_info':[],
			'index_currently_played':0,
			'download_complete':(False,0),#if raide index error donwload completed (playlist only), playlist index to play
			'has_played_the_first_track':False,
			'has_finished_playing':False,
			'playlist':[]
			}

		if 'list' in url and ' ' in url:
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
					keyword = info["entries"][0]

					self.music_info_per_guild[ctx.guild.id]["extracted_info"].append(keyword)
					self.bot.get_vars = keyword
					self.bot.has_downloaded_the_first_track[guild_id] = True
				removing_old_files()
			else:
				while not self.music_info_per_guild[ctx.guild.id]['stoped']:
					index = self.music_info_per_guild[ctx.guild.id]['download_state'][0]
					try:
						for x in range(index,index+2):
							if not x in self.music_info_per_guild[ctx.guild.id]['download_state'][1]:
								optns['playlist_items'] = str(x)
								optns['outtmpl'] = Consts.outtmpl.format(ctx.guild.id,x)
								if not self.music_info_per_guild[ctx.guild.id]['stoped']:
									with youtube_dl.YoutubeDL(optns) as ydl:
										info = ydl.extract_info(url)
										keyword = info["entries"][0]

										self.music_info_per_guild[ctx.guild.id]["extracted_info"].append(keyword)
										self.bot.get_vars = keyword
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
					except IndexError:
						self.music_info_per_guild[ctx.guild.id]['download_complete'] = (True,self.music_info_per_guild[ctx.guild.id]["extracted_info"][-1]["playlist_index"])
						return True
		
		#player
		async def messaging(self,ctx):
			while not self.music_info_per_guild[ctx.guild.id]['stoped']:
				message = self.music_info_per_guild[ctx.guild.id]['next_message']
				embed = self.music_info_per_guild[ctx.guild.id]['next_embed']
				if embed != None:
					await ctx.send(embed=embed)
					self.music_info_per_guild[ctx.guild.id]['next_embed'] = None
				elif message != '':
					await ctx.send(message)
					self.music_info_per_guild[ctx.guild.id]['next_message'] = ''
				await asyncio.sleep(0.10)
			print('has been stoped')
		#play function
		async def playing(self,ctx,url):
			def next_embed():
				#embed
				keyword = self.music_info_per_guild[ctx.guild.id]["extracted_info"][self.music_info_per_guild[ctx.guild.id]["index_currently_played"]]
				if keyword["uploader"] in keyword["title"]:
					pos_uploader_name = keyword["title"].index(keyword["uploader"])
					title = keyword["title"][:pos_uploader_name] + keyword["title"][len(keyword["uploader"]):]
				else:
					title = keyword["title"]
				
				upload_year = keyword["upload_date"][0:4]
				upload_month = keyword["upload_date"][4:6]
				upload_day = keyword["upload_date"][6:8]

				duration_secondes = keyword["duration"]%60
				duration_minutes = int((keyword["duration"]-duration_secondes)/60)
				duration_hour = 0
				while duration_minutes >= 60:
					duration_hour = duration_minutes+1
					duration_minutes -= 60

				embed=discord.Embed(title=title, url=keyword["webpage_url"])#, description=keyword["description"])
				embed.set_author(name=keyword["uploader"], url=keyword["uploader_url"])
				embed.set_thumbnail(url=keyword["thumbnail"])
				embed.add_field(name="Time information", value=f"Upload date : {upload_day}/{upload_month}/{upload_year} \n Duration: {duration_hour} h {duration_minutes} min {duration_secondes} sec", inline=True)
				embed.set_footer(text="Music currently played, if you dont wan't so many information try the simple music notification @juicybox")
				
				self.music_info_per_guild[ctx.guild.id]["next_embed"] = embed
				if self.music_info_per_guild[ctx.guild.id]["is_playlist"]:
					self.music_info_per_guild[ctx.guild.id]["index_currently_played"] += 1


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
				index = self.music_info_per_guild[ctx.guild.id]['download_state'][0]
				
				if self.music_info_per_guild[ctx.guild.id]['download_complete'][0] and self.music_info_per_guild[ctx.guild.id]['download_complete'][0]<index:
					self.music_info_per_guild[ctx.guild.id]['has_finished_playing'] = True
				
				elif self.music_info_per_guild[ctx.guild.id]['is_playlist'] and not self.music_info_per_guild[ctx.guild.id]['stoped']:				
					#waiting for file
					file_not_find = True
					
					while file_not_find:
						for x in os.listdir(Consts.music_location):
							if x.startswith(str(ctx.guild.id)+'[{}]'.format(index)):
								file = x
								file_not_find = False
								break
						time.sleep(1)
					
					title = ''.join(str(x) for x in file.split('-')[1:])
					title = ''.join(str(x) for x in title.split('.')[:-1])
					next_embed()

					if self.music_info_per_guild[ctx.guild.id]['next_embed'] != None:
						pass
					else:
						self.music_info_per_guild[ctx.guild.id]['next_message'] = '[Music] '+f'Playing: `{title}` :notes:'

					voice.play(discord.FFmpegPCMAudio(Consts.music_location+file), after=lambda e:next_track(self))
					voice.source = discord.PCMVolumeTransformer(voice.source)
					voice.source.volume = Consts.volume
					
					if not self.music_info_per_guild[ctx.guild.id]['stoped']:
						self.music_info_per_guild[ctx.guild.id]['download_state'][0] += 1
				
				else:
					self.bot.auto_leave_for_guild[ctx.guild.id] = True
					return True

			voice.play(discord.FFmpegPCMAudio(Consts.music_location+file), after=lambda e:next_track(self))

			voice.source = discord.PCMVolumeTransformer(voice.source)
			voice.source.volume = Consts.volume

			title = ''.join(str(x) for x in file.split('-')[1:])
			title = ''.join(str(x) for x in title.split('.')[:-1])
			next_embed()
			if self.music_info_per_guild[ctx.guild.id]['next_embed'] != None:
				pass
			else:
				await ctx.send('[Music] '+f'Playing: `{title}` :notes:')#insta format
			
			self.music_info_per_guild[ctx.guild.id]['has_played_the_first_track'] = True
			
			if self.music_info_per_guild[ctx.guild.id]['is_playlist'] and not self.music_info_per_guild[ctx.guild.id]['stoped']:
				self.music_info_per_guild[ctx.guild.id]['download_state'][0] += 1
		
		self.tasks[ctx.guild.id] = {}
		self.tasks[ctx.guild.id]['task_download'] = asyncio.create_task(download(self,url,(ytdl_optns),ctx.guild.id))
		self.tasks[ctx.guild.id]['task_play'] = asyncio.create_task(playing(self,ctx,url))
		self.tasks[ctx.guild.id]['task_message'] = asyncio.create_task(messaging(self,ctx))
		print("lets play some music\n")
		await asyncio.gather(self.tasks[ctx.guild.id]['task_download'],self.tasks[ctx.guild.id]['task_play'],self.tasks[ctx.guild.id]['task_message'])
