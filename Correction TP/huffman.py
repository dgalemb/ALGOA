# TP ALGOA : compression bzip
# Didier Lime, novembre 2022
#
# Tous droits réservés

from pqueue import PQueue
from constants import huffman_marker

class HuffmanTreeNode:
    def __init__(self, f, c):
        self.freq = f
        self.char = c
        self.left = None
        self.right = None

    def less(x, y):
        return x.freq < y.freq

    def merge(self, y):
        n = HuffmanTreeNode(self.freq + y.freq, 0)
        n.left = self
        n.right = y

        return n
    
    def make_codes(self, s, t):
        if self.left == None:
            t[self.char] = s
        else:
            self.left.make_codes(s + [0], t)
            self.right.make_codes(s + [1], t)




def snd(t):
    a, b = t
    return b

def binary_list(x, size):
    R = []
    mask = 1 << (size -1)
    while mask != 0:
        b = x & mask
        mask = mask >> 1
        if b != 0:
            R.append(1)
        else:
            R.append(0)

    return R


class Huffman:
    def __init__(self):
        self.codes = []
        self.tree = None

    def canonical_diffs(self):
        ll = []
        for c, code in enumerate(self.codes):
            if code:
                ll.append((c, len(code)))
    
        ll.sort(key=snd)
    
        s = 0
        R = []
        for i, t in enumerate(ll):
            c, l = t
            R.append(c)
            R.append(l - s) 
            s = l
    
        return R

    def build_canonical_codemap(self, diffs):
        self.codes = [None]*(huffman_marker+1)
        code = 0
        size = 0
        for i in range(0,len(diffs),2):
            c = diffs[i]
            s = diffs[i + 1]
            code = code << s
            size = size + s
            self.codes[c] = binary_list(code, size)
            code = code + 1 

    def rebuild_tree(self):
        I = []
        for i, c in enumerate(self.codes):
            if c:
                I.append(i)
        self.tree = self.rebuild_tree_rec(I, 0)

    def rebuild_tree_rec(self, L, k):
        zeroes = []
        ones = []
        if len(L) == 1:
            return HuffmanTreeNode(0, L[0])
        else:
            for i in L:
                if self.codes[i][k] == 0:
                    zeroes.append(i)
                else:
                    ones.append(i)
            N = HuffmanTreeNode(0, 0)
            N.left = self.rebuild_tree_rec(zeroes, k + 1)
            N.right = self.rebuild_tree_rec(ones, k + 1)
    
            return N

    def build_tree(self, m):
        # ajout d'un marqueur de fin de flux
        m.append(huffman_marker)
    
        freqs = [0]*(huffman_marker+1)
    
        for b in m:
            freqs[b] = freqs[b] + 1
    
        p = PQueue(HuffmanTreeNode.less)
        for i, c in enumerate(freqs):
            if c != 0:
                p.insert(HuffmanTreeNode(c, i))
    
        if p.empty():
            raise Exception("Huffman: no characters to code")
        else:
            while p.size() > 1:
                x = p.extract_min()
                y = p.extract_min()
    
                p.insert(x.merge(y))
    
            self.tree = p.extract_min()

    def build_codemap(self):
        self.codes = [[]]*(huffman_marker+1)
        self.tree.make_codes([], self.codes)

    def merge_symbols(diffs):
        bdiffs = []
        for c in diffs:
            if c < 256:
                bdiffs.append(c)
            else:
                bdiffs.append(0)
                bdiffs.append(c % 256)

        return bdiffs


    def split_symbols(bdiffs):
        diffs = []
        symbol = True
        symbol_ext = False
        for c in bdiffs:
            if symbol and c == 0:
                symbol = False
                symbol_ext = True
            else:
                if symbol_ext:
                    diffs.append(c + 256)
                    symbol_ext = False
                else:
                    diffs.append(c)
                    symbol = not symbol

        return diffs


    def encode(self, contents):
        out = []
        current = []
        for b in contents:
            current.extend(self.codes[b])
            while len(current) >= 8:
                byte = 0
                for i in range(8):
                    byte = byte << 1
                    byte = byte | current[0]
                    current.pop(0)
                out.append(byte)
    
        # À la fin, il nous reste potentiellement de 1 à 7 bits orphelins dans current
        # on les met dans les bits de poids faibles d'un dernier octet
        byte = 0
        size = 0
        while current:
            byte = byte << 1
            byte = byte | current[0]
            current.pop(0)
            size = size + 1
        
        while size < 8:
            byte = byte << 1
            size = size + 1
        
        out.append(byte)
    
        return out
    
    def decode(self, text):
        out=[]
        z = self.tree
        for b in text:
            mask = 1 << 7
            for i in range(8):
                if b & mask:
                    z = z.right
                else:
                    z = z.left
        
                if z.left == None:
                    if z.char == huffman_marker: #end of file
                        return out
                    else:
                        out.append(z.char)
                        z = self.tree
        
                mask = mask >> 1

