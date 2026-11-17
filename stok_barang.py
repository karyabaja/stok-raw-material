class ProgramStok:

  def __init__(self):
    # Menyimpan data inventaris: {'Nama Barang': jumlah_stok}
    self.inventaris = {}

  def tambah_barang_baru(self, nama_barang, stok_awal=0):
    if nama_barang in self.inventaris:
      print(f"-> Barang '{nama_barang}' sudah terdaftar di sistem.")
    else:
      self.inventaris[nama_barang] = stok_awal
      print(f"-> Berhasil menambahkan barang baru: '{nama_barang}' (Stok Awal: {stok_awal})")

  def barang_masuk(self, nama_barang, jumlah):
    if nama_barang in self.inventaris:
      self.inventaris[nama_barang] += jumlah
      print(f"-> Stok '{nama_barang}' bertambah {jumlah}. Total sekarang: {self.inventaris[nama_barang]}")
    else:
      print(f"-> Gagal: Barang '{nama_barang}' tidak ditemukan!")

  def barang_keluar(self, nama_barang, jumlah):
    if nama_barang not in self.inventaris:
      print(f"-> Gagal: Barang '{nama_barang}' tidak ditemukan!")
      return

    # Validasi agar stok tidak menjadi minus
    if self.inventaris[nama_barang] >= jumlah:
      self.inventaris[nama_barang] -= jumlah
      print(f"-> Stok '{nama_barang}' berkurang {jumlah}. Sisa sekarang: {self.inventaris[nama_barang]}")
    else:
      print(f"-> Gagal! Stok '{nama_barang}' tidak mencukupi (Sisa saat ini: {self.inventaris[nama_barang]}).")

  def cek_stok(self):
    print("\n" + "="*30)
    print("      DAFTAR STOK GUDANG")
    print("="*30)
    if not self.inventaris:
      print("Belum ada barang di dalam inventaris.")
    for barang, stok in self.inventaris.items():
      # Menentukan status stok
      if stok == 0:
        status = "HABIS ❌"
      elif stok <= 5:
        status = "MENIPIS ⚠️"
      else:
        status = "AMAN ✅"
      
      print(f"- {barang}: {stok} unit [{status}]")
    print("="*30 + "\n")


# --- SIMULASI MENJALANKAN PROGRAM ---
if __name__ == "__main__":
  gudang = ProgramStok()

  # 1. Menambahkan barang baru
  gudang.tambah_barang_baru("Buku Tulis", 15)
  gudang.tambah_barang_baru("Pulpen Hitam", 4)

  # 2. Cek stok awal
  gudang.cek_stok()

  # 3. Simulasi transaksi barang masuk dan keluar
  print("--- MELAKUKAN TRANSAKSI ---")
  gudang.barang_masuk("Pulpen Hitam", 10)  # Pulpen jadi 14
  gudang.barang_keluar("Buku Tulis", 12)   # Buku tulis sisa 3 (menipis)
  gudang.barang_keluar("Buku Tulis", 5)    # Gagal karena stok kurang

  # 4. Cek stok akhir
  gudang.cek_stok()
