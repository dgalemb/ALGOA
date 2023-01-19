# TP ALGOA : compression bzip
# Didier Lime, novembre 2022
#
# Tous droits réservés

from bwt import bwt_encode, bwt_decode
from mtf import mtf_encode, mtf_decode
from huffman import Huffman
from zrle import zrle_encode, zrle_decode
from constants import block_size


def encode(text):
    m = bwt_encode(text, block_size)
    print("bwt encode")

    m = mtf_encode(m)
    print("mtf encode")

    m = zrle_encode(m)
    print("zrle encode")

    h = Huffman()
    h.build_tree(m)
    h.build_codemap()
    #for i, c in enumerate(h.codes):
    #    if c:
    #        print(f'{i} {c}')

    diffs = h.canonical_diffs()
    h.build_canonical_codemap(diffs)
    #print()
    #for i, c in enumerate(h.codes):
    #    if c:
    #        print(f'{i} {c}')

    m = h.encode(m)
    print("huffman encode")

    bdiffs = Huffman.merge_symbols(diffs)
    
    m = [len(bdiffs) % 256, len(bdiffs) // 256] + bdiffs + m

    return m

def decode(text):
    i = text[0] + 256 * text[1] # taille de diffs
    bdiffs = text[2:i+2]
    text = text[i+2:]

    h = Huffman()

    diffs = Huffman.split_symbols(bdiffs)

    h.build_canonical_codemap(diffs)
    h.rebuild_tree()

    m = h.decode(text)
    print("huffman decode")

    m = zrle_decode(m)
    print("zrle decode")
    #print(m)
    
    m = mtf_decode(m)
    print("mtf decode")
    #print(m)
    
    m = bwt_decode(m, block_size)
    print("bwt decode")
    #print(m)

    return m


s = "pg5097.txt"
#s = "mississippi.txt"
with open(s, "rb") as f:
    contents = list(f.read())

#print("initial text")
#print(contents)
print(f'initial size: {len(contents)}')


m = encode(contents)
print(f'compressed size: {len(m)}')
#print(m)

with open(s+".bz", "wb") as f:
    f.write(bytes(m))

m = decode(m)
print(m == contents)
