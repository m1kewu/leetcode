# 605. Can Place Flowers

# to me, seems requires 2n consec zeros in the flowerbed to allow no-adjacent planting
# but tricky as 1001 cannot place 1 but 100 can

def canPlaceFlowers(flowerbed, n):

    # cool idea but does not work
    # flowerbed_str = "".join(str(x) for x in flowerbed)
    # return "0"*2*n in flowerbed_str

    count = 0

    for idx in range(len(flowerbed)):
        empty = (flowerbed[idx] == 0)
        left_empty = (idx == 0) or (flowerbed[idx - 1] == 0)
        right_empty = (idx == len(flowerbed)-1) or (flowerbed[idx + 1] == 0)

        if empty and left_empty and right_empty:
            flowerbed[idx] = 1
            count += 1

    return count >= n

if __name__ == '__main__':
    print(canPlaceFlowers([1,0,0,1],1))
    print(canPlaceFlowers([1,0,0,0,1],1))
