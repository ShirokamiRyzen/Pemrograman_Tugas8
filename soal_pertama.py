# Nama: Fatih Firdaus
# NIM: 241351132
# Kelas: PAGI A

# Sebuah toko elektronik memiliki daftar barang yang dijual beserta stoknya.
# Data awal barang dan stok disimpan dalam dua list terpisah sebagai berikut:

barang = ["Laptop", "HP", "Headphone", "Mouse", "Keyboard"]
stok = [10, 20, 15, 25, 30]

# a. Tambahkan barang baru bernama "Monitor" dengan stok awal 12 ke dalam list.
barang.append("Monitor")
stok.append(12)

# b. Hapus barang "Mouse" dari daftar barang dan stoknya.
index_mouse = barang.index("Mouse")
barang.pop(index_mouse)
stok.pop(index_mouse)

# c. Perbarui stok untuk barang "Keyboard" menjadi 40.
index_keyboard = barang.index("Keyboard")
stok[index_keyboard] = 40

# d. Hitung total stok semua barang.
total_stok = sum(stok)

print("Barang setelah penambahan:", barang)
print("Stok setelah penambahan:", stok)
print("Barang setelah penghapusan:", barang)
print("Stok setelah penghapusan:", stok)
print("Stok setelah pembaruan:", stok)
print("Total stok semua barang:", total_stok)
