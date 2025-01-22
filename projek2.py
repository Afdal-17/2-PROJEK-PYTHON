import os
os.system ("cls")
#Projek ke 2 TO-DO LIST

def tampilkan_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

def tampilkan_tugas(tugas):
    if not tugas:
        print("\nBelum ada tugas!")
    else:
        print("\nDaftar Tugas:")
        for i, (nama, selesai) in enumerate(tugas, start=1):
            status = "Selesai" if selesai else "Belum"
            print(f"{i}. {nama} [{status}]")

def tambah_tugas(tugas):
    nama_tugas = input("Masukkan nama tugas: ")
    tugas.append((nama_tugas, False))
    print(f"Tugas '{nama_tugas}' berhasil ditambahkan!")

def tandai_selesai(tugas):
    tampilkan_tugas(tugas)
    if tugas:
        try:
            indeks = int(input("Masukkan nomor tugas yang selesai: ")) - 1
            nama, _ = tugas[indeks]
            tugas[indeks] = (nama, True)
            print(f"Tugas '{nama}' telah ditandai selesai!")
        except (IndexError, ValueError):
            print("Nomor tugas tidak valid!")

def hapus_tugas(tugas):
    tampilkan_tugas(tugas)
    if tugas:
        try:
            indeks = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            nama, _ = tugas.pop(indeks)
            print(f"Tugas '{nama}' berhasil dihapus!")
        except (IndexError, ValueError):
            print("Nomor tugas tidak valid!")

def main():
    tugas = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_tugas(tugas)
        elif pilihan == "2":
            tampilkan_tugas(tugas)
        elif pilihan == "3":
            tandai_selesai(tugas)
        elif pilihan == "4":
            hapus_tugas(tugas)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan To-Do List!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if _name_ == "_main_":
    main()