"""
Utility functions and notes for lists

Cheat sheet: https://github.com/AbdulMalikDev/PythonCheatSheet
"""

import numpy as np
import time

def list_functions():
    nums = [1,2,3,10]
    
    outputs = [
        nums.index(10),#returns the first index of the value: O(n)
        nums.append(1), #adds to the end of the list: O(1)
        nums.insert(0,10), # inserts (index,value): O(n) **slow compared to append
        nums.remove(3), # removes FIRST occurance of value: O(n)
        nums.copy(), # returns shallow copy: O(n)
        nums.count(10), # returns number of occurrances of value: O(n)
        nums.extend([5,6,7]), #appends on other list: O(k)
        nums.pop(5), # removes and returns item [default = -1]: O(-k)
        # pop intermediate: O(n)
        # pop last: O(1)
        nums.reverse(), # reverses in place: O(n)
        nums.sort(), # sorts list: O(n*logn), in place
        del nums[4],  # deletes index O(n)
        nums[1:5], #gets slice O(k)
        nums[6] = 10, #setting item: O(1)
        nums[10:15] = [1,2,3,4], #setting a slice: O(k + n)
        
    ]

import itertools
def combine_list_of_lists(
        l_of_l:list=[[6,4,5],[5,6,7]]
    ) -> list:
    return itertools.chain.from_iterable(l_of_l)

def combinations(
    arr,c):
    return list(itertools.combinations(arr,c))
    
def permutations(
        arr,c):
    return list(itertools.permutations(arr,c))

def best_way_to_initialize_list(N = 100000,verbose = True):
    """
    Conclusion
    ----------
    Still better to just append onto list than preallocate

    Parameters
    ----------
    N : int, optional
        _description_, by default 100000
    verbose : bool, optional
        _description_, by default True
    """
    rand_list = np.random.rand(1,N)
    
    st = time.time()
    list_comp = [None]*len(rand_list)
    for i,k in enumerate(rand_list):
        list_comp[i] = k
    print(f"Runtime for preallocation = {time.time() - st}")
    
    st = time.time()
    append_list = []
    for i,k in enumerate(rand_list):
        append_list.append(k)
    print(f"Runtime for appending list = {time.time() - st}")