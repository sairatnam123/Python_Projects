"""
 Given an array of strings strs, group the anagrams together. You
 can return the answer in any order.
 An Anagram is a word or phrase formed by rearranging the letters
 of a different word or phrase, typically using all the original letters
 exactly once.
 Input: strs = ["eat","tea","tan","ate","nat","bat"]
 Output: [["bat"],["nat","tan"],["ate","eat","tea"]]"""



def sorting_string(string):
    string_list=[]
    for i in string:
        string_list.append(i)
    for i in range(len(string)):
        for j in range(i,len(string)):
            if ord(string_list[j-1])>=ord(string_list[j]):
                string_list[j],string_list[j-1]=string_list[j-1],string_list[j]
    new_string=""
    for i in string_list:
        new_string=new_string+i
    return new_string

def group_of_anagrams(strings):
    lists=[]
    i=0
    while i<len(strings):
        l=[strings[i]]
        j=i+1
        while j<len(strings):
            if sorting_string(strings[i])==sorting_string(strings[j]):
                l.append(strings[j])
                strings.remove(strings[j])
            j=j+1
        lists.append(l)
        i=i+1
    return lists

list_strings = ["eat","tea","tan","ate","nat","bat"]
anagram_lists=group_of_anagrams(list_strings)
if len(anagram_lists)!=0:
    print("Given the list have a anagram lists",anagram_lists)
else:
    print("Given the list does not contain anagrams")
