import time 
import random

long_liste = int(input("Veuillez choisir une longueur de liste :"))

# Ma liste aléatoire : 
liste_aleatoire = [random.randint(1, 1000) for i in range(long_liste)]

print("Ma liste à trier :")
print(liste_aleatoire)

class Trier:


    def __init__(self, liste):
        self.liste = liste
        
        # Dictionnaire des noms et de leurs résumés
        self.nom_tri = {
            1: ("Tri par sélection", "sélectionne progressivement l'élément minimum et le place à la bonne position."),
            2: ("Tri à bulles", "compare les éléments adjacents et les échange si nécessaire jusqu'à ce que tous les éléments soient ordonnés."),
            3: ("Tri par insertion", "insère chaque élément à sa place correcte parmi les éléments déjà triés, étendant ainsi la partie triée de la liste."),
            4: ("Tri fusion", "divise récursivement la liste en deux moitiés, trie chaque moitié séparément, puis les fusionne."),
            5: ("Tri rapide", "partitionne la liste autour d'un pivot, échange les éléments autour du pivot pour les ordonner."),
            6: ("Tri par tas", "organise les éléments dans un tas, puis réorganise le tas pour que l'élément racine soit le plus grand."),
            7: ("Tri à peigne", "- une variante du tri à bulles qui échange les éléments à des intervalles plus grands."),
        }

    def top_chrono(self):
        self.temps_debut = time.time()

    def temps_execution(self):
        if hasattr(self, 'temps_debut'):
            return time.time() - self.temps_debut
        else:
            return 0

    # Fonction pour donner le choix à l'utilisateur
    def main(self):
        # Demander à l'utilisateur de choisir un algorithme de tri
        print()
        print("Choisissez un algorithme de tri:")
        choix = int(input("1: Sélection, 2: Bulles, 3: Insertion, 4: Fusion, 5: Rapide, 6: Tas, 7: Peigne"))

        # Vérifier si le choix de l'utilisateur est valide
        if choix in self.nom_tri:
            # Accéder au nom et au résumé de l'algorithme choisi
            nom = self.nom_tri[choix][0]
            resume = self.nom_tri[choix][1]
            
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"""Choix : {choix}""")
            print(nom)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f""""Le savais-tu? Le {nom} {resume}""")
            print()
        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 7.")

        if choix == 1:
            tri_selection = TriSelection(self.liste)
            return tri_selection.trier()
        elif choix == 2:
            tri_bulles = TriBulles(self.liste)
            return tri_bulles.trier()
        elif choix == 3:
            tri_insertion = TriInsertion(self.liste)
            return tri_insertion.trier()
        elif choix == 4:
            tri_fusion = TriFusion(self.liste)
            return tri_fusion.trier()
        elif choix == 5:
            tri_rapide = TriRapide(self.liste)
            return tri_rapide.trier()
        elif choix == 6:
            tri_tas = TriTas(self.liste)
            return tri_tas.trier()
        elif choix == 7:
            tri_peigne = TriPeigne(self.liste)
            return tri_peigne.trier()
        else:
            print("Choix invalide")

# 1 
class TriSelection(Trier):
    def trier(self):
        # Démarrage du compteur 
        self.top_chrono()

        # Longueur de ma liste
        n = len(self.liste)

        # Boucle pour chaque élèments de ma liste + 1
        for i in range(n):
            # Création de la variable petit_nombre = i 
            petit_nombre = i
            # Boucle pour parcourir les élèments restants de ma liste
            for j in range(i+1, n) :
                # Condition de comparaison :
                # Si l'élèment actuel est plus petit que 
                # l'élèment le plus petit trouvé, 
                if self.liste[j] < self.liste[petit_nombre] :
                    # l'élèment actuel devient l'élèment le plus petit.
                    petit_nombre = j
            # Si l'élèment le plus petit est différent de l'élèment actuel 
            if petit_nombre != i :
                # échange de position 
                self.liste[i], self.liste[petit_nombre] = self.liste[petit_nombre], self.liste[i]

        print(f"""Temps d'exécution : {round((self.temps_execution()*1000),6)} ms""")
        print("La liste est triée")
        return self.liste

# 2 
class TriBulles(Trier):
    def trier(self):
        # Démarrage du compteur 
        self.top_chrono()

        # Longueur de ma liste
        n = len(self.liste)

        for passe in range(n - 1, 0, -1):
            echange = False
            for i in range(passe):
                if self.liste[i] > self.liste[i + 1]:
                    self.liste[i], self.liste[i + 1] = self.liste[i + 1], self.liste[i]
                    echange = True
            if not echange:
                break

        print(f"""Temps d'exécution : {round((self.temps_execution()*1000),6)} ms""")
        print("La liste est triée")
        return self.liste

# 3 
class TriInsertion(Trier):
    def trier(self):

        # Démarrage du compteur 
        self.top_chrono()

        # Boucle pour parcourir la liste de 1 à la longueur de la liste
        # On considère que 0 est à la bonne place
        for i in range(1, len(self.liste)):
            nb_permuter = self.liste[i]
            n = i - 1

            # Pendant que (i -1) est supérieur à 0,
            # et le nombre à permuter est inférieur 
            # au nombre le précédent
            while n >= 0 and nb_permuter < self.liste[n]:
                # de la valeur à droite pour faire de la place
                self.liste [n + 1] = self.liste [n]
                # on enlève - 1 pour pouvoir comparer à l'élément précédent
                n -= 1
            # on permute l'élèment à la place 
            self.liste [n + 1] = nb_permuter

        print(f"""Temps d'exécution : {round((self.temps_execution()*1000),6)} ms""")
        print("La liste est triée")
        return self.liste

# 4 
class TriFusion(Trier):
    def trier(self):

        # Démarrage du compteur 
        self.top_chrono()

        n = len(self.liste)

        if n <= 1:
            return self.liste

        moitie = len(self.liste) // 2
        tg = self.liste[:moitie]
        td = self.liste[moitie:]

        # Appel récursif pour trier les sous-listes
        tri_fusion_gauche = TriFusion(tg)
        tg_trie = tri_fusion_gauche.trier()

        tri_fusion_droite = TriFusion(td)
        td_trie = tri_fusion_droite.trier()

        # Début de la fusion
        n = len(tg) + len(td)
        t = []
        g = d = 0

        while g < len(tg_trie) and d < len(td_trie):
            if tg_trie[g] <= td_trie[d]:
                t.append(tg_trie[g])
                g += 1
            else:
                t.append(td_trie[d])
                d += 1

        # Ajouter les éléments restants de tg_trie et td_trie
        t.extend(tg_trie[g:])
        t.extend(td_trie[d:])

        return t

# 5
class TriRapide(Trier):
    def trier(self):

        # Démarrage du compteur 
        self.top_chrono()

        if not self.liste:
            return []
        else: 
            pivot=self.liste[len(self.liste)//2]
            g = [x for x in self.liste if x <  pivot]
            m = [x for x in self.liste if x == pivot]
            d = [x for x in self.liste[:-1] if x > pivot]

        return TriRapide(g).trier() + m + TriRapide(d).trier()

# 6
class TriTas(Trier):
    # Initialisation de l'objet tri_tas

    def trier(self):
        # Démarrage du compteur 
        self.top_chrono()

        # Première fonction pour entasser ma liste en tas
        # en créant des noeuds avec des fils : gauche et droite
        def entasser(i, n):
            maximum = i
            gauche = 2 * i + 1
            droite = 2 * i + 2

            if gauche < n and self.liste[gauche] > self.liste[maximum]:
                maximum = gauche
            if droite < n and self.liste[droite] > self.liste[maximum]:
                maximum = droite
            if maximum != i:
                self.liste[i], self.liste[maximum] = self.liste[maximum], self.liste[i]
                #self.nb_permutations += 1
                entasser(maximum, n)

        # Deuxième fonction trier qui contient la fonction construction
        # du tas. 
        n = len(self.liste)

        # Boucle interne de la fonction qui itère sur les noeuds du tas
        # Elle part du dernier noeud interne 'n // 2 - 1' et jusqu'à la racine.
        for i in range(n // 2 - 1, -1, -1):
            entasser(i, n)

        # Boucle qui itère à l'intérieur des indices
        # de la fin à la racine 
        # Elle permet de permuter les numéros 
        for i in range(n - 1, 0, -1):
            self.liste[0], self.liste[i] = self.liste[i], self.liste[0]
            entasser(0, i)

        print(f"""Temps d'exécution : {round((self.temps_execution()*1000),6)} ms""")
        print("La liste est triée")
        return self.liste

# 7 
class TriPeigne(Trier):

    def trier(self):

        # Démarrage du compteur 
        self.top_chrono()

        # Calculateur du nombre de permutation à 0
        #nb_permutations = 0

        n = len(self.liste)
        echange = True
        
        while echange or n>1:
        # échange n'est pas vrai
            echange = False
        # réduction progressive de l'écart
        # l'écart ne devrait pas être <1
            n = max(n * 10//13, 1)
            # facteur de réduction = 10//13 soit 1,3
            if n<1: n=1
            for i in range(0, len(self.liste) - n):
                    if self.liste[i]> self.liste[i + n]:
                        echange = True
                        # échange de position parce que echange = True
                        self.liste[i], self.liste[i + n] = self.liste[i + n], self.liste[i]

        print(f"""Temps d'exécution : {round((self.temps_execution()*1000),6)} ms""")
        print("La liste est triée")
        return self.liste



tri = Trier(liste_aleatoire)
tri.main()
