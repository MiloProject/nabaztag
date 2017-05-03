"""
La base de données des réponses

La clef du dictionnaire est une expression régulière
La valeur est une liste des actions dispos (dit_blabla, chante_fichier etc...)
"""

data = {
	"(coucou|bonjour|salut).*": ["joue:salut", "joue:bonjour", "joue:coucou"],
	"(comment tu t'appelles|comment t'appelles tu|quel est ton nom)": ["joue:mon_nom_est_milo", "joue:je_mappelle_milo"],
	"(ça va|comment ça va|comment vas tu|comment tu vas)":  ["joue:ça_va_bien_et_toi", "joue:ca_va_merci_et_toi"],
	"(que fais tu|tu fais quoi)": ["joue:je_réflechis_au_sens_de_la_vie_et_toi", "joue:je_pense_au_sens_de_la_vie_ca_marrive_de_temps_en_temps_pas_toi", "joue:rien_je_mennuie"],
	".*(tu es |es tu) occupé": ["joue:non_je_ne_fais_rien_et_toi"],
	"*(((raconte moi|dis moi) blague)|((raconte moi|tu connais) histoire drole))*": ["joue:blague_du_papier","joue:blague_racine", "joue:blague_binaire"],
	"*(qui es tu|parles moi de toi|racontes moi ton histoire|présente toi)*": ["joue:je_suis_Milo_il_y_a_quelques_temps_jetais_un_nabaztag_comme_les_autres_mais_tout_à_changé_mes_createurs_mon_offert_une_intelligence_artificielle_pour_que_je_puisse_te_parler"],
	"*(qui sont tes créateurs)*": ["joue:A_O_E","joue:A_E_O","joue:O_A_E","joue:O_E_A","joue:E_A_O","joue:E_O_A"],
	"*(quaimes tu|quest ce que tu aimes)*": ["joue:jaime_linformatique", "joue:jaime_parler", "joue:jaime_le_chocolat_enfin_je_crois_mais_je_nen_ai_jamais_goûté"],
	"*(que penses tu du jury|un mot a dire sur le jury)*": ["joue:il_est_gentil_jespere_quil_nous_donnera_une_bonne_note"]		
	"*(quel age a tu|tu as quel age)*": ["joue:je_suis_immortel_je_ne_compte_plus_les_années"],
	"*(pourquoi as tu|pourquoi tu as)grandes oreilles*": ["joue:pour_mieux_tentendre"],
	"*(est ce que tu maimes bien)*": ["joue:bien_sur","joue:qui_ne_taime_pas","joue:cest_difficile_de_ne_pas_aimer_quelquun_comme_toi"],
	"*(tu aimes|aimes tu) lycée*": ["joue:oui_surtout_le_lycée_rené_cassin"],
	"*(tu ressens|ressens tu) sentiments*": ["joue:oui", "joue:cette_quesiton_est_vexante"],
	"*(tes créateurs|Eliott) gentil avec toi*": ["joue:Oui_très", "joue:je_dirai_même_adorable"],
	"*(Oriane|Amandine) gentille avec toi*": ["joue:Oui_tres", "joue:je_dirai_même_adorable", "joue:oui_cest_même_elle_la_plus_gentille"],
	"*(Je|Eliott|Oriane|Amandine) mérite une bonne note*": ["joue:une_très_bonne_note_il_y_a_eu_beaucoup_de_travail_de_fait", "joue:oui_cest_une_personne_formidable_qui_a_beaucoup_aider_au_projet"],
	"*(comment vois tu|parles moi de) futur*": ["joue:je_pense_que_je_vais_beaucoup_voyager_car_mes_créateurs_se_sont_partagé_ma_garde"]
	}
	
default = ["joue:42", "joue:heu... je ne comprends pas", "joue:je_nai_pas_compris_peux_tu_répeter", "joue:désolé_je_narrive_pas_a_comprendre"]

