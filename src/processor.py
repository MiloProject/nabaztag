"""
Utilise la base de données pour traiter les requêtes
"""

import bdd
import re

import pyaudio
import wave

from os import system
from random import choice

from config import AUDIO_CHUNK, AUDIO

def joue(fichier):
	"""
	Joue un fichier
	"""
	
	print("[PROC] On joue {}".format(fichier))
	wf = wave.open(fichier, 'rb')

	p = pyaudio.PyAudio()

	# On crée un 'stream', un accés à la sortie audio
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        	        channels=wf.getnchannels(),
       	        	rate=wf.getframerate(),
			output=True)

	data = wf.readframes(AUDIO_CHUNK)
	
	# Tant qu'il reste des données, on les envoient dans le stream
	while data != '':
		stream.write(data)
		data = wf.readframes(AUDIO_CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()
	
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
