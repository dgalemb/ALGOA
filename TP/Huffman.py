# Il manque refaire la decodage, codage canonique
# Redo the decoding function and do Huffman canonical coding

# Q1 et Q2
def contents(nom_fichier):

    with open(nom_fichier, mode = 'rb') as f:
        text = f.read()

    octets = [k for k in text]

    return octets
    
#print(contents('pg5097.txt'), len(contents('pg5097.txt')))

# Q3 - Q5 et Q9 - Q10
class HuffmanTreeNode:

    def __init__(self, symbole = None, occurrences = None, 
                rightp = None, leftp = None):
        self.symbole = symbole
        self.occurrences = occurrences
        self.rightp = rightp
        self.leftp = leftp

    @classmethod
    def Merge(cls, nodea, nodeb):

        if nodea.occurrences > nodeb.occurrences:

            return cls(occurrences = nodea.occurrences + nodeb.occurrences, 
            rightp = nodea, leftp = nodeb, symbole = 'not_leaf')

        else:
            
            return cls(occurrences = nodea.occurrences + nodeb.occurrences, 
            rightp = nodeb, leftp = nodea)

    @staticmethod
    def less(nodea, nodeb):

        return nodeb.occurrences < nodea.occurrences

 
        if (root != None) :
     
            root.findFullNode(root.leftp)
            if (root.leftp != None and
                root.rightp != None) :
                print((root.symbole, root.occurrences), end = " ")
            root.findFullNode(root.rightp)

    @staticmethod
    def build_codemap_rec(root, dict, listt = []):   
        listt = listt
        if root.symbole != None:
            dict[root.symbole] = listt
        else:
            listt1 = listt + [0]
            root.build_codemap_rec(root.rightp, dict = dict, listt = listt1)
            listt2 = listt + [1]
            root.build_codemap_rec(root.leftp, dict = dict, listt = listt2)


        return dict

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.rightp is None and self.leftp is None:
            line = '%s' % self.occurrences
            width = len(str(self.symbole) + ': ' + str(self.occurrences))
            height = 1
            middle = width // 2
            return [str(self.symbole) + ': ' + str(self.occurrences)], width, height, middle

        # Only left child.
        if self.rightp is None:
            lines, n, p, x = self.leftp._display_aux()
            s = '%s' % self.occurrences
            u = len(str(self.symbole) + ': ' + str(self.occurrences))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(self.symbole) + ': ' + str(self.occurrences)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.leftp is None:
            lines, n, p, x = self.rightp._display_aux()
            s = '%s' % self.occurrences
            u = len(str(self.symbole) + ': ' + str(self.occurrences))
            first_line = str(self.symbole) + ': ' + str(self.occurrences) + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.leftp._display_aux()
        right, m, q, y = self.rightp._display_aux()
        s = '%s' % (self.occurrences)
        u = len(str(self.symbole) + ': ' + str(self.occurrences))
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(self.symbole) + ': ' + str(self.occurrences) + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# Q6
class PQueue:

    def __init__(self):
        Node = HuffmanTreeNode()
        Node.occurrences = 1
        Node.symbole = 259
        self.file = [Node]
        self.size = 0

    def taille(self):
        return len(self.file)

    def insert(self, k):
        
        self.file.append(k)
        self.size += 1
        self.heap_up(self.size)

    def heap_up(self, i):

        done = False

        while (i // 2 > 0 ) and done == False:

            if self.file[i].occurrences < self.file[i // 2].occurrences:
                self.file[i], self.file[i // 2] = self.file[i // 2], self.file[i]

            else:
                Stop = True

            i = i // 2

    def heap_sort(self):

        for k in range(self.taille()):
            self.heapify(k)
            self.file[0], self.file[self.taille() - k - 1] = self.file[self.taille() - k - 1], self.file[0]

    def heapify(self, p):

        for i in range(self.taille() - p):

            if i > 0 :
                child = i
                parent = (i+1)//2 - 1
                while self.file[parent].occurrences < self.file[child].occurrences and child != 0:
                    self.file[parent], self.file[child] = self.file[child], self.file[parent]
                    child = parent
                    parent = (parent + 1)//2 - 1

    def sup_min(self):

        if self.taille() == 0:
            return 'Vide !'

        popped = self.file[1]
        self.file = self.file[1:]
        self.size -= 1

        pass

    def minHeapify(self, i):
        pass
        if not (i*2 > self.size):
            if (self.file[i].occurrences > self.file[2*i].occurrences or 
               self.file[i].occurrences > self.file[2*i + 1].occurrences):

                if self.file[2*i].occurrences < self.file[2*i + 1].occurrences:
                    self.file[i], self.file[2*i] = self.file[2*i], self.file[i]
                    self.minHeapify(2*i)
  
                else:
                    self.file[i], self.file[2*i + 1] = self.file[2*i + 1], self.file[i]
                    self.minHeapify(2*i + 1)

    def extract_min(self, i):

        if (i * 2) + 1 > self.size:
            return i * 2
        
        else:
            if self.file[i*2] < self.file[(i*2)+1]:
                return i*2
            else:
                return (i * 2) + 1

# Q7 et Q8 et Q10-Q12
class Huffman:

    def __init__(self, tree = None, codes = None):
        self.tree = tree
        self.codes = codes

    def build_tree(self, tab):
        
        dict = {}

        for k in set(tab):
            dict[k] = tab.count(k)

        priority_queue = PQueue()

        #dict = {'C':32, 'D':42, 'E':120, 'K':7, 'L':42, 'M':24, 'U':37, 'Z': 2}

        for k in dict.keys():
            Node = HuffmanTreeNode()
            Node.occurrences = dict[k]
            Node.symbole = k
            priority_queue.insert(Node)
        priority_queue.heap_sort()
    
        ready = False

        #print([(k.symbole, k.occurrences) for k in priority_queue.file])

        while not ready:
            if priority_queue.size <= 1:
                ready = True

            priority_queue.insert(HuffmanTreeNode.Merge(priority_queue.file[0], priority_queue.file[1]))
            priority_queue.sup_min()
            priority_queue.sup_min()
            priority_queue.heap_sort()

        self.tree = priority_queue.file[0]

        pass

    def build_codemap(self):
        self.codes = self.tree.build_codemap_rec(self.tree, dict = {})
        pass

    def encode(self, tab):
        res = []
        codet = []
        for k in tab:
            codet.append(self.codes[k])

        codet = sum(codet, [])
        codet = "".join(map(str, codet))

        for k in range(len(codet)):
            if k % 8 == 0 and k != 0:
                res.append(int(codet[k-8:k], 2))
        return res

    #TODO: Arrumar decode
    def decode(self, coded):
        text = []
        for j in coded:
            text.append([k for k, v in self.codes.items() if v == j])
        return [k[0] for k in text]

    #Q33
    #TODO: Arrumar
    def canonical_diffs(self):
        self.codes = sorted(self.codes.items(), key=lambda x: len(x[1]))
        ans = self.codes[:]
        ans[0] = (ans[0][0], [0] * len(ans[0][1]))
        ans[1] = (ans[1][0], [0, 1, 0])
        for k in range(2, len(ans)):
            ans[k] = (ans[k][0], 
                    [j for j in str(
                    format(
                        int(
                            bin((1 + 
                                int(
                                    ''.join
                                    (map(str, ans[k-1][1]))
                                    , 2)
                                    ) << (len(self.codes[k][1]) - len(ans[k][1]))), 2),
                    f'#0{len(self.codes[k][1])+2}b'
                    )
                    )
                    ][2:]
            )

        return ans

#Q34
def binary_list(n):    
    return list(map(int,[k for k in bin(n)][2:]))

def main(nom_fichier):

    tab = contents(nom_fichier)
    with open(nom_fichier) as f: 
        text = f.read()

    Huf = Huffman()
    Huf.build_tree(tab)
    Huf.build_codemap()
    encoded = Huf.encode(tab)
    canon = Huf.canonical_diffs()
    #Huf.decode(Huf.encode(tab))

    print(Huf.codes)

    print(f'First 100 chars of the original message: {text[:min(100, len(text))]}\nFirst 100 ints of its binary representation: {tab[:min(100, len(tab))]}\nL arbre correspondant:')
    Huf.tree.display()
    print(f'The corresponding codemap: {Huf.codes}\nThe coded message: {encoded}\nThe canonical code: {canon}')


main(r'TP/teste.txt')