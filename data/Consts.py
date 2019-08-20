commands_prefix = '/'
version = 2.0
bot_name = 'JuiceBox'
discord = 'https://discord.gg/Abfvn9y'
website = 'https://juicebot.github.io/'
github = 'https://github.com/v0ltis/juicebox'
language = [['EN','En','en'],['FR','fr','Fr']]

news = ((
	'A full rewrite of the bot allowing it to be at the latest version of discord.py',
	'Nothing for the moment'),(
	"Une réécriture complète du bot lui permettant ainsi d'être à la dernière version de discord.py.",
	"Rien pour l'instant"
))

ban_users = []


admins = [402896241429577729,362615539773997056,600754461404823592]


reboot_channel_id = 600752747230265356
saves_location = 602514509394870274
ticket_location = 602223721033236513

#dev
tester = 600754461404823592
tester_admin = 402896241429577729

bot_messages = 603218967812767757

patching_filter = 613306094185349121

Juicy_author_as_embed = {bot_name:"https://discordemoji.com/assets/emoji/JuiceBox.png"}

error_messages_channel = 602459257375555603
dev_in_progress_embed_thumbnail = "https://pbs.twimg.com/profile_images/507225386027974656/GdTTaIrf.png"

options = ['JUICYS_REACTION']
commands = [
'ping',
'say',
'8ball',
'contact',
'answer_ticket',
'help',
'report'
]

help_args = [[None],
['support','community'],
['music'],
['fun'],
['bug','translation','trad'],
['reaction','react'],
['management','mngmt','manag'],
['options','opts','optns']
]

gifs = ["https://giphy.com/gifs/AuIvUrZpzBl04",
			"https://giphy.com/gifs/hello-hey-big-brother-l0MYBbEvqqi1kfuyA",
			"https://giphy.com/gifs/trump-donald-eclipse-xUNen16DFqlM6v6DEQ",
			"https://tenor.com/view/ok-okay-gif-5307535",
			"https://gph.is/2iUaL8y",
			"https://gph.is/19aLnvI",
			"https://gph.is/2fiQFj1",
			"https://gph.is/1rr0eCj",
			"https://media.giphy.com/media/joPQLwo2kbXe8/giphy.gif",
			"https://media.giphy.com/media/QGzPdYCcBbbZm/giphy.gif",
			"https://media.giphy.com/media/w1XrYq5PsCbyE/giphy.gif",
			"https://gph.is/2tBvKBE",
			"https://tenor.com/view/pinguino-furbo-frozen-excited-gif-13388703",
			"https://gph.is/2lnp32Z",
			"https://gph.is/2rwmnmy",
			"https://tenor.com/4iLj.gif",
			"https://tenor.com/4gdR.gif",
			"https://tenor.com/yFDW.gif",
			"https://tenor.com/4n8e.gif",
			"https://tenor.com/view/cobie-smulders-sad-crying-wine-upset-gif-3550883",
			"https://tenor.com/view/shocked-omg-australiasgottalent-noway-gif-5027549",
			"https://gph.is/2SGx6It",
			"https://media.giphy.com/media/l4FGpPki5v2Bcd6Ss/giphy.gif",
			"https://thumbs.gfycat.com/NaiveMatureArmedcrab-small.gif"]

offensive_one = ['https://media.giphy.com/media/QGzPdYCcBbbZm/giphy.gif',
'https://media.giphy.com/media/w1XrYq5PsCbyE/giphy.gif']


#music Consts
music_location = './Tracks/'
def my_hook(d):
	if d['status'] == 'finished':
		print("one track more")

ytdl_options = {
	'keepvideo':True,
	'format': 'bestaudio/best',
	'usenetrc': True,
	'outtmpl': music_location+'{}[{}]-%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'default_search': 'auto',
	'progress_hooks': [my_hook],
	'quiet': True,
	'no_warnings':True
	}

outtmpl = music_location+'{}[{}]-%(title)s.%(ext)s'

file_name = music_location+'{}[{}].webm'