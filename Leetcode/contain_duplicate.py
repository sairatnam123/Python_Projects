"""Given an integer array nums, return true if any value appears at
 least twice in the array, and return false if every element is
 distinct"""

import array

def contain_duplicate(arr,length):
    for i in range(length):
        for j in range(i+1,length):
            if arr[i]==arr[j]:
                return True
    return False

length_of_list=int(input("Enter a number of elements in array:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a value:")))
array1= array.array('i',list1)

return_value=contain_duplicate(array1,length_of_list)
if return_value:
    print("Given array contains duplicate values")
else:
    print("Given array does not contains duplicate values")