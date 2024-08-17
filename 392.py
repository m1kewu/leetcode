# 392. Is Subsequence

# surprisingly difficult
def sol(s, t):
    sp = tp = 0

    # this dual-pointer pattern is instructive
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1

    return sp == len(s)


if __name__ == "__main__":
    s = "abc"
    t = "xyzahbgdc"
    print(sol(s, t))

    s = "abc"
    t = "xyzahdccvgdcbb"
    print(sol(s, t))
