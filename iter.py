import sys

def fib_gen(max_num=sys.maxsize):
    '''http://www.learnpython.org/en/Generators'''
    curr, prev = [1, 0]
    i = 0

    while (i < max_num):
        i += 1
        next = curr
        curr, prev = curr + prev, curr
        yield next

class fib_iter(object):
    '''http://www.diveintopython3.net/iterators.html'''
    def __init__(self, n=sys.maxsize):
        self.max_num = n

    def __iter__(self):
        self.curr = 1
        self.prev = 0
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.max_num:
            self.i += 1
            next = self.curr
            self.curr, self.prev = self.curr + self.prev, self.curr
            return next
        else:
            raise StopIteration()


if __name__ == '__main__':
    print("Generator - first 10 fibonacci numbers")
    # https://wiki.python.org/moin/Generators
    # http://www.learnpython.org/en/Generators
    for n in fib_gen(10):
        print(n)

    print("Iterator - fibonacci numbers ")
    # https://wiki.python.org/moin/Iterator
    for n in fib_iter(10):
        print(n)

    print("List comprehension from generator - n**2")
    # http://www.learnpython.org/en/List_Comprehensions
    listcomp = [n**2 for n in range(10) if n**2 % 3 != 0]

    print("List comprehension from list - positive numbers as integer")
    # http://www.learnpython.org/en/List_Comprehensions
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    newlist = [int(n) for n in numbers if n > 0]

    print(numbers)
    print(newlist)

    print("Generator expression - n**2")
    genex = (n**2 for n in range(10))
    print(type(genex))
    for n in genex:
        print(n)

    # Can't use iterator or generator after it has been exhausted
    # Use list if it is required to iterate over multiple times
    # Create a list from a generator
    genex = (n**2 for n in range(10))
    l = list(genex)
    print(l)
