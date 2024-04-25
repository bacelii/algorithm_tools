"""
Review dictionary function and time complexity

Rules:
1) except for copy and iteration: dictionary complexity is O(1)
2) defaultdict() will help you not get KeyErrors and if key doesnt exist will:
    a. create the key,value pair with value = default
    
defaultdict tutorial:
    https://realpython.com/python-defaultdict/

1) the defaultdict(arg), arg is a callable or None
- ex: defaultdict(list) --> will generate an empty list if not exist
- DON'T DO: def_dict = defaultdict(list()), because argument must be callable

2) options for the callable: list,set,int,float

"""

from collections import defaultdict

def dict_operations():
    dict = {'a':1,'b':2,'c':3}
    dict2 = {'hello':5}
    mykey = "hello"
    
    results = [
        dict.keys(),
        dict.values(),
        dict.items(),
        dict.pop('key'),
        dict.popitem(), #removes most recent pair
        dict.get('a','some_default'),
        dict.setdefault('a',"default_value"), #will add the key,value pair to dict if doesn't already exist
        dict.copy(), #O(n)
        dict.update(dict2),
        mykey in dict, #O(1)
        
    ]
    
def defaultdict_instantiation():
    return defaultdict(list)

def using_default_dict_to_group_in_list():
    dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]
    
    d = defaultdict(list)
    for department,name in dep:
        d[department].append(name)
        
    return d

def using_default_dict_to_group_in_set():
    """
    Will eliminate duplicates (using the set as the iterable)

    Returns
    -------
    _type_
        _description_
    """
    dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

    d = defaultdict(set)
    for depart,name in dep:
        d[depart].add(name)
        
    return d

def using_defaultdict_to_count_items():
    s = 'mississippi'
    dd = defaultdict(int)
    for letter in s:
        dd[letter] += 1


from collections import Counter
def using_counter_to_count_items():
    s = 'mississippi'
    curr_counter= Counter(s)
    print(curr_counter.most_common(1))
    return 
    