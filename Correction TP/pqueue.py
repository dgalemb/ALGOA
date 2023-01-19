# TP ALGOA : compression bzip
# Didier Lime, novembre 2022
#
# Tous droits réservés

class PQueue:
    def __init__(self, c):
        self.tab = []
        self.comp = c

    def insert(self, c):
        self.tab.append(c)
        self.fix_up(len(self.tab)-1)

    def empty(self):
        return not self.tab
    
    def size(self):
        return len(self.tab)

    def extract_min(self):
        if self.empty():
            raise Exception("extract: heap is empty")
        else:
            r = self.tab[0]
            self.tab[0] = self.tab[len(self.tab)-1]
            self.tab.pop()

            self.fix_down(0)

            return r

    def fix_up(self, i):
        p = (i - 1) // 2
        while p >= 0 and self.comp(self.tab[i], self.tab[p]):
            self.tab[p], self.tab[i] = self.tab[i], self.tab[p]
            i = p
            p = (i - 1) // 2

    def fix_down(self, i):
        done = False
        while not done:
            done = True
            k = i
            if 2*i + 1 < len(self.tab) and self.comp(self.tab[2*i + 1], self.tab[k]):
                k = 2* i + 1
            if 2*i + 2 < len(self.tab) and self.comp(self.tab[2*i + 2], self.tab[k]):
                k = 2* i + 2
            if i != k:
                self.tab[k], self.tab[i] = self.tab[i], self.tab[k]
                i = k
                done = False


