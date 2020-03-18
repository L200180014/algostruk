# 1a
def cekMatrix(matrix):
    panjang = len(matrix)
    for x in matrix:
        lebar = len(x)
        for i in x:
            if type(i) != int:
                break
    return panjang == lebar and type(i) == int

m1 = [[2, 3], [2, 1]]
m2 = [[3, 3, 4], [4, 5, 7], [2, 0, 1]]
m3 = [[3, 3, 4], [4, '5', 7], [2, 0, '1']]  # ada string
m4 = [[2, 1], [2, 3, 1]]  # beda ukuran
m5 = [['5', 3, 5], [5, 6, 5]]  # ada string

# print(cekMatrix(m1))
# print(cekMatrix(m2))
# print(cekMatrix(m3))
# print(cekMatrix(m4))
# print(cekMatrix(m5))


# 1b
def ukuranMatrix(matrix):
    m = len(matrix)
    for i in matrix:
        n = len(i)
    return m, n

ma = [[2, 3], [2, 1]]
mb = [[3, 3, 4], [4, 5, 7], [2, 0, 1]]
mc = [[3, 3, 4], [4, '5', 7]]
md = [[2, 1], [2, 1], [5, 7]]

# print(ukuranMatrix(ma))
# print(ukuranMatrix(mb))
# print(ukuranMatrix(mc))
# print(ukuranMatrix(md))


# 1c
def menjumlahkan(X, Y):
    if ukuranMatrix(X) == ukuranMatrix(Y):
        result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for i in range(len(X)):
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]
        for r in result:
            print(r)
        print('\n')
    else:
        print('! Ukuran matriks ngga sama woyy !')


A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
C = [[12, 7],
     [4, 5]]

# menjumlahkan(A, B)
# menjumlahkan(A, C)


# 1d
def mengalikan(X, Y):
    for i in X:
        kolomX = len(i)
    barisY = len(Y)
    if barisY == kolomX:
        result = [[sum(a * b for a, b in zip(X_row, Y_col))
                   for Y_col in zip(*Y)] for X_row in X]

        for r in result:
            print(r)
    else:
        print('! Ukuran matrix tidak sesuai (baris Y != kolom X) !')
    print('\n')

X = [[1, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 0, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
Z = [[1, 2],
     [2, 5]]

# mengalikan(X, Y)
# mengalikan(X, Z)


# 1e
def determinan(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if len(A[i]) == x:
            z += 1
    if z == len(A):
        if x == len(A):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices:
                As = A
                As = As[1:]
                height = len(As)
                for i in range(height):
                    As[i] = As[i][0:fc] + As[i][fc + 1:]
                sign = (-1) ** (fc % 2)
                sub_det = determinan(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total

# J = [[3, 1], [2, 5]]
# K = [[1, 2, 1], [3, 3, 1], [2, 1, 2]]
# L = [[1, -2, 0, 0], [3, 2, -3, 1], [4, 0, 5, 1], [2, 3, -1, 4]]
# M = [[3, 4], [2, 4], [1, 5]]
# print(determinan(J))
# print(determinan(K))
# print(determinan(L))
# print(determinan(M))
