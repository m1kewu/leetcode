# 1768. Merge Strings Alternately

def sol(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    len_common = min(len1, len2)

    ans = ""
    for i in range(len_common):
        ans += word1[i] + word2[i]

    if len1 >= len2:
        ans += word1[len_common:]
    else:
        ans += word2[len_common:]

    return ans


if __name__ == "__main__":
    print(sol("hello", "12345678"))
