# 1071. Greatest Common Divisor of Strings
# incredibly clever GCD condition, one-liner implementation in c++ fastest, same algo in py only 65%-tile

import math


def sol(str1, str2):
    # if an only if GCD of strings present
    if str1 + str2 == str2 + str1:
        return str1[:math.gcd(len(str1), len(str2))]


if __name__ == "__main__":
    print(sol("testtest", "testtesttest"))
