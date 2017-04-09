# Gestion de la connexion

from processor import cmd

import config

import socket as sock

def teste(to_conn):
    """
    Teste la connexion Internet
    """
    result = None
    
    s = sock.socket()
    
    try:
        s.connect((to_conn))
        s.send("GET /") # Récupère la page principale
    except:
        # Il y un erreur donc pas de connexion
        result = False
    else:
        # si tout vas bien
        result = True
    finally:
        # On oublie pas de fermer la connexion
        s.close()
        
    return result

def demarre():
    """
    Démarre un réseau wifi (si aucun n'est disponible
    """
    
    # Setup l'addresse IP
    cmd("ip link set dev wlan0 down")
    cmd("ip a add 10.0.0.5/24 dev wlan0")
    cmd("ip link set dev wlan0 up")
    
    # On démarre hotsapd (crée le réseau) en arrière plan
    cmd("hostapd {} -B".format(config.HOSTAPD))
    # On démarre dnsmasq (gère l'addressage)
    cmd("dnsmasq -C {}".format(config.DNSMASQ))
