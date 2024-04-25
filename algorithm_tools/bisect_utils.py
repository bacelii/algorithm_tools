"""
Bisect module functionality

Purpose: find the insertion point for adding a given element to a list

requiremenets: 
1) must pass list in assending order
- the type of list past must be mutable (can't be string or tuple)

arguments:
1) lo and hi: the start and end indexes want to consider
- aka: lowest is the lowest index it can return, hi is the highest it can return

functions
bisect.bisect_left: will insert element leftmost of those like it
bisect.bisect_right:

--- insertion but in-place! ---
bisect.insort_left: will insert the element
bisect.insort_right: will insert the element
"""
import bisect

def example_bisect_left():
    a = [2,4,6,8,10,12,14]
    x = 7
    return bisect.bisect_left(a,x)