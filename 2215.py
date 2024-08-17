# 2215. Find the Difference of Two Arrays

# slow, beats 6%
def sol_brute(nums1, nums2):
    uniq1 = []
    uniq2 = []

    for i in nums1:
        if i not in nums2 and i not in uniq1:
            uniq1.append(i)

    for i in nums2:
        if i not in nums1 and i not in uniq2:
            uniq2.append(i)

    return [uniq1, uniq2]

# improved
def sol_set(nums1, nums2):
    s1, s2 = set(nums1), set(nums2)
    return [list(s1-s2), list(s2-s1)]

if __name__ == '__main__':
    print(sol_brute([1,2,3,3],[1,1,2,2]))
    print(sol_set([1,2,3,3],[1,1,2,2]))
