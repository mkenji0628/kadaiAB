"""
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""

input_number = [int(s) for s in input('データを入力してください(スペース区切り) > ').split()]


# 合計値
def total():
    add = 0
    for n in input_number:
        add += n
    return add


print(f"合計値: {total()}")


# 最大値
def max():
    max_num = input_number[0]
    for n in input_number:
        if max_num < n:
            max_num = n
    return max_num


print(f"最大値: {max()}")


# 最小値
def min():
    min_num = input_number[0]
    for n in input_number:
        if n < min_num:
            min_num = n
    return min_num


print(f"最小値: {min()}")


# 平均値
def avg():
    avg_num = input_number[0]
    for n in input_number:
        avg_num = total() // len(input_number)
    return avg_num


print(f"最小値: {avg()}")
