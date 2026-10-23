import numpy as np


# =====================================================================
# 1. Représentation des matrices en Python pur (sans bibliothèque)
# =====================================================================
# Une matrice est représentée par une liste de listes (lignes)

def creer_matrice_nulle(lignes, colonnes):
    """Crée une matrice nulle de dimensions (lignes x colonnes)."""
    return [[0.0 for _ in range(colonnes)] for _ in range(lignes)]


def afficher_matrice(M):
    """Affiche proprement une matrice."""
    for ligne in M:
        print([round(val, 4) for val in ligne])


# =====================================================================
# 2. Produit matriciel en Python pur
# =====================================================================

def produit_matriciel(A, B):
    """Multiplie deux matrices A (l_A x c_A) et B (l_B x c_B)."""
    l_A, c_A = len(A), len(A[0])
    l_B, c_B = len(B), len(B[0])

    if c_A != l_B:
        raise ValueError("Dimensions incompatibles pour le produit matriciel.")

    C = creer_matrice_nulle(l_A, c_B)
    for i in range(l_A):
        for j in range(c_B):
            somme = 0
            for k in range(c_A):
                somme += A[i][k] * B[k][j]
            C[i][j] = somme
    return C


# =====================================================================
# 3. Résolution d'un système linéaire par la méthode du Pivot de Gauss
# =====================================================================

def pivot_de_gauss(A, b):
    """Résout le système linéaire Ax = b par la méthode du pivot de Gauss simple.
    A est une matrice carrée (liste de listes), b est un vecteur colonne (liste).
    """
    n = len(A)
    # Copie pour ne pas modifier les objets originaux
    M = [row[:] for row in A]
    v = b[:]

    # Phase d'élimination vers l'avant
    for i in range(n):
        # Recherche du pivot maximal sur la colonne pour la stabilité numérique
        pivot = M[i][i]
        if abs(pivot) < 1e-12:
            raise ValueError(f"Pivot nul ou trop proche de zéro à l'indice {i}.")

        # Normalisation de la ligne i et élimination sur les lignes suivantes
        for j in range(i + 1, n):
            facteur = M[j][i] / pivot
            for k in range(i, n):
                M[j][k] -= facteur * M[i][k]
            v[j] -= facteur * v[i]

    # Phase de remontée (back-substitution)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = sum(M[i][k] * x[k] for k in range(i + 1, n))
        x[i] = (v[i] - somme) / M[i][i]

    return x


# =====================================================================
# 4. Utilisation de NumPy (Standard professionnel en BUT Informatique)
# =====================================================================

def resolution_avec_numpy(A_list, b_list):
    """Résout Ax = b en utilisant la bibliothèque optimisée NumPy."""
    A = np.array(A_list, dtype=float)
    b = np.array(b_list, dtype=float)

    # Résolution directe optimisée
    x = np.linalg.solve(A, b)
    return x


# =====================================================================
# Exemples d'utilisation et tests
# =====================================================================

if __name__ == "__main__":
    print("--- 1 & 2. Produit matriciel ---")
    A = [[1, 2],
         [3, 4]]
    B = [[5, 6],
         [7, 8]]

    C = produit_matriciel(A, B)
    print("Produit A x B (Python pur) :")
    afficher_matrice(C)

    print("\n--- 3. Pivot de Gauss maison ---")
    # Système :
    # 2x + y = 5
    # x + 3y = 5
    Mat_A = [[2.0, 1.0],
             [1.0, 3.0]]
    V_b = [5.0, 5.0]

    solution_gauss = pivot_de_gauss(Mat_A, V_b)
    print(f"Solution par Gauss : x = {solution_gauss[0]:.2f}, y = {solution_gauss[1]:.2f}")

    print("\n--- 4. Résolution avec NumPy ---")
    solution_np = resolution_avec_numpy(Mat_A, V_b)
    print(f"Solution par NumPy : {solution_np}")