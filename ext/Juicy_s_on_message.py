import discord
from discord.ext import commands

import random

from __main__ import Consts,Trad,Filter

class Messaging(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_message(self,message):
		try:

			await self.bot.verifie_loaded_data()
			lang_test_results = await self.bot.what_language(message)
			message_to_send = ''
			
			if type(message.channel) != discord.DMChannel:
				async def filter(message):
					await message.delete()
					message_to_send = '<@{}>\n :rage: || {} ||'.format(message.author.id,message.content)
					await message.channel.send(message_to_send)

				if message.author == self.bot.user:
					return False

				perms = message.channel.permissions_for(message.author)
				has_been_fitlered = False
				for x in Filter.fitler_FR_in:
					if x in message.content.lower() and not x in Filter.fitler_FR_not \
					and message.channel.permissions_for(message.author).administrator==False \
					and message.channel.permissions_for(message.author).manage_messages==False \
					and message.channel.permissions_for(message.author).manage_channels==False:
						await filter(message)
						has_been_fitlered = True
						return False
				for x in Filter.fitler_FR_emoji:
					if x in message.content.lower() \
					and message.channel.permissions_for(message.author).administrator==False \
					and message.channel.permissions_for(message.author).manage_messages==False \
					and message.channel.permissions_for(message.author).manage_channels==False:
						await filter(message)
						has_been_fitlered = True
						return False

			if message.guild != None:
				try:
					if self.bot.loaded_data['options'][message.guild.id][Consts.options[0]] == False:
						return False
				except KeyError:
					pass
			
			for word in message.content.split():
				if word.lower() in Filter.shit:
					await message.add_reaction(emoji='💩')
			
			if message.content.upper().startswith("<@{}>".format(self.bot.user.id)):
				await message.channel.send(Trad.do_you_call_me[lang_test_results[1]])
				return True
			elif "<@{}>".format(self.bot.user.id) in message.content.upper():
				await message.channel.send(Trad.do_you_call_me[lang_test_results[1]])
				return True

			for x in range(len(Trad.greetings)):
				for y in Trad.greetings[x]:
					if y in message.content.lower():
						await message.channel.send(random.choice(Trad.greetings[x]))
						return True
			'''
			elif 'XD' in message.content.upper():
				choice = random.choice(["lol",
				None,
				None])
				if choice != None:
					await message.channel.send(choice)
				return True
			'''

			if "BONJOUR" in message.content.upper() or "HELLO" in message.content.upper() :
				await message.channel.send("Hey !")
				return True
			
			elif "GG" in message.content.upper() or "GJ" in message.content.upper() \
				or "GOOD GAME" in message.content.upper() or "GOOD JOB" in message.content.upper():
				await message.channel.send(":clap: :clap: :clap:")				
				return True

			react_with = []
			for x in range(len(Filter.react_with_number)):
				for y in range(len(Filter.react_with_number[x])):
					if Filter.react_with_number[x][y] in message.content:
						react_with.append(y)
			for x in react_with:
				await message.add_reaction(emoji=Filter.reactions_numbers[x])
		except discord.errors.Forbidden:
			pass