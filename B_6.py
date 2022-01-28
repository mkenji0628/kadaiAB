"""
サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
"""

import random

men = int(input("サイコロの面の数は?: "))
kai = int(input("何回振りますか?: "))

daice_list = []
for n in range(0, kai):
    daice_list.append(random.randint(1, men))

print(daice_list)
