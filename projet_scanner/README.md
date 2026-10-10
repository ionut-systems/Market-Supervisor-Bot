# 📈 Projet 2 : Scanner de Marché Autonome

Ce répertoire démontre ma capacité à concevoir et sécuriser un processus s'exécutant en arrière-plan (daemon), appliqué à la surveillance de données financières.

## 🔄 Historique des versions

### 🔹 v1_scanner_basique.py
Prototype fonctionnel du moteur de scan.
- **Logique :** Boucle `while True` avec temporisation `time.sleep()`.
- **Fonctionnalité :** Détection de seuils (Take Profit) sur une liste de dictionnaires.
- **Contrôle :** Limiteur de cycles basique intégré.

### 🚀 v2_scanner_expert.py
Refactoring orienté production et tolérance aux pannes.
- **Horodatage :** Intégration du module `datetime` pour un tracking précis des événements.
- **Fail-Safe :** Sécurisation des accès aux données avec la méthode `.get()` et attribution de valeurs de repli (0.0) pour éviter tout crash en cas de perte de flux de l'API.
- **Modularité :** Encapsulation dans une fonction paramétrable (`cycles_max`, `intervalle_sec`) avec typage statique (`List`, `Dict`).
- **Structure :** Utilisation du point d'entrée `if __name__ == "__main__":`.