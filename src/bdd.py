"""
La base de données des réponses

La clef du dictionnaire est une expression régulière
La valeur est une liste des actions dispos (dit_blabla, chante_fichier etc...)
"""

data = {
	"(coucou|bonjour|salut).*": ["joue:salut", "joue:bonjour", "joue:coucou","joue:mieux_depuis_que_tu_es_la"],
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
	
### j'ai écris les sons "-é" sous la forme "-er" // du type "publiciter". Bien ou pas ?
	"*(Sais tu conduire)*": ["joue:lamborghini"],
	"*(Quel est le poids d'une pomme*": ["joue:environ_180_grammes_mais_attention_a_ne_pas_manger_les_pepins_car_ils_sont_toxiques_a_cause_du_cyanure_quil_contient"]
	"*(Que penses tu de Google, Apple et Microsoft)*": ["joue: je_ne_me_prononcerais_pas_sur_le_sujet_etant_donner_les_avis_divergents_de_mes_createurs"]
	"*(Cite moi les pays de l'Union Européenne)*": ["joue:allemagne_autriche_belgique_bulgarie_chypre_croatie_danemark_espagne_estonie_finlande_france_grece_hongrie_irlande_italie_lettonie_lituanie_luxembourg_malte_pays_bas_pologne_portugal_république_tcheque_roumanie_royaume_uni_slovaquie_slovénie_suede"]
	"*(Cite moi Bill Gates)*": ["joue:la_meilleure_des_publiciciter_est_un_client_satisfait", "joue:ce_que_je_sais_faire_de_meiux_cest_partager_mon-enthousiasme"]
	"*(Cite moi Steve Jobs)*": ["joue:innover_cest_savoir_abandonner_des_milliers_de_bonnes_idees", "joue:jechangerai_toute_ma_technologie_pour_un_apres_midi_avec_socrate"]
	"*(Cite moi Larry Page ou Sergei Brin)*": ["joue:la_vitesse_et_lexcellence_deux_concepts_cles_pour_google", "joue:pour_moi_il_sagit_de_preserver_lhistoire_et_la_rendre_accessible_a_tout_le_monde"]
	"*(Cite moi Richard Stallman)*": ["joue:si_les_programmeurs_meritent_detre_recompensés_pour_la_creation_de_programmes_novateurs_de_meme_ils_meritent_detre_punis_sils_limitent_lutilisation_de_ces_programmes"]
	}
	
default = ["joue:pas_compris", "joue:pas_compris_repete", "joue:arrive_pas_comprendre"]

