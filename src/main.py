# Pour avoir le mot clef!!
from snowboy_detect import decoder

from processor import joue
from recon import reco_vocale
from config import AUDIO_OK, SENSIBILITE, MODEL, TEST_HOST, SLEEP_TIME

# Pour les interruptions
import signal

import wifi

joue(AUDIO_START)

joue("verifie_connection.wav")
if not wifi.teste(TEST_HOST):
    # On n'est pas connecté
    joue("pas_connecte.wav")
    wifi.demarre()
else:
    # On vas pouvoir continuer
    joue("connecte.wav")
    
    # Marque s'il y eu une interruption
    interrupted = False
    
    def signal_handler(signal, frame):
        """
        Gère les interruptions (ctrl-c, kill, etc...)
        """
        global interrupted
        interrupted = True
        
    def interrupt_callback():
        global interrupted
        return interrupted
    
    # capture le signal SIGINT (ctrl-c)
    signal.signal(signal.SIGINT, signal_handler)
    # capture le signal SIGTERM (kill
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Détecte le mot clef (Milo)
    detecteur = snowboydecoder.HotwordDetector(MODEL, sensitivity=SENSIBILITE)
    print('[MAIN] En écoute...')
    
    # Dès qu'il y un mot clef, on démarre la reconnaissance vocale
    detecteur.start(detected_callback=reco_vocale, # Action dès que l'on capte un mot clef
                   interrupt_check=interrupt_callback, # Check si on s'est arrêté
                   sleep_time=SLEEP_TIME)
    
    # Si on arrive ici, le detecteur s'est arrêté
    detecteur.terminate()
