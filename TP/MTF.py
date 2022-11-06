# Complet
# All done

import math

#Q23 - 27, 29
class ListNode:

    def __init__(self, symbole = None, next = None):
        self.symbole = symbole
        self.next = next

    def insert_front_node(self, Node):

        Node.next = self
        return Node

    def insert_front_symbol(self, symbole):
        
        return self.insert_front_node(ListNode(symbole))

    def delete_next(self):

        if self.next == None:
            pass

        elif self.next.next == None:
            self.next = None
            pass

        else:
            save = self.next.next
            self.next = save
            pass

    @staticmethod
    def find_npi(self, symbole, indice = 0):

        current = self
        old = ListNode()

        while current != None:
            if current.symbole == symbole:
                return current, old, indice

            indice += 1
            old = current
            current = current.next

        return -1

    def find_np(self, indice):

        current = self
        old = ListNode()
        current_ind = 0

        if indice == 0:
            return current, old

        while current_ind != indice:
            old = current
            current = current.next
            current_ind += 1

        if current == None:
            return -1 

        return current, old

    def show(self, indice = 0):
        
        current = self

        while current != None:
            print(current.symbole, indice)
            indice += 1
            current = current.next


#Q28
def mtf_encode(text, flag = True):

    text_in_asc = [ord(j) for j in text]

    if flag:
        list = ListNode(255)
        for k in range(254,-1,-1):
            list = list.insert_front_symbol(k)

    else:

        set_in_asc = set(text_in_asc)

        set_in_asc = sorted([k for k in set_in_asc], reverse = True)

        list = ListNode(set_in_asc[0])
        for k in set_in_asc[1:]:
            list = list.insert_front_symbol(k)

    encoded = []

    for k in text_in_asc:
        returned = list.find_npi(list, k)
        if returned == -1:
            print('Non-ascii char found !')
            exit()
        found, parent, indice = returned[0], returned[1], returned[2]

        if indice == 0:
            encoded.append(indice)

        else:
            encoded.append(indice)
            parent.delete_next()
            list = list.insert_front_node(found)

    return [k for k in encoded]

#Q30
def mtf_decode(text, list):

    uncoded = []

    for k in text:

        if k == 0:
            uncoded.append(list.symbole)

        else:
            returned = list.find_np(k)
            if returned == -1:
                print('Non-ascii char found !')
                exit()
        
            found, parent = returned[0], returned[1]
            uncoded.append(found.symbole)
            parent.delete_next()
            list = list.insert_front_node(found)

    return ''.join([chr(k) for k in uncoded])

#Q31
def to_bijec(n):
    global ZRLE_ONE
    global ZRLE_TWO

    ZRLE_ONE = 257
    ZRLE_TWO = 258


    resp = []
    q0 = n
    q1 = math.ceil(q0/2) - 1

    while q1 > -1:
        resp.extend([ZRLE_ONE if q0 - 2*q1 == 1 else ZRLE_TWO])
        q0 = q1
        q1 = math.ceil(q0/2) - 1
    return int(''.join(map(str, resp[::-1])))

def zrle_encode(decod):
    ans = decod[:]
    dif_len = 0
    for k in range(len(decod)):
        if k == 0:
            if decod[k] == 0:
                i = k
                while decod[i] == 0:
                    i += 1

                ans[k-dif_len:i-dif_len] = [to_bijec(i - k)]
                dif_len += i - k - 1

        else:
            if decod[k] == 0 and decod[k - 1] != 0:
                    i = k
                    while i < len(decod) and decod[i] == 0: 
                        i += 1

                    ans[k-dif_len:i-dif_len] = [to_bijec(i - k)]
                    dif_len += i - k - 1


    return ans

#Q32
def zrle_decode(encodd):
    res = encodd[:]
    dif_len = 0
    for k in range(len(encodd)):
        if str(ZRLE_ONE) in str(encodd[k]) or str(ZRLE_TWO) in str(encodd[k]):
            new = str(encodd[k]).replace(str(ZRLE_ONE), str(1))
            new = [*new.replace(str(ZRLE_TWO), str(2))]
            real = 0
            for j in range(len(new)):
                real += int(new[j]) * 2**(len(new) - j - 1)

            res[k+dif_len:k+dif_len+1] = [0] * real
            dif_len += real - 1

    return res

text = 'rrrrepeeeeetiiiiingggg'
flag = True # if we're using all 256 ascii carachters as alphabet or only those who appear on the text

def main(text, flag = True):

    text_in_asc = [ord(j) for j in text]

    if flag:
        list = ListNode(255)
        for k in range(254,-1,-1):
            list = list.insert_front_symbol(k)

    else:
        set_in_asc = set(text_in_asc)

        set_in_asc = sorted([k for k in set_in_asc], reverse = True)

        list = ListNode(set_in_asc[0])
        for k in set_in_asc[1:]:
            list = list.insert_front_symbol(k)  

    encod = mtf_encode(text, flag)
    decod = mtf_decode(encod, list)
    encodd = zrle_encode(encod)
    decodd = zrle_decode(encodd)

    print(f'Original message: {text}\nEncoded message: {encod}\nZRLE encoded message: {encodd}\nZRLE decoded message: {decodd}\nDecoded message: {decod}\nIs original == decoded? {text==decod}\nWhat about ZRLE encoded == ZRLE decoded? {encodd == encodd}''')

main(text, flag)

