#coding utf-8
#import os
import sys
#os.system("shutdown -r")
#Liste de tous les tokens du code
listeTokens = []
#chaine de caracteres du code assembleur produit
chaineTexte = ""
index=0
#compteur pour les labels du code assembleur
label=0
#compteur de slots utilises par le programme assembleur
NbSlots=0
#pile pour la portee lexicale (Analyse Semantique)
pile=[]
#pile pour les labels entourant les boucles
pileBoucles=[]

#Table des operateurs et de leurs priorites, et du type de noeud associe
OP = {}
OP['addition', 'prioG'] = 40
OP['addition', 'prioD'] = 41
OP['addition', 'typeNoeud'] = "Nd_addition"
OP['soustraction', 'prioG'] = 40
OP['soustraction', 'prioD'] = 41
OP['soustraction', 'typeNoeud'] = "Nd_soustraction"
OP['multiplication', 'prioG'] = 50
OP['multiplication', 'prioD'] = 51
OP['multiplication', 'typeNoeud'] = "Nd_multiplication"
OP['diviseur', 'prioG'] = 50
OP['diviseur', 'prioD'] = 51
OP['diviseur', 'typeNoeud'] = "Nd_diviseur"
OP['modulo', 'prioG'] = 50
OP['modulo', 'prioD'] = 51
OP['modulo', 'typeNoeud'] = "Nd_modulo"
OP['puissance', 'prioG'] = 60
OP['puissance', 'prioD'] = 60
OP['puissance', 'typeNoeud'] = "Nd_puissance"
OP['inf', 'prioG'] = 30
OP['inf', 'prioD'] = 31
OP['inf', 'typeNoeud'] = "Nd_inf"
OP['sup', 'prioG'] = 30
OP['sup', 'prioD'] = 31
OP['sup', 'typeNoeud'] = "Nd_sup"
OP['infEgal', 'prioG'] = 30
OP['infEgal', 'prioD'] = 31
OP['infEgal', 'typeNoeud'] = "Nd_infEgal"
OP['supEgal', 'prioG'] = 30
OP['supEgal', 'prioD'] = 31
OP['supEgal', 'typeNoeud'] = "Nd_supEgal"
OP['egalEgal', 'prioG'] = 30
OP['egalEgal', 'prioD'] = 31
OP['egalEgal', 'typeNoeud'] = "Nd_egalEgal"
OP['different', 'prioG'] = 30
OP['different', 'prioD'] = 31
OP['different', 'typeNoeud'] = "Nd_different"
OP['et', 'prioG'] = 20
OP['et', 'prioD'] = 21
OP['et', 'typeNoeud'] = "Nd_et"
OP['ou', 'prioG'] = 10
OP['ou', 'prioD'] = 11
OP['ou', 'typeNoeud'] = "Nd_ou"
OP['egal', 'prioG'] = 5
OP['egal', 'prioD'] = 5
OP['egal', 'typeNoeud'] = "Nd_affectation"

########################################################################
#        OBJETS ANALYSE LEXICALE
########################################################################

class Token:
	def __init__(self):
		self.Type = None            #Type de Token
		self.ValeurChaine = None		#Valeur chainee : pour tous les tokens sauf les constantes
		self.ValeurEntiere = None		#Pour stocker la valeur des constantes
		self.NbLigne = None					#Ligne a laquelle le token a ete repere

	def afficher(self):
		print "Type : ", self.Type, "\nValeurChaine : ", self.ValeurChaine, "\nValeurEntiere : ", self.ValeurEntiere, "\nNbLigne : ", self.NbLigne


########################################################################
#        OBJETS ANALYSE SYNTAXIQUE
########################################################################

class Arbre:
  def __init__(self):
    self.Racine = None

class Noeud:
  def __init__(self):
    self.Type = None						#Type du noeud
    self.Enfants = []						#Liste de ses enfants
    self.NbLigne = None					#Ligne a laquelle le token impliquant le noeud a ete repere
    self.ValeurEntiere = None		#Pour les noeuds constantes Nd_const
    self.Identifiant = None			#Pour les noeuds comportant une variable, on stocke son nom ici
    self.Slot = None						#Pour les noeuds comportant une variable, on stocke son emplacement memoire


########################################################################
#        OBJETS ANALYSE SEMANTIQUE
########################################################################

class Symbole:
	def __init__(self):
		self.IdentifiantS=None			#Identifiant du Symbole (nom de la variable)
		self.TypeS=None							#Type du Symbole ("variable" ou "fonction")
		self.SlotS=None							#Emplacement memoire du Symbole (stockage de la valeur de la variable)


########################################################################
#        FONCTIONS POUR ANALYSE LEXICALE
########################################################################


def analyseLexicale(chaine):
	ligne = 1											#Ligne actuelle dans le fichier
	ignoreComment = False					#Balise pour savoir si on est dans une ligne de commentaire
	repetition = False						#Balise pour savoir si on a deja repete un caractere (ex : ==)
	memoireCarac = chaine[0]			#Pour stocker le caractere precedent
	constante = 0									#Pour stocker la constante precedente
	identifiant=""								#Pour stocker un identifiant en construction

	for carac in chaine :

		repetition = False
		if ignoreComment == False: #Si on est pas dans une ligne de commentaire, on cherche des tokens

			#CONSTANTE
			#On regarde si le caractere est un chiffre : si oui, on update constante. Si le precedent etait un
			#chiffre egalement, on multiplie constante par 10 et on lui ajoute le nouveau caractere. Si l'ancien
			#carac etait un chiffre mais que le nouveau n'en est pas, on cree le token constante (la constante est
			#"terminee"
			if carac.isdigit():
				if not memoireCarac.isdigit() :
					constante = int(carac)
			if memoireCarac.isdigit():
				if carac.isdigit() :
					constante = constante*10 + int(carac)
				else :
					createToken("constante", None, constante, ligne)

			#IDENTIFIANT
			#Meme principe que pour les constantes, sauf qu ici on concatene au lieu d additionner
			#De meme, lorsque l identifiant est "termine", on verifie que l on est pas en presence d un mot cle
			#Si c est le cas, le type du token est different
			if carac.isalpha() or carac == "_":
				if not memoireCarac.isalpha()  or carac =="_":
					identifiant = carac
			if memoireCarac.isalpha() or carac =="_":
				if carac.isalpha()  or carac =="_":
					identifiant = identifiant + carac
				else :
					if identifiant == "for" :
						createToken("for", identifiant, None, ligne)
					elif identifiant == "while" :
						createToken("while", identifiant, None, ligne)
					elif identifiant == "continue" :
						createToken("continue", identifiant, None, ligne)
					elif identifiant == "break" :
						createToken("break", identifiant, None, ligne)
					elif identifiant == "if" :
						createToken("if", identifiant, None, ligne)
					elif identifiant == "else" :
						createToken("else", identifiant, None, ligne)
					elif identifiant == "debug" :
						createToken("debug", identifiant, None, ligne)
					elif identifiant == "int" :
						createToken("int", identifiant, None, ligne)
					elif identifiant == "return" :
						createToken("return", identifiant, None, ligne)
					elif identifiant == "send":
							createToken("send", identifiant, None, ligne)
					elif identifiant == "receive":
							createToken("receive", identifiant, None, ligne)
					else :
						createToken("identifiant", identifiant, None, ligne)


			#OPERATEUR / OU COMMENTAIRE
			#Si l ancien carac est un / et que le nouveau aussi, on est en presence d un commentaire donc on passe
			#la balise a true. elle repassera a false a la prochaine ligne
			#Si seul l ancien carac est un /, alors c est un diviseur : on cree son token
			if memoireCarac == "/" :
				if carac == "/" :
					ignoreComment = True
				else :
					createToken("diviseur", memoireCarac, None, ligne)

			#COMPARATEURS
			#OPERATEUR / OU COMMENTAIRE
			#Meme principe que plus haut, en fonction de l ancien carac le type du token change
			if memoireCarac == "<" :
				if carac == "=" :
					createToken("infEgal", "<=", None, ligne)
					repetition = True
				else :
					createToken("inf", memoireCarac, None, ligne)
			if memoireCarac == ">" :
				if carac == "=" :
					createToken("supEgal", ">=", None, ligne)
					repetition = True
				else :
					createToken("sup", memoireCarac, None, ligne)
			if memoireCarac == "!" :
				if carac == "=" :
					createToken("different", "!=", None, ligne)
					repetition = True
				else :
					createToken("not", memoireCarac, None, ligne)
			if memoireCarac == "=" :
				if carac == "=" :
					createToken("egalEgal", "==", None, ligne)
					repetition = True
				else :
					createToken("egal", memoireCarac, None, ligne)

			#OPERATEURS LOGIQUES
			#ici on ne veut que des carac doubles. Si on trouve un & ou un | seul, c est une erreur
			if memoireCarac == "&" :
				if carac == "&" :
					createToken("et", "&&", None, ligne)
					repetition = True
				else :
					print("Caractere inconnu : ", memoireCarac, " a la ligne : ", ligne)
			if memoireCarac == "|" :
				if carac == "|" :
					createToken("ou", "||", None, ligne)
					repetition = True
				else :
					print("Caractere inconnu : ", memoireCarac, " a la ligne : ", ligne)

			#CARACTERES SEULS
			#Ici des qu on croise un tel carac, on cree un token du meme type
			if carac == "+" :
				createToken("addition", carac, None, ligne)
			if carac == "-" :
				createToken("soustraction", carac, None, ligne)
			if carac == "*" :
				createToken("multiplication", carac, None, ligne)
			if carac == "%" :
				createToken("modulo", carac, None, ligne)
			if carac == "^" :
				createToken("puissance", carac, None, ligne)
			if carac == "(" :
				createToken("parentheseO", carac, None, ligne)
			if carac == ")" :
				createToken("parentheseF", carac, None, ligne)
			if carac == "{" :
				createToken("accoladeO", carac, None, ligne)
			if carac == "}" :
				createToken("accoladeF", carac, None, ligne)
			if carac == ";" :
				createToken("pointVirgule", carac, None, ligne)
			if carac == "," :
				createToken("virgule", carac, None, ligne)
			if carac == "[" :
				createToken("crochetO", carac, None, ligne)
			if carac == "]" :
				createToken("crochetF", carac, None, ligne)

		#Si on a rencontre par exemple "==", repetition = true. Dans ce cas, memoireCarac est passe
		#a la main a " ". Cela evite que "===" nous cree deux tokens "==". La balise repetition nous permet de
		#traduire "===" par un token "==" et un token "=".
		if not repetition :
			memoireCarac = carac
		else :
			memoireCarac = " "

		#Si on commence une nouvelle ligne, la balise ignorerCommentaire passe a false
		if carac == '\n' :
				ligne += 1
				ignoreComment = False


#Charger le code source dans une string
def chargerFichier(path):
	str = open(path, 'r').read()
	return str

#Creer un Token et l'ajouter a la collection de Tokens
def createToken(typeToken, valeurC, valeurE, nbLigne):
	token = Token()
	token.Type = typeToken
	token.ValeurChaine = valeurC
	token.ValeurEntiere = valeurE
	token.NbLigne = nbLigne
	listeTokens.append(token)

#Affichage
def afficherListe():
	for i in listeTokens :
		i.afficher()


########################################################################
#        FONCTIONS POUR ANALYSE SYNTAXIQUE
########################################################################

#Retourne le Token sur lequel on pointe
def courant():
	if index<len(listeTokens):
		return listeTokens[index]
	else:
		return None

#Fait avancer le pointeur de 1
def avancer():
	global index
	index+=1

#Si le pointeur pointe bien sur un token du type en parametre, avance au prochaine token
#Sinon, cela veut dire que le type attendu n est pas respecte et que la syntaxe n est pas respectee.
#donc on signale le programme et on sort du programme.
def accepter(typeToken):
  if courant().Type == typeToken:
    avancer()
  else:
    print("ErreurFatale : attendu : ", typeToken, " | recu : ", courant().Type, " | ligne : ", courant().NbLigne)
    exit(0)
    return None

#Cree un nouveau noeud avec son nbligne
def nouveauNoeud(typeNoeud, nbLigne):
  n = Noeud()
  n.Type = typeNoeud
  n.NbLigne = nbLigne
  return n

#Ajoute enfant a la liste des enfants de parent. Parent et enfant sont des noeuds
def ajouterEnfant(parent, enfant):
  parent.Enfants.append(enfant)

#Si le token courant est du type attendu, renvoie true et le pointeur avance au prochain token
#Sinon, renvoie false et ne fait rien
def verifier(typeToken):
	if courant().Type == typeToken:
		avancer()
		return True
	else:
		return False

#Fonction pour verifier qu un token est bien un operateur present dans la table des priorites OP
def verifType(typeC):
	if typeC == "addition" or typeC == "soustraction" or typeC == "multiplication" or typeC == "diviseur" or typeC == "modulo":
		return True
	elif typeC == "inf" or typeC == "sup" or typeC == "infEgal" or typeC == "supEgal" or typeC == "egalEgal" :
		return True
	elif typeC == "puissance" or typeC == "constante" or typeC == "not" or typeC == "different" :
		return True
	elif typeC == "et" or typeC == "ou" or typeC == "egal" :
		return True
	else :
		return False

#Permet de constituer des atomes. Ces derniers peuvent avoir la forme suivante :
#		"(" E ")"															Forme 1
# 	"-" E																	Forme 2
#		"!" E																	Forme 3
#		constante															Forme 4
#		identifiant														Forme 5
#		identifiant "("E "," E "," ... ")"		Forme 6
#		"*" identifiant					Forme 7
def Atome():
	valeurEntiere = courant().ValeurEntiere
	if verifier("parentheseO"):
		#Forme 1
		N = E(0)
		accepter("parentheseF")
		return N
	elif verifier("constante") :
		#Forme 4
		N = nouveauNoeud("Nd_const", courant().NbLigne)
		N.ValeurEntiere = valeurEntiere
		return N
	elif verifier("receive"):
		N = nouveauNoeud("Nd_receive",courant().NbLigne)
		return N;
	elif verifier("soustraction"):
		#Forme 2
		N = nouveauNoeud("Nd_-u", courant().NbLigne)
		Arg = E(55)
		ajouterEnfant(N,Arg)
		return N
	elif verifier("not"):
		#Forme 3
		N = nouveauNoeud("Nd_!u", courant().NbLigne)
		Arg = E(55)
		ajouterEnfant(N,Arg)
		return N
	elif verifier("multiplication"):
		#Forme 7
		N = nouveauNoeud("Nd_indirection", courant().NbLigne)
		Arg = E(55)
		N.Identifiant = courant().ValeurChaine
		ajouterEnfant(N,Arg)
		return N
	elif courant().Type == "identifiant":
		T = courant()
		avancer()
		if verifier("parentheseO"):
			#Forme 6
			N = nouveauNoeud("Nd_appel", courant().NbLigne)
			print(T.ValeurChaine + "\n")
			N.Identifiant = T.ValeurChaine
			while courant().Type != "parentheseF":
				ajouterEnfant(N, E(0))
				if not verifier("virgule"):
					break
			accepter("parentheseF")
			return N
		else :
			#Forme 5
			N= nouveauNoeud("Nd_reference", T.NbLigne)
			N.Identifiant = T.ValeurChaine
			return N
	else :
		print("Erreur fatale : ni parenthese ouvrante ni constante ni identifiant ni ! ni -")
		exit(0)

def S():
	N = Atome()
	if verifier("crochetO"):
		e = E(0)
		accepter("crochetF")
		ind = nouveauNoeud("Nd_indirection",courant().NbLigne)
		add = nouveauNoeud("Nd_addition",courant().NbLigne)
		ajouterEnfant(ind,add)
		ajouterEnfant(add,e)
		ajouterEnfant(add,N)
		return ind
	return N



#Permet de constituer des expressions : pour cela on utilise la priorite a gauche et a droite
#pour constituer un arbre correct. Verifie egalement que l on commence par un atome, que l on a un operateur
#present dans la table OP, et que la suite est une expression (eventuellement)
#Forme :
#		A
#		A "operateur present dans OP" E
def E(prioMin) :
	N = S()
	while verifType(courant().Type) and OP[courant().Type, 'prioG'] > prioMin  :
		opPrioD = OP[courant().Type, 'prioD']
		opTypeNd = OP[courant().Type, 'typeNoeud']
		avancer()
		A = E(opPrioD)
		T = nouveauNoeud(opTypeNd,courant().NbLigne)
		ajouterEnfant(T, N)
		ajouterEnfant(T, A)
		N=T
	return N

#Permet de constituer des instructions. Peuvent etre de la forme :
#		E;											Forme 1
#		debug E;								Forme 2
#		"{" I* "}"							Forme 3
#		if(E) I									Forme 4
# 	if(E) I else I					Forme 5
#		while(E) I							Forme 6
#		for(E;E;E)I							Forme 7
#		return E;				Forme 8
def I():
	nbLigne=courant().NbLigne
	if verifier("debug"):
		#Forme 2
		E1=E(0)
		accepter("pointVirgule")
		N=nouveauNoeud("Nd_debug", nbLigne)
		ajouterEnfant(N,E1)
		return N
	elif verifier("send"):
			#Forme 2
			E1=E(0)
			accepter("pointVirgule")
			N=nouveauNoeud("Nd_send", nbLigne)
			ajouterEnfant(N,E1)
			return N
	elif verifier("return"):
		#Forme 8
		E1 = E(0)
		accepter("pointVirgule")
		N=nouveauNoeud("Nd_return", nbLigne)
		ajouterEnfant(N,E1)
		return N
	elif verifier("accoladeO") :
		#Forme 3
		N=nouveauNoeud("Nd_bloc", nbLigne)
		while not verifier("accoladeF"):
			ajouterEnfant(N,I())
		return N
	elif verifier("if"):
		#Forme 4
		accepter("parentheseO")
		E1 = E(0)
		accepter("parentheseF")
		I1=I()
		N=nouveauNoeud("Nd_test", nbLigne)
		ajouterEnfant(N,E1)
		ajouterEnfant(N,I1)
		if verifier("else"):
			#Forme 5
			I2=I()
			ajouterEnfant(N,I2)
		return N
	elif verifier("int"):
		#Forme 1
		N=nouveauNoeud("Nd_declaration", nbLigne)
		N.Identifiant = courant().ValeurChaine
		avancer()
		accepter("pointVirgule")
		return N
	elif verifier("while"):
		#Forme 6
		N=nouveauNoeud("Nd_loop", nbLigne)
		accepter("parentheseO")
		E1 = E(0)
		accepter("parentheseF")
		I1=I()
		cond = nouveauNoeud("Nd_test", nbLigne)
		Nbreak= nouveauNoeud("Nd_break", nbLigne)
		ajouterEnfant(N,cond)
		ajouterEnfant(cond,E1)
		ajouterEnfant(cond,I1)
		ajouterEnfant(cond,Nbreak)
		return N
	elif verifier("for"):
		#Forme 7
		accepter("parentheseO")
		E1 = E(0)
		accepter("pointVirgule")
		E2 = E(0)
		accepter("pointVirgule")
		E3 = E(0)
		accepter("parentheseF")
		I1=I()
		B1 = nouveauNoeud("Nd_bloc", nbLigne)
		D1 = nouveauNoeud("Nd_drop", nbLigne)
		LOOP=nouveauNoeud("Nd_loop", nbLigne)
		cond = nouveauNoeud("Nd_test", nbLigne)
		Nbreak= nouveauNoeud("Nd_break", nbLigne)
		B2 = nouveauNoeud("Nd_bloc", nbLigne)
		D2 = nouveauNoeud("Nd_drop", nbLigne)
		ajouterEnfant(B1,D1)
		ajouterEnfant(D1,E1)
		ajouterEnfant(B1,LOOP)
		ajouterEnfant(LOOP,cond)
		ajouterEnfant(cond,E2)
		ajouterEnfant(cond,B2)
		ajouterEnfant(cond,Nbreak)
		ajouterEnfant(B2,I1)
		ajouterEnfant(B2,D2)
		ajouterEnfant(D2,E3)
		return B1
	elif verifier("continue"):
		#Forme 1
		accepter("pointVirgule")
		N=nouveauNoeud("Nd_continue", nbLigne)
		return N
	elif verifier("break"):
		#Forme 1
		accepter("pointVirgule")
		N=nouveauNoeud("Nd_break", nbLigne)
		return N
	else:
		#Forme 1
		E1=E(0)
		accepter("pointVirgule")
		N=nouveauNoeud("Nd_drop", nbLigne)
		ajouterEnfant(N,E1)
		return N

#Permet de constituer des fonctions. Ces fonctions doivent avoir la forme suivante:
#"int" identifiant "(" "int" identifiant ["," "int" identifiant ... ")" ";"
#le nombre de parametres est optionnel
def F():
	accepter("int")
	T=courant()
	accepter("identifiant")
	accepter("parentheseO")
	N=nouveauNoeud("Nd_fonction", courant().NbLigne)
	N.Identifiant = T.ValeurChaine
	while courant().Type != "parentheseF":
		accepter("int")
		val=courant().ValeurChaine
		param = nouveauNoeud("Nd_declaration", courant().NbLigne)
		accepter("identifiant")
		param.Identifiant = val
		ajouterEnfant(N, param)
		if not verifier("virgule"):
			break
	accepter("parentheseF")
	ajouterEnfant(N, I())
	return N


#Parcours de l'arbre pour debugger
def afficherArbre(N) :
	if N == None :
		return None
	else:
		if(len(N.Enfants) > 0) :
			afficherArbre(N.Enfants[0])
		if(N.Type == "Nd_const"):
			print(N.ValeurEntiere)
		elif(N.Type == "Nd_fonction" or N.Type == "Nd_reference"):
			print(N.Identifiant)
		else:
			print(N.Type)
		if(len(N.Enfants) > 1) :
			afficherArbre(N.Enfants[1])
		if(len(N.Enfants)>2):
			afficherArbre(N.Enfants[2])


########################################################################
#        FONCTIONS POUR ANALYSE SEMANTIQUE
########################################################################

#Ajoute un dictionnaire a la pile
def debutBloc():
	global pile
	dico={}
	pile.append(dico)

#Retire le dictionnaire sur le haut de la pile
def finBloc():
	global pile
	pile.pop()

#Declare l existence d une variable en ajoutant celle ci au dictionnaire du haut de la pile
#la pile permet de gerer la portee lexicale d une variable : si la declaration a lieu dans un bloc,
#la variable est accessible dans ce bloc et ses sous blocs. (donc dans son dictionnaire et ceux ajoutes
#plus haut dans la pile, mais pas plus bas). Si une variable du meme nom est declaree dans un sous bloc
#c est cette derniere qui sera prise en compte dans le sous bloc (on surcharge)
#si le dernier dictionnaire (donc dans le meme sous bloc) une variable du meme nom a ete declaree, on
#renvoie une erreur
def declarer(identifiant):
	dico = pile[len(pile)-1]
	if identifiant in dico:
		print("Erreur fatale : variable deja declaree\n")
		exit(0)
	else :
		S=Symbole()
		S.IdentifiantS=identifiant
		dico[identifiant]=S
		return S

#Acceder recherche une variable declaree au prealable (donc dans le meme dictionnaire ou plus BAS dans la pile).
#On cherche donc dans le bloc et dans les surBlocs.
#Si on ne trouve rien, on declare une erreur et on abandonne le programme
def acceder(identifiant):
	for i in range(len(pile)-1, -1, -1):
		dico = pile[i]
		if identifiant in dico:
			return dico[identifiant]
	print("Erreur fatale : variable ", identifiant, " non declaree\n")
	exit(0)


#Cette fonction realise l analyse semantique du programme. Elle verifie que les variables sont bien declarees
#et que lorsqu elles sont appelees, elles sont bien accessibles en fonction des blocs
#De meme, cette fonction compte le nombre de variables dans NbSlots pour determiner combien de cases
#memoire seront necessaires a la machine
#De meme, cette fonction attribue un numero de slot a chaque variable : les objets symboles permettent
#de lier le nom de la variable ainsi que son numero de slot
def Sem(N):
	global NbSlots
	if N.Type == "Nd_bloc":
		debutBloc()
		for E in N.Enfants:
			Sem(E)
		finBloc()
	elif N.Type == "Nd_declaration":
		S=declarer(N.Identifiant)
		S.TypeS = "variable"
		S.SlotS=NbSlots
		NbSlots+=1
	elif N.Type == "Nd_reference":
		S=acceder(N.Identifiant)
		if S.TypeS != "variable":
			print("Erreur fatale : pas de variable de ce nom declaree")
			exit(0)
		else :
			N.Slot=S.SlotS
	elif N.Type == "Nd_fonction":
		NbSlots = 0
		S=declarer(N.Identifiant)
		S.TypeS = "fonction"
		debutBloc()
		for E in N.Enfants:
			Sem(E)
		finBloc()
		N.Slot = NbSlots
	elif N.Type == "Nd_appel":
		S=acceder(N.Identifiant)
		if S.TypeS != "fonction":
			print("Erreur fatale : pas de fonction de ce nom declaree")
			exit(0)
		for E in N.Enfants:
			Sem(E)
	else:
		for E in N.Enfants :
			Sem(E)

########################################################################
#        FONCTIONS POUR GENERATION DE CODE
########################################################################

#Cette fonction permet de generer le code a fournir a la machine msm
#Elle parcourt les noeuds de l arbre syntaxique et ajoute a chaineTexte les lignes de code
#necessaire en fonction du type des noeuds. Pour parcourir ce dernier, on utilise la 
#recurrence
def genCodeRec(N):
	global chaineTexte
	global label
	global pileBoucles
	if(N.Type == "Nd_const") :
		chaineTexte = chaineTexte + "push " + str(N.ValeurEntiere) + "\n"
	elif(N.Type == "Nd_addition") :
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "add\n"
	elif(N.Type == "Nd_soustraction") :
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "sub\n"
	elif(N.Type == "Nd_multiplication") :
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "mul\n"
	elif(N.Type == "Nd_diviseur") :
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "div\n"
	elif(N.Type == "Nd_modulo") :
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "mod\n"
	elif(N.Type == "Nd_-u"):
		chaineTexte = chaineTexte + "push 0\n"
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		chaineTexte = chaineTexte + "sub\n"
	elif(N.Type == "Nd_!u"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "not\n"
	elif(N.Type == "Nd_egalEgal"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "cmpeq\n"
	elif(N.Type == "Nd_different"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "cmpne\n"
	elif(N.Type == "Nd_inf"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "cmplt\n"
	elif(N.Type == "Nd_infEgal"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "cmple\n"
	elif(N.Type == "Nd_sup"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "cmpgt\n"
	elif(N.Type == "Nd_supEgal"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "cmpge\n"
	elif(N.Type == "Nd_et"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "and\n"
	elif(N.Type == "Nd_ou"):
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		if(len(N.Enfants)>1):
			genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "or\n"
	elif(N.Type == "Nd_debug"):
		genCodeRec(N.Enfants[0])
		chaineTexte = chaineTexte + "dbg\n"
	elif(N.Type == "Nd_drop"):
		genCodeRec(N.Enfants[0])
		chaineTexte = chaineTexte + "drop\n"
	elif(N.Type == "Nd_bloc"):
		for i in N.Enfants:
			genCodeRec(i)
	elif(N.Type == "Nd_test"):
		genCodeRec(N.Enfants[0])
		chaineTexte = chaineTexte + "jumpf if" + str(label)+ "\n"
		memLabelIf = label
		label+=1
		genCodeRec(N.Enfants[1])
		if len(N.Enfants) >2:
			chaineTexte = chaineTexte + "jump if" + str(label)+ "\n"
			memLabelElse = label
			label+=1
			chaineTexte = chaineTexte + ".if" + str(memLabelIf)+ "\n"
			genCodeRec(N.Enfants[2])
			chaineTexte = chaineTexte + ".if" + str(memLabelElse)+ "\n"
		else :
			chaineTexte = chaineTexte + ".if" + str(memLabelIf)+ "\n"
	elif(N.Type == "Nd_reference"):
		chaineTexte = chaineTexte + "get " + str(N.Slot) + "\n"
	elif(N.Type == "Nd_affectation"):
		if(N.Enfants[0].Type == "Nd_reference"):
			genCodeRec(N.Enfants[1])
			chaineTexte = chaineTexte + "dup\n"
			chaineTexte = chaineTexte + "set " + str(N.Enfants[0].Slot) + "\n"
		else:
			genCodeRec(N.Enfants[0].Enfants[0])
			genCodeRec(N.Enfants[1])
			chaineTexte = chaineTexte + "write\n"
			chaineTexte = chaineTexte + "dup\n"
	elif(N.Type == "Nd_loop"):
		pileBoucles.append("l"+str(label))
		label+=1
		pileBoucles.append("l"+str(label))
		label+=1
		chaineTexte = chaineTexte + "." + str(pileBoucles[len(pileBoucles)-2])+ "\n"
		if(len(N.Enfants)>0):
			genCodeRec(N.Enfants[0])
		else:
			print("Erreur fatale : mauvaise utilisation d'une boucle ligne " + str(N.NbLigne))
			exit(0)
		chaineTexte = chaineTexte + "jump " + str(pileBoucles[len(pileBoucles)-2])+ "\n"
		chaineTexte = chaineTexte + "." + str(pileBoucles[len(pileBoucles)-1])+ "\n"
		pileBoucles.pop()
		pileBoucles.pop()
	elif(N.Type == "Nd_continue"):
		chaineTexte = chaineTexte + "jump " + str(pileBoucles[len(pileBoucles)-2])+ "\n"
	elif(N.Type == "Nd_break"):
		chaineTexte = chaineTexte + "jump " + str(pileBoucles[len(pileBoucles)-1])+ "\n"
	elif(N.Type == "Nd_appel"):
		chaineTexte = chaineTexte + "prep " + str(N.Identifiant) + "\n"
		for E in N.Enfants :
			genCodeRec(E)
		chaineTexte = chaineTexte + "call " + str(len(N.Enfants)) + "\n"
	elif(N.Type == "Nd_fonction"):
		chaineTexte = chaineTexte + "." + str(N.Identifiant) + "\n"
		chaineTexte = chaineTexte + "resn " + str(N.Slot - (len(N.Enfants)-1)) + "\n"
		genCodeRec(N.Enfants[len(N.Enfants)-1])
		chaineTexte = chaineTexte + "push 0\n"
		chaineTexte = chaineTexte + "ret\n"
	elif(N.Type == "Nd_return"):
		genCodeRec(N.Enfants[0])
		chaineTexte = chaineTexte + "ret\n"
	elif(N.Type == "Nd_puissance"):
		chaineTexte = chaineTexte + "prep puissance\n"
		genCodeRec(N.Enfants[0])
		genCodeRec(N.Enfants[1])
		chaineTexte = chaineTexte + "call 2\n"
	elif(N.Type == "Nd_indirection"):
		genCodeRec(N.Enfants[0])
		chaineTexte = chaineTexte + "read\n"
	elif(N.Type == "Nd_send"):
		genCodeRec(N.Enfants[0])
		chaineTexte = chaineTexte + "send\n"
	elif(N.Type == "Nd_receive"):
		chaineTexte = chaineTexte + "recv\n"

#Ancienne fonction chapeau, qui etait utile auparavant mais qui n appelle plus que 
#genCodeRec
def genCode(N) :
	global chaineTexte
	genCodeRec(N)

#Ecrit la chaine dans le fichier disponible a path
def ecrireFichier(path, chaine):
	fichier = open(path, "w")
	fichier.write(chaine)
	fichier.close()


########################################################################
#        INIT
########################################################################

#Fonction qui cree la liste de tokens du runtime
def init():
	global chaineTexte
	global listeTokens
	global index
	index=0
	listeTokens = []
	fichierRuntime = chargerFichier("./runtime.c")

	analyseLexicale(fichierRuntime)
	#print("**********")
	#afficherListe()
	#print("**********")
	#debutBloc()
	#while courant().Type != "EOF":
	#	N=F()

	#	Sem(N)
	#	genCodeRec(N)
	#finBloc()


########################################################################
#        MAIN
########################################################################
#Si on a pas dans l appel le fichier source et le fichier de sortie, on signale
if len(sys.argv) != 3:
	print("Usage execution : python compilateur.py fileIn.* fileOut.*")
	exit(0)
#Si on a tout
else:
	fileIn = sys.argv[1]
	fileOut = sys.argv[2]
	fichierCode = chargerFichier(fileIn)
	#on cree les tokens des fonctions dans le fichier runtime
	init()
	#on ajoute aux tokens ceux du code de l'utilisateur (il peut ainsi utiliser les fonctions
	#du runtime)
	analyseLexicale(fichierCode)
	#A la fin du fichier, on cree un token EOF pour signaler la fin
	createToken("EOF", "EOF", None, 0)
	debutBloc()
	#afficherListe()
	while courant().Type != "EOF":
		#on cree l arbre syntaxique
		N=F()
		#optionnel : on affiche l arbre
		afficherArbre(N)
		#on realise l analyse semantique de la fonction
		Sem(N)
		#on genere le code de la fonction
		genCode(N)
		#... et on reboucle ainsi sur toutes les fonctions (dont le main)
	finBloc()
	
	#on construit le point de depart du programme et on appelle la fonction main sans 
	#parametre
	chaineTexte = chaineTexte + ".start\n"
	chaineTexte = chaineTexte + "prep main\n"
	chaineTexte = chaineTexte + "call 0\n"
	chaineTexte = chaineTexte + "halt"
	#optionnel : pour afficher le code ecrit
	print(chaineTexte)
	ecrireFichier(fileOut, chaineTexte)


#./msm -d codesource.txt
