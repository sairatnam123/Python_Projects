import array

def two_sum(li,length,sum1):

    for i in range(length):
        for j in range(i+1, length):
            if li[i] + li[j] == sum1:
                return [i, j]


length_of_list=int(input("Enter a number of array items:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a value")))
list1= array.array('i',list1)
#To add two numbers in a list it returns a sum that is target value
target=int(input("Enter a target value to sum a two numbers"))
return_list=two_sum(list1,length_of_list,target)
if return_list is not None:
    print("Two sum value for given list is ",list1,"having target value is",return_list)
else:
    print("Two sum value for given list is ",list1,"not having target value is ",return_list)





