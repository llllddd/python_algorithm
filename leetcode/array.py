'''
Array: a collection of items stored at contiguous memory locations.
There are several classes of array:
1. Static Array: the size of the array is fixed at the  time when it is created.
2. Dynamic Array: the array is resizeable, during runtime by allocating a new array and copying the old array to the new array.
'''

# Define a static array with fixed size 10

# assign value using index

# retriveve value using index

'''
Array or all the datastuctures are desgined for adding, removing, searching, and accessing elements.
Static array
1. Adding: O(n), since we need to shift existed elements to make space for the new element.
'''

#1. Append: add element at the tail, we add an element at index 5, for an existed array of size 4

#2. Insert: add element at the midle of the array
arr = [0]*10
for i in range (4):
    arr[i] = i

# insert element at the index 2
for i in range(4,2,-1):
    arr[i] = arr[i-1]
arr[2] = 99

'''
Dynamic Array: resizeable array
'''
arr = [] # We don't need to point the size explicitly.
for i in range(10):
    arr.append(i)

# insert element at index 5
arr.insert(5,99)

# remove element at the end
arr.pop()

# remove element at index 3
arr.pop(3)

# retrieve elament at index 4
val = arr[4]

# find the index of an element
index = arr.index(99)









