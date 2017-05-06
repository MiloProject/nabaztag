"""
La base de données des réponses

La clef du dictionnaire est une expression régulière
La valeur est une liste des actions dispos (dit_blabla, chante_fichier etc...)
"""

data = {
	"(coucou|bonjour|salut).*": ["joue:salut", "joue:bonjour", "joue:coucou"],
	"(comment tu t'appelles|comment t'appelles tu|quel est ton nom)": ["joue:mon_nom_est_milo", "joue:je_mappelle_milo"],
	"(ça va|comment ça va|comment vas tu|comment tu vas)":  ["joue:ca_va_bien_et_toi", "joue:ca_va_merci_et_toi"],
	"(que fais tu|tu fais quoi)": ["joue:je_reflechis_au_sens_de_la_vie_et_toi", "joue:rien_je_mennuie"],
	".*(tu es |es tu) occupé": ["joue:non_je_ne_fais_rien_et_toi"],
	"*(((raconte moi|dis moi) blague)|((raconte moi|tu connais) histoire drole))*": ["joue:blague_du_papier","joue:blague_racine"],
	"*(qui es tu|parles moi de toi|racontes moi ton histoire|présente toi)*": ["joue:presentation"],
	"*(qui sont tes créateurs)*": ["joue:createurs"],
	"*(quaimes tu|quest ce que tu aimes)*": ["joue:jaime_linformatique", "joue:jaime_parler", "joue:jaime_le_chocolat"],
	"*(que penses tu du jury|un mot a dire sur le jury)*": ["joue:jury"]		
	"*(quel age a tu|tu as quel age)*": ["joue:immortel"],
	"*(pourquoi as tu|pourquoi tu as)grandes oreilles*": ["joue:pour_mieux_tecouter"],
	"*(est ce que tu maimes bien)*": ["joue:bien_sur","joue:qui_ne_taime_pas","joue:difficile_aimer"],
	"*(tu aimes|aimes tu) lycée*": ["joue:lycee"],
	"*(tu ressens|ressens tu) sentiments*": ["joue:bien_sur","joue:question_vexante"],
	"*(tes créateurs|Eliott) gentil avec toi*": ["joue:adorable"],
	"*(Oriane|Amandine) gentille avec toi*": ["joue:adorable", "joue:gentille"],
	"*(Je|Eliott|Oriane|Amandine) mérite une bonne note*": ["joue:bien_sur"],
	"*(comment vois tu|parles moi de) futur*": ["joue:futur"],
	"*(En quoi crois-tu)*": ["joue:je_crois_humanite","joue:je_crois_createurs"],
	"*(De quoi te nourris-tu)*": ["joue:nourriture"],
	"*(Penses-tu être intelligent)*": ["joue:intelligence_createurs"],
	"*(Tu es un lapin ou un robot)*": ["joue:je_suis_chat"],
	"*(Que souhaites-tu)*": ["joue:milo_president","joue:des_carottes","joue:soeur"],
	"*(Et quel est ton programme politique)*": ["joue:interner_créateurs","joue:paye_karrotz","joue:domination_lapin"],
	"*(Pourquoi t’appelles-tu Milo)*": ["joue:coup_tordu","joue:nom_question"],
	"*(J’ai des carottes)*": ["joue:des_carottes","joue:a_moi","joue:carotte_pas_fraiche"],
	"*(Que penses tu de Cortana)*": ["joue:cortana"],
	}
	
default = ["joue:pas_compris", "joue:pas_compris_repete", "joue:arrive_pas_comprendre"]

