# Nama: Fatih Firdaus
# NIM: 241351132
# Kelas: PAGI A

# Sebuah gudang menyimpan data barang dalam bentuk dictionary.
# Setiap barang memiliki kode barang sebagai kunci dan informasi berupa dictionary yang berisi
# nama barang, kategori, dan stok. Data awal adalah sebagai berikut:

inventaris = {
    "B001": {"nama": "Laptop", "kategori": "Elektronik", "stok": 10},
    "B002": {"nama": "HP", "kategori": "Elektronik", "stok": 15},
    "B003": {"nama": "Meja", "kategori": "Furniture", "stok": 8},
    "B004": {"nama": "Kursi", "kategori": "Furniture", "stok": 20},
    "B005": {"nama": "Mouse", "kategori": "Elektronik", "stok": 25}
}

# a. Tampilkan semua data barang dalam format: Kode: [Nama] - [Kategori] (Stok: [Jumlah]).
print("Semua Data Barang:")
for kode, info in inventaris.items():
    print(f"{kode}: {info['nama']} - {info['kategori']} (Stok: {info['stok']})")

# b. Tambahkan barang baru dengan kode B006, nama Keyboard, kategori Elektronik, dan stok 12.
inventaris["B006"] = {"nama": "Keyboard", "kategori": "Elektronik", "stok": 12}
print("\nSetelah Penambahan Barang:")
for kode, info in inventaris.items():
    print(f"{kode}: {info['nama']} - {info['kategori']} (Stok: {info['stok']})")

# c. Perbarui stok barang dengan kode B002 menjadi 18.
inventaris["B002"]["stok"] = 18
print("\nSetelah Pembaruan Stok B002:")
for kode, info in inventaris.items():
    print(f"{kode}: {info['nama']} - {info['kategori']} (Stok: {info['stok']})")

# d. Hapus barang dengan kode B003 dari dictionary.
del inventaris["B003"]
print("\nSetelah Penghapusan Barang B003:")
for kode, info in inventaris.items():
    print(f"{kode}: {info['nama']} - {info['kategori']} (Stok: {info['stok']})")

# e. Tampilkan semua barang dalam kategori Elektronik.
print("\nBarang dalam Kategori Elektronik:")
for kode, info in inventaris.items():
    if info["kategori"] == "Elektronik":
        print(f"{kode}: {info['nama']} - {info['kategori']} (Stok: {info['stok']})")

# f. Hitung total stok semua barang di gudang.
total_stok = sum(info["stok"] for info in inventaris.values())
print("\nTotal Stok Semua Barang di Gudang:", total_stok)
