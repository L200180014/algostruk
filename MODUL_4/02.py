class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku


class buatArray(object):
    internalData = 11 * [None]

    def __getitem__(self, item):
        return self.internalData[item]

    def __setitem__(self, key, value):
        self.internalData[key] = value

    # 02
    def cariuangsaku(self):
        terkecil = self[0].uangSaku
        for i in self:
            if i.uangSaku < terkecil:
                terkecil = i.uangSaku
        return print(terkecil)


c = buatArray()
c[0] = MhsTIF('Andi', 10, 'Solo', 241000)
c[1] = MhsTIF('Budi', 51, 'Solo', 2000)
c[2] = MhsTIF('Patrick', 2, 'Laut', 249800)
c[3] = MhsTIF('Squidward', 18, 'Bikini Bottom', 2000)
c[4] = MhsTIF('Spongebob', 4, 'Bikini Bottom', 24670)
c[5] = MhsTIF('Bowo', 31, 'Serang', 260000)
c[6] = MhsTIF('Billy', 10, 'Klaten', 250000)
c[7] = MhsTIF('Pipit', 5, 'Batang', 222000)
c[8] = MhsTIF('Denis', 64, 'Klaten', 240600)
c[9] = MhsTIF('Nopnop', 23, 'Batang', 223000)
c[10] = MhsTIF('Naruto', 29, 'Konoha', 245000)

# c.cariuangsaku()
