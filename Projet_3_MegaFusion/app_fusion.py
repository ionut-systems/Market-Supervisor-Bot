import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import time
import threading

# ==========================================
# BASE DE DONNÉES DU MARCHÉ
# ==========================================
data_marche = [
    {"actif": "Solana" , "prix_actuel": 165.20, "take_profit": 160.00},
    {"actif": "Nvidia", "prix_actuel": 850.50, "take_profit": 900.00},
    {"actif": "Or", "prix_actuel": 2360.00, "take_profit": 2400.00},
    # J'ai mis le Sp500 au-dessus de son TP exprès pour déclencher l'alerte !
    {"actif": "Sp500", "prix_actuel": 5250.00, "take_profit": 5200.00} 
]

# ==========================================
# MOTEUR INTERNE (ETL : Extract, Transform, Load)
# ==========================================
def executer_pipeline():
    """Le moteur interne exécuté en arrière-plan"""
    bouton_lancer.config(state=tk.DISABLED) # On désactive le bouton pendant le scan
    zone_texte.insert(tk.END, f"\n[{datetime.now().strftime('%H:%M:%S')}] Démarrage de la Méga-Fusion...\n")
    
    opportunites = []
    
    # 1. SCAN & FILTRE (Extract & Transform)
    for token in data_marche:
        nom = token.get("actif", "Inconnu")
        prix = token.get("prix_actuel", 0.0)
        tp = token.get("take_profit", 0.0)
        
        # On ajoute un léger délai d'une demi-seconde pour simuler la requête réseau
        time.sleep(0.5) 
        
        if prix >= tp:
            message = f"🟢 ALERTE TP : {nom} a atteint {prix} (Objectif: {tp})\n"
            zone_texte.insert(tk.END, message)
            opportunites.append(f"{nom} | Prix actuel: {prix} | Cible: {tp}")
        else:
            message = f"⚪ {nom} : Actuel {prix} - Sous l'objectif.\n"
            zone_texte.insert(tk.END, message)
        
        zone_texte.see(tk.END) # Scroll automatique vers le bas
        
    # 2. EXPORT DU RAPPORT PHYSIQUE (Load)
    if opportunites:
        fichier_nom = "rapport_opportunites.txt"
        # Création et écriture du fichier
        with open(fichier_nom, "w", encoding="utf-8") as fichier:
            fichier.write(f"--- RAPPORT DE MARCHÉ : {datetime.now().strftime('%d/%m/%Y %H:%M')} ---\n\n")
            fichier.write("ACTIFS À CLÔTURER (TAKE PROFIT ATTEINT) :\n")
            for opp in opportunites:
                fichier.write(f"- {opp}\n")
        
        zone_texte.insert(tk.END, f"\n✅ FICHIER GÉNÉRÉ AVEC SUCCÈS : {fichier_nom}\n")
    else:
        zone_texte.insert(tk.END, "\n❌ Aucune opportunité détectée. Pas de fichier généré.\n")
        
    zone_texte.insert(tk.END, "--- FIN DU CYCLE ---\n")
    zone_texte.see(tk.END)
    bouton_lancer.config(state=tk.NORMAL) # On réactive le bouton

def lancer_fusion():
    """Fonction déclenchée par le bouton, utilise un Thread pour garder l'interface fluide"""
    threading.Thread(target=executer_pipeline, daemon=True).start()

# ==========================================
# CONFIGURATION DE L'INTERFACE GRAPHIQUE
# ==========================================
fenetre = tk.Tk()
fenetre.title("Superviseur de Marché (ETL)")
fenetre.geometry("600x400")
fenetre.configure(bg="#2c3e50")

titre = tk.Label(fenetre, text="Moteur d'Analyse et de Filtrage", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
titre.pack(pady=10)

bouton_lancer = tk.Button(fenetre, text="▶ LANCER LE SCAN", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", command=lancer_fusion)
bouton_lancer.pack(pady=10)

zone_texte = scrolledtext.ScrolledText(fenetre, width=70, height=15, bg="black", fg="#00ff00", font=("Consolas", 10))
zone_texte.pack(pady=10)
zone_texte.insert(tk.END, "Interface initialisée. En attente de lancement...\n")

if __name__ == "__main__":
    fenetre.mainloop()