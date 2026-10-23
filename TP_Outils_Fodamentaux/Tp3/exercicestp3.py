import matplotlib.pyplot as plt


# =====================================================================
# 1. Représentation et évaluation de polynômes
# =====================================================================
# Un polynôme P(x) = a_0 + a_1*x + a_2*x^2 + ... + a_n*x^n
# est représenté par la liste de ses coefficients [a_0, a_1, ..., a_n]

def eval_polynome(P, x):
    """Évalue un polynôme P en un point x en utilisant la méthode de Horner.
    La méthode de Horner est plus efficace et stable numériquement :
    P(x) = a_0 + x*(a_1 + x*(a_2 + ...))
    """
    resultat = 0
    for coeff in reversed(P):
        resultat = resultat * x + coeff
    return resultat


# =====================================================================
# 2. Dérivation d'un polynôme
# =====================================================================

def derivee_polynome(P):
    """Calcule la liste des coefficients du polynôme dérivé P'.
    Si P(x) = a_0 + a_1*x + a_2*x^2 + ... + a_n*x^n,
    alors P'(x) = a_1 + 2*a_2*x + ... + n*a_n*x^(n-1)
    """
    if len(P) <= 1:
        return [0]
    return [i * P[i] for i in range(1, len(P))]


# =====================================================================
# 3. Recherche de racine par dichotomie
# =====================================================================

def dichotomie(f, a, b, eps=1e-6, max_iter=1000):
    """Trouve une racine de la fonction f sur l'intervalle [a, b]
    par la méthode de la dichotomie (nécessite f(a) et f(b) de signes opposés).
    """
    if f(a) * f(b) > 0:
        raise ValueError("La fonction doit être de signes opposés en a et b (TVI).")

    for _ in range(max_iter):
        m = (a + b) / 2.0
        if abs(f(m)) < eps or (b - a) / 2.0 < eps:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2.0


# =====================================================================
# 4. Tracé de fonctions et polynômes avec Matplotlib
# =====================================================================

def tracer_fonction(f, x_min, x_max, nb_points=500, titre="Courbe"):
    """Trace la courbe représentative d'une fonction f sur [x_min, x_max]."""
    dx = (x_max - x_min) / (nb_points - 1)
    X = [x_min + i * dx for i in range(nb_points)]
    Y = [f(x) for x in X]

    plt.figure(figsize=(8, 5))
    plt.plot(X, Y, label=titre, color='blue', linewidth=2)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title(titre)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


# =====================================================================
# Exemples d'utilisation et tests
# =====================================================================

if __name__ == "__main__":
    # Exemple : P(x) = 2 - 3x + x^3  -> coefficients [2, 0, -3, 1]
    P = [2, 0, -3, 1]

    print("--- 1. Évaluation ---")
    print(f"P(2) = {eval_polynome(P, 2)}")  # 2 - 6 + 8 = 4

    print("\n--- 2. Dérivation ---")
    # P'(x) = -3 + 3x^2 -> coefficients [-3, 0, 3]
    dP = derivee_polynome(P)
    print(f"Coefficients de la dérivée P' : {dP}")

    print("\n--- 3. Recherche de racine ---")


    # Conversion du polynôme en fonction Python standard
    def f(x):
        return eval_polynome(P, x)


    racine = dichotomie(f, -3, -1)
    print(f"Racine trouvée par dichotomie sur [-3, -1] : {racine:.6f}")
    print(f"Vérification f(racine) = {f(racine)}")

    # Décommente la ligne ci-dessous si tu exécutes le script sur ta machine pour afficher le graphique
    # tracer_fonction(f, -3, 3, titre="P(x) = 2 - 3x + x^3")