# Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

import random

nums = []
for i in range(30):
   nums.append(random.randint(1,50))
print(nums)

for i in range(len(nums)):
    index_min = i
    for j in range(i, len(nums)):
        if nums[j] < nums[index_min]: index_min = j
    nums[j], nums[index_min] = nums[index_min], nums[i]
print(nums)
