"""
Utilise la base de données pour traiter les requêtes
"""

import bdd
import re

import pyaudio
import wave

from os import system
from random import choice

from config import AUDIO_CHUNK, AUDIO, AUDIO_ERR

from snowboy_detect import decoder

def joue(fichier):
	"""
	Joue un fichier
	"""
	
	if not fichier.endswith(".wav"):
		fichier += ".wav"
	
	print("[PROC] On joue {}".format(fichier))
	"""
	wf = wave.open(AUDIO + fichier, 'rb')

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
	"""

	decoder.play_audio_file(fname=AUDIO+fichier)
	
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
	print("[RECO] Execution {}".format(to_exec))
        # On récupère l'action et son param
	fct, param = to_exec.split(":")
	# Fix un petit bug ;)
	if fct == "joue":
		param = '"' + param + '"'
	# On l'execute
	# !!!! DANGER
	eval("{}({})".format(fct, param))

def process(phrase):
	"""
	Process la phrase dite via la BDD
	"""

	for key in bdd.data.keys():
		print("[PROC] Essai : {}".format(key))
		try:
			prog = re.compile(key)
		except Exception as e:
			print(e)
			joue(AUDIO_ERR)
			return
		if prog.match(phrase.lower()):
			traite(bdd.data[key])
			# Fin
			return
	
	# Si on est là, on a rien trouvé
	traite(bdd.default)
