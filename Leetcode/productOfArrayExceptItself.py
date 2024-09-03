"""Given an integer array nums, return an array answer such that
 answer[i] is equal to the product of all the elements of nums
 except nums[I]
"""
import array

def ProductOfArrayExpectItself(arr,length):
    result=[]
    for i in range(length):
        product=1
        for j in range(length):
            if i==j:
                continue
            else:
                product=product*arr[j]
        result.append(product)
    return result


length_of_list=int(input("Enter a number of elements in array:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a value:")))
array1= array.array('i',list1)
return_list=ProductOfArrayExpectItself(array1,length_of_list)
print("Product list expect itself",return_list)