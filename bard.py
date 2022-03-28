# Clé de domaine de l'URL qui redirige vers la base de données : cpludghqsjdhfg

from math import *

# Fonction qui retire à une chaine un caractère
def strremove(chaine, c):
	index = chaine.find(c)
	while index > -1:
		chaine = chaine[:index] + chaine[index+1:]
		index = chaine.find(c)
	return chaine
	
# Fonction qui retourne une matrice carrée nulle de taille n
def matriceNulle(n):
	return [[0 for i in range(n)] for j in range(n)]
	
# Fonction qui multiplie deux matrices carrées entre elles
def multiplieMatrices(A, B):
	retour = []
	for i in range(len(A)):
		retour.append([])
		for j in range(len(A)):
			somme = 0
			for k in range(len(A)):
				somme += A[i][k] * B[k][j]
			retour[i].append(somme)
	return retour

# Fonction qui calcule une transformation matricielle à un vecteur donné et la retourne
def transformation(A, x):
	retour = []
	for i in range(len(x)):
		somme = 0
		for j in range(len(x)):
			somme += A[i][j] * x[j]
		retour.append(somme)
	return retour














import discord
import datetime
import os
os.chdir("bdd")
url_local = "http://cpludghqsjdhfg.freeboxos.fr/bard/"

# Listes opérateurs (je m'ajoute :D )
operateurs = []
operateursNom = []
operateurs.append(280453752283201536)
operateursNom.append("Harrybreak")

'''
	CODE SOURCE DU BOT PRINCIPAL
	programmé par HarryBreak;
	
	<--- Variables temporaires --->
	$data			: pour un objet
	$information 	: pour un long message
	$contenu 		: pour une longue liste
	$nombre 		: pour une quantité
	$position 		: pour une position
	$date			: pour une date
	$index 			: pour une indexation de structure de données (comme une liste : i = index ; L[i])
	$id				: pour un identifiant (un nombre très grand ou une chaine de caractère contenant un nombre très grand ou une clef)
	$link			: pour un lien (fichier ou web)
	$a et $b 		: respectivement pour un point de départ et un point de fin
	$ligne 			: pour une position en ligne dans un fichier
	$liste			: pour une liste (tableau de dimension 1)
	$matrice		: pour une liste de listes (tableau de dimension 2)
	
	<--- Variables intemporaires --->
	$operateurs		: id  des utilisateurs possédant les hauts privilèges
	$operateursNom	: nom des utilisateurs possédant les hauts privilèges
	$utilisateurs	: dictionnaire {id : ["nom", Application()]} qui répertorie les utilisateurs du jeu
	$histoires		: dictionnaire {id : [id_auteur, Histoire()]} qui répertorie les histoires du jeu
	$embeds			: dictionnaire {id : discord.Embed()} où l'id ici est un id de fenêtre
	$fenetres		: dictionnaire {id : Fenetre()} où l'id ici est un id de fenêtre
	$url_local		: url locale (string)
	
	@TODO LIST :
	 + Établir les fonctions de calculs matriciels sur les graphes des histoires
'''

# La classe d'une boîte de dialogue
# Cinq types de dialogue sont possibles : passe (0), choix (1), fin, chrono ou un type non reconnu qui désignera une boite de dialogue puit/fantôme
# Dans le cas "fin", il faut indiquer si c'est une bonne ou une mauvaise fin
# Dans le cas "chrono", il faut indiquer le temps mis au bot pour laisser le message affiché avant de passer au suivant.
# Dans le cas "passe", il faut indiquer le texte, car si on le laisse vide, la boîte sera considérée comme fantôme
class Dialogue:
	def __init__(self, type = "", texte = "", lienImage = ""):
		self.texte = texte
		# La variable data a un type qui varie en fonction du type de la boîte de la dialogue
		if type == "choix":
			# S'il s'agit d'une boîte à choix multiples, data est un dictionnaire
			# La structure de ce dictionnaire sera la suivante :
			# {id : text} avec id qui correspond à un id d'émoji (-1 -> 12)
			# Il y a toujours l'ID -1 connecté à la chaîne vide
			self.data = {-1 : ""}
		elif type == "chrono":
			# S'il s'agit d'une boîte de dialogue chronométrée, data est un temps en secondes
			self.data = 10 # secondes par défaut et maximum autorisé !
		elif type == "fin":
			# S'il s'agit d'une boîte de fin, data est un booléen indiquant si le joueur a perdu ou gagné
			self.data = True # bonne fin par défaut
		else:
			# S'il s'agit d'une boîte de passage ou d'une boîte fantôme, data est de type NoneType!
			self.data = None
		# On paramètre la variable de l'image avec les méthodes de la classe
		self.lienImage = lienImage

	def type(self):
		if isinstance(self.data, dict):
			return "choix"
		elif isinstance(self.data, int):
			return "chrono"
		elif isinstance(self.data, bool):
			return "fin"
		elif len(self.texte) > 0:
			return "passe"
		else:
			return ""

	def estFantome(self):
		if not(self.type() in ["passe", "choix", "fin", "chrono"]):
			return True
		elif self.type() == "choix" and len(self.data) < 2:
			return True
		else:
			return False
			
	def setChoix(self, liste):
		if self.type() == "choix":
			if len(liste) < 2:
				raise Exception("List too small !")
			else:
				for i in liste:
					if not(isinstance(i, tuple)):
						raise Exception("Wrong type of element in list !")
					elif not(isinstance(i[0])) or (not(isinstance(i[1], str)) or not(isinstance(i[1], unicode))) or i[0] < -1:
						raise Exception("Wrong element in list !")
				self.data = liste
		else:
			raise Exception("Wrong dialogue box to do this !")
			
	def ajouterChoix(self, id, texte):
		if self.type() == "choix" and isinstance(i, int) and i > -2 and (isinstance(texte, str) or isinstance(texte, unicode)):
			self.data.append((id, texte))
		else:
			raise Exception("Error while adding new option !")

	def __str__(self):
		retour = self.texte
		if self.type() == "choix":
			retour += "\n"
			for i in self.data:
				retour += str(i[0]) + ") " + i[1] + "\n"
			retour = retour[:-1]
		return retour
		
		
class Histoire:
	def __init__(self, titre, auteur, lienImage = ""):
		self.titre    	= titre
		self.auteur 	= auteur
		self.lienImage	= lienImage
		self.position	= 0
		# Liste des boîtes de dialogue de l'histoire.
		self.dialogues  = []
		# self.chemins est le graphe théorique (modélisé par une matrice) fléché et pondéré des chemins possibles entre les dialogues
		# Le poids de chaque chemin correspondant au numéro de choix qui ira de 1 à 13 !
		# Il y a donc 13 choix possibles, pour convertir à l'émoji correspondant on soustrait donc par 1
		self.chemins	= [] # Matrice carrée modélisant un graphe
		
	def __int__(self):
		return self.position
		
	# Gérer la modification d'une matrice de graphe en temps voulu !
	# data est le dialogue, liste est la liste des numéros de dialogues connectés.
	# L'ordre des numéros de dialogue dans la liste est l'ordre de choix !
	# liste est un entier naturel, id de dialogue si dialogue.type() != "choix" !
	def ajouterDialogue(self, data, liste):
		if isinstance(data, Dialogue):
			self.dialogues.append(Dialogue)
			if data.type() == "choix":
				# On construit le vecteur chemin du graphe à partir de la liste des dialogues connectés
				# Le FOR parcourt tous les dialogues déjà dans l'histoire, on aura donc len(vecteur) = len(self.dialogue)
				vecteur = [int(i in liste) for i in range(len(self.dialogues))]
				# Et on rajoute les poids. Si le numéro de dialogue n'est pas trouvable dans la liste, on remplace par 0
				for i in range(len(vecteur)):
					if vecteur[i] == 1:
						try:
							vecteur[i] *= (liste.index(i) + 1)
						except ValueError:
							vecteur[i] = 0
				# On rajoute enfin la colonne et la ligne nécessaire dans la matrice de l'histoire
				self.chemins.append(vecteur)
				for i in range(len(self.chemins)):
					if i < len(vecteur):
						self.chemins[i].append(vecteur[i])
					else:
						self.chemins[i].append(0)
			else:
				# On construit de même le vecteur chemin du graphe
				vecteur = [int(i == liste) for i in range(len(self.dialogus))]
				# Et on rajoute la colonne et la ligne nécessaire dans la matrice de l'histoire
				self.chemins.append(vecteur)
				for i in range(len(self.chemins)):
					if i < len(vecteur):
						self.chemins[i].append(vecteur[i])
					else:
						self.chemins[i].append(0)
		else:
			raise Exception("Wrong data type entered !")
	
	def retirerDialogue(self, n):
		self.dialogues = self.dialogues[:n] + self.dialogues[n+1:]
		self.chemins = self.chemins[:n] + self.chemins[n+1:]
		for i in range(len(self.chemins)):
			self.chemins[i] = self.chemins[i][:n] + self.chemins[i][n+1:]
		
	def recommencerLecture(self):
		self.position = 0
		
	def lectureFinie(self):
		return self.position >= len(self.dialogues) or self.dialogues[position].type() == "fin"

	# Fonction qui fait avancer l'histoire selon le choix de l'utilisateur ou son entrée et retourne l'embed de la fenêtre de dialogue suivante
	def continuerLecture(self, id_reaction):
		# On commence par récupérer les chemins possibles à partir de la position actuelle
		vecteur = self.chemins[position]
		# Puis, on vérifie si id_reaction + 1 est bien dedans
		# Si ce n'est pas le cas, on retourne l'embed vide.
		# Le test de l'embed sera vérifié en aval pour prévoir une mauvaise réaction de joueur.
		# Sinon, on récupère la nouvelle position de l'histoire
		try:
			position = vecteur.index(id_reaction + 1)
		except ValueError:
			return discord.Embed()
		# On prépare ensuite l'embed
		retour = discord.Embed(title = self.titre, description = str(self.dialogues[position]), type = rich)
		retour.set_author(name = self.auteur)
		if len(self.dialogues[position].lienImage) > 0:
			retour.set_image(url = url_local + self.auteur + "/" + self.titre + "/" + self.dialogues[position].lienImage)
		if len(self.lienImage) > 0:
			retour.set_thumbnail(url = url_local + auteur + "/" + self.lienImage)
		else:
			retour.set_thumbnail(url = url_local + "logo.png")
		retour.set_footer(text = "Ici seront bientôt affichées la date de création et la date de dernière mise à jour de l'histoire !")
		# Et on le retourne
		return retour
		
'''
	CRÉATION DES EMBEDS DE L'APPLICATION
'''
# L'EMBED D'ERREUR
embedError = discord.Embed(title = "Une erreur inconnue est survenue !", description = "Tapez ,start pour revenir à l'écran titre", type = "rich")
# LES AUTRES EMBEDS
embeds = dict()
# La fenêtre de démarrage
embeds[0] = discord.Embed(title = "Bienvenue chez Bard !", description = "Programmé par HarryBreak", type = "rich")
embeds[0].set_author(name = "Fenêtre titre", icon_url = url_local + "logo.png")
embeds[0].set_image(url = url_local + "logo.png")
embeds[0].set_thumbnail(url = url_local + "logo.png")
embeds[0].set_footer(text = "Choix disponibles :\n0) Parcourir les histoires tendances\n1) Rechercher une histoire\n2) Éditeur d'histoire")
print("Taille du premier embed : " + str(len(embeds[0])))
# La fenêtre de parcours des tendances
embeds[1] = discord.Embed(title = "Page 1 sur 5", description = "**HarryBreak** : Man VS Wild\n**Aliel** : L'entrée au paradis", type = "rich")
embeds[1].set_author(name = "Histoires tendances", icon_url = url_local + "logo.png")
# La fenêtre de recherche d'histoire
embeds[2] = discord.Embed(title = "Tapez les mots-clé de votre recherche dans le formulaire de texte.", description = "*Ce formulaire n'est jamais à utiliser sauf dans quelques cas exceptionnels où il vous le sera demandé, comme ici !*", type = "rich")
embeds[2].set_author(name = "Rechercher une histoire", icon_url = url_local + "logo.png")
# La fenêtre de bienvenue d'édition
embeds[3] = discord.Embed(title = "Entrez le nom de votre nouvelle histoire dans le formulaire de texte.", description = "L'édition des histoires s'effectue avec le bot Muse ou l'application dédiée à cet usage.\n*Ce formulaire n'est jamais à utiliser sauf dans quelques cas exceptionnels où il vous le sera demandé, comme ici !*", type = "rich")
embeds[3].set_author(name = "Mode édition d'histoires", icon_url = url_local + "logo.png")
'''
	FIN DE LA CRÉATION DES EMBEDS
'''

# Les listes des chemins de chaque fenêtre représentent ce qu'on peut faire
# Si on clique sur l'émoji [2] on va à la fenêtre d'Id chemin[2]
# Si pour i € [|-1;12|], chemin[i] = -1, la réaction n'est pas affichée et son ajout ne conduit à rien :)
# Par défault, on crée la fenêtre d'écran titre
class Fenetre:
	def __init__(self, id = 0, chemin = [1, 2, 3], embed = embeds[0]):
		self.id			= id
		self.chemin 	= chemin
		self.embed  	= embed
		self.waitEntry	= False
		self.entry		= ""
		
	def drawable(self):
		try:
			return len(self.embed) <= 6000 and len(self.embed) > 0 and self.id > -1
		except TypeError:
			return False
			
	def onWaitEntry(self):
		self.waitEntry = True
'''
	CRÉATION DES FENETRES DE L'APPLICATION
'''
fenetres = {}
# Les fenêtres de lecture(-1) et d'édition(-2) d'une histoire
# Édition
fenetres[-2] = Fenetre()
fenetres[-2].id = -2
fenetres[-2].chemin = []
fenetres[-2].embed = discord.Embed()
# Lecture
fenetres[-1] = Fenetre()
fenetres[-1].id = -1
fenetres[-1].chemin = []
fenetres[-1].embed = discord.Embed()
# La fenêtre de démarrage
fenetres[0] = Fenetre()
# La fenêtre de parcours des tendances
id = 1
fenetres[id] = Fenetre()
fenetres[id].id = id
fenetres[id].chemin = [0]
fenetres[id].embed = embeds[id]
# La fenêtre de recherche d'histoire
id = 2
fenetres[id] = Fenetre()
fenetres[id].id = id
fenetres[id].chemin = [0]
fenetres[id].embed = embeds[id]
# La fenêtre de bienvenue d'édition
id = 3
fenetres[id] = Fenetre()
fenetres[id].id = id
fenetres[id].chemin = [0]
fenetres[id].embed = embeds[id]
'''
	FIN DE LA CRÉATION DES FENETRES
'''
class Application:
	def __init__(self):
		self.fenetre_act = Fenetre()
		self.histoire_act = None
		self.on_error = False
		self.on_editing = False
		self.on_reading = False
		
	async def draw(self, user):
		if self.fenetre_act.drawable():
			data = await user.send(embed = embeds[self.fenetre_act.id])
			# Ajout des réactions nécessaires
			if len(self.fenetre_act.chemin) > 0:
				await data.add_reaction(str('0\uFE0F\u20E3'))
				if len(self.fenetre_act.chemin) > 1:
					await data.add_reaction(str('1\uFE0F\u20E3'))
					if len(self.fenetre_act.chemin) > 2:
						await data.add_reaction(str('2\uFE0F\u20E3'))
						if len(self.fenetre_act.chemin) > 3:
							await data.add_reaction(str('3\uFE0F\u20E3'))
							if len(self.fenetre_act.chemin) > 4:
								await data.add_reaction(str('4\uFE0F\u20E3'))
								if len(self.fenetre_act.chemin) > 5:
									await data.add_reaction(str('5\uFE0F\u20E3'))
									if len(self.fenetre_act.chemin) > 6:
										await data.add_reaction(str('6\uFE0F\u20E3'))
										if len(self.fenetre_act.chemin) > 7:
											await data.add_reaction(str('7\uFE0F\u20E3'))
											if len(self.fenetre_act.chemin) > 8:
												await data.add_reaction(str('8\uFE0F\u20E3'))
												if len(self.fenetre_act.chemin) > 9:
													await data.add_reaction(str('9\uFE0F\u20E3'))
													if len(self.fenetre_act.chemin) > 10:
														await data.add_reaction(str('\u21A9'))
														if len(self.fenetre_act.chemin) > 11:
															await data.add_reaction(str('\u23EA'))
															if len(self.fenetre_act.chemin) > 12:
																await data.add_reaction(str('\u23E9'))
		else:
			await user.send(embed = embedError)
			self.on_error = True
			
	async def cls(self, user):
		compteur = 0
		async for i in user.history():
			if compteur > 2:
				break
			else:
				try:
					await i.delete()
					compteur += 1
				except discord.errors.Forbidden:
					pass
				
	async def bindReaction(self, user, n):
		# La réaction est-elle utilisable? Sinon on ne fait rien c:
		if n < len(self.fenetre_act.chemin) and self.fenetre_act.chemin[n] > -1:
			index = self.fenetre_act.chemin[n]
			self.fenetre_act = fenetres[index]
			await self.cls(user)
			await self.draw(user)
	
	async def bindEntry(self, user, s):
		# Attendions-nous une entrée? Sinon on ne fait rien c:
		if self.fenetre_act.waitEntry:
			await self.cls(user)
			await user.send(embed = embedError)
			self.on_error = True
		
# Dictionnaire des utilisateurs (je m'ajoute :D)
# Syntaxe : {id : ["nom", Application()]}
utilisateurs = {280453752283201536 : ["HarryBreak", Application()]}

async def action(entier, user):
	if user.id in utilisateurs:
		utilisateurs[user.id][0] = user.name
		await utilisateurs[user.id][1].bindReaction(user, entier)
		
async def entree(message, user):
	if id in utilisateurs:
		utilisateurs[id][0] = user.name
		await utilisateurs[id][1].bindEntry(user, message)

# Voici la fonction qui va récupérer les données de la mémoire morte, elle est très importante.
# Premièrement, il faut récolter l'id et le pseudonyme des utilisateurs qui ont démarré une session de jeu avec 'start.
# Ensuite, il y a un dossier pour chaque utilisateur connu qui contient des sous-dossiers correspondant à leur création et deux fichiers, state.txt et saves.txt
# Le premier enregistre les statistiques de l'utilisateur : où il est dans l'application, et si il est dans une histoire, quelles sont ses statistiques actuelles dans le jeu.
# Le second enregistre les noms des sous-dossiers correspondant aux oeuvres de l'utilisateur.
# Il faut une variable pour le token
token = ""
def loadbdd():
	# Pour le token
	with open('token.txt', 'r') as file:
		global token
		for line in file:
			token = line
			break
	return True

def savebdd():
	return True

print("==========================================================")
print("Lecture des données dans la base de données ...")
loadbdd()

print("==========================================================")
print("Configuration du bot...")
# Configuration du reboot du bot
instance_intents = discord.Intents.default()
instance_intents.members = True

# Reboot du bot
client = discord.Client(intents=instance_intents)

@client.event
async def on_ready():
	data = discord.Game("Envoyez moi \",start\" pour me (re)démarrer !")
	await client.change_presence(activity = data)
	print("==========================================================")
	print("Le bot est connecté !")
	
@client.event
async def on_reaction_add(reaction, user):
	if user != client.user and isinstance(user, discord.User):
		if reaction.emoji == str('0\uFE0F\u20E3'):
			try:
				await action(0, user)
			except IndexError:
				print("Indexation erreur ligne 392")
		elif reaction.emoji == str('1\uFE0F\u20E3'):
			try:
				await action(1, user)
			except IndexError:
				pass
		elif reaction.emoji == str('2\uFE0F\u20E3'):
			try:
				await action(2, user)
			except IndexError:
				pass
		elif reaction.emoji == str('3\uFE0F\u20E3'):
			try:
				await action(3, user)
			except IndexError:
				pass
		elif reaction.emoji == str('4\uFE0F\u20E3'):
			try:
				await action(4, user)
			except IndexError:
				pass
		elif reaction.emoji == str('5\uFE0F\u20E3'):
			try:
				await action(5, user)
			except IndexError:
				pass
		elif reaction.emoji == str('6\uFE0F\u20E3'):
			try:
				await action(6, user)
			except IndexError:
				pass
		elif reaction.emoji == str('7\uFE0F\u20E3'):
			try:
				await action(7, user)
			except IndexError:
				pass
		elif reaction.emoji == str('8\uFE0F\u20E3'):
			try:
				await action(8, user)
			except IndexError:
				pass
		elif reaction.emoji == str('9\uFE0F\u20E3'):
			try:
				await action(9, user)
			except IndexError:
				pass
		elif reaction.emoji == str('\u21A9'):
			try:
				await action(10, user)
			except IndexError:
				pass
		elif reaction.emoji == str('\u23EA'):
			try:
				await action(11, user)
			except IndexError:
				pass
		elif reaction.emoji == str('\u23E9'):
			try:
				action(12, user)
			except IndexError:
				pass

@client.event
async def on_message(message):
	#print(f"[{time.strftime('%X')}]",message.author,":",message.content)
	'''
	COMMAND SECTION
	'''
	### AVANT TOUTE CHOSE ON VÉRIFIE SI LE MESSAGE PROVIENT BIEN D'UN SALON PRIVÉ (DMChannel --> obj User)
	if isinstance(message.author, discord.User):
		## START COMMAND
		if message.content.split()[0] == ",start":
			if message.author.id in utilisateurs:
				utilisateurs[message.author.id][0] = message.author.name
				utilisateurs[message.author.id][1].fenetre_act = Fenetre()
				utilisateurs[message.author.id][1].on_error = False
				utilisateurs[message.author.id][1].histoire_act = None
			else:
				utilisateurs[message.author.id] = [message.author.name, Application()]
			await utilisateurs[message.author.id][1].cls(message.author)
			await utilisateurs[message.author.id][1].draw(message.author)
		## SAVE COMMAND (OPÉRATION QUI NÉCESSITE D'ÊTRE OPÉRATEUR)
		elif message.content.split()[0] == ",save":
			if message.author.id in operateurs:
				if savebdd():
					await message.author.send("Base de donnée sauvegardée !")
				else:
					await message.author.send("**Echec de la sauvegarde !**")
		## UPGRADE COMMAND (OPÉRATION QUI NÉCESSITE D'ÊTRE OPÉRATEUR)
		elif message.content.split()[0] == ",upg":
			if message.author.id in operateurs:
				contenu = message.content.split()
				if len(contenu) == 1 or (len(contenu) == 2 and contenu[1] == "help"):
					information = "Voici la liste des opérateurs:\n"
					for i in operateursNom:
						information += "+ " + str(i) + "\n"
					information += "Pour augmenter des utilisateurs, suivez cette commande de leur @pseudo."
					await message.channel.send(information)
				elif len(contenu) > 1 and len(message.mentions) == 0:
					await message.channel.send("**Erreur d'identification** ! Impossible d'augmenter les utilisateurs indiqués !")
				else:
					information = "Les utilisateurs suivants sont dorénavant des opérateurs :\n"
					for i in message.mentions:
						if not(i.id in operateurs):
							operateurs.append(i.id)
						if not(i.name in operateursNom):
							operateursNom.append(i.name)
							information += "+ " + i.name + "\n"
					await message.channel.send(information)
		## DOWNGRADE COMMAND (OPÉRATION QUI NÉCESSITE D'ÊTRE OPÉRATEUR)
		elif message.content.split()[0] == ",dwng":
			if message.author.id in operateurs:
				contenu = message.content.split()
				if len(contenu) == 1 or (len(contenu) == 2 and contenu[1] == "help"):
					await message.channel.send("Pour retirer les privilèges d'opérateur de plusieurs utilisateurs, suivez cette commande de leur @pseudo")
				elif len(contenu) > 1 and len(message.mentions) == 0:
					await message.channel.send("**Erreur d'identification** ! Impossible d'identifier les utilisateurs indiqués !")
				else:
					information = "Les utilisateurs suivants ne jouissent dorénavant plus des privilèges d'opérateur :\n"
					for i in message.mentions:
						try:
							operateurs.remove(i.id)
							operateursNom.remove(i.name)
						except ValueError:
							information += "+ " + i.name + "  *(était déjà dépourvu des privilèges)*" + "\n"
						else:
							information += "+ " + i.name + "\n"
					information += "Pour leur redonner accès aux fonctions d'opérateur, utilisez la commande ``&upg``."
					await message.channel.send(information)
		## GLOBAL DEL COMMAND (OPÉRATION QUI NÉCESSITE D'ÊTRE OPÉRATEUR)
		elif message.content.split()[0] == ",del":
			if message.author.id in operateurs:
				async for i in message.author.history():
					try:
						await i.delete()
					except discord.errors.Forbidden:
						pass
		## KILL COMMAND (OPÉRATION QUI NÉCESSITE D'ÊTRE OPÉRATEUR)
		elif message.content.split()[0] == ",kill":
			if message.author.id in operateurs:
				await message.channel.send("**Quelqu'un m'a tué, je vais me déconnecter....**")
				await client.close()
		## UNE ENTRÉE UTILISATEUR (S'il ne s'agît pas d'une commande)
		else:
			await entree(message.content, message.author)
	
client.run(token)
	

print("==========================================================")
print("Sauvegarde de la base de données en cours ...")
savebdd()
print("Sauvegarde terminée avec succès !")
print("==========================================================")
print("Le bot a bien été déconnecté !")