# 📈 Market Supervisor Bot (V1.1)

Bienvenue sur le dépôt du **Market Supervisor Bot**. Cet outil est un exécutable de bureau autonome (RPA léger) conçu pour automatiser la surveillance d'actifs, l'analyse de données et la génération de rapports métier en temps réel.

<div align="center">
  <img width="856" height="480" alt="Démo Market Supervisor" src="https://github.com/user-attachments/assets/3faa9cf0-1119-4292-a740-d0f368cdf517" />
</div>

## 🎯 Cas d'usage & Valeur Ajoutée
- **Automatisation (ETL) :** Extraction des données de marché, analyse par rapport à des seuils critiques (Take Profit), et génération de rapports physiques exploitables.
- **Gain de temps de production :** Alertes visuelles instantanées permettant d'optimiser la prise de décision, supprimant la nécessité de surveiller manuellement les cours.

## 🛠️ Stack Technique & Architecture (V1.1 "Clean Code")
- **Langage :** Python 3.x
- **GUI :** Tkinter (Bibliothèque native, approche orientée objet pour une interface fluide).
- **Déploiement :** PyInstaller (Compilation standalone furtive `--noconsole` pour un rendu logiciel de bureau 100 % propre).
- **Architecture :** Conception modulaire avec découplage strict des responsabilités :
  - `moteur.py` : Cœur logique (ETL) et traitement des données isolés.
  - `gui.py` : Gestion exclusive de l'interface visuelle (POO).
  - `main.py` : Chef d'orchestre léger reliant le moteur et la vue. Intégration du multithreading pour garantir la stabilité de l'application pendant les cycles de scan.

## 🚀 Fonctionnalités Clés
- **Scan en arrière-plan :** Boucle d'analyse continue sans gel de l'interface (Threading).
- **Alertes Dynamiques :** Détection et notification du franchissement des objectifs.
- **Reporting Automatisé :** Génération de fichiers texte horodatés (`rapport_opportunites.txt`) récapitulant les actifs à clôturer.
- **Résilience :** Gestion des exceptions (`try/except`) pour assurer la stabilité du processus en cas de coupure réseau.

## 📦 Release Notes (V1.1)
- Refonte architecturale totale (passage du script monolithique à une structure Modèle-Vue-Contrôleur simplifiée).
- Déploiement de `MSv1.1.exe` en mode furtif (suppression de la console d'arrière-plan).
