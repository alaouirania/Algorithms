
ouvrantes = ['(','{','[']
fermantes = [')','}',']']
def equilibre(string):
    pile = []
    for i in string:
        if i in ouvrantes:
            pile.append(1)
            print("ouvrantes",i)
        elif i in fermantes:
            pile.pop()
            print("fermantes",i)
    if len(pile) == 0:
            return "Expression équilibrée"
    else:
            return "Expression non équilibrée"
print(equilibre("{()}[()[)"))