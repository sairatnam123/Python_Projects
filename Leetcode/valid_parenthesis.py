"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.
"""
def valid_parenthesis(string):
    matching_pairs={')':'(',']':'[','}':'{'}
    stack=[]
    for char in string:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if not stack or stack[-1]!=matching_pairs[char]:
                return False
            stack.pop()
        else:
            continue
    return not stack

print(valid_parenthesis("{[]}"))