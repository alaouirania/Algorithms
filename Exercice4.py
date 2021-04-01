import copy #librairie python utilisée ici pour pouvoir modifier une copie sans modifier l'autre
words = ["go","bat","me","eat","goal","boy", "run","check"]
chars = ['e','o','b','a','m','g','l',"c","h","k"]
def rep(words,chars):
    wasFound = [] #liste vide
    for word in words:
        checkChars = ""
        copyChars = copy.copy(chars) #autre copie de la liste "chars"
        for element in word:
            if element in copyChars:
                checkChars += element #ajouter les éléments qui existent dans le mot
                copyChars.remove(element) #enlever l'élément s'il existe déjà sur la liste "chars"
            if checkChars == word:
                wasFound.append(word)
    return wasFound
print(rep(words,chars))
'''     
    Complexité:
Utilisation de piles donc complexité algorithmique optimale ==> O(n)
'''