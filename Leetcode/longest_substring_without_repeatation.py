"""Longest Substring Without
 Repeating Characters
 Given a string s, find the length of the longest
substring without repeating characters.
 Input: s = "abcabcbb"
 Output: 3
 Explanation: The answer is "abc", with a length of 3"""

def longestStringWithOutRepeating(string):
    remove_duplicates=""
    for i in string:
        if i not in remove_duplicates:
            remove_duplicates=remove_duplicates+i
    return remove_duplicates

user_string=input("enter a string with repeating words")

unique_string=longestStringWithOutRepeating(user_string)

print(f'unique string is {unique_string}  and its length is {len(unique_string)}')

