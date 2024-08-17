# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels += [x.upper() for x in vowels]

    vowels_in_word = []

    for ch in s:
        if ch in vowels:
            vowels_in_word.append(ch)

    new_word = ""

    for ch in s:
        if ch in vowels:
            new_word += vowels_in_word.pop()
        else:
            new_word += ch

    return new_word

# improved python3 simple solution
def sol2(s):
    s = list(s)
    n = len(s)
    left = 0
    right = n - 1
    vowels = set('AEIOUaeiou')

    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1

        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)


if __name__ == '__main__':
    # print(reverseVowels("WE must wIn tHIs!"))

    print(sol2("WE must wIn tHIs!"))
