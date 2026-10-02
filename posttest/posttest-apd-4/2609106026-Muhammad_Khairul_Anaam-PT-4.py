username_benar = "herul"   
password_benar = "026"
kesempatan = 0
login_berhasil = False

while kesempatan < 3:
    print("\n=========== HALAMAN LOGIN ===========")

    username = input("Masukkan nama panggilan: ")
    password = input("Masukkan 3 digit terakhir nim anda: ")

    if username != username_benar or password != password_benar:
        kesempatan += 1
        print("username atau password anda salah. silahkan coba kembali")
        print("percobaan tersisa: ", 3 - kesempatan)
    else: 
        username == username_benar and password == password_benar
        print("Selamat, login anda berhasil")
        login_berhasil = True
        break

if login_berhasil == False:
    print("\nMohon maaf anda telah login sebanyak 3 kali")
    print("Program berhenti")

else:
    nama = []
    kelas = []
    ikut = []
    nilai_siswa = []
    jumlah_siswa = 0

    while True:
        print("\n========== INPUT DATA SISWA ==========")

        nama_siswa = input("Nama siswa: ")
        kelas_siswa = input("Kelas siswa: ")
        ikut_ujian = input("Apakah siswa mengikuti ujian? (ya/tidak): ")

        if ikut_ujian.lower() == "tidak":
            nilai = 0 
            nama += [nama_siswa]
            kelas += [kelas_siswa]
            ikut += [ikut_ujian]
            nilai_siswa += [nilai]
            jumlah_siswa = jumlah_siswa + 1
            print("Siswa tidak mengikuti ujian")
            print("Nilai siswa tersebut adalah: ", nilai)

        elif ikut_ujian.lower() == "ya":
            print("\n========== NILAI UJIAN SISWA ==========")
            benar = int(input("Jumlah soal benar: "))
            salah = int(input("Jumlah soal salah: "))
            nilai = benar * 5
            nama += [nama_siswa]
            kelas += [kelas_siswa]
            ikut += [ikut_ujian]
            nilai_siswa += [nilai]
            jumlah_siswa = jumlah_siswa + 1
            print("Nilai siswa tersebut adalah: ", nilai)

        else:
            print("Input harus (ya/tidak)")
            continue

        lagi = input("\nApakah anda ingin menginput siswa lagi? (ya/tidak)")
        if lagi.lower() == "ya":
            continue
        elif lagi.lower() == "tidak":
            break
        else:
            print("Input harus (ya/tidak)")
            break

    print("\n")
    print("====================================")
    print("          HASIL NILAI SISWA         ")
    print("====================================")

    for i in range(jumlah_siswa):
        if nilai_siswa[i] >= 80:
            kategori = "Sangat Baik"
        elif nilai_siswa[i] >= 60:
            kategori = "Baik"
        elif nilai_siswa[i] >= 40:
            kategori = "Cukup"
        else:
            kategori = "Perlu belajar lagi"

        print("\nNama Siswa     : ", nama[i])
        print("Kelas Siswa    : ", kelas[i])
        print("Ikut Ujian     : ", ikut[i])
        print("Nilai Siswa    : ", nilai_siswa[i])
        print("Kategori Nilai : ", kategori)

    print("====================================")