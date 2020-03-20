print("""
Soal :
    Pada permainan tebak angka, 1-100 dibutuhkan maksimal 7 kali tebakan untuk
    menemukan angka yang TEPAT. untuk angka 1-1000 dibutuhkan
    maksimal 10 kali tebakan. Mengapa demikian? Bagaimana polanya""")

print("""
Jawab :
    Ada dua kemungkinan pola yang bisa digunakan.
    Misalkan, angka yang akan ditebak adalah 70.

    -POLA PERTAMA-
        a = nilai tebakan pertama // 2
        tebakan selanjutnya = nilai tebakan "lebih dari" + a

        *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang dipakai
        tetap nilai lebih dari sebelumnya"

        a = a // 2

        SIMULASI
            tebakan ke-1 : 50 (mengambil nilai tengah) Jawaban = "Lebih dari Itu"
            tebakan ke-2 : 75 (dari 50 + 25) Jawaban = "Kurang dari Itu"
            tebakan ke-3 : 62 (dari 50 + 12) Jawaban = "Lebih dari Itu"
            tebakan ke-4 : 68 (dari 62 + 6) Jawaban = "Lebih dari Itu"
            tebakan ke-5 : 71 (dari 68 + 3) Jawaban = "Kurang dari Itu"
            tebakan ke-6 : 69 (dari 68 + 1) Jawaban = "Lebih dari Itu"
            tebakan ke-7 : antara 71 dan 69 hanya ada 1 angka = 70

    -POLA KEDUA-
        menggunakan barisan geometri Sn = 2^n

        barisan yang terjadi adalah : 2, 4, 8, 16, 32, 64
        Misal angka yang akan diebak adalah 68
        Tebakan ke-1 : 64 dijawab lebih dari itu
        Tebakan ke-2 : 96(dari 64 + 32) dijawab "Kurang dari itu"
        Tebakan ke-3 : 80(dari 64 + 16) dijawab "Kurang dari itu"
        Tebakan ke-4 : 72(dari 64 + 8) dijawab "Kurang dari itu"
        Tebakan ke-5 : 68(dari 64 + 4) dijawab "Lebih dari itu"
        Tebakan ke-6 : 70(dari 68 + 2) dijawab "TEPAT"
        """)
