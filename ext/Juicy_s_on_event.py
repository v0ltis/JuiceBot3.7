import discord
from discord.ext import commands

import random

from __main__ import Consts,Trad

class Eventing(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.chat = False

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id == Consts.tester:
			admin = self.bot.get_user(Consts.tester_admin)
			if admin.dm_channel == None:
				await admin.create_dm()
			admin_dm = admin.dm_channel
			ctx = await self.bot.get_context(message)
			try:
				await self.bot.invoke(ctx)
			except:
				await admin_dm.send(traceback.format_exc())
		if message.author.id in Consts.ban_users:
			pass
		elif message.author == self.bot.user:
			pass

	@commands.Cog.listener()
	async def on_member_join(self,member):
		lang_test_results = await self.bot.what_language(None,author_id=member.id)
		channel = discord.utils.find(lambda a : type(a) == discord.TextChannel and a.name in Trad.welcome_channel, member.guild.channels)
		await self.bot.verifie_loaded_data()
		await channel.send(random.choice(Trad.welcome_messages[lang_test_results[1]]).format(user_name=member.id,guild_name=member.guild.name))
