import array

def rotateSearch(arr,target_value):
    for i in range(len(arr)):
        if arr[i]==target_value:
            return i
    return -1


length_of_list=int(input("Enter a number of elements in array:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a value:")))
array1= array.array('i',list1)

target=int(input("enter a target value:"))

return_list=rotateSearch(array1,target)

print("Target value is found at index position is ",return_list,"in given list is",array1)