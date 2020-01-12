class trad():
    ball = {"fr":"oui non :person_shrugging_tone1: Je§ne§sais§pas Pourquois§tu§pose§la§question§? Sans§doutes Nan! Мен§кодексине§ката§жок§деп§ойлойм§! Nan§pourquois§?","en":"Absolutely§not§! Surely§! I§won't§awnser§this§question§. Of§course§not yes no :person_shrugging_tone1: nope I§don't§know Probably§... Of§course§! Yes§yes§and§yes§! I§think§yes. Nooooooooooooooooo§! Why§do§you§ask§me§this§question§? Мен§кодексине§ката§жок§деп§ойлойм§!"}





    emb_en = ('Here is the commands list :',"Server management commands:", "Here are the server mannagment commands :\n ``{}report @Naughty_User motive`` in a text channel for report him in #report","Options commands:","Send ``{}options`` in a channel for get all of options commands !",'Fun commands:','Here is fun commands: \n ``{}ping`` : Give you the ping of the bot \n ``{}say [text]``: Make say you\'r message, and delete it if you are admin. \n ``{}gif`` : Send a random GIF, if he is marked like "Spoiler", he could be offensive. \n ``{}info``: Send informations about a guild member.... or yourself ! \n ``{}8ball``: Answer your questions with his crystal ball,but he is sometimes very indecisive \n ``{}calc``: Allows you to calculate, large numbers! After that it’s a bit of a joke ... \n ``{} bin``: 01010100 01110010 01100001 01101110 01110011 01101100 01100001 01110100 01100101 00100000 01111001 01101111 01110101 01110010 00100000 01101101 01100101 01110011 01110011 01100001 01100111 01100101 01110011 00100000 01101001 01101110 01110100 01101111 00100000 01100010 01101001 01101110 01100001 01110010 01111001',"Premuims commands :","Here are premuims commands \n ``{}set-status [text] (type*)`` : Will change my status by the text! (* The type could be ``dnd``, ``idle``, ``online`` default)Be careful, all rich presence are **saved**!")






    emb_fr = ('Voici la liste des commandes :','Commandes de modération:','Voici la liste des commandes de modération :\n ``{}report @Méchant_Utilisateur Raison`` pour signialer l\'utilisateur dans #report',"Commandes d'options:","Envoyez ``{}options`` dans un channel pour obtenir toutes les commandes !",'Commandes fun:','Voici les commandes fun: \n ``{}ping`` vous donne le ping du bot  \n ``{}say [texte]``: Fait dire au bot votre texte et supprime votre message si vous êtes admin. \n ``{}gif``: Envoie un GIF aléatoire, s\'il est marqué comme spoiler il peut être offenssant. \n ``{}info``: Donne de nonbreuses informations à propos des membres du serveur... ou vous-même ! \n ``{}8ball``: Répond à vos questions après un temps de réflexion, pour sa boule de crystal. \n ``{}calc``:  Vous permet de calculer, de grands nombres ! Apres c\'est un peu buggé :/ \n ``{}bin``: 01010100 01110010 01100001 01100100 01110101 01101001 01110100 00100000 01110110 01101111 01110011 00100000 01101101 01100101 01110011 01110011 01100001 01100111 01100101 01110011 00100000 01100101 01101110 00100000 01100010 01101001 01101110 01100001 01101001 01110010 01100101',"Commandes Premiums :","Voicis les commandes premuims : \n ``{}set-status [texte] (type*)`` : Changera mon status avec le texte ! (* le type peut etre ``dnd`` : Ne pas deranger , ``idle`` : Inactif , ``online`` : en ligne , par default) Attention, ils sont tous **sauvegardé** !")


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


    repo_fr = ("Signalement de :","Signalé par:","Raison \:" ,"Signialé à:")
    repo_en = ("Reported by :","Reported user :","Reason \:","Reported at:")

    NoFoudChanRepo = {"fr":"Je n'ai pas pu trouver de channel nommé #report, envoie du signalement annulé !","en":"Could not find any channel named #report, report cancelled !"}

    err_repo = {"en":"An error occured! Check than you ping someone in you'r message, or put a reason ! \n Command : ``{}report [ping(s)] [reason]``","fr":"Une erreure est survenue ! Verifiez bien que vous avez mentioné des utilisateurs, ou mis une raison ! \n syntaxe : ``{}report [mention(s)] [raison]``"}
    err = {"en":"Sorry, an error occured: \n Error: `` {} `` \n Command: ``{}`` .","fr":"Désolé, une erreure est survenue ! \n Erreure : {} \n Commande : ``{}`` ."}

    ticket = {"fr":"Votre ticket a été envoyé avec succès!\nUn membre du staff vous demandera peut-etre en ami pour pouvoir vous envoyer un message! Verifiez vos demandes :wink:","en":"Your ticket has been sent successfully! \n A staff member may ask you as a friend to send you a message! Check your requests :wink:"}

    help_1 = {"fr":"Voici mon site: https://juicebot.github.io \net voici mon serveur discord : https://discordapp.com/invite/Abfvn9y ","en":"Hey, here is my website : (frensh only) https://juicebot.github.io \nand here is my discord server : https://discordapp.com/invite/Abfvn9y"}

    emo = {"fr":"Je n'ai pas réussi a ajouter la réaction ``{}`` ! Veuillez verifier l'emoji et reessayer. \n Il se peut que je n'ai pas les permissions pour ajouter cette reaction !","en":"I did not manage to add the reaction ``{}`` Please check the emoji and try again. \n I may not have the permissions to add this reaction!"}


    req_arg = {"fr":"Vous devez preciser un status! \n Exemple : ``{}set-status J'aime Juicy``","en":"You must precise a status! \n Exemple : ``{}set-status I love Juicy``"}
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
	'outtmpl': music_location+'{}[{}]-%(title)s-%(url)s.%(ext)s',
	'nocheckcertificate': True,
	'default_search': 'auto',
	'progress_hooks': [my_hook],
	'quiet': True,
	'no_warnings':True,
    'ignoreerrors':True,
	}

    outtmpl = music_location+'{}[{}]-%(title)s.%(ext)s'

    file_name = music_location+'{}[{}].webm'

    volume = 0.5

    cant_say = {"fr":"Vous n'avez pas le droit de dire ``{}`` :rage: !","en":"You can't say ``{}`` here !"}
class opt_trad():

    help = {'fr':"Choisisez : \n\
    **__get :__** ``prefix/admins/language/word`` \n\
    **__set :__** ``prefix/language [value]`` \n\
    **__add :__** ``admins/word [value]`` \n\
    **__del :__** ``admins [value]`` \n\
    **__reset :__** ``prefix/admins/language/word``",
    "en":
    "Make a choice : \n\
    **__get :__** ``prefix/admins/language/word`` \n\
    **__set :__** ``prefix/language [value]`` \n\
    **__add :__** ``admins/word [value]`` \n\
    **__del :__** ``admins/word [value]`` \n\
    **__reset :__** ``prefix/admins/language/word``"}


    need_ID = {"fr":"Veuillez precisez un id !","en":"Please specify an id!"}

    err = {"fr":"Une erreure est survenue","en":"An error occurred"}


    del_id = {"fr":"l'id ``{}`` à corectement été suprimé !","en":"The id {} was suscessfuly deleted"}

    add_id = {"fr":"l'id ``{}`` à corectement été ajouté !","en":"The id {} was suscessfuly added"}

    now_id = {'fr':"Voicis les ID des admins du serveur : ``{}``","en":"Here is server admin's ID : {}"}

    no_id_admin = {"fr":"Cet utilisateur n'est pas stocké en temps qu'admin !","en":"This user is not an admin !"}

    id_is_admin = {"fr":"Vous ne pouvez pas retirer les droit du propriétaire du serveur","en":"You cannot take away the owner's rights from the server"}

    alr_admin = {"fr":"Cet utilisateur est deja administrateur !","en":"This user is already administrator !"}

    admin_reset = {"fr":"Les IDs des admins sont désormais : ``{}``","en":"ID's admins are now : ``{}``"}


    lang_propos = {"fr":"Veuillez preciser une langue valide (Ex : ``fr``,``en``)","en":"Please sezlect a valid language (Ex : ``fr``,``en``)"}


    pref_propos = {"fr":"Veuillez preciser un carractère pour le prefix (Ex : ``/``,``>``,``!``)","en":"Please precise a prefix (Ex : ``/``,``>``,``!``)"}


    now_prefix = {"fr":"Le prefix est ``{}``","en":"The prefix is ``{}``"}

    now_word = {"fr":"Les mots bannis sont : `` {} ``","en":"Banneds words are : `` {} ``"}

    syn_err = {"fr":"Syntaxe : ``{}options {} [prefix/admins/langue]``","en":"Syntax: ``{}options {} [prefix / admins / language]``"}

    word_succès = {"fr":"``{}`` à été ajouté avec succès !","en":"``{}`` was successfully added !"}

    del_word_succès = {"fr":"``{}`` à été suprimé avec succès !","en":"``{}`` was successfully deleted !"}

    lang = {"fr":"La langue est {}","en":"The language is {}"}

music_tags = {"music_functs":"[Music] ","error":"[Error] "}

music_trad = \
    {"fr":
        {
        "play":
            {"not_switching":music_tags["music_functs"]+"Pas de problème je ne vais pas changer la musique actuelle.",
            "switching":music_tags["music_functs"]+"Pas de problème je vais changer la musique actuelle...",
            "switching_track":music_tags["music_functs"]+"Voulez-vous vraiment jouer cette musique `{}` ?",
            "searching":music_tags["music_functs"]+"Recherche de **{}** :mag_right:",
            "receiving_data":music_tags["music_functs"]+"Reception des données de **{}** :arrow_down:"},
        "pause":
            {"successfully":music_tags["music_functs"]+"Musique mise en pause.","failed":""},
        "resume":
            {"successfully":music_tags["music_functs"]+"Musique résumé.","failed":""},        
        "join":
            {"successfully":music_tags["music_functs"]+"Salon vocal rejoint avec succès. :sound:",
            "movement":music_tags["music_functs"]+"Déplacement vers votre salon vocal terminé avec succès.",
            "failed":music_tags["music_functs"]+"Impossible de se connecter..."},

        "global_failed":
            {"not_connected":music_tags["error"]+"Je ne suis pas connecté à un salon vocal.",
            "already_connected":music_tags["error"]+"Je suis déjà connecté à un salon vocal.",
            "not_playing":music_tags["error"]+"Je ne joue pas de musique actuellement.",
            "already_playing":music_tags["error"]+"Je joue déjà de la musique..."}
        },

    "en":
        {
        "play":
            {"not_switching":music_tags["music_functs"]+"All rights, i won't change the current track.",
            "switching":music_tags["music_functs"]+"All rights, changing song...",
            "switching_track":music_tags["music_functs"]+"Do you want to switch to this track `{}` ?",
            "searching":music_tags["music_functs"]+"Searching for **{}** :mag_right:",
            "receiving_data":music_tags["music_functs"]+"Receiving data from **{}** :arrow_down:"},
        "pause":
            {"successfully":music_tags["music_functs"]+"Music paused.","failed":""},
        "resume":
            {"successfully":music_tags["music_functs"]+"Music resumed.","failed":""},
        "join":
            {"successfully":music_tags["music_functs"]+"Vocal channel successfully joined. :sound:",
            "movement":music_tags["music_functs"]+"Successfully moved to your voice channel.",
            "failed":music_tags["music_functs"]+"Failed to join your voice channel..."},

        "global_failed":
            {"not_connected":music_tags["error"]+"I'm not conected to a voice channel.",
            "already_connected":music_tags["error"]+"I'm already connected to a voice channel.",
            "not_playing":music_tags["error"]+"I'm not playing music at the moment.",
            "already_playing":music_tags["error"]+"I'm already playing music..."}
        }
    }