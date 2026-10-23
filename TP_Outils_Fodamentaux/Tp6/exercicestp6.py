# TP6 : Géométrie du plan
# Auteur : Noah (BUT Informatique)
# Ce script gère les bases de la géométrie vectorielle 2D :
# vecteurs, distances, déterminant, aire de triangles et test point dans un polygone.

import math


# =====================================================================
# 1. Manipulation de vecteurs et points (représentés par des tuples (x, y))
# =====================================================================

def creer_vecteur(A, B):
    """Crée un vecteur AB à partir de deux points A et B."""
    return (B[0] - A[0], B[1] - A[1])


def longueur_vecteur(v):
    """Calcule la norme (longueur) d'un vecteur."""
    return math.sqrt(v[0] ** 2 + v[1] ** 2)


def distance_points(A, B):
    """Calcule la distance euclidienne entre deux points A et B."""
    v = creer_vecteur(A, B)
    return longueur_vecteur(v)


def produit_scalaire(u, v):
    """Calcule le produit scalaire de deux vecteurs u et v."""
    return u[0] * v[0] + u[1] * v[1]


def determinant(u, v):
    """Calcule le déterminant (produit en croix 2D) de deux vecteurs."""
    return u[0] * v[1] - u[1] * v[0]


# =====================================================================
# 2. Calcul d'aires géométriques
# =====================================================================

def aire_triangle(A, B, C):
    """
    Calcule l'aire d'un triangle ABC en utilisant le déterminant
    des vecteurs AB et AC.
    """
    u = creer_vecteur(A, B)
    v = creer_vecteur(A, C)
    # L'aire d'un triangle c'est la moitié de la valeur absolue du déterminant
    return abs(determinant(u, v)) / 2.0


# =====================================================================
# 3. Test d'appartenance : Point dans un polygone (Ray Casting)
# =====================================================================

def point_dans_polygone(P, polygone):
    """
    Détermine si un point P(x, y) est à l'intérieur d'un polygone
    en utilisant l'algorithme des rayonnements (ray casting).
    'polygone' est une liste de points ordonnés [(x1, y1), (x2, y2), ...]
    """
    x, y = P
    n = len(polygone)
    interieur = False

    p1x, p1y = polygone[0]
    for i in range(n + 1):
        p2x, p2y = polygone[i % n]
        # On vérifie si le rayon horizontal partant de P coupe le segment [p1, p2]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        interieur = not interieur
        p1x, p1y = p2x, p2y

    return interieur


# =====================================================================
# Bloc d'exécution principal / Tests
# =====================================================================

if __name__ == "__main__":
    print("=== DEBUT DU SCRIPT TP6 : GÉOMÉTRIE DU PLAN ===")

    # Définition de quelques points pour tester
    A = (0.0, 0.0)
    B = (4.0, 0.0)
    C = (0.0, 3.0)

    print(f"Distance entre A{A} et B{B} : {distance_points(A, B)}")

    # Test de l'aire du triangle ABC (triangle rectangle de côtés 3 et 4, aire = 6)
    aire = aire_triangle(A, B, C)
    print(f"Aire du triangle ABC : {aire}")

    # Test pour un polygone (un rectangle de sommets (0,0), (4,0), (4,3), (0,3))
    rectangle = [(0.0, 0.0), (4.0, 0.0), (4.0, 3.0), (0.0, 3.0)]

    point_dedans = (2.0, 1.5)
    point_dehors = (5.0, 5.0)

    print(f"Le point {point_dedans} est dans le polygone ? -> {point_dans_polygone(point_dedans, rectangle)}")
    print(f"Le point {point_dehors} est dans le polygone ? -> {point_dans_polygone(point_dehors, rectangle)}")

    print("=== FIN DU SCRIPT TP6 ===")