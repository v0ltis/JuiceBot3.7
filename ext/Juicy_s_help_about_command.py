import discord
from discord.ext import commands

from __main__ import Trad,Consts

import copy

class Help_Command(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	def make_embed(self,lang_tests_results,Trad_embed,last=None):
		title_name = [title_name for title_name in list(Trad_embed[lang_tests_results[1]].keys())]
		help_embed = discord.Embed(title=title_name[0], description=Trad_embed[lang_tests_results[1]][title_name[0]], colour=0x7a2581)

		for x in title_name[1:last]:
			print(x,Trad_embed[lang_tests_results[1]][x])
			help_embed.add_field(name=x,value=Trad_embed[lang_tests_results[1]][x],inline=False)
		return help_embed

	@commands.command()
	async def help(self,ctx,arg=None):
		lang_tests_results = await self.bot.what_language(ctx)
		
		if arg in Consts.help_args[0]:
			title_name = [title_name for title_name in list(Trad.help_embed[lang_tests_results[1]].keys())]

			help_embed = discord.Embed(title=title_name[0], description=Trad.help_embed[lang_tests_results[1]][title_name[0]], colour=0x7a2581)
			
			for x in title_name[1:3]:
				help_embed.add_field(name=x, value=Trad.help_embed[lang_tests_results[1]][x],inline=True)
			for x in title_name[4:]:
				help_embed.add_field(name=x, value=Trad.help_embed[lang_tests_results[1]][x],inline=False)

		elif arg in Consts.help_args[1]:
			help_embed = self.make_embed(lang_tests_results,Trad.help_support_embed)

		elif arg in Consts.help_args[2]:
			title_name = [title_name for title_name in list(Trad.help_music_embed[lang_tests_results[1]].keys())]
			help_embed = self.make_embed(lang_tests_results,Trad.help_music_embed)
			help_embed.set_thumbnail(url=Consts.dev_in_progress_embed_thumbnail)

		elif arg in Consts.help_args[3]:
			help_embed = self.make_embed(lang_tests_results,Trad.help_fun_embed)
		
		elif arg in Consts.help_args[4]:
			title_name = [title_name for title_name in list(Trad.help_bug_embed[lang_tests_results[1]].keys())]
			help_embed = discord.Embed(title=title_name[0])
			help_embed.add_field(name= title_name[1],value=Trad.help_bug_embed[lang_tests_results[1]][title_name[1]],inline=False)

		elif arg in Consts.help_args[5]:
			help_embed = self.make_embed(lang_tests_results,Trad.help_reaction_embed)

		elif arg in Consts.help_args[6]:
			help_embed = self.make_embed(lang_tests_results,Trad.help_management_embed)
		
		elif arg in Consts.help_args[7]:
			help_embed = self.make_embed(lang_tests_results,Trad.help_options_embed)
		
		else:
			await ctx.send(Trad.invalid_arg_help[lang_tests_results[1]],delete_after=5)
			return False
		help_embed.set_author(name=Consts.bot_name, icon_url=Consts.Juicy_author_as_embed[Consts.bot_name])
		help_embed.set_footer(text=ctx.author)
		await ctx.send(embed=help_embed)
		return True
	
	@commands.command()
	async def discord(self,ctx):
		lang_tests_results = await self.bot.what_language(ctx)
		await ctx.send(Trad.discord[lang_tests_results[1]].format(discord=Consts.discord))
	
	@commands.command()
	async def website(self,ctx):
		lang_tests_results = await self.bot.what_language(ctx)
		await ctx.send(Trad.website[lang_tests_results[1]].format(website=Consts.website))

	@commands.command(aliases=['github'])
	async def botadmin(self,ctx):
		lang_tests_results = await self.bot.what_language(ctx)
		await ctx.send(Trad.botadmin[lang_tests_results[1]].format(github=Consts.github))

	@commands.command()
	async def news(self,ctx):
		lang_tests_results = await self.bot.what_language(ctx)
		title_name = [title_name for title_name in list(Trad.news[lang_tests_results[1]].keys())]

		news_embed = self.make_embed(lang_tests_results,Trad.news,last=-1)

		news_embed.set_author(name=Consts.bot_name, icon_url=Consts.Juicy_author_as_embed[Consts.bot_name])

		news_embed.set_footer(text=Trad.news[lang_tests_results[1]][title_name[-1]])
		await ctx.send(embed=news_embed)
