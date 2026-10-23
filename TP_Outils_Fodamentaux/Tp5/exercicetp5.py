# TP5 : Synthèse - Résolution d'un problème complet de bout en bout
# Auteur : Noah (BUT Informatique)
# Ce script regroupe les notions clés des TP précédents (fonctions, structures de données,
# manipulation de listes et vérifications de robustesse).

import math


def charger_donnees(nom_fichier):
    """
    Petite fonction pour lire un fichier ligne par ligne et nettoyer les données.
    On gère le cas où le fichier n'existe pas pour éviter que le programme plante net.
    """
    print(f"Chargement du fichier : {nom_fichier}...")
    donnees = []
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne_propre = ligne.strip()
                if ligne_propre:  # on saute les lignes vides
                    donnees.append(ligne_propre)
        print(f"-> {len(donnees)} lignes chargées avec succès.")
        return donnees
    except FileNotFoundError:
        print("Erreur : le fichier est introuvable. Vérifie le chemin.")
        return []


def analyser_valeurs(liste_valeurs):
    """
    Parcourt une liste de valeurs numériques (converties en float)
    pour en extraire les métriques de base : min, max et moyenne.
    """
    if not liste_valeurs:
        return None, None, 0.0

    val_min = liste_valeurs[0]
    val_max = liste_valeurs[0]
    total = 0

    for v in liste_valeurs:
        if v < val_min:
            val_min = v
        if v > val_max:
            val_max = v
        total += v

    moyenne = total / len(liste_valeurs)
    return val_min, val_max, moyenne


def traitement_principal(elements):
    """
    Fonction de synthèse qui applique un traitement logique sur les données.
    Par exemple, filtre les éléments selon un seuil ou effectue un calcul itératif.
    """
    resultats = []
    for el in elements:
        # On essaie de convertir en nombre si possible, sinon on laisse en string
        try:
            valeur = float(el)
            # Petit traitement perso : si c'est positif, on prend la racine carrée
            if valeur >= 0:
                resultats.append(round(math.sqrt(valeur), 3))
            else:
                resultats.append(0.0)  # valeur négative gérée
        except ValueError:
            # Ce n'est pas un nombre, on garde une trace ou on ignore
            continue

    return resultats


# =====================================================================
# Bloc d'exécution principal
# =====================================================================
if __name__ == "__main__":
    print("=== DEBUT DU SCRIPT DE SYNTHESE (TP5) ===")

    # Test avec une liste de test en dur (pratique si pas de fichier sous la main)
    brut = ["12.5", "-4", "25", "abc", "9.0", "16"]
    print(f"Données de test brutes : {brut}")

    # Nettoyage et conversion rapide
    numeriques = []
    for x in brut:
        try:
            numeriques.append(float(x))
        except ValueError:
            pass  # on ignore les éléments non convertibles

    print(f"Après nettoyage (que des nombres) : {numeriques}")

    # Calculs stats
    mini, maxi, moy = analyser_valeurs(numeriques)
    print(f"Min : {mini} | Max : {maxi} | Moyenne : {moy:.2f}")

    # Application du traitement
    res_final = traitement_principal(brut)
    print(f"Résultats après traitement principal : {res_final}")

    print("=== FIN DU SCRIPT ===")