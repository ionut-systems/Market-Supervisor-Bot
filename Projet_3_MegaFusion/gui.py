import tkinter as tk
from tkinter import scrolledtext

class ApplicationInterface:
    def __init__(self, fenetre, commande_lancer):
        self.fenetre = fenetre
        self.commande_lancer = commande_lancer
        
        self.fenetre.title("Superviseur de Marché (V1.1)")
        self.fenetre.geometry("600x400")
        self.fenetre.configure(bg="#2c3e50")

        self.titre = tk.Label(fenetre, text="Moteur d'Analyse et de Filtrage", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
        self.titre.pack(pady=10)

        self.bouton_lancer = tk.Button(fenetre, text="▶ LANCER LE SCAN", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", command=self._on_click_lancer)
        self.bouton_lancer.pack(pady=10)

        self.zone_texte = scrolledtext.ScrolledText(fenetre, width=70, height=15, bg="black", fg="#00ff00", font=("Consolas", 10))
        self.zone_texte.pack(pady=10)
        self.zone_texte.insert(tk.END, "Interface initialisée. En attente de lancement...\n")

    def _on_click_lancer(self):
        self.bouton_lancer.config(state=tk.DISABLED)
        # On passe à la fonction externe les moyens de communiquer avec l'interface
        self.commande_lancer(self.afficher_log, self.reactiver_bouton)

    def afficher_log(self, message):
        # Sécurité pour éviter les crashs Tkinter liés aux threads
        self.fenetre.after(0, self._inserer_texte, message)

    def _inserer_texte(self, message):
        self.zone_texte.insert(tk.END, message)
        self.zone_texte.see(tk.END)

    def reactiver_bouton(self):
        self.fenetre.after(0, lambda: self.bouton_lancer.config(state=tk.NORMAL))