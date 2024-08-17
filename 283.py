# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
import numpy as np
def sol(nums):
    print("-"*50)
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:

    # not very obvious, print out should aid the mechanics

            print(f"swap of left={nums[left]}[idx={left}] and right={nums[right]}[idx={right}] ")
            nums[right], nums[left] = nums[left], nums[right]

            print(f"\tafter swap: {nums}")
            left += 1
    print("-" * 50)

    return nums


def sol_short(nums):
    l = 0

    for r in range(len(nums)):
        if nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
    return nums


if __name__ == '__main__':
    example1 = [1, 0, 0, 2, 3, 0, 4, 5, 0, 0, 6, 7, 0, 0, 0, 0, 8, 9, 0, 0]
    example2 = [1, 2, 3, 4, 5]

    sol(example1)
    sol(example2)
