import discord
from discord.ext.commands import Bot
import os
import json
import time
from lang import trad
import random

client = Bot(command_prefix="/")

#
#DEF del_opt
#

def del_opt(serv, option, new):
    param = open(str(serv) + "/option.txt","r")
    param = param.read()
    param = (json.loads(param) )

    #del opt
    if not new in param[option]:
        del_opt.already = "oui"


    else:
        del_opt.already = None
        try:


            param[option] = str(param[option]).replace(" " + str(new),"")
            del_opt.err = "non"

        except:
            del_opt.exce = Exception
            del_opt.err = True

        del_opt.new = param[option]

        new_param = open(str(serv) + "/option.txt","w")

        param = json.dumps(param)
        new_param.write(param)



#
#DEF add_opt
#
def add_opt(serv, option, new):
    param = open(str(serv) + "/option.txt","r")
    param = param.read()
    param = (json.loads(param) )

    #add opt
    if new in param[option]:
        add_opt.already = True

    else:
        param[option] = param[option] + (" " + str(new))

        add_opt.new = param[option]

        new_param = open(str(serv) + "/option.txt","w")

        param = json.dumps(param)
        new_param.write(param)

#
# DEF set_opt
#
def set_opt(serv, option, new):

    param = open(str(serv) + "/option.txt","r")
    param = param.read()
    param = (json.loads(param) )

    #new opt :

    param[option] = new

    set_opt.new = param[option]

    new_param = open(str(serv) + "/option.txt","w")
    param = json.dumps(param)
    new_param.write(param)


#
#DEF Opt
#
def opt(guild,owner):
    try:
        serv =  guild.id
#       ouvre les paramètres
        param = open(str(serv) + "/option.txt","r")
        param = param.read()
        param = (json.loads(param) )

    except FileNotFoundError:
#       crée le fichier si il n'existe pas
        os.makedirs(str(serv))
        param = open(str(serv) + "/option.txt","a")
        param.write('{"langue":"en","admin":"' + owner + '","prefix":"/"}')
#          ouvre les paramètres
        param = open(str(serv) + "/option.txt","r")
        param = param.read()
        param = (json.loads(param) )


    opt.admin = str(param["admin"])

    opt.prefix = str(param["prefix"])

    opt.langue = str(param["langue"])






@client.event
async def on_message(message):
	if message.author == client.user or message.channel.type == "private":
		pass

	else:
		try:
			opt(message.guild,str(message.guild.owner.id))

			prefix = opt.prefix

			langue = opt.langue

			admin = opt.admin


			if message.content.upper().startswith(str(opt.prefix) + "OPTIONS"):
				if not message.content[8:]:
					await message.channel.send("Choisisez : \n\
                	**__get :__** ``prefix/admins/langue`` \n\
                	**__set :__** ``prefix/langue [value]`` \n\
                	**__add :__** ``admins [value]`` \n\
                	**__del :__** ``admins [value]`` \n\
                	**__reset :__** ``prefix/admins/langue``")



				elif str(message.author.id) not in admin:
					await message.channel.send("Vous n'avez pas les permissions pour faire ça !")

				elif message.content.upper()[9:12] == "GET":

					if message.content.upper()[13:] == "PREFIX":
						await message.channel.send("Le prefix est :``" + opt.prefix + "``")

					elif message.content.upper()[13:] == "ADMINS":
						await message.channel.send("Les IDs des admins sont :``" + opt.admin + "``")

					elif message.content.upper()[13:] == "LANGUE":
						await message.channel.send("La langue choisie est: ``" + opt.langue + "``")


					else : await message.channel.send("Syntaxe : ``" + str(opt.prefix) + "options get [prefix/admins/langue]``" )

        #
        #RESET
        #

				elif message.content.upper()[9:14] == "RESET":

					if message.content.upper()[15:] == "PREFIX":
						set_opt(message.guild.id,"prefix","/")
						await message.channel.send("Le prefix est désormais ``" + str(set_opt.new) + "``")

					elif message.content.upper()[15:] == "ADMINS":
						set_opt(message.guild.id,"admin",message.guild.owner.id)
						await message.channel.send("Les IDs des admins sont désormais :" + str(set_opt.new))

					elif message.content.upper()[15:] == "LANGUE":
						set_opt(message.guild.id,"langue","en")
						await message.channel.send("La langue choisie est désormais: " + set_opt.new)
					else :
						await message.channel.send("Syntaxe : ``" + str(opt.prefix) + "options get [prefix/admins/langue]``" )


        #
        #EDIT
        #

				elif message.content.upper()[9:12] == "SET":

					if message.content.upper()[13:19] == "PREFIX":
						if message.content[20:21]:
							set_opt(message.guild.id,"prefix",message.content[20:21])
							await message.channel.send("Le prefix est désormais `` " + set_opt.new + " ``")
						else:
							await message.channel.send("Veuillez preciser un carractère pour le prefix (Ex : ``/``,``>``,``!``)")


					elif message.content.upper()[13:21] == "LANGUAGE":
						print(message.content[22:24])

						if message.content[22:24] == "fr" or message.content[22:24] == "en":
							set_opt(message.guild.id,"langue",message.content[22:24])

							if message.content[22:24] == "fr":
								lang = "``Français (fr)``"
								await message.channel.send("La langue choisie est désormais: " + lang)
							elif message.content[22:24] == "en":
									lang = "``English (en)``"
									await message.channel.send("La langue choisie est désormais: " + lang)

							else:
								await message.channel.send("Veuillez preciser une langue valide (Ex : ``fr``,``en``)")


        #
        #add
        #
				elif message.content.upper()[9:12] == "ADD":
					if message.content.upper()[13:18] == "ADMIN":
						id = message.content.upper()[19:37]
						add_opt(message.guild.id,"admin",id)
						if add_opt.already:
							await message.channel.send("Cette personne est deja admin !")
						else:
							await message.channel.send("l'id ``" + id + "`` à corectement été ajouté !")
							await message.channel.send("Voicis les ID des admins du serveur : ``" + add_opt.new + " ``")


        #
        #remove
        #

				elif message.content.upper()[9:12] == "DEL":
					if message.content.upper()[13:18] == "ADMIN":
						id = message.content.upper()[19:37]
						if message.content[19:37]:
							if id == str(message.guild.owner.id):
								await message.channel.send("Vous ne pouvez pas retirer les droit du propriétaire du serveur")
							else:
								del_opt(message.guild.id,"admin",id)
								if del_opt.already == "oui":
									await message.channel.send("Cet utilisateur n'est pas stocké en temps qu'admin !")
								elif del_opt.err == "non":
									await message.channel.send("l'id ``" + id + "`` à corectement été suprimé !")
									await message.channel.send("Voicis les ID des admins du serveur : ``" + del_opt.new + " ``")
								else :
									await message.channel.send("Une erreure est survenue !")
									await print(del_opt.exce)
						else:
							await message.channel.send("Veuillez preciser un ID !")

			elif message.content.lower().startswith(prefix + 'ping'):
				ping_time = time.monotonic()
				pinger = await message.channel.send(":ping_pong: **Pong !**")
				ping = "%.2f"%(1000* (time.monotonic() - ping_time))
				await pinger.edit(content=":ping_pong: **Pong !**\n `Ping:" + ping + "`")


			elif message.content.lower().startswith(prefix + "say"):
				args = message.content[4:]

				if not str(message.author.id) in admin:
					await message.channel.send("<@"  + str(message.author.id) + ">")

				await message.channel.send(args)


			elif message.content.lower().startswith(prefix + "8ball"):
				bal = random.choice(trad.ball[langue].split())
				await message.channel.send(bal.replace("§"," "))

			elif "BONJOUR" in message.content.upper() or "HELLO" in message.content.upper() :
				await message.channel.send("Hey !")

			elif ("GG " or "GL ") in message.content.upper():
				await message.channel.send(":clap: :clap: :clap:")

			elif message.content.lower().startswith(prefix + "help"):
				if langue == "fr":
				   need = trad.mod_fr
				elif langue == "en":
				     need = trad.mod_en

				help = discord.Embed(title="Help",description=need[0])
				help.add_field(name = need[1],value = need[2].format(prefix), inline=False)
				help.add_field(name = need[3],value = need[4].format(prefix), inline=False)
				await message.channel.send(embed=help)

		except Exception as e:
		          print(e)
		          file = open("errors.txt","a")
		          file.write(str(e) + "/n")

client.run(TOKEN)
#opt = file param open
