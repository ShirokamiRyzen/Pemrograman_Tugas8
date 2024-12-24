# Nama: Fatih Firdaus
# NIM: 241351132
# Kelas: PAGI A

# Sebuah aplikasi toko online mencatat data pesanan dalam bentuk tuple.
# Setiap pesanan berisi informasi:
# (ID Pesanan, Nama Barang, Jumlah, Harga per Unit). 
# Berikut adalah data pesanan yang tercatat:

pesanan = [
    (101, "Laptop", 1, 15000000),
    (102, "HP", 2, 3000000),
    (103, "Headphone", 3, 500000),
    (104, "Keyboard", 4, 250000),
    (105, "Mouse", 5, 100000)
]

# a. Tampilkan semua data pesanan.
print("Semua Data Pesanan:")
for pesanan_item in pesanan:
    print(pesanan_item)

# b. Hitung total harga untuk setiap pesanan (Jumlah × Harga per Unit) dan tampilkan hasilnya.
print("\nTotal Harga Setiap Pesanan:")
for pesanan_item in pesanan:
    total_harga = pesanan_item[2] * pesanan_item[3]  # Jumlah × Harga per Unit
    print(f"ID Pesanan: {pesanan_item[0]}, Nama Barang: {pesanan_item[1]}, Total Harga: {total_harga}")

# c. Cari pesanan dengan ID 103 dan tampilkan detailnya
print("\nDetail Pesanan dengan ID 103:")
for pesanan_item in pesanan:
    if pesanan_item[0] == 103:
        print(pesanan_item)

# d. Hitung total pendapatan dari semua pesanan.
total_pendapatan = sum(pesanan_item[2] * pesanan_item[3] for pesanan_item in pesanan)
print("\nTotal Pendapatan dari Semua Pesanan:", total_pendapatan)
