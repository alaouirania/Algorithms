memo = dict() #on met en place un disctionnaire pour mémoriser les valeurs
def set(liste,sommeRecherche):
    liste1 = [] #création de liste où l'on va mettre les valeurs inférieures de la somme recherchée
    for j in liste:
        if j < sommeRecherche:
            liste1.append(j) #à chaque fois que l'on trouve une valeur inférieure on l'ajoute dans la liste vide
    if sommeRecherche in memo: #on stock les valeurs dans le dictionnaire
        return memo.get(sommeRecherche)
    if sommeRecherche == 0:  #si la somme recherchée est == 0 on return Faux
        return False
    else:
        for num in liste1:
            SumIs = num
            for i in range(0, len(liste1)):
                for e in range(0, len(liste1)):  #liste imbriquée pour comparer les valeurs
                     if i != e:
                         if SumIs + liste1[e] <= sommeRecherche:
                            SumIs += liste1[e] #on additionne les nombres jusqu'à trouver le résultat voulu
                         elif SumIs == sommeRecherche:
                            return True
                     if SumIs == sommeRecherche:
                         return True
        return False
print(set([34, 12, 3, 5, 2, 3],9))
'''     
    Complexité:
Utilisation de méthode memoisation donc algorithmes dynamiques ==> O(n)
'''
