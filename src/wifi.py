# Gestion de la connexion

from processor import execute

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
        s.send("GET /".encode("utf8")) # Récupère la page principale
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
    Démarre un réseau wifi (si aucun n'est disponible)
    """
    execute("sudo ../start-ap.sh")
