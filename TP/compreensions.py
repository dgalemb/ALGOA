import math

def contents(nom_fichier):

    with open(nom_fichier, mode = 'rb') as f:
        text = f.read()

    octets = [k for k in text]

    return octets
    
#print(contents('pg5097.txt'), len(contents('pg5097.txt')))

class HuffmanTreeNode:

    def __init__(self, symbole, occurrences) -> None:
        self.symbole = symbole
        self.occurrences = occurrences
        self.rightp = None
        self.leftp = None

    def Merge(self, nodeb):

        if self.occurrences > nodeb.occurrences:

            newNode = HuffmanTreeNode(None, self.occurrences + nodeb.occurrences)
            newNode.rightp = self
            newNode.leftp = nodeb

        else:

            newNode = HuffmanTreeNode(None, self.occurrences + nodeb.occurrences)
            newNode.rightp = nodeb
            newNode.leftp = self

        return newNode

    def less(nodea, nodeb):

        return nodea.occurrences < nodeb.occurrences

class priorityQ:

    def __init__(self) -> None:
        self.file = []

    def insert(self, a):
        A = self.file

        A.append(a)

        i = len(A) - 1
        p = math.floor((i - 1)/ 2)
        
        while p >= 0 and A[i].occurrences < A[p].occurrences:
            A[i].occurrences, A[p].occurrences = A[p].occurrences, A[i].occurrences
            i = p
            p = math.floor((i - 1)/ 2)

    def taille_file(self) -> int:

        return len(self.file)

    def extract_min(self):
        A = self.file
        n = len(A)

        r = A[0][1]
        A[0][1] = A[n - 1][1]
        n -= 1

        done = False
        i = 0

        while not done:
            done = True
            k = i
            if 2*i + 1 < n and A[2*1 + 1][1] < A[k][1]:
                k = 2*i + 1
            if 2*i + 2 < n and A[2*i + 2][1] < A[k][1]:
                k = 2*i + 2
            if i != k:
                A[i][1], A[k][1] = A[k][1], A[i][1]
                i = k
                done = False

        return r

class Huffman:

    def __init__(self, Node) -> None:
        self.tree = Node

    def build_tree(self, tab):
        
        dict = {}

        for k in set(tab):
            occ = 0
            for i in tab:
                if i == k:
                    occ += 1
            dict[k] = occ

        dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}

        priority_queue = priorityQ()
        
        for k in dict.keys():
            priority_queue.insert(HuffmanTreeNode(k, dict[k]))

        for k in priority_queue:


#Nodea = HuffmanTreeNode('a', 4)
#Nodeb = HuffmanTreeNode('b', 2)
#Node = Nodea.Merge(Nodeb)

tab = contents('teste.txt')
Node = HuffmanTreeNode(None, None)
Huf = Huffman(Node)
print([(k.symbole, k.occurrences) for k in Huf.build_tree(tab).file])