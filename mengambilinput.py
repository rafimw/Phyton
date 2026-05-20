## Kelas terbuka Episode 7
# input dan jenis data

data = input ("Masukkan data = ") #data apapun yang kita masukkan pasti berupa str
print("data", data, ", bertipe", type(data))

data_int = int (input("Masukkan data = ")) #data dicasting menjadi int
print("data", data_int, ", bertipe", type(data_int)) #apabila ada data str maka err

data_bool = bool (int(input("Masukkkan data = "))) #data boolean harus di ubah menjadi int terlebih dahulu
print("data", data_bool, ", bertipe", type(data_bool))


