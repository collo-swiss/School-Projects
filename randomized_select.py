"""Gathumbi Collins Githiari
A program to sort elements using randomized select algorithm"""
import random
def r_select(Array, start, end, i):
    if(start == end):
        return Array[start]  
    
    pivot = r_partition(Array, start, end)
    #pivot = r_partition(Array, start, end)
    k = pivot-start+1
    print(k)
    if(i == k):
        return (Array[pivot])
    elif(i < k):
        r_select(Array, start, pivot-1, i)
    else:
        r_select(Array, pivot+1, end, i-k)

def r_partition(Array, start, end):
    a = random.randint(start, end)
    Array[a], Array[end] = Array[end], Array[a]
    p_index = partition(Array, start, end)
    return p_index

def partition(Array,start,end):
    p_index=start
    pivot=Array[start]
    for j in range(start+1,end+1):
        if Array[j]<=pivot:
            p_index += 1
            Array[p_index],Array[j] = Array[j],Array[p_index]
    Array[p_index],Array[start] = Array[start],Array[p_index]
    return p_index


array = [8, 5, 9, 4, 3, 1, 7]
start = 0
end = (len(array)-1)
print(array)
i = int(input("What rank of array would you like to get element for?\n"))
a = r_select(array, start, end, i)
print(array)
print('According to increasing size, the number ' + str(i) +' smallest element is: \n'+ str(a))
