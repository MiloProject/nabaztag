#! /usr/bin/python3

from processor import joue
from recon import reco_vocale
from config import AUDIO_ERR, AUDIO_START, AUDIO_OK, SENSIBILITE, MODEL, TEST_HOST, SLEEP_TIME

from time import sleep

# Pour les interruptions
import signal

import wifi

joue(AUDIO_START)

# On attend que la connexion soit établie
sleep(2)

if not wifi.teste(TEST_HOST):
    # On n'est pas connecté
    joue(AUDIO_ERR)
    wifi.demarre()
else:
    # On vas pouvoir continuer
    joue(AUDIO_OK)
    
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
    #detecteur = decoder.HotwordDetector(MODEL, sensitivity=SENSIBILITE)
    print('[MAIN] En écoute...')

    while !interrupted: # On boucle !
        reco_vocale()
    
    print("[MAIN] Fin.")
