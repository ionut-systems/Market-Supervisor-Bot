from typing import List, Dict

def filtrer_minerai(tas :List[Dict], type_cible:str, calibre_cible:str, purete_cible:str) ->List[Dict]:
    """
    Filtre un tas de minerai selon le type et le calibre spécifiés.
    Retourne une liste contenant uniquement les pierres correspondantes.
    """

    wagonnet = []
    for pierre in tas:
        #usage de .get qui est plus pro : si la clé n'existe pas ca permet au programme de tourner
        if pierre.get("type") == type_cible and pierre.get("calibre") == calibre_cible and pierre.get("purete") == purete_cible:
            wagonnet.append(pierre)
    return wagonnet

# ==========================================
# ZONE D'EXECUTION PRINCIPALE (CONTROL ROOM)
# ==========================================

if __name__ == "__main__":
    print("---Démarrage de la cabine de tri experte ---\n")
    #1. Nos données brutes (Data Source)
    tas_de_minerai = [ 
        {"type": "or", "calibre":"2", "purete":"haute"},
        {"type": "quartz", "calibre": "3" , "purete":"moyenne"},
        {"type": "emeraude", "calibre": "4", "purete":"moyenne"},
        {"type": "topaze", "calibre" : "5", "purete": "basse"},
        {"type": "quartz", "calibre": "3", "purete": "haute"}
    ]

    #2. On fait travailler notre machine avec des paramètres dynamiques
    resultat_tri = filtrer_minerai(tas=tas_de_minerai, type_cible="quartz", calibre_cible="3", purete_cible="haute")

    #3 affichage propre
    print("Commande prête pour la joaillerie")
    print(f"quantité extraite : {len(resultat_tri)}pierre(s) correspondante(s)")
    for pierre in resultat_tri:
        print(f"   -> {pierre['type'].capitalize()}(Purete:{pierre['purete']})")
    print("\n--- Fin des opérations---")