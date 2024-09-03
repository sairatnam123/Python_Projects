"""Given an integer array nums, return all the triplets [nums[i],
 nums[j], nums[k]]
 such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 Notice that the solution set must not contain duplicate triplets."""

import array

def remove_duplicate(arr):
    i=0
    while i<len(arr):
        sorted_i = sorted(arr[i])
        j=i+1
        while j<len(arr):
            count=0
            sorted_j=sorted(arr[j])
            for k in range(len(sorted_j)):
                if sorted_i[k]==sorted_j[k]:
                    count=count+1
            if count==len(arr[j]):
                del arr[j]
            j=j+1
        i=i+1
    return arr

def triplets_sum(arr,length):
    result_list=[]
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if i!=j and j!=k and k!=i and arr[i]+arr[j]+arr[k]==0:
                    result_list.append([arr[i],arr[j],arr[k]])
    result_list=remove_duplicate(result_list)
    return result_list

length_of_list=int(input("Enter a number of elements in array:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a value:")))
array1= array.array('i',list1)
print(triplets_sum(array1,length_of_list))

