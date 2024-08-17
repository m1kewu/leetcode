def kidsWithCandies(candies, extraCandies):
    current_most = max(candies)
    return [x + extraCandies >= current_most for x in candies]


if __name__ == '__main__':
    print(kidsWithCandies([1, 2, 3, 4, 5], 2))
