# Projet : Fantasy Coach / Optimisation d'effectif Basketball (Version Avancée)
# Auteur : Noah (BUT Informatique)
# Description : Optimisation d'un 5 majeur avec contraintes budgétaires, de taille
# et de postes stricts (systèmes/matrices), avec analyse du temps d'exécution.

import time
import numpy as np
from itertools import combinations

# =====================================================================
# 1. Base de données élargie des joueurs
# =====================================================================
# Postes : 1 = Meneur, 2 = Arrière, 3 = Ailier, 4 = Intérieur, 5 = Pivot

JOUEURS = [
    {"nom": "Stephen Cooker.", "poste": 1, "salaire": 40.0, "per": 28.5, "taille": 188},
    {"nom": "Luka Donkich.", "poste": 1, "salaire": 42.0, "per": 31.0, "taille": 201},
    {"nom": "Trae old boy .", "poste": 1, "salaire": 34.0, "per": 23.5, "taille": 185},

    {"nom": "Devin B.", "poste": 2, "salaire": 35.0, "per": 24.0, "taille": 196},
    {"nom": "Anthony E.", "poste": 2, "salaire": 30.0, "per": 25.5, "taille": 193},
    {"nom": "Donovan M.", "poste": 2, "salaire": 33.0, "per": 26.0, "taille": 191},

    {"nom": "LeBron James.", "poste": 3, "salaire": 45.0, "per": 29.0, "taille": 206},
    {"nom": "Jayson T.", "poste": 3, "salaire": 38.0, "per": 26.5, "taille": 203},
    {"nom": "Kawhi L.", "poste": 3, "salaire": 39.0, "per": 27.0, "taille": 201},

    {"nom": "Giannis A.", "poste": 4, "salaire": 44.0, "per": 32.0, "taille": 211},
    {"nom": "Kevin Durant.", "poste": 4, "salaire": 41.0, "per": 29.5, "taille": 208},
    {"nom": "Zion W.", "poste": 4, "salaire": 31.0, "per": 24.5, "taille": 198},

    {"nom": "Nikolas Jakson .", "poste": 5, "salaire": 46.0, "per": 33.5, "taille": 211},
    {"nom": "Joel E.", "poste": 5, "salaire": 43.0, "per": 30.0, "taille": 213},
    {"nom": "Rudy G.", "poste": 5, "salaire": 25.0, "per": 21.0, "taille": 216}
]


# =====================================================================
# 2. Validation par calcul matriciel et contraintes de postes (TP4)
# =====================================================================

def verifier_contraintes(equipe_5, budget_max, taille_min_moyenne):
    """
    Vérifie l'ensemble des contraintes tactiques et budgétaires à l'aide de NumPy.
    """
    if len(equipe_5) != 5:
        return False

    salaires = np.array([j["salaire"] for j in equipe_5])
    tailles = np.array([j["taille"] for j in equipe_5])
    postes = [j["poste"] for j in equipe_5]

    # 1. Contrainte de poste strict : l'équipe doit contenir exactement un joueur par poste de 1 à 5
    # On utilise une matrice de comptage ou un test d'unicité trié
    if sorted(postes) != [1, 2, 3, 4, 5]:
        return False

    # 2. Contrainte budgétaire (Somme vectorielle)
    if np.sum(salaires) > budget_max:
        return False

    # 3. Contrainte de taille moyenne (Produit scalaire avec vecteur de poids 0.2)
    poids = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
    taille_moy = np.dot(tailles, poids)
    if taille_moy < taille_min_moyenne:
        return False

    return True


# =====================================================================
# 3. Algorithme de recherche avec analyse de performance
# =====================================================================

def trouver_meilleure_equipe(liste_joueurs, budget_max, taille_min):
    """
    Explore l'espace des combinaisons possibles et mesure le temps d'exécution.
    """
    debut_temps = time.time()

    meilleure_equipe = None
    max_per = -1.0
    combinaisons_testees = 0

    # Test de toutes les combinaisons de 5 joueurs parmi l'effectif global
    for equipe in combinations(liste_joueurs, 5):
        combinaisons_testees += 1
        if verifier_contraintes(equipe, budget_max, taille_min):
            per_total = sum(j["per"] for j in equipe)
            if per_total > max_per:
                max_per = per_total
                meilleure_equipe = equipe

    fin_temps = time.time()
    temps_execution = fin_temps - debut_temps

    return meilleure_equipe, max_per, combinaisons_testees, temps_execution


# =====================================================================
# Programme principal
# =====================================================================
if __name__ == "__main__":
    print("=== PROJET : FANTASY COACH BASKETBALL (MODE OPTIMISÉ) ===\n")

    BUDGET_MAX = 190.0  # en millions de $
    TAILLE_MIN_MOYENNE = 197.0  # en cm

    print(f"Effectif total disponible : {len(JOUEURS)} joueurs")
    print(f"Budget max autorisé : {BUDGET_MAX}M$")
    print(f"Taille moyenne minimale exigée : {TAILLE_MIN_MOYENNE} cm")
    print(f"Règle tactique : Exactement 1 joueur par poste (1 à 5).\n")

    print("Recherche de la meilleure combinaison en cours...")
    meilleur_cinq, score_max, nb_test, duree = trouver_meilleure_equipe(JOUEURS, BUDGET_MAX, TAILLE_MIN_MOYENNE)

    print("\n--- RÉSULTATS DE L'ANALYSE ---")
    print(f"Combinaisons testées : {nb_test}")
    print(f"Temps de calcul : {duree:.6f} secondes (Complexité testée)")

    if meilleur_cinq:
        print("\n>>> COMPOSITION DU 5 MAJEUR OPTIMAL <<<")
        cout_total = sum(j["salaire"] for j in meilleur_cinq)
        taille_moy = sum(j["taille"] for j in meilleur_cinq) / 5

        for joueur in meilleur_cinq:
            print(
                f"- Poste {joueur['poste']} | {joueur['nom']} | Salaire: {joueur['salaire']}M$ | PER: {joueur['per']} | Taille: {joueur['taille']}cm")

        print(f"\nBilan financier et sportif :")
        print(f"- Coût total : {cout_total}M$ / {BUDGET_MAX}M$")
        print(f"- Taille moyenne de l'équipe : {taille_moy:.1f} cm")
        print(f"- Score de performance global (PER cumulé) : {score_max:.1f}")
    else:
        print("\nAucune combinaison ne respecte l'ensemble des contraintes strictes.")