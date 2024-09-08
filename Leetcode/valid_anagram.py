"""Given two strings s and t, return true if t is an anagram of s, and
 false otherwise.
 An Anagram is a word or phrase formed by rearranging the letters
 of a different word or phrase, typically using all the original letters
 exactly once.
 Input: s = "anagram", t = "nagaram"
 Output: true
 Input: s = "rat", t = "car"
 Output: false"""

def sorting_string(string):
    string_list=[]
    for i in string:
        string_list.append(i)
    for i in range(len(string)):
        for j in range(i,len(string)-1):
            if ord(string_list[j])>=ord(string_list[j+1]):
                string_list[j],string_list[j+1]=string_list[j+1],string_list[j]
    new_string=""
    for i in string_list:
        new_string=new_string+i
    return new_string

def valid_anagram(string,target):
    string=sorting_string(string)
    target=sorting_string(target)
    count=0
    for i in range(len(string)):
        if string[i]==target[i]:
            count=count+1
    if count==len(string):
        return True
    return False

user_string=input("enter a user anagram:")
target_=input("enter a target:")
valid=valid_anagram(user_string,target_)
if valid:
    print(f"{target_} and {user_string} both are anagram")
else:
    print(f"{target_} and {user_string} both does not a anagram")

