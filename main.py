import sys,os
from subprocess import call
import youtube_dl
'''
from importlib import reload
call(sys.executable +' -m pip install --upgrade youtube_dl')#upgrading youtube dl lib to avoid music bugs
reload(youtube_dl)
'''
from importlib import reload

import discord
from discord.ext import commands


sys.path.append('./data/')

import Consts
import Trad,Filter,Token

sys.path.append('./ext/')

import discord_data_saver, gif_giffy

from Juicy_s_on_event import Eventing
from Juicy_s_dev_tools import Dev_Tools
from Juicy_s_commands import Commanding
from Juicy_s_dev_tools_commands import Dev_Tools_Commands
from Juicy_s_background import Background_Tasks
from discord_data_saver import DiscordDataSaver
from Juicy_s_help_about_command import Help_Command
from Juicy_s_on_message import Messaging

sys.path.append('./ext/music/')

from Music_event import Music_Event
from Music_Commands import Music_Commands_Class

class Juicy(commands.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		#super().add_cog(None) add extensions
		super().add_cog(Eventing(self))
		super().add_cog(Dev_Tools(self))
		super().add_cog(Commanding(self))
		super().add_cog(Dev_Tools_Commands(self))
		super().add_cog(Background_Tasks(self))
		super().add_cog(Help_Command(self))
		super().add_cog(Messaging(self))
		
		#music
		super().add_cog(Music_Event(self))
		super().add_cog(Music_Commands_Class(self))
		self.auto_leave_for_guild = {}

	async def on_ready(self):
		print('Ready !')
		reboot_channel = self.get_channel(Consts.reboot_channel_id)
		await reboot_channel.send('Reboot complete !',delete_after=5)

	async def verifie_loaded_data(self):
		channel = self.get_channel(Consts.saves_location)
		self.Saver = DiscordDataSaver(self,channel)
		self.loaded_data = await self.Saver.load()

	async def what_language(self,ctx,author_id=None,member_id=None):
		if ctx == None or member_id != None:
			author_id = member_id
			guild_id = None
		elif ctx.guild != None:
			author_id = ctx.author.id
			guild_id = ctx.guild.id
		else:
			author_id = ctx.author.id
			guild_id = None
		
		await self.verifie_loaded_data()
		
		try:
			self.lang = self.loaded_data['lang']
		except AttributeError:
			self.lang = {}
		except KeyError:
			self.lang = {}

		if author_id in list(self.loaded_data.keys()):
			language = loaded_data[ctx.author.id]
			return (1,language)#1 : author language, 
		elif guild_id != None:
			if guild_id in list(self.loaded_data.keys()):
				language = loaded_data[ctx.guild.id]
				return (2,language)
			else:
				return (0,0)
		else:
			return (0,0)

Bot = Juicy(command_prefix=Consts.commands_prefix,help_command=None)
Bot.run(os.environ["TOKEN_HERE"])

print('Finished')
