import traceback, sys

import discord,asyncio
from discord.ext import commands,tasks

from __main__ import Consts

class Dev_Tools(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.chat = False

	@commands.command()
	async def dev_info(self,ctx):
		if ctx.author.id in Consts.admins:
			app_info = await self.bot.application_info()
			await ctx.author.create_dm()
			commands_msg = ''
			for x in self.bot.commands:
				commands_msg = commands_msg + x.name
			await ctx.author.dm_channel.send((app_info,commands_msg,self.bot.latency,'https://discordapp.com/oauth2/authorize?&client_id=566334647424778251&scope=bot&permissions=8'))

	@commands.command(pass_context=True)
	async def chat(self,ctx,arg):
		if arg.upper() == 'ON':
			self.chat = True
		elif arg.upper() == 'OFF':
			self.chat = False

	@commands.Cog.listener()
	async def on_message(self, message):
		if self.chat == True and message.author != self.bot.user:
			chat_message = ''
			if message.guild != None:
				chat_message = "Serveur du message : {}, ".format(message.guild.name)
			if type(message.channel) != discord.DMChannel:
				chat_message = chat_message + "channel du message : {}, ".format(message.channel.name)
			chat_message = chat_message + " message : {}".format(message.content)
			print(chat_message)
			channel = self.bot.get_channel(id=Consts.bot_messages)
			await channel.send(chat_message)
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		error_channel = self.bot.get_channel(Consts.error_messages_channel)
		"""The event triggered when an error is raised while invoking a command.
		ctx   : Context
		error : Exception"""

		# This prevents any commands with local handlers being handled here in on_command_error.
		if hasattr(ctx.command, 'on_error'):
			return
		
		ignored = (commands.CommandNotFound, commands.UserInputError)
		
		# Allows us to check for original exceptions raised and sent to CommandInvokeError.
		# If nothing is found. We keep the exception passed to on_command_error.
		error = getattr(error, 'original', error)
		
		# Anything in ignored will return and prevent anything happening.
		if isinstance(error, ignored):
			return

		elif isinstance(error, commands.DisabledCommand):
			return await ctx.send(f'{ctx.command} has been disabled.')

		elif isinstance(error, commands.NoPrivateMessage):
			try:
				return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
			except:
				pass

		# For this error example we check to see where it came from...
		elif isinstance(error, commands.BadArgument):
			if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
				return await ctx.send('I could not find that member. Please try again.')
		
		#Added code
		Error_msg = 'Ignoring exception in command {}]:\n'.format(ctx.command)
		Error_msg = Error_msg + '='*(len(Error_msg)+1) + '\n'
		for x in traceback.format_exception(type(error), error, error.__traceback__):
			Error_msg = Error_msg + x

		to_send = "```Markdown\n [Error : {}\n#[Command : {}]```".format(Error_msg,ctx.message.content)
		await error_channel.send(to_send)


#https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
