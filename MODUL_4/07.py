def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    listku = []

    while low <= high:
        if kumpulan[low] == target:
            listku.append(low)
            low += 1
        else:
            low += 1
    return listku


s = [2, 6, 5, 6, 4, 6, 7, 8, 6, 2, 4, 10, 4, 14, 15]
# binSe(s, 6)
