""" Given an integer array nums, find a subarray that has the largest
 product, and return the product."""


import array

def maximum_product_subarray(arr,length):
    maximum=0
    result=[]
    for i in range(length):
        product=1
        for j in range(i,length):
            product=product*arr[j]
            if maximum<product:
                maximum=product
                result=arr[i:j+1]
    if len(result)==0:
        return 0
    return result



length_of_list=int(input("Enter a number of elements in array:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a value:")))
array1= array.array('i',list1)
return_list=maximum_product_subarray(array1,length_of_list)

print("maximum product of subarray for given list",return_list)
