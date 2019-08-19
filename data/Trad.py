import Consts

import random
from random import randint

x = randint(-5000, 10000)
z = randint(10, 1000)


greetings = (['hello ','hi ','hi,','hello,'],['bonjour ','salut ','salut'],['hey'])
#greetings = ((['hello','hey','hi'],['greetings']),[,'bonjour','salut','hey',],['salutation'])

do_you_call_me = ("Do you talk about me ?","On parle de moi ?")

#startwith @juicy
do_you_call_me_beg = ("Hi, i'm {}, here are some commands that could help you :\n".format(Consts.bot_name)+\
	"```{}help``` : print all available commands, ```{}help support``` : print commands to contact us".format(Consts.commands_prefix,Consts.commands_prefix),
	"Bonjour, je suis {}, voici quelques commandes qui pourraient t'aider:\n".format(Consts.bot_name)+\
	"```{}help``` : affiche toutes les commandes discponible, ```{}help support``` affiche les commandes pour nous contacter".format(Consts.commands_prefix,Consts.commands_prefix)
	)

reacts = (["Unknown emoji ```{}``` if you think that is a bug please use \
	```{}help bug```".format('{}',Consts.commands_prefix),
	"Cannot find this message, please check that it is in the specified channel (current/specified).",
	"Reaction(s) successfully edited !",
	"Message id is required when using the channel id",
	""
	],[
	"emoji inconnue ```{}``` si vous penssez qu'il s'agit d'un bug veuillez utiliser \
	```{}help bug```".format('{}',Consts.commands_prefix),
	"Impossible de trouver le message, veuillez vérifier qu'il est dans le salon spécifié (actuel/spécifié)",
	"Réaction(s) modifiée(s) avec succès !",
	"L'id du message est requis en cas d'utilisation de l'id du salon"
	])

#options messages
options = ([
	"Unknown option for more information please use ```{}help``` command ".format(Consts.commands_prefix),
	"Option edited successfully",
	'You need to send this message in a channel of a server']
	,
	["Option inconnue pour plus d'informations, veuillez utiliser la commande ```{}help```".format(Consts.commands_prefix),
	'Option modifié avec succès',
	"Vous devez envoyez ce message dans le salon d'un serveur"]
	)

#report embed/messages
report_msgs = ((
	{
		'Reported user:':'{}',
		'Reported by:':'{}',
		'For the following reason:':'{}'
	},
	['The specified server was not found',
	'There is no #report channel on this server',
	'Report successfully send !',
	"The mention (@Username) is incorrect verifie you write it correcly (@Username#user_discriminator). \n \
	(start typing the mention on the server clic on the user and copy paste the result)",
	"You need to tell me the server name where you want me to report somebody"])
	,
	{
		'Utilisateur signalé:':'{}',
		'Signalé par:':'{}',
		'Pour la raison suivante:':'{}'
	},
	["Le serveur indiqué n'a pas été trouvé",
	"Il n'y a pas de salon #report sur ce serveur",
	'Signalement envoyé avec succès !',
	"La mention (@Nom d'utilisateur) est incorrecte vérifiez que vous l'avez écrite correctement (@Nom d'utilisateur#id de l'utilisateur).\n \
	(commencer à taper la mention sur le serveur appuyez sur l'utilisateur et copiez collez le tout)",
	"Vous devez me dire le nom du serveur dans lequel vous voulez que je signale quelqu'un"]
	)


#language messages

language = (
(
	('for you','for your guild'),
	'''You haven't enough permissions to do that. (You need "manage guild" permission)''',
	'Language successfully set {} !',
	'You must send this message in the server whose default language you want to change.'
	),
(	('pour vous','pour votre serveur'),
	'''Vous n'avez pas les permissions neccessaire pour faire cela. (Vous avez besoin de la permission "gérer le serveur")''',
	"Langue mise à jour avec succès {} !",
	"Vous devez envoyer ce message dans le serveur dont vous voulez modifier la langue par default."
	)
)

#8ball messages

ball_aswer = (["I don't know.",
	"I think yes.",
	"Yes yes and yes !",
	"Of course !",
	"Probably ...",
	'Nooooooooooooooooo !',
	'Why do you ask me this question ?',
	'Мен кодексине ката жок деп ойлойм !',
	'Of course not',
	"I won't awnser this question .",
	'Nope !',
	'Surely !',
	'Absolutely not !',
	'I reassure you, no.',
	'Ask your question again later.'
	],
	["Je ne sais pas.",
	"Je pense que oui.",
	"Surement !",
	"Oui oui et oui !",
	"Evidement !",
	"Sans doutes ...",
	"Nooooonnnnnnnnnnnn !",
	"Pourquois tu pose cette question ?",
	"Мен ката коду бар деп ойлойм !",
	"Surement pas !",
	"Je ne repondrais pas à cette question .",
	"Nan !",
	"Forcement !",
	"Absolument pas !",
	"Je te rassure , non.",
	"Repose ta question plus tard."])

#Contact confirmations messages

contact = (
	"Your message has been sent. Thank you for contacting us, our team will answer you as soon as possible.",
	"Votre message à bien été envoyé. Merci de nous avoir contacté, notre équipe va vous répondre au plus vite."
	)

#Welcome messages

welcome_messages = (
	["<@{user_name}> has join **{guild_name}** ! Don't you say hello ?",
	"<@{user_name}> has join the server !"],
	
	["Tiens ! <@{user_name}> a rejoint **{guild_name}** ! On lui dit pas bonjour ?",
	"<@{user_name}> à rejoint le serveur !"]
	)

welcome_channel = ('welcome','bienvenue')

#About messages
discord = ('Come talk here : {discord}','Viens parler ici : {discord}')
website = ('My house is here : {website}','Ma maison est ici : {website}')
botadmin = ("Hey Boss, here is my code: {github}",
	"Hey Boss, mon code se trouve ici: {github}")

calc = (["That makes " + str(x) + " almost",
        "I would say " + str(x),
        str(x) + "," + str(z) + " normally",
        "Error System",
        "It's equal to " + str(x),
	"Aproximately " + str(x) + "!",
        "it's exactly " + str(x) + "," + str(z)
	],
	["Ça fais " + str(x) + " à peu près",
        "Je dirai " + str(x),
        str(x) + "," + str(z) + " normalement",
        "Error System",
        "C'est égal à " + str(x),
        "Aproximativement " + str(x) +" !",
        "C'est " + str(x) + "," + str(z) + " pile !"])

news = ({
	'News':'Here are my lastest patch note:',#title/desc
	'Patch note:':Consts.news[0][0],#field 1
	'For the future update:':Consts.news[0][1],#field 2
	'Ver':'Version : v{}'.format(Consts.version)#footer ?
	},{
	'News':'Voici ma dernière note de patch:',#title/desc
	'Note de patch:':Consts.news[1][0],
	'Pour la prochaine mise à jour:':Consts.news[1][1],
	'Ver':'Version : v{}'.format(Consts.version)})

#Help embeds

help_embed = (
	{'Commands:':'Here is the list of available commands:',
	'Prefix:':Consts.commands_prefix,
	'help fun':'Tell you the funny commands',
	'help management':'Tell you the server management commands',
	'help music':'Tell you the music command',#+' ***Available soon***',
	'help support':'Tell you the commands to communicate with our team',
	'help reaction':'Tell you the commands about reaction',
	'news':'Tell you the last news about Juicebox',
	'botadmin/github':"Tell you where you can find Juicy's code (python)"
	},
	{'Commandes:':'Voici la liste des commandes:',
	'Prefix:':Consts.commands_prefix,
	'help fun':'Donne les commandes pour le fun',
	'help management':"Donne les commandes de gestion d'un serveur",
	'help music':'Donne les commandes de musique'+' ***Bientôt disponible***',
	'help support':'Donne les commandes en rapport avec mon équipe',
	'help reaction':'Donne les commandes en rapport avec les réactions',
	'news':'Ok Juicebox, quelles sont les dernière nouveautées ?',
	'botadmin/github':"Te dis où trouver le code de Juicy (python)"
	})

help_support_embed = ({
	'Help commands:':'Here are the commands to help you to better know Juicy:',
	'contact':'Send a message to my team,'+' use : ```{}contact "Your Subject" your message```'.format(Consts.commands_prefix)+\
	"\nDon't hesitate to correct our translation or report a bug (for more information use : help bug)",
	'website':'Tell you the link of our website : ``https://juicebot.github.io``',
	'discord':'Tell you the link of our support server: ``https://discord.gg/Abfvn9y``'
	},
	{"Commandes d'aide":"Voici la liste des commandes pour vous aider à mieux connaître Juicy:",
	"contact":'Envoi un message à mon équipe,'+' utilise : ```{}contact "Ton Sujet" ton message```'.format(Consts.commands_prefix)+\
	"\nN'ésitez pas à coriger nos traduction ou à signaler un bug (pour plus d'information utiliser la commande : help bug)",
	'website':'Donne le lien de notre site : ``https://juicebot.github.io``',
	'discord':'Donne le lien de notre server de support : ``https://discord.gg/Abfvn9y``'
	})

help_music_embed = (
	{'Music commands :':"Music player's developement in progress ...","play":'play music from youtube use\
	 ```{}play url/playlist url```'.format(Consts.commands_prefix),'skip':'skip one music video',
	 'stop':'stop the player','pause':'pause the player','resume':'resume the player'},
	{'Commandes de musique :':'Le lecteur de musique est en cours de developement ...',
	'play':"joue de la musique de youtube utilisez ```{}play url/url d'un playlist```".format(Consts.commands_prefix),
	'skip':'saute une video de musique',
	'stop':'stop le lecteur',
	'pause':'met en pause le lecteur',
	'resume':'reprend la lecture de la musique'})


help_fun_embed = (
	{'Fun commands:':'Here are fun commands:',
	'say':'Juicy say your text and delete your message,'+' use : ```{}say Your message```'.format(Consts.commands_prefix),
	'gif':'Send a random GIF if it is mark as spoiler, it can be offensive',
	'memeaudio':'Play a random audio meme in a Voice Channel',
	'info':'Send informations about a guild member.... or yourself !',
	'8ball':'Answer your questions with his crystal ball,but he is sometimes very indecisive'},
	{'Commandes fun:':'Voici les commandes fun:',
	'say':'Fait dire au bot votre texte et supprime votre message,'+' utilise : ```{}say Ton Message```'.format(Consts.commands_prefix),
	'gif':"Envoie un GIF aléatoire s'il est marqué comme spoiler, il peut être offenssant",
	'memeaudio':'Joue un meme audio aléatoire dans un salon vocal',
	'info':'Donne de nonbreuses informations à propos des membres du serveur... ou vous-même !',
	'8ball':'Répond à vos questions après un temps de réflexion, pour sa boule de crystal'
	})

help_bug_embed = ({
	"Report an error or bug ":None,
	"contact":'Use contact command with "Bug" or "Translation" as Subject (for more informations about contact command consult : help support)'}
	,{
	"Signaler une erreur ou un bug":None,
	"contact":'''Utilisez la commande contact avec "Bug" ou "Translation" comme sujet (pour plus d'informations à propose de la commande contact consultez : help support)'''
	})

help_reaction_embed = ({
	"Reactions:":"Here are Juicy's reactions fonctions:",
	"react":"Add or remove a reaction from your message, use ```{}react [message id*] [message's channel**] your emoji(s)```\
	*(optional/enable developers options (discord settings/appearance) to see ids of channel or messages/else add or remove reaction(s) to this message)\n".format(Consts.commands_prefix)+"\
	**(optional/required with message id/else search message in the current channel)",
	"[number]-":'Add 0-, 1- ... or -0, -1 ... in your message to add a reaction'
	},{
	"Reactions:":"Voici comment peut réagir Juicy's à vos messages:",
	"react":'Ajoute ou suprime une réaction de votre message, utilisez ```{}react [id du message*] [id du salon**] vo(tre/s) emoji(s)```\
	*(optionnel/activez les options pour développeur (paramètre discord/apparence) pour voir les ids des messages ou des salons/sinon ajoute ou suprime l(a/es) réaction(s) à ce message)\n'.format(Consts.commands_prefix)+"\
	**(optionnel/requis avec l'id du message/sinon cherche le message dans le salon actuel)",
	"[nombre]-":'Ajoutez 0-, 1-, etc... ou -0, -1, etc... à votre message pour ajouter ces réactions'
	})

help_management_embed = (
	{'Server management commands:':'Here are the server management commands:',
	'report':'Report the bad guys in #report (if the channel exists in that server),'+' \
	use ```{}report @Naughty_User motive``` in a text channel \n or ```{}safe_report @Naughty_User \
	"Server name" motive``` in a dm channel'.format(Consts.commands_prefix,Consts.commands_prefix),
	'Swearword':"I automatically remove frensh insults (send us english insults to fitler them(use help support or help translation)) if you don't have certain permissions"
	},
	{'Commandes de modération:':'Voici la liste des commandes de modération:',
	'report':'Signale les méchants utilisateur dans #report (si le salon existe sur ce serveur),'+' utilisez ```\
	{}report @Vilain_Utilisateur motif```dans une salon textuel ou ````{}safe_report @Vilain_Utilisateur "Nom du serveur" motif``` \
	en message privé'.format(Consts.commands_prefix,Consts.commands_prefix),
	'Gros-mots':"Je suprime automatiquement les insultes si vous n'avez pas certaines permissions"
	})

help_options_embed = ({
	"Options management for servers:":'Here are the editable options list:',
	"JUICYS_REACTION":"Enable or disable Juicy's reaction like when you say 'gg' juicy answer :clap: :clap: :clap:",
	"To edit options use :":" ```{}options OPTION VALUE```VALUE can be True or False to enable or disable this option".format(Consts.commands_prefix)
	},{
	"Gestion des options pour les serveurs":'Voici la liste des fonctions modifiable:',
	"JUICYS_REACTION":"Active ou désactive les réaction de Juicy comme quand vous dîtes 'gg' Juicy répond :clap: :clap: :clap:",
	"Pour modifier une options utilisez :":" ```{}options UNE_OPTION VALEUR```VALEUR peut être True ou False pour activer ou désactiver cette option.".format(Consts.commands_prefix)
	})

invalid_arg_help = ('Unknown argument for more help see ```{}help```'.format(Consts.commands_prefix),"Argument inconnnu pour plus d'aide consultez {}help".format(Consts.commands_prefix))


