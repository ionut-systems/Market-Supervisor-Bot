import time
from datetime import datetime

# BASE DE DONNÉES DU MARCHÉ
DATA_MARCHE = [
    {"actif": "Solana", "prix_actuel": 165.20, "take_profit": 160.00},
    {"actif": "Nvidia", "prix_actuel": 850.50, "take_profit": 900.00},
    {"actif": "Or", "prix_actuel": 2360.00, "take_profit": 2400.00},
    {"actif": "Sp500", "prix_actuel": 5250.00, "take_profit": 5200.00}
]

def executer_pipeline(callback_log, callback_fin):
    """
    Exécute le scan.
    callback_log: Fonction pour envoyer du texte à l'interface.
    callback_fin: Fonction pour prévenir l'interface que c'est terminé.
    """
    try:
        callback_log(f"\n[{datetime.now().strftime('%H:%M:%S')}] Démarrage de la Méga-Fusion...\n")
        opportunites = []

        for token in DATA_MARCHE:
            nom = token.get("actif", "Inconnu")
            prix = token.get("prix_actuel", 0.0)
            tp = token.get("take_profit", 0.0)

            time.sleep(0.5)

            if prix >= tp:
                message = f"🟢 ALERTE TP : {nom} a atteint {prix} (Objectif: {tp})\n"
                callback_log(message)
                opportunites.append(f"{nom} | Prix actuel: {prix} | Cible: {tp}")
            else:
                message = f"⚪ {nom} : Actuel {prix} - Sous l'objectif.\n"
                callback_log(message)

        # EXPORT DU RAPPORT
        if opportunites:
            fichier_nom = "rapport_opportunites.txt"
            with open(fichier_nom, "w", encoding="utf-8") as fichier:
                fichier.write(f"--- RAPPORT DE MARCHÉ : {datetime.now().strftime('%d/%m/%Y %H:%M')} ---\n\n")
                fichier.write("ACTIFS À CLÔTURER (TAKE PROFIT ATTEINT) :\n")
                for opp in opportunites:
                    fichier.write(f"- {opp}\n")
            
            callback_log(f"\n✅ FICHIER GÉNÉRÉ AVEC SUCCÈS : {fichier_nom}\n")
        else:
            callback_log("\n❌ Aucune opportunité détectée. Pas de fichier généré.\n")

        callback_log("--- FIN DU CYCLE ---\n")

    except Exception as e:
        callback_log(f"\n⚠️ ERREUR CRITIQUE : {str(e)}\n")
    
    finally:
        callback_fin() # Indique à l'interface de réactiver le bouton