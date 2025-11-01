class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama           # public → boleh diakses dari luar
        self.__saldo = saldo       # private → tidak boleh diakses langsung dari luar

    # Method untuk melihat saldo (tanpa menampilkan nilainya)
    def lihat_saldo(self):
        print("Akses ke saldo dibatasi. Data saldo bersifat rahasia.")

    # Method untuk menambah saldo
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil menambah saldo sebesar Rp{jumlah}")
        else:
            print("Jumlah setor harus lebih dari 0!")

    # Method untuk menarik saldo
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil menarik Rp{jumlah}")
        else:
            print("Penarikan gagal! Jumlah tidak valid atau saldo tidak cukup.")


# Program utama
akun_budi = RekeningBank("Budi", 1000000)
print(f"Nama akun: {akun_budi.nama}")   # boleh diakses

# akses saldo langsung → error
try:
    print(akun_budi.__saldo)
except AttributeError:
    print("ERROR: Tidak dapat mengakses saldo secara langsung!")

# cara yang benar
akun_budi.lihat_saldo()
