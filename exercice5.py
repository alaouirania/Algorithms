memo = dict()
def set(liste,sommeRecherche):
    resultat = 0
    if sommeRecherche in memo:
        return memo.get(sommeRecherche)
    if sommeRecherche == 0:
        return resultat
    else:
        for i in liste:
             while resultat != sommeRecherche:
                resultat = liste[i] + liste[i+1]
                return resultat

print(set([3, 34, 4, 12, 5, 2],7))

#on additionne petit à petit jusqu'a trouver la somme voulue