# TODO: load reco_vocale

# Pour avoir le mot clef!!
from snowboy_detect import decoder

# Pour les interruptions
import signal

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
detecteur = snowboydecoder.HotwordDetector(config.MODEL, sensitivity=config.SENSIBILITE)
print('[MAIN] En écoute...')

# Dès qu'il y un mot clef, on démarre la reconnaissance vocale
detecteur.start(detected_callback=reco_vocale, # Action dès que l'on capte un mot clef
               interrupt_check=interrupt_callback, # Check si on s'est arrêté
               sleep_time=config.SLEEP_TIME)

# Si on arrive ici, le detecteur s'est arrêté
detecteur.terminate()
