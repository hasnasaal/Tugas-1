print("Selamat Datang!")

#menu
def fungsiMenu():
    print('''
    --- Menu ---
    1. Daftar Kontak
    2. Tambah Kontak
    3. Keluar''')
    menu = (int(input("Pilih menu: ")))
    while menu != 3:
        while menu == 2:
            menudua()
        while menu == 1:
            menusatu()
        else:
            print("Menu tidak tersedia")
            fungsiMenu()
    print("Program selesai, sampai jumpa!")
    exit()

#list
listNama = []
listNomor = []

#fungsi menu satu
def menusatu() :
    print("Daftar Kontak")
    for x in range(0, len(listNama)):
        print(x+1,". Nama: " ,listNama[x] )
        print("Nomor Telepon: ",listNomor[x])
    fungsiMenu()


#fungsi menu dua
def menudua() :
    listNama.append(str(input("Nama: ")))
    listNomor.append(input("Nomor Telepon: "))
    print("Kontak berhasil ditambahkan")
    fungsiMenu()

fungsiMenu()