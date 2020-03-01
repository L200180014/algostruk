def gambarlahPersegiEmpat(tinggi, lebar):
    for i in range(tinggi):
        if i == 0 or i == (tinggi - 1):
            print("@" * lebar)
        else:
            print("@" + (" " * (lebar-2) + "@"))
