vokal = "aiueo"

def jumlahHurufVokal(kata):
    kata = kata.lower()
    jml = len(kata)
    jmlV = 0
    for huruf in kata:
        if huruf in vokal:
            jmlV += 1
    print("(" + str(jml) + "," + str(jmlV) + ")")
    return jmlV

def jumlahHurufKonsonan(kata):
    jml = len(kata)
    jmlK = jml - jumlahHurufVokal(kata)
    print("(" + str(jml) + "," + str(jmlK) + ")")
    return jmlK
