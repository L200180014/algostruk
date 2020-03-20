def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return "target berada di index " + str(mid)
            break

        elif target < kumpulan[mid]:
            high = mid - 1

        else:
            low = mid + 1
    return False


# kumpulan (list) harus sudah urut
# daftar = [10, 25, 30, 45, 75, 80, 100]
#
# print(binSe(daftar, 50)) # False
# print(binSe(listnya, 75)) # index-4
