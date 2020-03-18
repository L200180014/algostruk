# 2a
def buatNol(m, n=0):
    if n != 0:
        matriks = [[0 for i in range(m)] for j in range(n)]
        for item in matriks:
            print(item)
    else:
        matriks = [[0 for i in range(m)] for j in range(m)]
        for item in matriks:
            print(item)
    print('\n')

buatNol(3)
buatNol(2, 4)


# 2b
def buatIdentitas(m):
    matriks = [[1 if j == i else 0 for j in range(m)] for i in range(m)]
    for baris in matriks:
        print(baris)
    print('\n')

buatIdentitas(4)
buatIdentitas(3)
