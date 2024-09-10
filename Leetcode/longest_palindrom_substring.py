""" Given a string s, return the longest palindromic substring in s.
 Input: s = "babad"
 Output: "bab"
 Explanation: "aba" is also a valid answer
 """
def longest_palindromic_substring(string):
    longest_palindromic_strings=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if string[i:j]==string[i:j][::-1]:
                longest_palindromic_strings.append(string[i:j])
    maximum=len(longest_palindromic_strings[0])
    index=0
    for i in range(len(longest_palindromic_strings)):
        if maximum<len(longest_palindromic_strings[i]):
            maximum=len(longest_palindromic_strings[i])
            index=i
    return longest_palindromic_strings[index]

user_string=input("enter a your string:")

palindromic_string=longest_palindromic_substring(user_string)
print(palindromic_string)
