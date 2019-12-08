class trad():
    ball = {"fr":"oui non :person_shrugging_tone1: Je§ne§sais§pas Pourquois§tu§pose§la§question§? Sans§doutes Nan! Мен§кодексине§ката§жок§деп§ойлойм§! Nan§pourquois§?","en":"Absolutely§not§! Surely§! I§won't§awnser§this§question§. Of§course§not yes no :person_shrugging_tone1: nope I§don't§know Probably§... Of§course§! Yes§yes§and§yes§! I§think§yes. Nooooooooooooooooo§! Why§do§you§ask§me§this§question§? Мен§кодексине§ката§жок§деп§ойлойм§!"}





    emb_en = ('Here is the commands list :',"Server management commands:", "Here are the server mannagment commands :\n ``{}report @Naughty_User motive`` in a text channel for report him in #report","Options commands:","Send ``{}options`` in a channel for get all of options commands !",'Fun commands:','Here is fun commands: \n ``{}say [text]``: Make say you\'r message, and delete it if you are admin. \n ``{}gif`` : Send a random GIF, if he is marked like "Spoiler", he could be offensive. \n ``{}memeaudio``: Play a random audio-meme in a vocal channel. Only in frensh \n ``{}info``:Send informations about a guild member.... or yourself ! \n ``{}8ball`` : Answer your questions with his crystal ball,but he is sometimes very indecisive')






    emb_fr = ('Voici la liste des commandes :','Commandes de modération:','Voici la liste des commandes de modération :\n ``{}report @Méchant_Utilisateur Raison`` pour signialer l\'utilisateur dans #report',"Commandes d'options:","Envoyez ``{}options`` dans un channel pour obtenir toutes les commandes !",'Commandes fun:','Voici les commandes fun: \n ``{}say [texte]`` Fait dire au bot votre texte et supprime votre message si vous êtes admin. \n ``{}gif`` : Envoie un GIF aléatoire, s\'il est marqué comme spoiler il peut être offenssant. \n ``{}memeaudio``: Joue un meme audio aléatoire dans un salon vocal \n ``{}info`` :Donne de nonbreuses informations à propos des membres du serveur... ou vous-même ! \n ``{}8ball`` : Répond à vos questions après un temps de réflexion, pour sa boule de crystal')


    calc_en = ["That makes almost {}",
                "I would say {}",
                "{} normally",
                "Error System",
                "It's equal to {}",
        	"Aproximately {} !",
                "it's exactly {}"
        	]
    calc_fr = ["Ça fais {} à peu près",
                "Je dirai {}",
                "{} normalement",
                "Error System",
                "C'est égal à {}",
                "Aproximativement {} !",
                "C'est {} pile !"]



    news = {'fr':'Nouveautées : \n __Options:__ Choisisez desormais votre prefix, admins, langue ...','\
                en':'News : \n __Options:__ Choice now you\'r prefix, admins or language !'}


    info_en = ("Here is info about :","Name/ID","On this server since:","Account creation date:","With roles:")

    info_fr = ("Voici les infos de :","Pseudo/ID","Sur ce serveur depuis","Datte de creation du compte","Avec les roles:")


class data():
    gifs = ["https://giphy.com/gifs/AuIvUrZpzBl04",
    			"https://giphy.com/gifs/hello-hey-big-brother-l0MYBbEvqqi1kfuyA",
    			"https://giphy.com/gifs/trump-donald-eclipse-xUNen16DFqlM6v6DEQ",
    			"https://tenor.com/view/ok-okay-gif-5307535",
    			"https://gph.is/2iUaL8y",
    			"https://gph.is/19aLnvI",
    			"https://gph.is/2fiQFj1",
    			"https://gph.is/1rr0eCj",
    			"https://media.giphy.com/media/joPQLwo2kbXe8/giphy.gif",
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
    			"https://thumbs.gfycat.com/NaiveMatureArmedcrab-small.gif",
                '|| https://media.giphy.com/media/QGzPdYCcBbbZm/giphy.gif ||',
                '|| https://media.giphy.com/media/w1XrYq5PsCbyE/giphy.gif ||']


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

    volume = 4
