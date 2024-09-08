string="zerox"
number=2
string1=""

for i in range(len(string)):
    char_number=ord(string[i])
    char_=char_number+number
    if char_>ord('z'):
        char_ =char_-26
    character=chr(char_)
    string1=string1+character
print(string1)






