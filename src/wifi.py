# Gestion de la connexion

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
