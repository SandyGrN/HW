'''
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase,
typically using all the original letters exactly once.
'''

# 242. Valid Anagram


def is_anagram(s: str, t: str) -> bool:
    if ''.join(sorted(s)) == ''.join(sorted(t)):
        return True
    else:
        return False


s = "dnagram"
t = "dnagram"
print(is_anagram(s, t))


'''
Given an integer array nums, return the third distinct maximum number
in this array.
If the third maximum does not exist, return the maximum number.
'''
# знайти n із найбільшим значенням у list
# 414. Third Maximum Number


def third_max(nums: list) -> int:
    return sorted(nums)[-1]


nums = [2, 1, 3]
print(third_max(nums))

'''
Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one. You must implement a solution with
a linear runtime complexity and use only constant extra space.
'''
# 136. Single Number


def single_number(nums: list) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i


def single_number1(nums: list) -> int:
    num = ''.join(str(i) for i in nums if nums.count(i) == 1)
    return int(num)


nums = [4, 1, 2, 1, 2, 4, 4, 6]
print(single_number(nums))
