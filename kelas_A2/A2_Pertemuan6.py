# kartu = {"merah", "merah", "biru", "hijau"}
# kartu.discard("kuning")
# kartu.remove("merah")

# print(kartu)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)

# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(Biodata["Instagram"])
# print(Biodata.get("coba", "coba tidak ditemukan"))
# # print(Biodata.get("Alamat", "Alamat tidak ditemukan"))

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }

# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }

# game["resident evil"] = "horror"
# game["ML"] = "moba"

# coba = game.pop("pou")
# print(coba)
# game.clear()
# print(game)

# gamebaru = game.copy()
# print(game)
# print(gamebaru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000

# menu = dict.fromkeys(key, value)
# print(menu)

data_siswa = {
    "siswa1": {
        "nama" : "Johan",
        "kelas" : "A2",
        "nilai" : 95
    },
    "siswa2": {
        "nama" : "Niyah",
        "kelas" : "A2",
        "nilai" : 96
    }
}

print(data_siswa["siswa1"]["nama"])
print(data_siswa["siswa1"]["nama"])
