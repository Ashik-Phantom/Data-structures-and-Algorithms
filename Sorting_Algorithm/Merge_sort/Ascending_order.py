# Python program for implementation of  
# MergeSort - Sort by Ascending order
# This program get a input N and a array if input of size N and sorts the array in ascending order
  
def merge_sort(values):  
    if len(values) > 1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort(left) 
        right = merge_sort(right)   
        values =[]   
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0) 
            else: 
                values.append(right[0]) 
                right.pop(0) 
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i)                   
    return values 

n = int(input()) 
a=list(map(int,input().split()))  
print("Given array is : ") 
print(*a,'\n')  
a = merge_sort(a)   
print("Sorted array is : ") 
print(*a) 
