import math


def sjf(C, n):
    return sorted(list(range(0,n)), key=lambda x: C[x])



# trouve le prochain instant auquel il y a des nouvelles tâches prêtes
def next_srtf(D, t, n):
    m = math.inf
    for x in D:
        if x < m and x > t:
            m = x

    return m


def srtf(C, D, t, n):
    if t < math.inf:
        m = math.inf
        k = -1
        for x in range(0, n):
            if D[x] <= t and C[x] < m:
                k = x
                m = C[x]

        if k == -1:
            # on a pas trouvé de tâche à ordonnancer, c'est fini
            return []
        else:
            t2 = next_srtf(D, t, n)

            # la tâche en cours sera finie avant la prochaine activation
            if t2 >= t + C[k]:
                t2 = t + C[k]
                D[k] = math.inf

            C[k] = C[k] - (t2 - t)
            return [k] + srtf(C, D, t2, n)
    else:
        return []


C = [3, 1, 4, 2, 1, 3, 2, 2]

n = 8
print(sjf(C, n))

D = [1, 2, 5, 6, 7, 8, 9, 10]
C = [3, 1, 4, 2, 1, 3, 2, 2]
print(srtf(C, D, next_srtf(D, -1, n), n))
