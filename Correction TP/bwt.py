# TP ALGOA : compression bzip
# Didier Lime, novembre 2022
#
# Tous droits réservés

from constants import bwt_marker

def get_element(t, x, text, size):
    return text[(size - t + x) % size]

def counting_sort(A, r, f, x, text, start, end):
    size = len(text)
    freqs = [0]*r 

    for i in range(start, end):
        c = f(A[i], x, text, size)
        freqs[c] = freqs[c] + 1

    s = start
    letters = []
    indices = [0]*r
    for i, c in enumerate(freqs):
        if c != 0:
            letters.append(i)
            indices[i]= s
            s = s + c

    s = start
    for d in letters:
        j = indices[d]
        s = s + freqs[d]
        while j < s:
            c = f(A[j], x, text, size)
            k = indices[c]
            b = f(A[k], x, text, size)
            if b != c:
                A[j], A[k] = A[k], A[j]
            else:
                j = j + 1
            indices[c] = indices[c] + 1

    # À la fin pour chaque lettre c, la plage [indices[c] - freqs[c], indices[c] - 1]
    # contient les mots pour lesquels la lettre courante était c
    R = []
    for d in letters:
        R.append((indices[d] - freqs[d], indices[d]))

    return R

def radix_sort(A, r, f, n, text, start, end):
    if n < len(text):
        R = counting_sort(A, r, f, n, text, start, end)
        for s, e in R:
            radix_sort(A, r, f, n + 1, text, s, e)

def radix_sort_nr(A, r, f, text, start, end):
    W = [(0, start, end)]
    while W:
        n, s, e = W.pop()
        R = counting_sort(A, r, f, n, text, s, e)
        if n < len(text) - 1:
            for s1, e1 in R:
                if s1 < e1 - 1:
                    W.append((n + 1, s1, e1))



def bwt_encode(text, bs):
    R = []
    while text:
        txt = text[:bs]
        text = text[bs:]

        txt.append(bwt_marker) # add end marker 
        size = len(txt)
        t = list(range(size))
        #radix_sort(t, bwt_marker+1, get_element, 0, txt, 0, size)
        radix_sort_nr(t, bwt_marker+1, get_element, txt, 0, size)

        R.extend([get_element(t[i], size - 1, txt, size) for i in range(size)])
        txt.pop() # remove end marker for original text

    return R 
    
def id(i, x, text, size):
    return i

def find_rank(A, i):
    x = A[i]
    r = 1
    while i >= r and A[i - r] == x:
        r = r + 1

    return r

def find_rank_sorted(A, s, i):
    e = i
    while s < e:
        m = (s + e) // 2
        if A[m] == A[i]:
            e = m
        else:
            s = m + 1

    return i - e + 1

def find_nth(A, x, n):
    i = 0
    while i < len(A):
        if A[i] == x:
            n = n - 1
            if n == 0:
                return i
        i = i + 1

    return -1

def bwt_decode(text, bs):
    R = []
    while text:
        txt = text[:bs+1] # including end marker
        text = text[bs+1:]

        corresp = [[] for i in range(bwt_marker+1)]
        for i, c in enumerate(txt):
            corresp[c].append(i)

        sorted_text = txt[:]
        counting_sort(sorted_text, bwt_marker+1, id, 0, sorted_text, 0, len(sorted_text))
        #ib = find_nth(txt, bwt_marker, 1)
        i = corresp[bwt_marker][0]
        if i == -1:
            raise Exception("find nth: element not found")
        R.append(sorted_text[i])
        

        for k in range(len(txt) - 1):
            #rb = find_rank(sorted_text, i)
            r = find_rank_sorted(sorted_text, 0, i)
            #ib = find_nth(txt, sorted_text[i], r)
            i = corresp[sorted_text[i]][r - 1]
            if i == -1:
                raise Exception("find nth: element not found")
            R.append(sorted_text[i])

        R.pop() # remove the end marker

    return R


