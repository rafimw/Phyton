# definisi rumus luas persegi panjang
def Lbalok(p,s):
    return p*s
# definisi rumus luas persegi
def Lkubus(s):
    return s**2
# definisi rumus luas lingkaran
def Llingkaran(r):
    return 3.14*r**2
#While digunakan sebagai fungsi loop
while True :
    print("\n_________________________")
    print("1. Menghitung luas persegi panjang")
    print("2. Menghitung luas kubus")
    print("3. Menghitung luas lingkaran")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    pilih = input("Pilih 1/2/3 = ")   
    #Loop ini berfungsi untuk memastikan pilihan adalah 1/2 atau 3  
    if pilih in('1','2','3'):
        if pilih == '1' :
            print("\n===Menghitung luas persegi panjang===")
            p=float(input("Masukkan panjang = "))
            s=float(input("Masukkan sisi = "))
            print("Luas persegi panjang = Panjang x Sisi")
            print("Luas =", p,"x",s)
            print(Lbalok(p,s), "  =", p, "x", s)
            print("Maka luas persegi panjang = ", Lbalok(p,s))  
        if pilih =='2' :
            print("\n===Menghitung luas kubus===")
            s = float(input("Masukkan sisi = "))      
            print("Luas kubus = sisi^2")
            print("L  =", s,"^2")
            print(Lkubus(s), "=",s,"^2")
            print("Maka luas kubus = ", Lkubus(s))
        if pilih =='3' :
            print("\n===Menghitung luas lingkaran===")
            r = float(input("Masukkan jari2 = "))      
            print("Luas lingkaran = 3.14 x jari^2")
            print("L =", "3.14","x",r,"^2")
            r = r**2
            print(Llingkaran(r), "=", "3.14","x",r)
            print("Maka luas kubus = ", Llingkaran(r))
    #Jika input selain 1/2 atau 3
    else :
            print("Masukkin angka antara 1,2,3 aja ngab !!!")