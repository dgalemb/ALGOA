from file_pile import File, Pile


def bataille(L1, L2):
    # Q1, Q2 sont des files et P1, P2 sont des piles
    Q1 = File()
    Q2 = File()
    P1 = Pile()
    P2 = Pile()

    for c in L1:
        Q1.enqueue(c)
    
    for c in L2:
        Q2.enqueue(c)

    while not Q1.empty() and not Q2.empty():
        done = False
        while not done and not Q1.empty() and not Q2.empty():
            done = True
            P1.push(Q1.dequeue())
            P2.push(Q2.dequeue())

            if P1.top() > P2.top():
                while not P1.empty():
                    Q1.enqueue(P1.pop())
                    Q1.enqueue(P2.pop())
            elif P1.top() < P2.top():
                while not P1.empty():
                    Q2.enqueue(P2.pop())
                    Q2.enqueue(P1.pop())
            else:
                if not Q1.empty() and not Q2.empty():
                    P1.push(Q1.dequeue())
                    P2.push(Q2.dequeue())
                    done = False

    if Q1.empty():
        return 2
    else:
        return 1

print(bataille([2, 14, 14, 8, 7, 5, 11, 12], [14, 13, 4, 5, 8, 9, 9, 2]))
