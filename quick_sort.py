"""Gathumbi Collins Githiari
A program to sort elements using Quick Sort algorithm."""
def quick_sort(array, start, end):
    if(start < end):
        p_index = partition(array)
        quick_sort(array, start, p_index-1)
        quick_sort(array, p_index+1, end)
    return(array)

def partition(array):
    end = (len(array)-1)
    start = 0
    pivot = array[end]
    p_index = array[start]
    i = 0
    print(array)

    while i < end:
        if (array[i] < pivot):
            array[i], p_index = p_index, array[i]
            p_index += 1
        i += 1
    pivot, p_index = p_index, pivot
    return (p_index)

array = [8, 5, 9, 4, 3, 1, 7]
start = 0
end = (len(array)-1)
print('The unsorted array is \n',array,'\n')
print('the sorted array \n',quick_sort(array, start, end))
