# TP ALGOA : compression bzip
# Didier Lime, novembre 2022
#
# Tous droits réservés

from constants import rle_two, rle_one
from math import ceil

def zrle_encode(text):
    R = []
    s = 0
    for c in text:
        if c == 0:
            s = s + 1
        else:
            if s > 0: 
                Z = []
                while s > 0:
                    q = ceil(s/2) - 1
                    if s - 2*q == 1:
                        Z.append(rle_one)
                    else:
                        Z.append(rle_two)
                    s = q
                R.extend(reversed(Z))

            R.append(c)

    return R

def zrle_decode(text):
    R = []
    s = 0
    for c in text:
        if c != rle_two and c != rle_one:
            while s > 0:
                R.append(0)
                s = s - 1
            R.append(c)
        else:
            s = s << 1
            if c == rle_one:
                s = s + 1
            else:
                s = s + 2

    return R
