import asyncio
import discord
from discord.ext import commands,tasks

from __main__ import Consts,Trad

import time
import random
from random import randint
from discord_data_saver import DiscordDataSaver
from gif_giffy import gifsearch

class Commanding(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def options(self,ctx,option,True_or_False):
		await self.bot.verifie_loaded_data()
		lang_tests_results = await self.bot.what_language(ctx)
		if not option in Consts.options:
			await ctx.send(Trad.options[lang_tests_results[1]][0])
			return False
		if ctx.guild == None:
			await ctx.send(Trad.options[lang_tests_results[1]][2])
			return False
		if True_or_False.upper() == 'TRUE':
			value = True
		elif True_or_False.upper() == 'FALSE':
			value = False
		new_data = {'options':{ctx.guild.id:{option:value}}}

		channel = self.bot.get_channel(Consts.saves_location)
		saver = DiscordDataSaver(self.bot,channel)
		await saver.save(new_data)
		await ctx.send(Trad.options[lang_tests_results[1]][1])
		return True

	@commands.command()
	async def language(self,ctx,arg,me_or_server):
		if me_or_server == 'me':
			me_or_server = 0
		elif me_or_server == 'server' or me_or_server == 'guild':
			me_or_server = 1

		channel = self.bot.get_channel(Consts.saves_location)
		
		await self.bot.verifie_loaded_data()

		self.data = {}
		if 'lang' in self.bot.loaded_data:
			self.lang = self.bot.loaded_data['lang']
		else:
			self.lang = {}

		local_lang = 0#0 en 1 fr

		for x in range(len(Consts.language)):
			if arg in Consts.language[x]:
				local_lang = x
		
		author_or_guild = '' #for confirmation message
		if type(ctx.channel) == discord.DMChannel:
			if me_or_server == 0:
				self.lang[ctx.author.id] = local_lang
				author_or_guild = Trad.language[local_lang][0][0]
			elif me_or_server == 1:
				await ctx.send(Trad.language[local_lang][3])
				return False
		elif type(ctx.channel) == discord.TextChannel:
			if me_or_server == 0:
				self.lang[ctx.author.id] = local_lang
				author_or_guild = Trad.language[local_lang][0][0]
			elif me_or_server == 1:
				author_permissions = ctx.author.guild_permissions
				#await ctx.send(str(author_permissions)+str(author_permissions.manage_guild))
				if author_permissions.manage_guild:
					self.lang[ctx.guild.id] = local_lang
					author_or_guild = Trad.language[local_lang][0][1]
				else:
					await ctx.send(content=Trad.language[local_lang][1])
					return False

		self.data['lang'] = self.lang
		
		await self.bot.Saver.save(self.data)
		
		if local_lang == 0:
			await ctx.send(content=Trad.language[local_lang][2].format(author_or_guild))		
		elif local_lang == 1:
			await ctx.send(content=Trad.language[local_lang][2].format(author_or_guild))

		return True

	@commands.command()
	async def ping(self,ctx):
		ping_time = time.monotonic()
		pinger = await ctx.send(":ping_pong: **Pong !**",delete_after=10)
		ping = "%.2f"%(1000* (time.monotonic() - ping_time))
		await pinger.edit(content=":ping_pong: **Pong !**\n `Ping:" + ping + "`")

	@commands.command()
	async def say(self,ctx,*,args):
		new_string = args
		if '\\n' in args:
			new_string = ''''''
			for x in args.split('\\n'):
				new_string = new_string + x + '\n'
		
		args = new_string
		author = ctx.author
		channel = ctx.channel
		say_message = ''
		if type(channel) != discord.DMChannel:
			Member_perms = ctx.author.guild_permissions
			if not author.id in Consts.admins and \
				Member_perms.administrator == False and \
				Member_perms.manage_messages == False and \
				Member_perms.manage_channels == False: 
				say_message = say_message + '<@{}>'.format(author.id) + '\n'
		say_message = say_message + args
		await ctx.message.delete()
		await ctx.send(content=say_message)

	@commands.command(name='8ball')
	async def ball(self,ctx,*,args):
		async with ctx.channel.typing():
			lang_tests_results = await self.bot.what_language(ctx)

			message = random.choice(Trad.ball_aswer[lang_tests_results[1]])

			await asyncio.sleep(len(message)/10)
			await ctx.send(content=message)
	
	@commands.command()
	async def test(self,ctx):
		if ctx.author.id in Consts.admins:
			async for x in ctx.channel.history():
				if x.author == self.bot.user:
					await x.delete()
	
	
	
	
	#@commands.command()
	#async def calc(self,ctx):
	#	lang_tests_results = await self.bot.what_language(ctx)
    	#	mess = Trad.calc[lang_tests_results[1]]
	#	cal = await ctx.send("Calcul en cours . . .",delete_after=10)
	#	ctx.channel.typing():
	#	time.sleep(5)
	#	await cal.edit(content=mess)
	
	
	
	
	@commands.command()
	async def contact(self,ctx,request,*,message):
		lang_tests_results = await self.bot.what_language(ctx)

		ticket = discord.Embed(color=0x7a2581)
		ticket.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
		ticket.add_field(name="Utilisateur :", value=ctx.author, inline=False)
		if ctx.guild != None:
			ticket.add_field(name="Via :", value=ctx.guild,inline=False)
		ticket.add_field(name='Objet :', value=request,inline=False)
		ticket.add_field(name="Tiket :", value=message, inline=False)
		ticket.set_footer(text="ID de l'utilisateur : " + str(ctx.author.id) + ' langue id : ' + str(lang_tests_results[0]))
		ticket_channel = self.bot.get_channel(Consts.ticket_location)
		await ticket_channel.send(embed=ticket)

		if lang_tests_results[0] == -1:
			language = 0
		await ctx.channel.send(Trad.contact[lang_tests_results[1]])

	@commands.command()
	async def answer_ticket(self,ctx,user_id : int,*,message):
		if ctx.author.id in Consts.admins or ctx.author.id == Consts.tester:
			user = self.bot.get_user(user_id)
			if user.dm_channel == None:
				await user.create_dm()
			user_s_dm_channel = user.dm_channel
			if not ctx.author.id == Consts.tester:
				await user_s_dm_channel.send(message)
			else:
				await user_s_dm_channel.send(message,delete_after=2.5)
			await ctx.send('Your message has been sent successfully.',delete_after=5)

	@commands.command()
	async def gif_giffy(self,ctx):
		'''à tester '''
		await gifsearch(ctx.channel)

	async def report(self,user_mention,ctx,message,server_name=None):
		await ctx.author.create_dm()
		author_dm = ctx.author.dm_channel
		
		lang_tests_results = await self.bot.what_language(ctx)
		
		if type(ctx.channel) == discord.DMChannel and server_name == None:
			await author_dm.send(Trad.report_msgs[lang_tests_results[1]][1][4])
		
		if type(ctx.channel) != discord.DMChannel:
			await ctx.message.delete()
		
		if server_name != None:
			server = discord.utils.find(lambda x : x.name == server_name,self.bot.guilds)
			if server == None:
				await author_dm.send(Trad.report_msgs[lang_tests_results[1]][1][0])
				return False
			report_channel = discord.utils.find(lambda x : x.name == 'report',server.channels)
		else:
			server = ctx.guild
			report_channel = discord.utils.find(lambda x : x.name == 'report',server.channels)
		
		if '<' in user_mention and '>' in user_mention and '@' in user_mention:
			user_id = int(user_mention[2:-1])
			user = self.bot.get_user(user_id)
		else:
			user = discord.utils.find(lambda x: x.name == user_mention[1:-5] and x.discriminator == user_mention[-4:], server.members)

		title_name = [title_name for title_name in list(Trad.report_msgs[lang_tests_results[1]][0].keys())]
		embed = discord.Embed(color=0x700127)
		embed.set_author(name=Consts.bot_name, icon_url=Consts.Juicy_author_as_embed[Consts.bot_name])
			
		embed.add_field(name=title_name[0],value=user,inline=False)
		embed.add_field(name=title_name[1],value=ctx.author,inline=False)
		embed.add_field(name=title_name[2],value="```Markdown\n {}```".format(message),inline=False)
		try:
			if report_channel == None:
				await author_dm.send(Trad.report_msgs[lang_tests_results[1]][1][1])
				return False
			elif report_channel != None:
					await report_channel.send(embed=embed)
					await author_dm.send(Trad.report_msgs[lang_tests_results[1]][1][2])
					return True
		except discord.errors.Forbidden:
			pass
	@commands.command(name='report')
	async def report_normal(self,ctx,user_mention,*,message):
		await self.report(user_mention,ctx,message)

	@commands.command()
	async def safe_report(self,ctx,user_mention,server_name,*,message):
		await self.report(user_mention,ctx,message,server_name=server_name)
		#await ctx.send('```{us} {message}```'.format(us=user_id,message=message))
	
	@commands.command()
	async def reacts(self,ctx,message_id,channel_id,*,emojis=None):
		lang_tests_results = await self.bot.what_language(ctx)
		def RepresentsInt(s):
			try: 
				int(s)
				return True
			except ValueError:
				return False

		emojis_list = []

		if RepresentsInt(channel_id):
			channel = self.bot.get_channel(int(channel_id))
		else:
			emojis_list = [channel_id]
			channel = ctx.channel

		if RepresentsInt(message_id):
			message = await channel.history().get(id=int(message_id))
			if emojis != None:
				emojis_list = emojis_list + emojis.split()
			else:
				pass
			if message == None:
				test = self.bot.get_channel(int(message_id))
				if test != None:
					await ctx.send(Trad.reacts[lang_tests_results[1]][3])
					return False
		else:
			if emojis != None:
				emojis_list = [message_id] + emojis.split()
			else:
				emojis_list = [message_id]
			message = ctx.message
	
		if message == None:
			await ctx.send(Trad.reacts[lang_tests_results[1]][1])
			return False

		for emoji in emojis_list:
			already = discord.utils.find(lambda x: x.emoji == emoji, message.reactions)
			try:
				if already != None:
					await message.remove_reaction(emoji,ctx.guild.get_member(self.bot.user.id))
				else:
					await message.add_reaction(emoji)
			except discord.errors.HTTPException:
				await ctx.send(Trad.reacts[lang_tests_results[1]][0].format(emoji))
				return False
			
		await ctx.send(Trad.reacts[lang_tests_results[1]][2])
		return True
	
	@commands.command()
	async def gif(self,ctx):
		choice = random.choice(Consts.gifs)
		if choice in Consts.offensive_one:
			choice = "|| {} ||".format(choice)
		await ctx.send(choice)
