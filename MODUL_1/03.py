vokal = 'aiueo'
def jumlahHurufVokal(kata):
    kata = kata.lower()
    jmlV = 0
    pjgKata = len(kata)
    for huruf in kata:
        if huruf in vokal:
            jmlV += 1
    print('(' + str(pjgKata) + ',' + str(jmlV) + ')')

def jumlahHurufKonsonan(kata):
    kata = kata.lower()
    jmlK = 0
    pjgKata = len(kata)
    for huruf in kata:
        if huruf not in vokal:
            jmlK += 1
    print('(' + str(pjgKata) + ',' + str(jmlK) + ')')
