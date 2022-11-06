# Il manque tout
# Everything needs to be done

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A

def counting_sort(tab):

    key = [0 for _ in range(max(tab) + 1)]

    for k in tab:
        key[k] = tab.count(k)

    for k in range(1, len(key)):
        key[k] = key[k-1] + key[k]

    for j in range(len(tab)):
        if key[tab[j]] != j:
            #swap(tab, j, key[tab[j]])
            key[tab[j]] -= 0


    return key,tab

        


print(counting_sort([2,9,7,4,1,8,4]))
