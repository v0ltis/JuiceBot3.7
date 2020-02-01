import discord
import asyncio
import os
import json
import aiohttp

from __main__ import Token

#GIPHY_KEY = os.environ[token.GIPHY_KEY]

async def gifsearch(message):
	linkstart = "http://api.giphy.com/v1/gifs/search?q="
	linkmiddle = "&api_key="
	linkend = "&limit=5"
	arg = "message.content"
	mess = "".join(arg[5:])
	lien = str(linkstart) + str(mess) + str(linkmiddle) + str(token.GIPHY_KEY) + str(linkend)
	async with aiohttp.ClientSession() as ses:
		async with ses.get(lien) as resp:
			gif = json.dumps(ses, sort_keys=True, indent=4)
	await channel.send(gif)
	
