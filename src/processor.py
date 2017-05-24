"""
Utilise la base de données pour traiter les requêtes
"""

import bdd
import re

import pyaudio
import wave
import time

from os import system
from random import choice

from config import AUDIO_CHUNK, AUDIO, AUDIO_ERR

def joue(fichier):
	"""
	Joue un fichier
	"""
	
	if not fichier.endswith(".wav"):
		fichier += ".wav"
	
	print("[PROC] On joue {}".format(fichier))
	
	wav = wave.open(AUDIO + fichier, 'rb')
	data = wav.readframes(wav.getnframes())
	audio = pyaudio.PyAudio()
	stream_out = audio.open(
		format=audio.get_format_from_width(wav.getsampwidth()),
		channels=wav.getnchannels(),
		rate=wav.getframerate(), input=False, output=True)
	stream_out.start_stream()
	stream_out.write(data)
	time.sleep(0.2)
	stream_out.stop_stream()
	stream_out.close()
	audio.terminate()
	
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
