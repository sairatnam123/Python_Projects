"""
In Doraland, people have unique Identity Numbers called D-id.
Doraemon owns the most popular gadget shop in Doraland.
Since his gadgets are in high demand and he has only K gadgets left he has decided to sell his gadgets to his most frequent customers only.
N customers visit his shop and D-id of each customer is given in an array array[ ].
In case two or more people have visited his shop the same number of time he gives priority to the customer with higher D-id.
Find the D-ids of people he sells his K gadgets to.

Example 1:

Input:
N = 6
array[] = {1, 1, 1, 2, 2, 3}
K = 2
Output:
1 2
Explanation:
Customers with D-id 1 and 2 are most
frequent.
"""


def TopK(array, k):
    # code here
    freq = {}
    for i in array:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] = freq[i] + 1
    print(freq)
    values=freq.values()
    l=[]
    for i in range(k):
        max_value=max(values)
        keys = [key for key, value in freq.items() if value == max_value]
        l.append(max(keys))
        freq.pop(max(keys))
    print(l)
N = 6
array = [1, 1, 1, 2, 2, 3,3]
K = 2

TopK(array,K)

