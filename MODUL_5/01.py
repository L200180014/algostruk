class MhsTIF(object):
    def __init__(self, nama, nim, asal, us):
        self.nama = nama
        self.nim = nim
        self.asal = asal
        self.uangsaku = us

def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp

def nimurut(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j].nim > A[j + 1].nim:
                swap(A, j, j + 1)
    listUrut = []
    for k in A:
        listUrut.append((k.nim, k.nama, k.asal, k.uangsaku))
    return listUrut

daftar = [(MhsTIF('Andi', 'L200210060', 'Solo', 10000)),
          (MhsTIF('Budi', 'L200200003', 'Konoha', 2000)),
          (MhsTIF('Cici', 'L200210085', 'Sukoharjo', 15000)),
          (MhsTIF('Dyah', 'L200210065', 'Pekalongan', 22000)),
          (MhsTIF('Ekky', 'L200210070', 'Pabelan', 23000)),
          (MhsTIF('Fred', 'L200200081', 'New Yoke', 25000)),
          (MhsTIF('Gery', 'L200210045', 'Seberang', 25000)),
          (MhsTIF('Pipit', 'L200210030', 'Batang Pisang', 19000)),
          (MhsTIF('Nopnop', 'L200210026', 'Pluto', 18000)),
          (MhsTIF('Billy', 'L200200075', 'Laut', 21000))]

# nimurut(daftar)
