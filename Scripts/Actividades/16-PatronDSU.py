# Patron dsu
#Decorate
#tenemos una lista y la decoramos
printListOTupleConIndice(Lestudiantes)
listDecorate = list()
for est in Lestudiantes:
    listDecorate.append((len(est),est))
printListOTupleConIndice(listDecorate)
#Sort
listDecorate.sort(reverse=True)
printListOTupleConIndice(listDecorate)
#undecorate
finalList = list()
for lgt,est in listDecorate:
    finalList.append(est)

printListOTupleConIndice(finalList)