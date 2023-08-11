# En

# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# Ru

# Учитывая отсортированный массив различных целых чисел и целевое значение,
# верните индекс, если целевое значение найдено. Если нет, верните индекс туда,
# где он был бы, если бы он был вставлен по порядку.
#
# Вы должны написать алгоритм со сложностью выполнения O(log n).
#
# Пример 1:
#
# Ввод: числа = [1,3,5,6], цель = 5
# Вывод: 2
# Пример 2:
#
# Ввод: числа = [1,3,5,6], цель = 2
# Вывод: 1
# Пример 3:
#
# Ввод: числа = [1,3,5,6], цель = 7
# Вывод: 4
#
#
# Ограничения:
#
# 1 <= числа.длина <= 104
# -104 <= числа[i] <= 104
# nums содержит различные значения, отсортированные в порядке возрастания.
# -104 <= цель <= 104

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    nums.append(target)
    return sorted(nums).index(target)

print(searchInsert([1,3,5,6], 7))
