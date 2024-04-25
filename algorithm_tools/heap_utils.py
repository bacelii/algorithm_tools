"""
review heap functionality

idea: nodes in heap will always be at least as large as root (always greater)
- can help make a priority queue

Heap creation: O(n): uses siftDown operation on n nodes
sift up (insertions): O(log(n))

Notes:
1) O(logN) for heappush and heappop
2) Creating the heap: linear time OPERATION WILL DO IN PLACE
3) heapq.heapify is always min heap, if want max heap then just turn neg
4) ALWAYS HAVE TO INCLUDE THE LIST AS AN ARGUMENT TO HEAPIFY


Insertion: bubbling up 
1) Put at bottom of tree, and then keep swapping with parent until
parent is less than it

Removing: bubbling down
1) pop the minute element
2) put last element in the root node
3) bubble down (swapping with smaller of the 2)

implementation: use an array to store:
left child = 2*k + 1
right child = 2*k + 2
parent index = (k - 1) // 2

"""
import heapq

def heap_operations(
        nums = [5,7,9,10]
        ):
    
    heapq.heapify(nums)
    elem = 11
    
    results = [
        heapq.heapify(nums), # O(n)
        heapq.heappush(nums,elem),
        heapq.heappop(nums), # O(log(n))
    ]
    
    print(results)
    
    
def creating_max_heap():
    heap = []
    heapq.heappush(heap, 1*(-1))
    heapq.heappush(heap, 10*(-1))
    heapq.heappush(heap, 20*(-1))
    print(heap)

    """    
    The output will look like:

    [-20, -1, -10]
    """
    #when popping element multiply it with -1

    max_element = -heapq.heappop(heap)
    print(max_element)

    