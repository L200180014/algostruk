def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp


def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini + 1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil


def bubblesort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)


def selectionsort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiterkecil(A, i, n)
        if indexkecil != i:
            swap(A, i, indexkecil)


def insertionsort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai


from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak()
bubblesort(u_bub)
ak = detak()
print('Buble      : %g detik' % (ak - aw))
aw = detak()
selectionsort(u_sel)
ak = detak()
print('Selection  : %g detik' % (ak - aw))
aw = detak()
insertionsort(u_ins)
ak = detak()
print('Insertion  : %g detik' % (ak - aw))
