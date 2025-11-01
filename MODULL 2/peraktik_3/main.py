# percobaan 1

class Mobil:
    
    total_mobil_dibuat = 0   # Atribut class

    def __init__(self, nama):
        self.nama = nama     # Atribut objek
        Mobil.total_mobil_dibuat += 1 

    def nyalakan_mesin(self):               # Method objek
        print(f"Mesin {self.nama} menyala!")

    @classmethod
    def get_total_produksi(cls):            # Method class
        print(f"Pabrik telah memproduksi {cls.total_mobil_dibuat} unit mobil.")

# ===== Program utama =====
m1 = Mobil("Toyota")
m2 = Mobil("Honda")
m3 = Mobil("Suzuki")

m1.nyalakan_mesin()
Mobil.get_total_produksi()

# percobaan 2

class Kalkulator:

    def __init__(self, nilai_awal):
        self.nilai = nilai_awal
    
    def tambah(self, angka):
        self.nilai += angka
        return self.nilai

    @staticmethod
    def kali(a, b):
        return a * b

calc = Kalkulator(10)
print(f"Hasil tambah: {calc.tambah(5)}")

print(f"Hasil kali: {Kalkulator.kali(5, 3)}")