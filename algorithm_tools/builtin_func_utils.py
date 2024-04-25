"""

Useful functions for built in:

1) map(fun, iter): creates an iterator (call next over)
2) zip(l1,l2,l3)
3) any([]), any([]): computes logical equivalence
4) math
    math.ceil
    math.floor
    math.pi
    math.e
"""

def map_example():
    def add_one(x):
        return x + 1

    list(map(add_one,[1,2,3,4]))