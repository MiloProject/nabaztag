"""
La base de données des réponses

La clef du dictionnaire est une expression régulière
La valeur est une liste des actions dispos (dit_blabla, chante_fichier etc...)
"""

data = {
	"*hey*": ["dit_salut", "dit_bonjour", "dit_casse toi"]
	}
	

default = ["dit_42", "dit_heu... je ne comprends pas"]
