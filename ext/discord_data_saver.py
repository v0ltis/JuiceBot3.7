import discord
import asyncio
from __main__ import Consts
import ast


class DiscordDataSaver():
	def __init__(self,bot,saves_channel):#self.saves_location == channel
		self.bot = bot
		self.saves_location = saves_channel
	
	async def save(self,data):#data = {}
		data_to_send = ''
		data_keys = list(data.keys())
		for x in range(len(data_keys)):
			if type(data[data_keys[x]]) == str:
				data_to_send = data_to_send + str(data_keys[x]) + " = '" + data[data_keys[x]] + "'\n"
			else:
				data_to_send = data_to_send + str(data_keys[x]) + " = " + str(data[data_keys[x]]) + "\n"
		splitedlines_data = data_to_send.splitlines()
		firstelem_splitedlines_data = []
		
		for x in splitedlines_data:
			firstelem_splitedlines_data.append(x.split()[0])
		
		async for message in self.saves_location.history():
			if message.content.split()[0] in firstelem_splitedlines_data:
				a = firstelem_splitedlines_data.index(message.content.split()[0])
				#print(splitedlines_data[a])
				await message.edit(content=splitedlines_data[a])
				splitedlines_data.remove(splitedlines_data[a])

		for x in splitedlines_data:
			await self.saves_location.send(x)
		return True

	async def clear_command(self,ctx):
		channel = self.saves_location
		verif_clear_message = await channel.send('Are you sure you want to erase all the content of this channel ?')

		await verif_clear_message.add_reaction('✅')

		def check(reaction,user):
			return user.id in Consts.admins and str(reaction.emoji) == '✅'

		try:
			reaction, user = await self.bot.wait_for('reaction_add',timeout=10,check=check)
		except asyncio.TimeoutError:
			await channel.send("I'll do nothing.",delete_after=5)
		else:
			await channel.send('All rights !',delete_after=5)
			await verif_clear_message.delete()
			async for x in channel.history():
				await x.delete()
			await channel.send('Finish !',delete_after=2)
	
	async def load(self):
		channel = self.saves_location
		
		vars = []
		async for message in channel.history():
			vars.append(message.content)
		vars_decrypt = {}

		for element in vars:
			add = None
			if element.split()[2:][0][0] == "'" and element.split()[2:][0][-1] == "'":
				add = ''
				for x in range(len(element.split()[2:][0])):
					if x == 0 or x == len(element.split()[2:][0])-1:
						pass
					else:
						add = add + element.split()[2:][0][x]

			elif '.' in element.split()[2:][0]:
				add = float(element.split()[2:][0])
			
			elif '{' == ''.join(element.split()[2:])[0] and '}' == ''.join(element.split()[2:])[-1]:
				add = ast.literal_eval(''.join(element.split()[2:]))
			elif element.split()[2] == 'True':
				add = True
			elif element.split()[2] == 'False':
				add = False
			else:
				add = int(element.split()[2:][0])
			vars_decrypt[element.split()[0]] = add
		
		return vars_decrypt
