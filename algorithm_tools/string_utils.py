"""

Notes:
- boolean value of string is if len(str) > 0s
- Strings are immutable, when alter it, then create new object
- to concatenate str, better to collect in list and then join at end (instead of adding on incrementally becasue that would be O(n+m) everytime )
"""
import time


def string_operations(s = "+++-hELLO123 there"):
    results = [
        s.lower(), # makes all lowercase
        s.upper(),
        s.title(), # make captialize first letter
        s.strip("++-"),#removes characters from beginning and end of string
        s.split(" "),# splits into list on whitespace (default) or specified arg
        s.find("L"), #returns index of FIRST occurence of string, -1 if none found
        s.replace("L","y"), #replaces ALL OCCURRENCES of first argument with second
        "---".join(s.split("e")),
        "E" in s, #deterimines if substring is found
        s[5:9], # can slice a string
        [k for k in s], # can iterate through string like list
        s + " hhhiiiii", # can concatenate strings, but creates new str obj
        s.isnumeric(), # returns if numeric
        s.isdigit(),
    ]   
    
    for k in results:
        print(k)
        
def best_string_concatenation():
    s_list = ['hi','hello','howdy','yes']*1000
    
    st = time.time()
    total_str = ""
    for k in s_list:
        total_str += k
    print(f"incrementally concatenaating: {time.time() - st}")
    
    st = time.time()
    total_str = "".join(s_list)
    print(f"join: {time.time() - st}")