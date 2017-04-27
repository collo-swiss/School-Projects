"""Gathumbi Collins Githiari
A Program to sort elements using merge sort"""
def sort(array):
    if int(len(array)>1):
        half = int(len(array)/2)
        a_list = array[:half]
        b_list = array[half:]
        
        sort(a_list)
        sort(b_list)

        print(a_list)
        print(b_list)
        
        a = 0
        b = 0
        c = 0
        
        while a < len(a_list) and b < len(b_list):
             if a_list[a] < b_list[b]:
                 array[c] = a_list[a]
                 a=a+1
             else:
                array[c]= b_list[b]
                b=b+1         
             c=c+1

        while a < len(a_list):
            array[c]= a_list[a]
            a=a+1
            c=c+1
        while b < len(b_list):
            array[c]= b_list[b]
            b=b+1
            c=c+1

hold = input("Please enter elements of list: ")
array = []
array = hold.strip().split(',')
print(array)
sort(array)
print(array)
    
