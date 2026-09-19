bagasi_1 = 12
bagasi_2 = 18
bagasi_3 = 7
bagasi_4 = 15
bagasi_5 = 20
bagasi_6 = 10

total_berat = bagasi_1 + bagasi_2 + bagasi_3 + bagasi_4 + bagasi_5 + bagasi_6

kompensasi = total_berat * 0.05

total_berat_akhir = total_berat + kompensasi

bagasi = [bagasi_1, bagasi_2, bagasi_3, bagasi_4, bagasi_5, bagasi_6]

bagasi_tengah = bagasi[2:5]

rata_rata = total_berat / len(bagasi)

nim = 26

bolean = nim < rata_rata

total_berat_gram = total_berat_akhir * 1000

print("Total berat bagasi: ", total_berat, "kg")
print("Kompensasi: ", kompensasi, "kg")
print("Total berat akhir: ", total_berat_akhir, "kg")

print("Data Bagasi: ", bagasi)
print("Data Bagasi tengah: ", bagasi_tengah)
print("Rata-rata: ", rata_rata, "kg")

print("NIM: ", nim)
print("Hasil perbandingan: ", bolean)
print("Total berat akhir= ", total_berat_gram, "gram")
