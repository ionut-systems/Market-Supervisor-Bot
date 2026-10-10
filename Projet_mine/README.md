# 📁 Projet 1 : Filtre et Tri de Données (Cas pratique : Mine)

Ce répertoire illustre ma progression dans la structuration de code Python, en passant d'un script procédural simple à une architecture fonctionnelle et robuste.

## 🔄 Historique des versions

### 🔹 v1_script_basique.py
Il s'agit de la version initiale du projet. 
- **Approche :** Procédurale et linéaire.
- **Logique :** Tri d'une liste de dictionnaires via une boucle `for` et une condition `if`.
- **Limitation :** Paramètres codés en dur et vulnérabilité aux clés manquantes (`KeyError`).

### 🚀 v2_tri_expert.py
Refactoring complet pour atteindre les standards professionnels de production.
- **Modularité :** Création d'une fonction dédiée `filtrer_minerai()` paramétrable.
- **Type Hinting :** Typage statique des arguments et des retours (`List`, `Dict`, `str`) pour une meilleure lisibilité.
- **Sécurité (Error Handling) :** Utilisation de la méthode `.get()` sur les dictionnaires pour éviter les crashs si une donnée est corrompue.
- **Structure Standard :** Implémentation du point d'entrée `if __name__ == "__main__":` séparant la définition de l'outil de son exécution.

## 🛠 Compétences démontrées
- Refactoring et optimisation de code.
- Maîtrise des structures de données (Listes, Dictionnaires).
- Typage statique et sécurisation des variables.