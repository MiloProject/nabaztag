"""
Utilise la base de données pour traiter les requêtes
"""

import bdd
import re

from os import system
from random import choice


def dit(phrase):
	"""
	Utilise espeak/flite pour dire la phrase
	"""

	#TODO
	pass

def chante(fichier):
	"""
	Joue un fichier audio via aplay
	"""

	#TODO
	pass

def execute(cmd):
	"""
	Execute une commande
	"""
	system(cmd)

def traite(todo):
	"""
	Traite une réponse
	"""
	
	to_exec = choice(todo)
	# On récupère l'action et son param
	fct, param = to_exec.split("_")
	# On l'execute
	# !!!! DANGER
	eval("{}({})".format(fct, param))

def process(phrase):
	"""
	Process la phrase dite via la BDD
	"""

	for key in bdd.data.keys():
		if re.match(key, phrase):
			traite(bdd.data[key])
			# Fin
			return
	
	# Si on est là, on a rien trouvé
	traite(bdd.default)
