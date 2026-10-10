# 🚀 Projet 3 : Méga-Fusion (Pipeline ETL & Interface Tkinter)

Ce projet représente l'aboutissement de mes compétences en automatisation et en développement logiciel. Il s'agit d'un outil complet de type **ETL (Extract, Transform, Load)**, doté d'une interface graphique, conçu pour la surveillance de données de marché.

![Application de suivi de marché en cours de fonctionnement, montrant une interface Tkinter de surveillance de marché, avec des tableaux, des indicateurs de performance et des données de prix en temps réel sur un écran de bureau. La fenêtre principale affiche une vue densemble de plusieurs actifs financiers, avec des panneaux de suivi, des seuils de prise de profit et des indicateurs visuels de tendances. L environnement est minimaliste et professionnel, centré sur l analyse automatique des opportunités de trading. Le ton est sérieux et orienté produit, avec un usage fonctionnel et analytique.](./assets/App_fusion_suivi_marché.mp4)

## 🛠️ Architecture Technique

- **Front-End (Tkinter) :** Interface utilisateur interactive permettant le contrôle du moteur d'analyse, remplaçant l'usage classique de la ligne de commande.
- **Multithreading :** Exécution du processus d'analyse en arrière-plan (`threading.Thread`) pour garantir une interface fluide et non-bloquante pendant les calculs.
- **Moteur ETL autonome :**
  - **Extract :** Lecture continue d'un flux de données (dictionnaires Python simulant un flux d'API).
  - **Transform :** Filtrage algorithmique des actifs ayant atteint leur seuil critique (Take Profit).
  - **Load :** Génération automatique d'un livrable physique exploitable (`rapport_opportunites.txt`) avec horodatage précis.

## 🎯 Objectif Métier
Démontrer ma capacité à architecturer un produit logiciel de bout en bout : passer d'un script console basique à une véritable application de bureau robuste, tolérante aux pannes et générant de la donnée actionnable.

[def]: ./assets/App_fusion_suivi_marché.mp4