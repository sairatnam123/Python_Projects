"""
 Given a string s, return the number of palindromic substrings in it.
 A string is a palindrome when it reads the same backward as
 forward.
 A substring is a contiguous sequence of characters within the
 string.
 """

def longest_palindromic_substring(string):
    longest_palindromic_strings=[]
    for i in range(len(string)+1):
        for j in range(i+1,len(string)+1):
            if string[i:j]==string[i:j][::-1]:
                longest_palindromic_strings.append(string[i:j])
    return longest_palindromic_strings

user_string=input("enter a your string:")

palindromic_strings=longest_palindromic_substring(user_string)
print("length of palindromic strings is",len(palindromic_strings),"list of strings",sorted(palindromic_strings))
