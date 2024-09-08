"""
 Given two strings s and t of lengths m and n respectively, return
 the minimum window substring of s such that every character in t
 (including duplicates) is included in the window. If there is no such
 substring, return the empty string ""
 Input: s = "ADOBECODEBANC", t = "ABC"
 Output: "BANC"
 Explanation: The minimum window substring "BANC" includes 'A',
 'B', and 'C' from string t.
 """


def cartesian_product(lists):
    result = [[]]
    for lst in lists:
        new_result = []
        for prefix in result:
            for item in lst:
                new_result.append(prefix + [item])
        result = new_result

    return result


def windows_substrings(string_1,target):
    dic={}
    for i in range(len(string_1)):
        if string_1[i] not in dic:
            dic[string_1[i]]=[i]
        else:
            dic[string_1[i]]=dic[string_1[i]]+[i]

    list_of_target=[]
    for i in target:
        list_of_target.append(dic[i])
    lists=cartesian_product(list_of_target)
    list_of_strings=[]
    for i in range(len(lists)):
        sorted_list=sorted(lists[i])
        list_of_strings.append(string_1[sorted_list[0]:sorted_list[-1]+1])
    minimum_length=len(list_of_strings[0])
    minimum_position=0
    for i in range(len(list_of_strings)):
        if len(list_of_strings[i])<minimum_length:
            minimum_length=len(list_of_strings[i])
            minimum_position=i
    return list_of_strings[minimum_position]

string=input("enter a string:")
t=input("enter you want to find a window string:")
print("window string is",windows_substrings(string,t),"and it's length",len(windows_substrings(string,t)))





