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

# Tri fusion
# Stable 

# Tri rapide
# Pas stable

# Tri par tas
# Pas stable

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