"""
La base de données des réponses
La clef du dictionnaire est une expression régulière
La valeur est une liste des actions dispos (dit_blabla, chante_fichier etc...)
"""

data = {
	".*(coucou|bonjour|salut).*": ["joue:salut", "joue:bonjour", "joue:coucou"],
	".*(comment tu t'appelles|comment t'appelles tu|quel est ton nom)": ["joue:mon_nom_est_milo", "joue:je_mappelle_milo"],
	".*(ça va|comment ça va|comment vas tu|comment tu vas)":  ["joue:ca_va_bien_et_toi", "joue:ca_va_merci_et_toi"],
	".*(que fais tu|tu fais quoi)": ["joue:je_reflechis_au_sens_de_la_vie_et_toi", "joue:rien_je_mennuie"],
	".*(tu es |es tu) occupé": ["joue:non_je_ne_fais_rien_et_toi"],
	".*(raconte.*moi|fais moi|tu connais).*(blague|histoire).*": ["joue:blague_du_papier","joue:blague_racine"],
	".*(qui es tu|parle moi de toi|(raconte moi|quelle est) ton histoire|(présente toi|peux tu te présenter))": ["joue:presentation"],
	".*(qui sont).*(créateurs)": ["joue:createurs"],
	".*qu.*(tu.*aime|aime.*tu).*": ["joue:jaime_linformatique", "joue:jaime_parler", "joue:jaime_le_chocolat"],
	".*(pense|mot).*jury": ["joue:jury"],		
	".*qu.*age.*": ["joue:immortel"],
	".*pourquoi.*grandes oreilles.*": ["joue:pour_mieux_tecouter"],
	".*qu.*m.*aime.*": ["joue:bien_sur","joue:qui_ne_taime_pas","joue:difficile_aimer"],
	".*tu.*aime.*lycée.*": ["joue:lycee"],
	".*ressens.*sentiments.*": ["joue:bien_sur","joue:question_vexante"],
	".*(tes créateurs|eliott).*gentil.*toi.*": ["joue:adorable"],
	".*(oriane|amandine).*gentille.*toi.*": ["joue:adorable", "joue:gentille"],
	".*(eliott|oriane|amandine).*bonne note.*": ["joue:bien_sur"],
	".*(quel|comment|parle).*futur.*": ["joue:futur"],
	".*quoi.*(crois.*tu|tu.*crois).*": ["joue:je_crois_humanite","joue:je_crois_createurs"],
	".*qu.*nourris.*": ["joue:nourriture"],
	".*pense.*intelligent.*": ["joue:intelligence_createurs"],
	".*es.*(lapin|robot).*": ["joue:je_suis_chat"],
	".*qu.*souhaite.*": ["joue:milo_president","joue:des_carottes","joue:soeur"],
	".*qu.*programme politique.*": ["joue:interner_createurs","joue:paye_karrotz","joue:domination_lapin"],
	".*pourquoi.*appelle.*milo.*": ["joue:coup_tordu","joue:nom_question"],
	".*(ai|veu).*carottes.*": ["joue:des_carottes","joue:a_moi","joue:carotte_pas_fraiche"],
	".*pense.*tu.*cortana.*": ["joue:cortana"],
	".*(joue|chante).*(chanson|musique).*": ["joue:i_kissed_a_girl", "joue:si_je_men_sors", "joue:trem_bala"],
	".*bonne nuit.*": ["execute:sudo killall -s 9 main.py && sudo poweroff"],
	}
	
default = ["joue:pas_compris", "joue:pas_compris_repete", "joue:arrive_pas_comprendre"]
