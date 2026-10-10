import time
from datetime import datetime
from typing import List, Dict

def scanner_marche(portefeuille:List[Dict], cycles_max: int = 3, intervalle_sec: int = 60) -> None:

    """
    Moteur de scan de marché autonome.
    Surveille les prix et déclenche des alertes Take Profit de manière sécurisée
    """

    cycle_effectue = 0

    while True:
        cycle_effectue +=1
        #Ajout horodatage(obligatoire dans les outils financiers)
        heure_actuelle = datetime.now().strftime("%H:%M:%S")
        print(f"[{heure_actuelle}] --- Cycle de scan n°{cycle_effectue}---")

        for token in portefeuille:
        #sécurisation absolue : si une clé saute, on donne une valeur par défaut (0.0 ou "Inconnu")
            nom = token.get("actif", "Inconnu")
            prix = token.get("prix_actuel", 0.0)
            tp = token.get("take_profit", 0.0)

        if prix >= tp:
            print(f"ALERTE TP: {nom} déclenche le profit à {tp}!")
        else:
            print(f"{nom} suit les prix du marché (Actuel: {prix})")

    #Superviseur de cycle (Kill Switch)
        if cycle_effectue >= cycles_max:
            print("\n limite de cycles atteint: le programme coupe ses positions et s'éteint proprement.")
            break

    print(f"\n En attente ({intervalle_sec}s) pour le prochain scan...\n")
    time.sleep(intervalle_sec)

    # ==========================================
# ZONE D'EXECUTION PRINCIPALE (CONTROL ROOM)
# ==========================================

if __name__ == "__main__":
    print("Démarrage du Superviseur de Marché...\n")

    #1. Base de données
    data_marche = [
        {"actif": "Solana" , "prix_actuel" : 165.20, "take_profit": 160.00},
        {"actif": "Nvidia" , "prix_actuel" : 850.50, "take_profit": 900.00},
        {"actif" : "Or" , "prix_actuel" : 2360.00, "take_profit": 2400.00},
        {"actif" : "Sp500" , "prix_actuel" : 5120.00, "take_profit": 5200.00}
    ]

    # 2. Lancement du moteur (j'ai mis 2 secondes d'intervalle pour que tu testes dans attendre 1 minute !)
    scanner_marche(portefeuille=data_marche, cycles_max=3, intervalle_sec=2)