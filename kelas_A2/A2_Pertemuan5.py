nama1 = "Attar"
nama2 = "johan"
nama3 = "azka"

list_nama = [nama1, nama2, nama3]
print(list_nama)
for i in(list_nama):
    print(i)

list_nama.append("Julpa")
print(list_nama)
for i in(list_nama [1:3]):
    print(i)

list_nama.extend(["Mirza", "Wili"])
print(list_nama)

list_nama.insert(2, "Mustafid")
print(list_nama)

list_nama[0:3] = ["hafiz", "dewi", "meisya"]
print(list_nama)

del list_nama[0]
print(list_nama[0])

list_nama.remove("dewi")
print(list_nama)

ambil_nama = list_nama.pop(1)
print(list_nama)
print(ambil_nama)


poin = [1, 2, 3, 4, 5, 6, 7]
print(poin[1:5:2])

nama = ["Attar", "Johan", "Azka", "Julpa", "Mirza", "Wili"]
print(nama)

hapus = int(input("Masukkan index yang ingin dihapus: "))
del nama[hapus]
print(nama)

buah = ("apel", "mangga", "nanas")
print(buah)
print

listbuah = list(buah)
listbuah.append("pisang")
buah = tuple(listbuah)
print(buah)

game = ("ml", "genshin")
(moba,open_world) = game

print(moba)
print(open_world)

#ubah poin 1 sampai 3 menjadi 11, 12, 13
#poin[0:3] = [11, 12, 13]
#print(poin)