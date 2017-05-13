# La reconnaissance vocale

import speech_recognition as sr

from processor import process, joue
from config import AUDIO_OK

recon = sr.Recognizer()
micro = sr.Microphone()

def calibre():
	print("[RECO] Calibration...")
	with micro as source: recon.adjust_for_ambient_noise(source)
	print("[RECO] Calibration : {}".format(recon.energy_threshold))
  
# Prend n'importe quel argument(s)
def reco_vocale(*args, **kwargs):
	print("[RECO] En écoute...")
	with micro as source: audio = recon.listen(source)
	print("[RECO] Entendu quelque chose...")

	try:
		phrase = recon.recognize_google(audio, language="fr-FR")
		print("[RECO] Phrase : {}".format(phrase))
	except sr.UnknownValueError:
		joue(AUDIO_ERR)
		print("[RECO] Valeur inconue... :(")
	except sr.RequestError as e:
		joue(AUDIO_ERR)
		print("[RECO] Je ne peux pas contacter Google :(")
		print("[RECO] Erreur: {}".format(e))
	else: # Si tout vas bien
		joue(AUDIO_OK)
		process(phrase)
    
