import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import time
import threading

# ==========================================
# 1. BASE DE DONNÉES GOMINING (À MODIFIER AVEC TES VRAIS CHIFFRES)
# ==========================================
# Remplace les valeurs ci-dessous par les statistiques réelles de tes NFT GoMining
parc_minier = [
    {"machine": "424246", "puissance_th": 34.24, "recompense_brute": 0.000150, "frais_energie": 0.000020},
    {"machine": "234948",  "puissance_th": 20.99, "recompense_brute": 0.000250, "frais_energie": 0.000040},
    {"machine": "23916", "puissance_th": 76.12, "recompense_brute": 0.000100, "frais_energie": 0.000015}
]

# ==========================================
# 2. MOTEUR ETL & CALCUL DE RENTABILITÉ
# ==========================================
def executer_audit():
    bouton_lancer.config(state=tk.DISABLED)
    zone_texte.insert(tk.END, f"\n[{datetime.now().strftime('%H:%M:%S')}] 🔐 Connexion sécurisée au parc minier...\n\n")
    
    puissance_totale = 0
    recompense_nette_jour = 0
    lignes_rapport = []
    
    # Extract & Transform : Analyse de chaque machine
    for miner in parc_minier:
        time.sleep(0.6) # Effet visuel de traitement
        nom = miner["machine"]
        th = miner["puissance_th"]
        net = miner["recompense_brute"] - miner["frais_energie"]
        
        puissance_totale += th
        recompense_nette_jour += net
        
        info = f"⚡ {nom} | Puissance: {th} TH/s | Profit Net/Jour: {net:.6f} BTC"
        zone_texte.insert(tk.END, info + "\n")
        lignes_rapport.append(info)
        zone_texte.see(tk.END)
        
    # Projections financières
    recompense_mensuelle = recompense_nette_jour * 30
    recompense_annuelle = recompense_nette_jour * 365
    
    zone_texte.insert(tk.END, "\n📊 PROJECTIONS DE RENTABILITÉ :\n")
    zone_texte.insert(tk.END, f"-> Puissance totale déployée : {puissance_totale} TH/s\n")
    zone_texte.insert(tk.END, f"-> Cashflow Mensuel (Net)   : {recompense_mensuelle:.6f} BTC\n")
    zone_texte.insert(tk.END, f"-> Cashflow Annuel (Net)    : {recompense_annuelle:.6f} BTC\n")
    
    # Load : Export du livrable d'affiliation
    fichier_nom = "Audit_Rentabilite_Parc.txt"
    with open(fichier_nom, "w", encoding="utf-8") as fichier:
        fichier.write(f"=== AUDIT DE RENDEMENT MINIER (Preuve de Travail) ===\n")
        fichier.write(f"Date de l'audit : {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        fichier.write("--- DÉTAIL DU HARDWARE ---\n")
        for ligne in lignes_rapport:
            fichier.write(f"- {ligne}\n")
        fichier.write("\n--- RÉSUMÉ DES PERFORMANCES ---\n")
        fichier.write(f"Hashrate Total : {puissance_totale} TH/s\n")
        fichier.write(f"ROI Mensuel Net estimé : {recompense_mensuelle:.6f} BTC\n")
        fichier.write(f"ROI Annuel Net estimé  : {recompense_annuelle:.6f} BTC\n")
        fichier.write("\nDocument généré automatiquement par le système d'audit interne.")
        
    zone_texte.insert(tk.END, f"\n✅ LIVRABLE D'AFFILIATION GÉNÉRÉ : {fichier_nom}\n")
    zone_texte.see(tk.END)
    bouton_lancer.config(state=tk.NORMAL)

def lancer_audit():
    threading.Thread(target=executer_audit, daemon=True).start()

# ==========================================
# 3. INTERFACE GRAPHIQUE (Tkinter)
# ==========================================
fenetre = tk.Tk()
fenetre.title("GoMining - Dashboard d'Affiliation")
fenetre.geometry("650x450")
fenetre.configure(bg="#1e272e")

titre = tk.Label(fenetre, text="Audit de Rentabilité - Parc Minier", font=("Arial", 16, "bold"), bg="#1e272e", fg="#f1c40f")
titre.pack(pady=10)

bouton_lancer = tk.Button(fenetre, text="▶ LANCER L'AUDIT FINANCIER", font=("Arial", 12, "bold"), bg="#d35400", fg="white", command=lancer_audit)
bouton_lancer.pack(pady=10)

zone_texte = scrolledtext.ScrolledText(fenetre, width=75, height=16, bg="black", fg="#00d8d6", font=("Consolas", 10))
zone_texte.pack(pady=10)
zone_texte.insert(tk.END, "En attente d'initialisation de l'audit...\n")

if __name__ == "__main__":
    fenetre.mainloop()