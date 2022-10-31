#1
def countdown(num):
    newlist = []
    for i in range(num,-1,-1):
        newlist.append(i)
    return newlist

print(countdown(5))

#2
def print_and_return(arr):
    for i in range(len(arr)):
        print(arr[0])
        return arr[1]

print(print_and_return([1,2]))

#3
def first_plus_length(arr):
    sum = arr[0] + len(arr)
    return sum

print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(arr): 
    newlist = []
    for i in range(len(arr)): 
        if len(arr) < 2:
            return False
        if arr[i] > arr[1]: 
            newlist.append(arr[i])
    if len(newlist) < 2:
            return False
    print(len(newlist))
    return newlist

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5
def length_and_value(size,value):
    newlist = []
    for i in range(size):
        newlist.append(value)
    return newlist

print(length_and_value(4,7))
print(length_and_value(6,2))
