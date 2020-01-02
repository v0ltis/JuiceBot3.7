import json,os

#
#DEF del_opt
#

def del_opt(serv, option, new):
	param = open(str(serv) + "/option.txt","r")
	param = param.read()
	param = (json.loads(param) )

	if option == "bw":
		bw = open(str(serv) + "/bw.txt","r")
		bw = bw.read()
		new = new.replace(" ","_")
		new += " "
		nFile = bw.replace(new,"")
		bw = open(str(serv) + "/bw.txt","w")
		bw.write(nFile)
		del_opt.good = True

	#del opt
	elif not new in param[option]:
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
	if option == "bw":
		bw = open(str(serv) + "/bw.txt","a")
		new = new.replace(" ","_")
		new += " "
		bw.write(new)
		add_opt.good = True


	elif new in param[option]:
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


	if option == "bw":
		file = open(str(serv) + "/bw.txt","w")
		file.write("")


	else:
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

	#ouvre les paramètres
		param = open(str(serv) + "/option.txt","r")
		ban_w = open(str(serv) + "/bw.txt","r")
		param = param.read()
		ban_w = ban_w.read()
		param = (json.loads(param) )

	except FileNotFoundError:
		#crée le fichier si il n'existe pas
		os.makedirs(str(serv))
		param = open(str(serv) + "/option.txt","a")
		param.write('{"langue":"en","admin":"' + owner + '","prefix":"/"}')
		ban_w = open(str(serv) + "/bw.txt","a")
		#ouvre les paramètres
		param = open(str(serv) + "/option.txt","r")
		ban_w = open(str(serv) + "/bw.txt","a")
		param = param.read()
		ban_w = ban_w.read()
		param = (json.loads(param) )

	ban_w = ban_w.split()
	opt.bw = [w.replace('_', ' ') for w in ban_w]

	opt.admin = str(param["admin"])

	opt.prefix = str(param["prefix"])

	opt.langue = str(param["langue"])

	try:
		prem = open(str(serv) + "/premuim.txt","r")
		opt.premuim = prem.read()

	except:
		opt.premuim = False
