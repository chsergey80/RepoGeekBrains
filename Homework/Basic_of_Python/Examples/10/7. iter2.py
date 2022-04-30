class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    def __next__(self):
        print("NEXT")
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration

    def __iter__(self):
        print("ITER")
        return self


obj = Iter(start=-2)
for el in obj:
    print(el)

print()
for el in obj:
    print(el)