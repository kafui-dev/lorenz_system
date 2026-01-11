Projet Lorenz - Simulation rapide

Ce dépôt contient une petite simulation du système de Lorenz (méthode d'Euler explicite) et quelques scripts/visualisations.

Contenu du dossier

- simulation.ipynb : Notebook principal montrant la résolution du système de Lorenz pour plusieurs valeurs du paramètre r, des visualisations 2D/3D et une animation interactive (Plotly). Le notebook inclut une version optimisée de l'animation pour éviter l'envoi d'un très gros payload au navigateur.
- README.md : Ce fichier (en français).
- plots/ : Dossier contenant des images exportées de simulations/visualisations.
- scripts/lorenz_solutions.py : Fonctions pour calculer la solution (Euler explicite) — utilitaire.
- scripts/simul_2_conditions.py : Script pour lancer des simulations avec deux conditions initiales.

Rappel rapide

Il s'agit d'une simulation rapide et pédagogique, pas d'une mise en œuvre hautement optimisée ou validée numériquement pour usages scientifiques sévères. Les animations interactives dans `simulation.ipynb` peuvent devenir lentes si on construit trop de frames (grand nombre de points) : le notebook contient une version qui réduit le nombre de frames et échantillonne la trajectoire avant d'animer pour améliorer la réactivité.

Comment utiliser

1. Ouvrez `simulation.ipynb` dans Jupyter ou JupyterLab.
2. Exécutez les cellules du haut vers le bas.
3. Si l'animation bloque, exécutez la cellule marquée "optimisée" qui utilise un échantillonnage (downsampling) pour limiter le nombre de frames.

Licence

Usage pédagogique.

