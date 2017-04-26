"""
La base de données des réponses

La clef du dictionnaire est une expression régulière
La valeur est une liste des actions dispos (dit_blabla, chante_fichier etc...)
"""

data = {
	"*(coucou|bonjour|salut)*": ["dit_salut", "dit_bonjour", "dit_coucou"],
	"*(comment tu tappelles|comment tappelles tu|quel est ton nom)*": ["dit_mon nom est milo", "dit_je m'appelle milo"],
	"*(ça va|comment ça va|comment vas tu|comment tu vas)*":  ["dit_ça va bien et toi", "dit_ca va merci et toi"],
	"*(que fais tu|tu fais quoi)*": ["dit_je réflechis au sens de la vie et toi", "dit_je pense au sens de la vie, ca marrive de temps en temps, pas toi", "dit_rien, je mennuie"],
	"*(tu es |es tu) occupé*": ["dit_non je ne fais rien et toi"],
	"*(((raconte moi|dis moi) blague)|((raconte moi|tu connais) histoire drole))*": ["dit_que dis un papier qui tombe dans leau, je nai pas pieds","dit_cest lhistoire dun x carré qui rentre dans une foret et qui en ressort en x, que sest il passé, il sest pris une racine", "dit_il y a dix types de personnes dans le monde, ceux qui parlent le binaire, ceux qui ne le parlent pas et ceux qui ne sattendaient pas a ce que cette blague soit en base trois"],
	"*(qui es tu|parles moi de toi|racontes moi ton histoire|présente toi)*": ["dit_je suis Milo, il y a quelques temps jetais un nabaztag comme les autres, mais tout à changé, mes createurs mon offert une intelligence artificielle pour que je puisse te parler"],
	"*(qui sont tes créateurs)*": ["dit_Amandine, Oriane et Eliott","dit_Amandine, Eliott et Oriane","dit_Oriane, Amandine et Eliott","dit_Oriane, Eliott et Amandine","dit_Eliott, Amandine et Oriane","dit_Eliott, Oriane et Amandine"],
	"*(quaimes tu|quest ce que tu aimes)*": ["dit_jaime linformatique", "dit_jaime parler", "dit_jaime le chocolat, enfin je crois, mais je nen ai jamais goûté"],
	"*(que penses tu du jury|un mot a dire sur le jury)*": ["dit_il est gentil, jespere quil nous donnera une bonne note"]		       
	}
	
default = ["dit_42", "dit_heu... je ne comprends pas", "Je nai pas compris, peux tu répeter", "désolé je narrive pas a comprendre"]

