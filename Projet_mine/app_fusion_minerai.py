import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import time
import threading

# ==========================================
# 1. BASE DE DONNÉES (Data Source)
# ==========================================
tas_de_minerai = [ 
    {"type": "or", "calibre":"2", "purete":"haute"},
    {"type": "quartz", "calibre": "3" , "purete":"moyenne"},
    {"type": "emeraude", "calibre": "4", "purete":"moyenne"},
    {"type": "topaze", "calibre" : "5", "purete": "basse"},
    {"type": "quartz", "calibre": "3", "purete": "haute"}
]

# ==========================================
# 2. MOTEUR ETL & LOGIQUE DE FILTRAGE
# ==========================================
def executer_pipeline():
    bouton_lancer.config(state=tk.DISABLED)
    zone_texte.insert(tk.END, f"\n[{datetime.now().strftime('%H:%M:%S')}] Démarrage de la cabine de tri experte...\n")
    
    # Paramètres cibles (Extract condition)
    type_cible = "quartz"
    calibre_cible = "3"
    purete_cible = "haute"
    
    wagonnet = []
    
    zone_texte.insert(tk.END, f"[FILTRE ACTIF] Recherche : {type_cible.capitalize()} | Calibre: {calibre_cible} | Pureté: {purete_cible}\n\n")
    
    # Transform (Filtrage)
    for pierre in tas_de_minerai:
        time.sleep(0.5) # Simulation du tapis roulant
        p_type = pierre.get("type", "inconnu")
        p_calibre = pierre.get("calibre", "inconnu")
        p_purete = pierre.get("purete", "inconnue")
        
        if p_type == type_cible and p_calibre == calibre_cible and p_purete == purete_cible:
            message = f"🟢 SÉLECTIONNÉ : {p_type.capitalize()} (Calibre: {p_calibre}, Pureté: {p_purete})\n"
            zone_texte.insert(tk.END, message)
            wagonnet.append(pierre)
        else:
            message = f"⚪ Rejeté : {p_type.capitalize()} (Calibre: {p_calibre}, Pureté: {p_purete})\n"
            zone_texte.insert(tk.END, message)
        
        zone_texte.see(tk.END)
        
    # Load (Génération du livrable physique)
    if wagonnet:
        fichier_nom = "bon_de_commande_joaillerie.txt"
        with open(fichier_nom, "w", encoding="utf-8") as fichier:
            fichier.write(f"--- BON DE COMMANDE JOAILLERIE : {datetime.now().strftime('%d/%m/%Y %H:%M')} ---\n\n")
            fichier.write(f"Filtres de la commande : Type={type_cible.capitalize()}, Calibre={calibre_cible}, Pureté={purete_cible}\n")
            fichier.write(f"Quantité extraite : {len(wagonnet)} pierre(s)\n\n")
            fichier.write("DÉTAIL DU WAGONNET :\n")
            for p in wagonnet:
                fichier.write(f"-> {p.get('type').capitalize()} | Calibre: {p.get('calibre')} | Pureté: {p.get('purete')}\n")
                
        zone_texte.insert(tk.END, f"\n✅ LIVRABLE GÉNÉRÉ : {fichier_nom}\n")
    else:
        zone_texte.insert(tk.END, "\n❌ Aucune pierre ne correspond. Pas de livrable.\n")
        
    zone_texte.insert(tk.END, "--- FIN DES OPÉRATIONS ---\n")
    zone_texte.see(tk.END)
    bouton_lancer.config(state=tk.NORMAL)

def lancer_tri():
    threading.Thread(target=executer_pipeline, daemon=True).start()

# ==========================================
# 3. INTERFACE GRAPHIQUE (Tkinter)
# ==========================================
fenetre = tk.Tk()
fenetre.title("Superviseur de Tri - Joaillerie")
fenetre.geometry("600x420")
fenetre.configure(bg="#2c3e50")

titre = tk.Label(fenetre, text="Moteur de Tri & Filtrage de Minerai", font=("Arial", 16, "bold"), bg="#2c3e50", fg="#f39c12")
titre.pack(pady=10)

bouton_lancer = tk.Button(fenetre, text="▶ LANCER LE TRI EXPERT", font=("Arial", 12, "bold"), bg="#2980b9", fg="white", command=lancer_tri)
bouton_lancer.pack(pady=10)

zone_texte = scrolledtext.ScrolledText(fenetre, width=70, height=15, bg="black", fg="#f39c12", font=("Consolas", 10))
zone_texte.pack(pady=10)
zone_texte.insert(tk.END, "Système de tri initialisé. En attente d'exécution...\n")

if __name__ == "__main__":
    fenetre.mainloop()