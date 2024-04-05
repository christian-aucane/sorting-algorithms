import time 
import random

# Ma liste aléatoire : 
liste_aleatoire = [random.randint(1, 1000) for i in range(15)]

# Tri par sélection
# Pas stable
def tri_selection(liste):
    # Début de l'enregistrement de mon temps
    top_chrono = time.time() 
    # Calculateur du nombre de permutation à 0
    nb_permutations = 0
    
    print(f"""Ma liste aléatoire et non triée est : 
{liste}""")
    # Longueur de ma liste
    longueur_liste = len(liste)

    # Boucle pour chaque élèments de ma liste + 1
    for i in range(longueur_liste + 1):
        # Création de la variable petit_nombre = i 
        petit_nombre = i
        # Boucle pour parcourir les élèments restants de ma liste
        for j in range(i+1, longueur_liste) :
            # Condition de comparaison :
            # Si l'élèment actuel est plus petit que 
            # l'élèment le plus petit trouvé, 
            if liste[j] < liste[petit_nombre] :
                # l'élèment actuel devient l'élèment le plus petit.
                petit_nombre = j
        # Si l'élèment le plus petit est différent de l'élèment actuel 
        if petit_nombre != i :
            # échange de position 
            liste[i], liste[petit_nombre] = liste[petit_nombre], liste[i]
            nb_permutations += 1
    
    temps_fini = time.time()
    mesure_temps = temps_fini - top_chrono
    print()
    print(f"""Ma liste triée avec le tri de sélection est :
{liste}""")
    print()
    print(f"""Temps d'exécution : {round(mesure_temps * 1000, 6)} ms""")
    print(f"""Nombre d'échanges : {nb_permutations}""")

# Exécution
tri_selection(liste_aleatoire)

# Tri à bulles (≠ tri à gnomes)
# Stable
def tri_bulles(liste):
    top_chrono = time.time() 
    nb_permutations = 0
    
    print(f"""Ma liste aléatoire et non triée est : 
{liste}""")
    longueur_liste = len(liste)

    for passe in range(longueur_liste - 1, 0, -1):
        echange = False
        for i in range(passe):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                nb_permutations += 1
                echange = True
        if not echange:
            break

    temps_fini = time.time()
    mesure_temps = temps_fini - top_chrono
    print()
    print(f"""Ma liste triée avec le tri de sélection est :
{liste}""")
    print()
    print(f"""Temps d'exécution : {round(mesure_temps*1000, 6)} ms""")
    print(f"""Nombre d'échanges : {nb_permutations}""")

# Exécution
tri_bulles(liste_aleatoire)

# Tri par insertion
# Stable
def tri_insertion(liste):
    # Début de l'enregistrement de mon temps
    top_chrono = time.time() 
    # Calculateur du nombre de permutation à 0
    nb_permutations = 0

    print(f"""Ma liste aléatoire et non triée est : 
{liste}""")

    # Boucle pour parcourir la liste de 1 à la longueur de la liste
    # On considère que 0 est à la bonne place
    for i in range(1, len(liste)):
        nb_permuter = liste[i]
        n = i - 1

        # Pendant que (i -1) est supérieur à 0,
        # et le nombre à permuter est inférieur 
        # au nombre le précédent
        while n >= 0 and nb_permuter < liste[n]:
            # de la valeur à droite pour faire de la place
            liste [n + 1] = liste [n]
            # Calcul du nombre de permumu
            nb_permutations +=1
            # on enlève - 1 pour pouvoir comparer à l'élément précédent
            n -= 1
        # on permute l'élèment à la place 
        liste [n + 1] = nb_permuter
    
    temps_fini = time.time()
    mesure_temps = temps_fini - top_chrono
    print()
    print(f"""Ma liste triée avec le tri d'insertion est :
{liste}""")
    print()
    print(f"""Temps d'exécution : {round(mesure_temps*1000, 6)} ms""")
    print(f"""Nombre d'échanges : {nb_permutations}""")

# Exécution
tri_insertion(liste_aleatoire)

# Tri fusion
# Stable 


# Tri rapide
# Pas stable

# Tri par tas
# Pas stable
# Création d'une classe pour encapsuler mes deux fonctions du tri par tas
class tri_tas:
    # Initialisation de l'objet tri_tas
    def __init__(self):
        self.nb_permutations = 0
        # Attribut nb_permutations pour calculer le nb de permu

    def trier(self, tas):
        # Lancement du compteur
        top_chrono = time.time() 

        # Première fonction pour entasser ma liste en tas
        # en créant des noeuds avec des fils : gauche et droite
        def entasser(tas, i, len_table):
            maximum = i
            gauche = 2 * i + 1
            droite = 2 * i + 2

            if gauche < len_table and tas[gauche] > tas[maximum]:
                maximum = gauche
            if droite < len_table and tas[droite] > tas[maximum]:
                maximum = droite
            if maximum != i:
                tas[i], tas[maximum] = tas[maximum], tas[i]
                self.nb_permutations += 1
                entasser(tas, maximum, len_table)

        # Deuxième fonction trier qui contient la fonction construction
        # du tas. 
        len_table = len(tas)

        # Boucle interne de la fonction qui itère sur les noeuds du tas
        # Elle part du dernier noeud interne 'n // 2 - 1' et jusqu'à la racine.
        for i in range(len_table // 2 - 1, -1, -1):
            entasser(tas, i, len_table)

        # Boucle qui itère à l'intérieur des indices
        # de la fin à la racine 
        # Elle permet de permuter les numéros 
        for i in range(n - 1, 0, -1):
            tas[0], tas[i] = tas[i], tas[0]
            entasser(tas, 0, i)
        
        # Temps
        temps_fini = time.time()
        mesure_temps = temps_fini - top_chrono
        print()
        print(f"""Temps d'exécution : {round(mesure_temps*1000, 6)} ms""")
        print(f"""Nombre d'échanges : {self.nb_permutations}""")

# Exécution
print(f"""Liste non triée: {liste_aleatoire}""")
tri = tri_tas()
tri.trier(liste_aleatoire)
print()
print(f"""Liste triée par tas: {liste_aleatoire}""")

# Tri à peigne // comb sort 
# Pas stable

def tri_peigne(liste):
    # Début de l'enregistrement de mon temps
    top_chrono = time.time() 
    # Calculateur du nombre de permutation à 0
    nb_permutations = 0
    
    print(f"""Ma liste aléatoire et non triée est : 
{liste}""")
    longueur_liste = len(liste)
    echange = True
    
    while echange or longueur_liste>1:
      # échange n'est pas vrai
      echange = False
      # réduction progressive de l'écart
      # l'écart ne devrait pas être <1
      longueur_liste = max(longueur_liste * 10//13, 1)
      # facteur de réduction = 10//13 soit 1,3
      if longueur_liste<1: longueur_liste=1
      for i in range(0, len(liste) - longueur_liste):
            if liste[i]> liste[i + longueur_liste]:
                echange = True
                # échange de position parce que echange = True
                liste[i], liste[i + longueur_liste] = liste[i + longueur_liste], liste[i]
                nb_permutations += 1
    temps_fini = time.time()
    mesure_temps = temps_fini - top_chrono
    print()
    print(f"""Ma liste triée avec le tri de peigne est :
{liste}""")
    print()
    print(f"""Temps d'exécution : {round(mesure_temps*1000, 6)} ms""")
    print(f"""Nombre d'échanges : {nb_permutations}""")

# Exécution 
tri_peigne(liste_aleatoire)