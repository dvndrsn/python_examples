import inspect

def lineno():
    input() # this just makes it step through when people press enter.
    return "at line " + str(inspect.currentframe().f_back.f_lineno)

class yrange(object):
    def __init__(self, max):
        print("initializing ", lineno())
        self.max = max
        self.current = 0

    def __iter__(self):
        print("converting to an iter, but we are "
            "an iter already, so just return self ", lineno())
        return self

    def __next__(self):
        print("inside next ", lineno())
        if self.current >= self.max:
            print("self.current >= self.max, so "
                 "time to raise StopIteration()", lineno())
            raise StopIteration()
        tmp = self.current
        self.current += 1
        return tmp

def yrange_gen(max):
    print("at beginning of yrange_gen ", lineno())
    i = 0
    while i < max:
       print("inside loop of yrange_gen ", lineno())
       yield i
       i += 1
    print("finished loop of yrange_gen ", lineno())

print("=" * 80)
print("with an iterator")
print("=" * 80)

for i in yrange(3):
    print(i, " ", lineno())


print("\n" * 2)

print("=" * 80)
print("with a generator")
print("=" * 80)

for i in yrange_gen(3):
    print(i, " ", lineno())
