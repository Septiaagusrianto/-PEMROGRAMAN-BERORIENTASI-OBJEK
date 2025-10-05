# Latihan Soal Modul 1
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


# Program utama
if __name__ == "__main__":
    # Input dari pengguna
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))

    # Membuat objek
    persegi = PersegiPanjang(panjang, lebar)

    # Menghitung dan menampilkan hasil
    print(f"Luas persegi panjang: {persegi.luas()}")
    print(f"Keliling persegi panjang: {persegi.keliling()}")