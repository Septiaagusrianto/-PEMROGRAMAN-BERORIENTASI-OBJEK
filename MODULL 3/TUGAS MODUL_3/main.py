class Pegawai:
    def __init__(self, nama, nip, gaji_pokok):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = gaji_pokok    # PRIVATE ATTRIBUTE

    # Getter untuk gaji pokok
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Method bonus (akan dioverride di child)
    def hitung_bonus(self):
        return 0

    # Getter gaji total
    def get_gaji_total(self):
        return self.__gaji_pokok + self.hitung_bonus()

    # Method tampilkan info dasar
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.get_gaji_pokok():,}")


# =====================================================
# CHILD CLASS : MANAGER
# =====================================================
class Manager(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    # Override bonus: 15% dari gaji pokok
    def hitung_bonus(self):
        return int(self.get_gaji_pokok() * 0.15)

    # Override tampilkan_info
    def tampilkan_info(self):
        print("--- Info Manager ---")
        super().tampilkan_info()
        print(f"Tunjangan: Rp {self.tunjangan_jabatan:,}")
        print(f"Gaji Total Manager: Rp {self.get_gaji_total():,}")
        print("\n" + "="*30 + "\n")

 
# ========================================/============
# CHILD CLASS : STAFF TEKNIS
# =====================================================
class StaffTeknis(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, jumlah_proyek):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = jumlah_proyek

    # Override bonus: 500.000 x jumlah proyek
    def hitung_bonus(self):
        return 500_000 * self.jumlah_proyek

    # Override tampilkan_info
    def tampilkan_info(self):
        print("--- Info Staff Teknis ---")
        super().tampilkan_info()
        print(f"Jumlah Proyek: {self.jumlah_proyek}")
        print(f"Gaji Total Staff: Rp {self.get_gaji_total():,}")
        print("\n" + "="*30 + "\n")


# =====================================================
# PEMBUATAN OBJECT
# =====================================================

manager_budi = Manager("Budi Hartono", "M-001", 10_000_000, 5_000_000)
staff_susi = StaffTeknis("Susi Susanti", "S-001", 6_000_000, 3)

manager_budi.tampilkan_info()
staff_susi.tampilkan_info()


# =====================================================
# TES ENKAPSULASI
# =====================================================
print("--- Tes Keamanan (Encapsulasi) ---")
try:
    print(staff_susi.__gaji_pokok)  # mencoba akses langsung → ERROR
except Exception as e:
    print("ERROR:", e)
    print("-> TIDAK BISA diakses langsung dari luar!")

print(f"Gaji Total Susi (tetap): Rp {staff_susi.get_gaji_total():,}")