def sommeMax(tableau):
    maxi1 = tableau[0]
    maxi2 = tableau[1]
    for j in tableau:
        if j >= maxi2 and j!= maxi1:
                maxi2 = j
        if j >= maxi1 and j!=maxi2:
                maxi1 = j
    return maxi2,maxi1
def getIndexOfMaxValues(tableau):
    maxi1 = sommeMax(tableau)[0]  #prendre l'index des deux valeurs pour faire la somme des éléments à l'intérieur
    maxi2 = sommeMax(tableau)[1]
    indexMaxi1 = tableau.index(maxi1)
    indexMaxi2 = tableau.index(maxi2)
    somme = 0
    for i in range(indexMaxi1,indexMaxi2+1):
        somme += tableau[i]
    print(somme)
getIndexOfMaxValues([-2, -5, 6, -2, -3, 1, 5, -6])
"""
    Complexité:
Algorithme de recherche pour valeurs max ==> O(n)
"""