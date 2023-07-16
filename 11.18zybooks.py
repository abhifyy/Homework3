"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
int_list = list(map(int, input().split()))
non_negative_list = []
for num in int_list:
    if num >= 0:
        non_negative_list.append(num)
non_negative_list.sort()
for num in non_negative_list:
    print(num, end=' ')
