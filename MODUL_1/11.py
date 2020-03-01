def cekKabisat(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 == 0:
            return True
        elif n % 100 == 0 and n % 400 != 0:
            return False
        return True
    return False


def apakahKabisat(n):
    if cekKabisat(n):
        print(str(n) + " adalah Tahun kabisat")
    else:
        print(str(n) + " bukan Tahun kabisat")


# Cek langsung beberapa contoh tahun
apakahKabisat(1896)
apakahKabisat(1897)
apakahKabisat(1900)
apakahKabisat(2000)
apakahKabisat(2004)
apakahKabisat(2100)
