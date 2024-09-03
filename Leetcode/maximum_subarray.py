"""Given an integer array nums, find the subarray with the largest
 sum, and return its sum.
 Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
 Output: 6"""


import array

def maximum_subarray(arr,length):
    global list1
    maximum=0
    for i in range(length):
        summation=0
        for j in range(i,length):
            summation=summation+arr[j]
            if maximum<summation:
                maximum=summation
                list1=arr[i:j+1]
    return list1



length_of_list=int(input("Enter a number of elements in array:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a value:")))
array1= array.array('i',list1)
return_list=maximum_subarray(array1,length_of_list)
print("maximum subarray of given list",return_list)
