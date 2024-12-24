# Nama: Fatih Firdaus
# NIM: 241351132
# Kelas: PAGI A

# Sebuah toko memiliki data pelanggan yang datang pada beberapa hari tertentu
# Data dicatat sebagai berikut:

pelanggan_hari_1 = {"Ali", "Budi", "Citra", "Dina", "Eka"}
pelanggan_hari_2 = {"Budi", "Citra", "Fahmi", "Gina", "Eka"}
pelanggan_hari_3 = {"Ali", "Gina", "Henry", "Eka", "Fahmi"}

# a. Tampilkan daftar pelanggan yang datang pada hari pertama saja.
hari_pertama_saja = pelanggan_hari_1 - (pelanggan_hari_2 | pelanggan_hari_3)
print("Pelanggan yang datang pada hari pertama saja:", hari_pertama_saja)

# b. Tampilkan daftar pelanggan yang datang pada semua hari.
semua_hari = pelanggan_hari_1 & pelanggan_hari_2 & pelanggan_hari_3
print("Pelanggan yang datang pada semua hari:", semua_hari)

# c. Tampilkan daftar pelanggan yang datang pada minimal dua hari.
minimal_dua_hari = (pelanggan_hari_1 & pelanggan_hari_2) | (pelanggan_hari_2 & pelanggan_hari_3) | (pelanggan_hari_1 & pelanggan_hari_3)
print("Pelanggan yang datang pada minimal dua hari:", minimal_dua_hari)

# d. Tambahkan pelanggan baru bernama "Irma" ke daftar pelanggan hari kedua.
pelanggan_hari_2.add("Irma")
print("\nSetelah Penambahan Pelanggan Baru pada Hari Kedua:")
print(pelanggan_hari_2)

# e. Hitung total pelanggan unik yang datang selama tiga hari.
total_pelanggan_unik = pelanggan_hari_1 | pelanggan_hari_2 | pelanggan_hari_3
print("\nTotal Pelanggan Unik yang datang selama tiga hari:", len(total_pelanggan_unik))
