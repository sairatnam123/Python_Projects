"""You are given a string s and an integer k. You can choose any
 character of the string and change it to any other uppercase
 English character. You can perform this operation at most k times.
 Return the length of the longest substring containing the same
 letter you can get after performing the above operations.
 Input: s = "ABAB", k = 2
 Output: 4"""

def find_longest_substring(new_string,target_char):
    target_substring=""
    for i in range(1,len(new_string)-1):
        if  (new_string[i]==new_string[i+1] and new_string[i]==target_char) or (new_string[i-1]==new_string[i] and new_string[i]==target_char):
                target_substring=target_substring+new_string[i]

    return target_substring

def replacing_characters(string_,char_):
    remove_duplicates=""
    for i in string_:
        if i not in remove_duplicates:
            remove_duplicates=remove_duplicates+i
    source=remove_duplicates[0]
    target=remove_duplicates[len(remove_duplicates)-1]
    string_=string_.replace(source,target,char_)
    target_string=find_longest_substring(string_,target)
    return target_string




string=input("enter a capital letters String")
k=int(input("enter an integer"))
#replace the above string with its any character by n times

result = replacing_characters(string,k)

print("The longest substring after perform kth operations",result,"and length is",len(result))

