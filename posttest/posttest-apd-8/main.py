import autentikasi
import menu
from tampilan import tampilkan_menu
from utilitas import bersihkan_layar, jeda, pesan_error, pesan_info, tampilkan_header

def alur_login():
    hasil = autentikasi.login()
    if hasil is None:
        pesan_error("Mohon maaf, anda gagal login, silahkan kembali ke menu utama")
        jeda()
        return
    user_aktif, role_aktif = hasil
    if role_aktif == "Admin":
        menu.menu_admin()
    else:
        menu.menu_user(user_aktif)

def main():
    while True:
        bersihkan_layar()
        tampilkan_header("Koleksi Gantungan Kunci")
        tampilkan_menu(["Login", "Register", "Keluar"])
        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            alur_login()
        elif pilihan == "2":
            autentikasi.register()
            jeda()
        elif pilihan == "3":
            bersihkan_layar()
            pesan_info("Terima kasih sudah mampir! Jaga koleksimu ya")
            return
        else:
            pesan_error("Pilihan tidak valid, pilih 1-3 ya!")
            jeda()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa (Ctrl+C). Sampai jumpa!")
    except EOFError:
        print("\nInput terputus. Program ditutup.")
    finally:
        print("Program selesai.")