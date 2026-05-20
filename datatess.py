n = int(input("Masukkann banyak data : "))
for data in range n :
    inp = int(input("Masukkan Data ke -",n, "="))



#Mengurutkan bilangan
print("Jadi dari data = ", all_data)
all_data.sort()
print ("Data yang telah diurutkan =\n",all_data)

#Median
x = len(all_data) 
datatengah = x // 2
me = (all_data[datatengah - 1] + all_data[datatengah]) / 2


#Rata_rata
ave = sum(all_data)
rata = ave / x

#Hasil
print("Diperoleh informasi bahwa : ")
print("Median = ", all_data[datatengah-1], "dan", all_data[datatengah])
print("Median = ", me)
print("Dan rata-rata data adalah = ", rata)