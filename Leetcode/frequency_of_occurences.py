
n = int(input())
dic = {}
for i in range(n):
    freq, num = tuple(map(int, input().split()))
    dic[num] = freq


if len(dic) == 1:
    print(0)
else:
    max_freq = -float('inf')
    min_freq = float('inf')

    min_num = None
    max_num = None

    for num, freq in dic.items():
        if freq < min_freq or (freq == min_freq and num < min_num):
            min_freq = freq
            min_num = num
        if freq > max_freq or (freq == max_freq and num > max_num):
            max_freq = freq
            max_num = num

    if min_num is not None and max_num is not None:
        print(max_num - min_num)
