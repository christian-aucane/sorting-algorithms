## Les différents tris :

### Les tris demandés: 

1. Tri par sélection : 
    *Sélectionne progressivement l'élément minimum et le place à la bonne position, en répétant cette opération pour chaque élément.*

2. Tri à bulles :
    *Compare les éléments adjacents et les échanges si nécessaire, répétant ce processus jusqu'à ce que tous les éléments soient ordonnés.*

3. Tri par insertion :
    *Insère chaque élément à la place correcte parmi les éléments déjà triés, étandant ainsi la partie triée de la liste.*

4. Tri fusion :
    *Divise de manière récursive la liste en deux moitiés  puis trie chaque moitié séparément pour ensuite fusionner, en comparant d'après chaque moitié, quel est l'élément le plus bas.*

5. Tri rapide :
    *Prend deux parties de la liste selon un pivot puis échange les éléments les plus bas et les plus hauts dans la partie, toujours selon le pivot.*

6. Tri à peigne :
    *Tri à bulles amélioré: échange les éléments non pas adjacents mais à intervalle plus grandes et les échange.*

7. Tri par tas :
    *Organise les élements dans une structure de tas, puis réorganise la structure pour que l'élément racine soit toujours le plus grand.*

### Les autre tris trouvés :

1. Tri par d ́enombrement :
    *Compte le nombre d'occurrences de chaque élément distinct dans le tableau, puis reconstruit le tableau en plaçant chaque élément à sa position selon son dénombrement.*

2. Tri Gnome :
    *Parcourt le tableau, en comparant chaque élément avec son prédécesseur ; si l'élément est mal placé, il l'échange avec son prédécesseur et recule d'une position, sinon il avance d'une position.*

3. Tri par pigeon :
    *Répartit les éléments dans des "nids" selon leur valeur, puis rassemble les éléments des nids dans l'ordre.*

4. Tri par comptage :
    *Compte le nombre d'éléments de chaque valeur distincte dans le tableau, puis reconstruit le tableau en plaçant chaque élément à sa position selon son rang de comptage.*

5. Tri Cocktail :
    *Une variante du tri à bulles qui parcourt alternativement le tableau dans les deux sens, échangeant les éléments mal placés jusqu'à ce que le tableau soit entièrement trié.*

### Classification des tris 
#### 1. Stabilité du tri 

*Tri stable:*

Un tri stable garentira l'ordre relatif des éléments égaux. 

*Tri instable:*

Un tri instable ne garenti pas l'ordre relatif des éléments égaux. 
Si l'algorithme est instable, 

*Classifiction des tris selon leurs stabilités* 

| Tris stables | Tris instables | 
| --------- | --------- | 
| Tri à bulles | Tri sélection |
| Tri par insertion | Tri rapide |
| Tri fusion | Tri par tas|
|  | Tri à peigne |

#### 2. Tri par comparaisons

*Def*
Un tri basé sur la comparaison est un algorithme qui compare à plusieurs reprises des paires d'éléments et en les échangeant si elles sont dans le désordre.  
Ici, tous les tris proposés dans l'application sont des tris par comparaisons

#### 3. Tri en place
*Tri en place:*
Il modifie directement les éléments de la liste d'entrée sans nécessiter de mémoire supplémentaire. Il réorganise les éléments de la liste directement dans la lsite d'origine.

*Tri non en place:*
Il crée une nouvelle structure de données pour stocker les éléments triés plus tôt. 
Il nécessite généralement plus d'espace de mémoire car il doit stocker les éléments triés séparéments de la liste input. 

*Classifiction des tris en place et non en place* 

| Tris en place | Tris non en place | 
| --------- | --------- | 
| Tri sélection | Tri fusion |
| Tri à bulles |  |
| Tri par insertion |  |
| Tri rapide |  |
| Tri par tas |  |
| Tri à peigne |  |

     
#### 4. Complexité du temps

Plus la taille de la liste sera grande, plus 
  
Le tri le plus lent est : Bubble Sort, avec un temps d'exécution supérieur à la moyenne - pour n, taille de l'échantillon = 10, 50, 100 et 1000. 

Le tri de sélection est le deuxième le plus lent du groupe. 
  
*Pour n = 10, où n = taille de la liste:* 
Le tri Insertion  est le plus performant : 0,000 007 secondes en temps d'exécution. 
Le tri Rapide et le tri à peigne, se placent simultanément en seconde position : 0, 000 009 secondes en temps d'exécution. 

Le tri par tas mets 0,000 012 secondes et se place en 4e position. 

Puis le tri fusion arrive en 5e position avec  0,000 023 secondes en temps d'exécution.  

*Pour n = 50, où n = taille de la liste:* 
Le classement des tris les plus rapides et des plus lents restent plus ou moins pareils sauf pour le tri à peigne qui se place en première position avec  0,000 048 secondes d'exécutions. Le quick sort le suit. 

*Pour n = 100, où n = taille de la liste:* 
Le tri à peigne reste le plus rapide. 
Le tri rapide en seconde position. 
Ensuite, le tri par tas prend la 3e position avec  0,000 174 secondes. 
Le tri insertion prends la 4e position et le tri fusion la 5e position. 

Le bubble sort reste le plus lent avec  0,008 104 secondes. Le tri par sélection reste le 2e le plus lent avec  0,001 635 secondes. 

*Pour n = 1 000, où n = taille de la liste:* 
Le tri le plus rapide et le plus performant est le tri rapide :  0,000 830 secondes.
En 2nde position : le tri fusion. 
Le tri à peigne se place en 3e position. 
Le tri par tas en 4e place. 

Le tri par insertion est en 5e position. 

Le tri par sélection rest en 6e position avec  0,117 secondes.  
Le bubble sort est toujours le plus lent avec  2,6 secondes. 

*Pour n = 10 000, où n = taille de la liste:* 
Classement : 
Tri rapide
Tri à peigne
Tri fusion
Tri par tas
Tri sélection
Tri insertion
Tri à bulles

*Analyse en ascendant*
Taille de la liste = 10 
| Nom Tris | Temps exécution | 
| --------- | --------- | 
| Tri sélection |  0,0000329  |
| Tri à bulles |  0,0000405   |
| Tri fusion |  0,0000238  |
| Tri par insertion |  0,0000069  |
| Tri rapide |  0,00000858  |
| Tri par tas |  0,0000122  |
| Tri à peigne |  0,00000858  |
  
Taille de la liste = 50
| Nom Tris | Temps exécution | 
| --------- | --------- | 
| Tri sélection |   0,0006251  |
| Tri à bulles |   0,0014071   |
| Tri fusion |   0,0001402  |
| Tri par insertion |   0,0000682  |
| Tri rapide |   0,0000625  |
| Tri par tas |   0,0000975  |
| Tri à peigne |   0,0000486  |

Taille de la liste = 100
| Nom Tris | Temps exécution | 
| --------- | --------- | 
| Tri sélection |   0,0016356  |
| Tri à bulles |   0,0081043   |
| Tri fusion |   0,0002508  |
| Tri par insertion |   0,0002246  |
| Tri rapide |   0,0001144  |
| Tri par tas |   0,0001740  |
| Tri à peigne |   0,0001032  |
  
Taille de la liste = 1 000
| Nom Tris | Temps exécution | 
| --------- | --------- | 
| Tri sélection |  0,1177248  |
| Tri à bulles |  2,5972666   |
| Tri fusion |  0,0018897  |
| Tri par insertion |  0,0210373  |
| Tri rapide |  0,0008304  |
| Tri par tas |  0,0024409  |
| Tri à peigne |  0,0021963  |

Taille de la liste = 10 000
| Nom Tris | Temps exécution | 
| --------- | --------- | 
| Tri sélection |   0,7836649  |
| Tri à bulles |  526,3726317   |
| Tri fusion |  0,0300781  |
| Tri par insertion |  2,1984450  |
| Tri rapide |  0,0073828  |
| Tri par tas |  0,0332305  |
| Tri à peigne |  0,0258309  |
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
#### Ressources :
  
https://webusers.imj-prg.fr/~francois.le-maitre/enseignements/2324/algo/Chap_Tris.pdf  
http://lwh.free.fr  
https://zanotti.univ-tln.fr/ALGO/II/  

