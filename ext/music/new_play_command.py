import discord,asyncio,os,time,youtube_dl
from __main__ import Consts

async def play(self,ctx,url):
	self.bot.auto_leave_for_guild[ctx.guild.id] = False

	#removing old files
	try:
		for x in os.listdir(Consts.music_location):
			if x.startswith(str(ctx.guild.id)):
				os.remove(Consts.music_location+x)
	except PermissionError:
		print("Trying to delete song file, but it's being played")
		await ctx.send('[Music] '+"ERROR: Music playing")
		return False

	await ctx.send('[Music] '+"Getting everything ready now")


	#setting ytdl_optns
	ytdl_optns = Consts.ytdl_options
	ytdl_optns['outtmpl'] = Consts.outtmpl.format(ctx.guild.id,1)
	print(Consts.outtmpl.format(ctx.guild.id,1))
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
						print(optns['outtmpl'])
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
			await asyncio.sleep(2)

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
			

		#joining
		try:#to do later ne pas laisser cela comme sa le mettre autre par tester les erreurs ==> doc
			await self.join(ctx)
		except:
			pass


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
				title = title.split('.')[:-1]
				self.music_info_per_guild[ctx.guild.id]['next_message'] = f'Playing: {title}'

				voice.play(discord.FFmpegPCMAudio(Consts.music_location+file), after=lambda e:next_track(self))
				voice.source = discord.PCMVolumeTransformer(voice.source)
				voice.source.volume = 0.02
				
				if not self.music_info_per_guild[ctx.guild.id]['stoped']:
					self.music_info_per_guild[ctx.guild.id]['download_state'][0] += 1
			
			else:
				self.bot.auto_leave_for_guild[ctx.guild.id] = True
				return True
		print(Consts.music_location+file)
		voice.play(discord.FFmpegPCMAudio(Consts.music_location+file), after=lambda e:next_track(self))

		voice.source = discord.PCMVolumeTransformer(voice.source)
		voice.source.volume = 0.02

		print(file)
		title = ''.join(str(x) for x in file.split('-')[1:])
		print(title)
		title = title.split('.')[:-1]
		print(title)
		await ctx.send('[Music] '+f'Playing: {title}')

		if self.music_info_per_guild[ctx.guild.id]['is_playlist'] and not self.music_info_per_guild[ctx.guild.id]['stoped']:
			self.music_info_per_guild[ctx.guild.id]['download_state'][0] += 1

	task_download = asyncio.create_task(download(self,url,ytdl_optns))
	task_play = asyncio.create_task(playing(self,ctx,url))
	task_message = asyncio.create_task(messaging(self,ctx))

	await asyncio.gather(task_play,task_download,task_message)

