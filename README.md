# Simulation rapide du système de Lorenz

Ce dépôt contient une petite simulation du système de Lorenz (un modèle chaotique classique) et quelques scripts/plots associés.

Contenu du dossier
- `lorenz_solutions.py` : fonctions pour résoudre le système de Lorenz (intégration par la méthode d'Euler) et pour tracer les solutions.
- `simul_2_conditions.py` : script d'exemple qui exécute la simulation pour deux conditions initiales différentes, génère des graphiques et compare les trajectoires.
- `simulation.ipynb` : carnet Jupyter (notebook) présentant probablement des expériences interactives ou des visualisations complémentaires.
- `plots/` : dossier contenant les figures générées (ex. `simul_2_cond/` avec les images des simulations et comparaisons).

Dépendances
- Python 3.x
- numpy
- matplotlib

Installation rapide
1. Créez un environnement virtuel (optionnel) :
   python -m venv .venv
2. Activez l'environnement (Windows PowerShell) :
   .\.venv\Scripts\Activate.ps1
3. Installez les dépendances :
   pip install numpy matplotlib

Exécution
- Pour lancer la simulation d'exemple et produire les graphiques :
  python simul_2_conditions.py

Notes
- La résolution est réalisée ici par une intégration simple (méthode d'Euler) : c'est suffisant pour des démonstrations rapides, mais pas pour des simulations hautement précises. Pour des résultats plus fiables, utilisez des solveurs d'ordre supérieur (par exemple `scipy.integrate.solve_ivp`).
- Les figures sont enregistrées dans le dossier `plots/`.

But: Ceci est une simulation rapide à des fins pédagogiques et d'exploration.

Auteurs
- Dépôt fourni par l'utilisateur (scripts locaux).

Licence
- À ajouter selon vos préférences.

