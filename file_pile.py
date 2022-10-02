class File:
    def __init__(self):
        self.contents = []

    def enqueue(self, x):
        self.contents.append(x)

    def dequeue(self):
        x = self.contents[0]
        self.contents.pop(0)

        return x

    def empty(self):
        return not self.contents

class Pile:
    def __init__(self):
        self.contents = []

    def push(self, x):
        self.contents.append(x)

    def pop(self):
        e = len(self.contents) - 1
        x = self.contents[e]
        self.contents.pop(e)

        return x

    def top(self):
        return self.contents[len(self.contents) - 1]

    def empty(self):
        return not self.contents
