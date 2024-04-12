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


#### 5. Complexité de la mémoire






































#### Ressources :

https://webusers.imj-prg.fr/~francois.le-maitre/enseignements/2324/algo/Chap_Tris.pdf
http://lwh.free.fr
https://zanotti.univ-tln.fr/ALGO/II/

