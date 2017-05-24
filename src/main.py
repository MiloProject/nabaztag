#! /usr/bin/python3

from processor import joue
from recon import reco_vocale, calibre
from config import AUDIO_ERR, AUDIO_START, AUDIO_OK, TEST_HOST

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
    # Marque s'il y eu une interruption
    interrupted = False
    
    def signal_handler(signal, frame):
        """
        Gère les interruptions (ctrl-c, kill, etc...)
        """
        global interrupted
        print("[MAIN] Interruption interceptée")
        interrupted = True
        
    def interrupt_callback():
        global interrupted
        return interrupted
    
    # capture le signal SIGINT (ctrl-c)
    signal.signal(signal.SIGINT, signal_handler)
    # capture le signal SIGTERM (kill
    signal.signal(signal.SIGTERM, signal_handler)

    calibre()

    # On vas pouvoir continuer
    joue(AUDIO_OK)

    print('[MAIN] En écoute...')

    while not interrupted: # On boucle !
        reco_vocale()
    
    print("[MAIN] Fin.")
