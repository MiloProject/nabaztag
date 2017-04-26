# Configure le projet

# Snowboy
MODEL = "../snowboy.umdl"
SENSIBILITE = 0.5 # entre 0 et 1!
SLEEP_TIME = 0.03 # Temps entre chaque recherche de mot clef

# Chemin vers les fichiers audio
AUDIO = "../data/audio/"
AUDIO_OK = AUDIO + "utils/ok.wav"
AUDIO_START = AUDIO + "utils/start.wav"
AUDIO_ERR = AUDIO + "utils/err.wav"

AUDIO_CHUNK = 1024 # pour pyaudio

# Hote vers qui tester la connexion, site d'Eliott
TEST_HOST = ("developpsoft.github.io", 80)

# Configuration pour le hotspot
HOSTAPD = "../hostapd.conf"
DNSMASQ = "../dnsmasq.conf"
