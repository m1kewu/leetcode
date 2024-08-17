# 643. Maximum Average Subarray
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

# time limit exceeded!
# then still struggled with cases

def sol_brute(nums, k):
    l = len(nums)

    if l == 1:
        return nums[0]

    avg = []
    for i in range(l-k+1): # discovered via a failed case
        # print(nums[i:i+k])
        avg.append(sum(nums[i:i+k])/k)

    return max(avg)

# only beats 40%
def sol_sliding(nums, k):
    currSum = maxSum = sum(nums[:k])

    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, currSum)

    return maxSum / k


if __name__ == '__main__':
    # print(sol_brute([5], 1))
    # print(sol_brute([5,8,9,3,7,4,1], 2))
    # print(sol_brute([0,1,1,3,3], 4))

    print(sol_sliding([0,1,1,3,3], 4))
    print(sol_sliding([0,4,0,3,2], 1))
    print(sol_sliding([4,2,1,3,3], 2))