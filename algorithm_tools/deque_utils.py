"""
Overview of double-ended queue (deque) functionality

Cheat sheet: https://github.com/AbdulMalikDev/PythonCheatSheet?tab=readme-ov-file#deque

Advantage: 
1) can add or remove from either end with O(1)
2) used to build FIFO efficiently because will use popleft

Notes:
1) from collections (just like defaultdict and Counter)
2) cannot perform a slice on a deque

"""
from collections import deque

def deque_operations():
    q = deque(['name','age','DOB'])
    
    index = 0
    element = 'hi'
    
    results = [
        q.copy(), #copies O(n)
        q.append("appended_to_right"),# O(1)
        q.appendleft('append_to_left'), # O(1)
        q.pop(), #pops from right: O(1)
        q.popleft(), #pops from right O(1)
        q.extend(), # O(k)
        q.extendleft(), # O(k)
        q.insert(index,element),
        q.remove, #removes the first instance: O(n)
        q.reverse, #reverses inplace: O(n)
        
    ]
