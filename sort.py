def mergeSort(n,nlist):
    evens = [nlist[i] for i in range(n) if i % 2 == 0]
    odds = [nlist[i] for i in range(n) if i % 2 != 0]
    new_odds=[]
    while len(evens)>0:
        i=evens.index(min(evens))
        new_odds.append(odds[i])
        evens.remove(evens[i])
        odds.remove(odds[i])

    print(new_odds)
mergeSort()
