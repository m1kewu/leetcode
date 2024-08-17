# 1732. Find the Highest Altitude
# The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude. Return the highest altitude of a point.

# finally an easy one, beats 96%
def sol(gain):
    alt = ans = 0

    for g in gain:
        alt += g
        ans = max(ans, alt)

    return ans


if __name__ == '__main__':
    print(sol([-5,1,5,0,-7]))
    print(sol([-4,-3,-2,-1,4,3,2]))