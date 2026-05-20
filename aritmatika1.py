# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil, "--> Adalah operasi penjumlahan")

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil, "--> Adalah operasi penjumlahan")

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil, "--> Adalah operasi perkalian")

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil, "--> Adalah operasi pembagian")

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil, "--> Adalah operasi pangkat/eksponen")

# operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil, "--> Adalah operasi madulus/sisa pembagian")

# # Kelas terbuka Episode 8
# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil, "--> Adalah operasi floor division\n\n")

# prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'^',y,'x',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)