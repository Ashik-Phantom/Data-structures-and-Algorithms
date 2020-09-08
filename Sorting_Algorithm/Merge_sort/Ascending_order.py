# Python program for implementation of  
# MergeSort - Sort by Ascending order
# This program get a input N and a array if input of size N and sorts the array in ascending order
  
def merge_sort(arr):  
    if len(arr) > 1: 
        mid = len(arr)//2
        left = arr[:mid] 
        right = arr[mid:] 
        left = merge_sort(left) 
        right = merge_sort(right)   
        arr = []   
        while len(left) > 0 and len(right) > 0: 
            if left[0]<right[0]: 
                arr.append(left[0]) 
                left.pop(0) 
            else: 
                arr.append(right[0]) 
                right.pop(0) 
        for i in left: 
            arr.append(i) 
        for i in right: 
            arr.append(i)                   
    return arr 

n = int(input()) 
a=list(map(int,input().split()))  
print("Given array is : ") 
print(*a,'\n')  
a = merge_sort(a)   
print("Sorted array is : ") 
print(*a) 
