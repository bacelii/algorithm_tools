"""
review functionality of sets: unordered, immutable, unindexed,

Sets are implemented as a hash table, so most of the operations are O(1)

Notes:
1) can have multiple arguments in set difference, intersection, union
- and when do this they don't have to be sets themselves
2) ADD not append
3) REMOVE not delete
4) a set is an unhashable type
"""



def set_operations(
        s = {1,2,3},
        anotherset = {4,5,6,}
        ):
    
    item = 10
    anotherset 
    
    results = [
        3 in s,# O(1)
        s.add(item),
        s.remove(item),
        s.pop(), # removes a random item O(1)
        
        # advanced sets
        s.isdisjoint(anotherset),
        s.issubset(anotherset), # checks if anotherset is subset
        s.issuperset(anotherset),
        
        #differences,intersections and unions
        s.difference(anotherset), # O(s)
        s.intersection(anotherset), # O(min(s,a))
        s.union(anotherset), # O(len(s) + len(a))
        
        
        s.update(anotherset),
    ]
    
    
