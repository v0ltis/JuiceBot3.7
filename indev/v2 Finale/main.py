print("Demarage en cours . . .")
import discord
print("Discord importé !")
import asyncio
print("Asyncio importé !")
from discord.ext import commands, tasks
from discord.ext.commands import Bot
print("Discord.ext importé !")
import os
print("Os importé !")
import json
print("Json importé !")
import time
print("Time importé !")
import random
print("Random importé !")
import datetime
print("Datetime importé !")
from ext import trad,data,opt_trad
print("La traduction a été importée !")
client = Bot(command_prefix="/")

@client.event
async def on_ready():

    await client.change_presence(activity=discord.Activity(name="/help - @JuiceBox#5545",type=discord.ActivityType.watching), status=discord.Status.dnd)
    print("Rich presence activé !")

    print("Informations du bot : \nNom: {}, \nID: {}".format(client.user.name,client.user.id))

    guil = "Serveurs : \n"
    guil_ = []
    for x in client.guilds:
        guil += str(x.name) + " "
        guil_.append(str(x.name))
    print(guil)
    print(len(guil_))

    print("Demarage terminé")
    while True:
        await client.change_presence(activity=discord.Activity(name="/help - @JuiceBox#5545",type=discord.ActivityType.watching), status=discord.Status.dnd)
        await asyncio.sleep(0.5)
        await client.change_presence(activity=discord.Activity(name="/help - @JuiceBox#5545",type=discord.ActivityType.watching), status=discord.Status.dnd)
        await asyncio.sleep(3600)
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
#DEF opt
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

    try:
        prem = open(str(serv) + "/premuim.txt","r")
        opt.premuim = prem.read()

    except:
        opt.premuim = False






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
					await message.channel.send(opt_trad.help[langue])



				elif str(message.author.id) not in admin:
					await message.channel.send("Vous n'avez pas les permissions pour faire ça !")

				elif message.content.upper()[9:12] == "GET":

					if message.content.upper()[13:] == "PREFIX":
						await message.channel.send(opt_trad.now_prefix[langue].format(opt.prefix))

					elif message.content.upper()[13:] == "ADMINS":
						await message.channel.send(opt_trad.now_id[langue].format(opt.admin))

					elif message.content.upper()[15:] == "LANGUAGE":
						await message.channel.send(opt_trad.lang.format(opt.langue))


					else : await message.channel.send(syn_err )

        #
        #RESET
        #

				elif message.content.upper()[9:14] == "RESET":

					if message.content.upper()[15:] == "PREFIX":
						set_opt(message.guild.id,"prefix","/")
						await message.channel.send(opt_trad.now_prefix[langue].format(str(set_opt.new)))

					elif message.content.upper()[15:] == "ADMINS":
						set_opt(message.guild.id,"admin",message.guild.owner.id)
						await message.channel.send(opt_trad.admin_reset[langue].format(str(set_opt.new)))

					elif message.content.upper()[17:] == "LANGUAGE":
						set_opt(message.guild.id,"langue","en")
						await message.channel.send("The selected language is now:  " + set_opt.new)
					else :
						await message.channel.send(opt_trad.syn_err[langue].format(prefix, "reset"))


        #
        #EDIT
        #

				elif message.content.upper()[9:12] == "SET":

					if message.content.upper()[13:19] == "PREFIX":
						if message.content[20:21]:
							set_opt(message.guild.id,"prefix",message.content[20:21])
							await message.channel.send(opt_trad.now_prefix[langue].format(set_opt.new))
						else:
							await message.channel.send(opt_trad.pref_propos[langue])


					elif message.content.upper()[13:21] == "LANGUAGE":
						print(message.content[22:24])

						if message.content[22:24] == "fr" or message.content[22:24] == "en":
							set_opt(message.guild.id,"langue",message.content[22:24])

							if message.content[22:24] == "fr":
								lang = "``Français (fr)``"
								await message.channel.send("La langue choisie est désormais: " + lang)
							elif message.content[22:24] == "en":
									lang = "``English (en)``"
									await message.channel.send("the language is now: " + lang)

							else:
								await message.channel.send(opt_trad.lang_propos[langue])


        #
        #add
        #
				elif message.content.upper()[9:12] == "ADD":
					if message.content.upper()[13:18] == "ADMIN":
						id = message.content.upper()[19:37]
						add_opt(message.guild.id,"admin",id)
						if add_opt.already:
							await message.channel.send(opt_trad.alr_admin[lanu])
						else:
							await message.channel.send(opt_trad.add_id[langue].format(id))
							await message.channel.send(opt_trad.now_id[langue].format(add_opt.new))


        #
        #remove
        #

				elif message.content.upper()[9:12] == "DEL":
					if message.content.upper()[13:18] == "ADMIN":
						id = message.content.upper()[19:37]
						if message.content[19:37]:
							if id == str(message.guild.owner.id):
								await message.channel.send(opt_trad.id_is_admin[langue])
							else:
								del_opt(message.guild.id,"admin",id)
								if del_opt.already == "oui":
									await message.channel.send(opt_trad.no_id_admin[langue])
								elif del_opt.err == "non":
									await message.channel.send(opt.tard.del_id.format(id))
									await message.channel.send(opt.trad.now_id[langue].format(admin))
								else :
									await message.channel.send(opt_trad.err[langue])
									await print(del_opt.exce)
						else:
							await message.channel.send(opt_trad.need_ID[langue])

			elif message.content.lower().startswith(prefix + 'ping'):
				ping_time = time.monotonic()
				pinger = await message.channel.send(":ping_pong: **Pong !**")
				ping = "%.2f"%(1000* (time.monotonic() - ping_time))
				await pinger.edit(content=":ping_pong: **Pong !**\n `Ping:" + ping + "`")


			elif message.content.lower().startswith(prefix + "8ball"):
				async with message.channel.typing():
				      bal = random.choice(trad.ball[langue].split())
				      await asyncio.sleep(len(bal)/8)
				await message.channel.send(bal.replace("§"," "))

			elif "BONJOUR" in message.content.upper() or "HELLO" in message.content.upper() :
				await message.channel.send("Hey !")

			elif ("GG " or "GL ") in message.content.upper():
				await message.channel.send(":clap: :clap: :clap:")

			elif message.content.lower().startswith(prefix + "help"):
				if langue == "fr":
				   need = trad.emb_fr
				elif langue == "en":
				     need = trad.emb_en

				help = discord.Embed(title="Help",description=need[0],color=0x7851A9)
				help.add_field(name = need[1],value = need[2].format(prefix), inline=False)
				help.add_field(name = need[3],value = need[4].format(prefix), inline=False)
				help.add_field(name= need[5],value = need[6].format(prefix,prefix,prefix,prefix,prefix,prefix,prefix), inline=False)
				help.add_field(name= need[7],value = need[8].format(prefix), inline=False)
				help.set_footer(text = message.author.name,icon_url=message.author.avatar_url)
				await message.channel.send(embed=help)



			elif message.content.upper().startswith(prefix + "GIF"):
			    gif = random.choice(data.gifs)
			    await message.channel.send(gif)

			elif message.content.upper().startswith(prefix + "CALC"):
			    virg = random.randint(1,7)
			    x = random.randint(int(-99),int(9999))
			    if virg == 1:
			        y = random.randint(0,9999999)
			        x = str(x) + "," + str(y)

			    if langue == "fr":
			       phrase = random.choice(trad.calc_fr).format(x)
			    elif langue == "en":
			       phrase = random.choice(trad.calc_en).format(x)
			    await message.channel.send(phrase)


			elif message.content.lower().startswith(prefix + "news"):
			     await message.channel.send(trad.news[langue])


			elif message.content.lower().startswith(prefix + "info"):
			    info_mention_user = None
			    if langue == 'fr':
			       info = trad.info_fr
			    elif langue == "en":
			       info = trad.info_en

			    if message.mentions != []:
			       info_mention_user = message.mentions[0]
			    else:
			       info_mention_user = message.author
			    info_mention=discord.Embed(color=0x7851A9)
			    info_mention.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
			    info_mention.set_thumbnail(url=info_mention_user.avatar_url)
			    info_mention.add_field(name=info[0],value=info_mention_user, inline=False)
			    info_mention.add_field(name=info[1], value=info_mention_user.name + " / " + str(info_mention_user.id), inline=False)
			    info_mention.add_field(name=info[2], value=info_mention_user.joined_at, inline=False)
			    info_mention.add_field(name=info[3], value=info_mention_user.created_at, inline=False)
			    list_user_roles = []

			    r = 0
			    for x in info_mention_user.roles:
			       if r == 0:
			           list_user_roles.append(x.name)
			           r += 1
			       else:
			           list_user_roles.append("<@&{}>".format(x.id))

			    list_user_roles = str(list_user_roles).replace("'"," ")
			    list_user_roles = str(list_user_roles).replace("[","")
			    list_user_roles = str(list_user_roles).replace("]","")

			    info_mention.add_field(name=info[4], value=list_user_roles, inline=False)

			    info_mention.set_footer(text=message.author)

			    await message.channel.send(embed=info_mention)

			elif message.content.upper().startswith(prefix + "REACTS"):
			    mess = message.content.split()
			    try:
			       try :
                        #channel
			           channel = client.get_channel(int(mess[2]))
                        #message
			           message = await channel.history().get(id=int(mess[1]))
			           emojis = str(mess[3])
			       except:
			           channel = client.get_channel(int(mess[1]))
			           message = await channel.history().get(id=int(mess[2]))
			           emojis = str(mess[3])
			    except :
			        emojis = str(mess[1])
			    try:
			        await message.add_reaction(emojis)
			    except:
			        await message.channel.send(trad.emo[langue].format(emojis))



			elif message.content.upper().startswith(prefix + "REPORT"):
			    try:
			        repo = message.mentions
			        auth = message.author
			        len_repo = len(repo)
			        raison = message.content.split()[int(len_repo)+1:]

			        raison = str(raison)
			        raison = raison.replace("'"," ")
			        raison = raison.replace("[","")
			        raison = raison.replace("]","")
			        raison = raison.replace(",","")

			        if langue == "fr": repor = trad.repo_fr
			        elif langue == "en": repor = trad.repo_en
			        new_rep = ""
			        for i in repo:
			            new_rep += i.mention

			        report=discord.Embed(color=0x7851A9)
			        report.set_author(name="JuiceBox", icon_url="https://juicebot.github.io/assets/images/juicebox-112x112.png")
			        report.set_thumbnail(url=message.author.avatar_url)
			        report.add_field(name=repor[0],value=new_rep.replace(",",""), inline=False)
			        report.add_field(name=repor[1], value=auth.name + " / " + auth.mention, inline=False)
			        report.add_field(name=repor[2], value=raison, inline=False)
			        report.add_field(name="ID:", value=message.author.id, inline=False)
			        Find_Chan =  False
			        for channel in message.guild.channels:
			            if channel.name == 'report':

			                await channel.send(embed=report)
			                Find_Chan = True

			        if Find_Chan == False:
			            await message.channel.send(trad.NoFoudChanRepo[langue])

			    except Exception as e:
			        print(e)
			        await message.channel.send(trad.err_repo[langue].format(prefix))

			elif message.content.lower().startswith(prefix + "bin"):
			    to_bin = message.content[5:]
			    await message.channel.send(' '.join('{0:08b}'.format(ord(x), 'b') for x in to_bin))


			elif message.content.upper().startswith(prefix + "CONTACT"):
			    contact = message.content[9:]
			    ticket_chan = client.get_channel(653195902910988309)

			    ticket = discord.Embed(color=0x7851A9)
			    ticket.add_field(name="ticket de :",value=message.author.mention,inline=False)
			    ticket.add_field(name="Contenu ticket :",value=contact,inline=False)
			    ticket.set_author( name=message.author.name, icon_url=message.author.avatar_url)
			    ticket.set_footer(text="ID de l'utilisateur :" + str(message.author.id))
			    await ticket_chan.send(embed=ticket)
			    await message.channel.send(trad.ticket[langue])

			elif message.content.upper().startswith(prefix + "SUPPORT") or message.content.startswith("<@!528268989525131274>") or message.content.startswith("<@528268989525131274>"):
			    await message.channel.send(trad.help_1[langue])


			elif message.content.upper().startswith(prefix + "SERVER-INFO"):
			    prop = str(guild.owner.id)

			
			elif opt.premuim:
				pass
'''		
			    if message.content.lower().startswith(prefix + "set-status") and str(message.author.id) in str(admin):

			        no_com = message.content.replace("{}set-status ".format(prefix),"",1)

			        for_file = no_com

			        mess = str(no_com).split()

			        if mess[len(mess)-1].upper() in ("DND","ONLINE","IDLE"):
			            stat = mess[-1]
			            print(stat)
			            no_com = no_com.replace("{}".format(stat),"")
			            print(no_com)
			            del mess[-1]
			        else:
			            stat = "online"

			        if len(mess) >= 1:
			            await client.change_presence(activity=discord.Activity(name=str(no_com),type=discord.ActivityType.playing), status=str(stat))
			            pres = open("pres.txt","a")
			            pres.write(str(datetime.datetime.now()) + " - \"" + for_file + "\" - " + str(message.author.id) + " - " + str(message.author) + "\n")
			        else:
			            await message.channel.send(trad.req_arg[langue].format(prefix))'''



		except Exception as e:
		          print(e)
		          file = open("errors.txt","a")
		          file.write(str(e) + "\n")
		          await message.channel.send(trad.err[langue].format(str(e), str(message.content) ))

client.run(TOKEN)
