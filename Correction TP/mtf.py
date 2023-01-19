# TP ALGOA : compression bzip
# Didier Lime, novembre 2022
#
# Tous droits réservés

def iless(x, y):
    return x < y

class ListNode:
    def __init__(self, a):
        self.char = a
        self.next = None

    def insert_front_node(self, node):
        node.next = self
        return node

    def insert_front_element(self, a):
        return self.insert_front_node(ListNode(a))

    def delete_next(self, prev_node):
        if prev_node == None:
            return self.next
        else:
            if prev_node.next != None:
                prev_node.next = prev_node.next.next
            # sinon rien à faire mais ça ne devrait pas arriver

            return self

    def find_npi(self, a):
        i = 0
        p = None
        n = self
        while n != None and n.char != a:
            p = n
            n = n.next
            i = i + 1

        return (n, p, i)

    def find_np(self, i):
        p = None
        n = self
        while n != None and i > 0:
            p = n
            n = n.next
            i = i - 1

        return (n, p)


def mtf_encode(text):
    A = ListNode(256)
    for i in range(255, -1, -1):
        A = A.insert_front_element(i)

    out = []
    for c in text:
        n, p, i = A.find_npi(c)
        if n != None:
            out.append(i)
            if p != None:
                A = A.delete_next(p)
                A = A.insert_front_node(n)
            # sinon c'est le début de la liste, rien à faire
        else:
            raise Exception('mtf_encode: element not found')

    return out

def mtf_decode(text):
    A = ListNode(256)
    for i in range(255, -1, -1):
        A = A.insert_front_element(i)

    out = []
    for c in text:
        n, p = A.find_np(c)
        if n != None:
            out.append(n.char)
            if p != None:
                A = A.delete_next(p)
                A = A.insert_front_node(n)
            # sinon c'est le début de la liste, rien à faire
        else:
            raise Exception('mtf_decode: element not found')

    return out



