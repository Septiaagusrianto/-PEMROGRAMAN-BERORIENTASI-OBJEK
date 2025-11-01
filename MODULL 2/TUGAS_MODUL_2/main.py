class Hero:
    # variabel class (private)
    __jumlah = 0

    # constructor
    def __init__(self, name, health, attPower, armor):
        # atribut private (base stats)
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        # level & exp
        self.__level = 1
        self.__exp = 0

        # atribut dinamis
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax

        # tambah jumlah hero
        Hero.__jumlah += 1

    # getter info (read only)
    @property
    def info(self):
        return f"{self.__name} level {self.__level}: \n" \
               f"\thealth = {self.__health}/{self.__healthMax} \n" \
               f"\tattack = {self.__attPower} \n" \
               f"\tarmor = {self.__armor}"

    # getter gainEXP (hanya agar setter bisa dipakai)
    @property
    def gainEXP(self):
        pass

    # setter gainEXP
    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP
        # cek level up
        while self.__exp >= 100:
            self.__exp -= 100
            self.__level += 1
            print(f"{self.__name} level up")

            # hitung ulang atribut dinamis
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            self.__health = self.__healthMax

    # method attack
    def attack(self, musuh):
        # logika serangan sederhana
        print(f"{self.__name} menyerang {musuh.__name}!")
        self.gainEXP = 50  # tambah exp

# ======== TEST CASE ========
zilong = Hero('zilong', 100, 5, 10)
alucard = Hero('alucard', 100, 5, 10)

print(zilong.info)

zilong.attack(alucard)
zilong.attack(alucard)
zilong.attack(alucard)

print(zilong.info)

alucard = Hero('alucard', 100, 5, 10)
zilong = Hero('zilong', 101, 5, 10)

print(alucard.info)

alucard.attack(zilong)
alucard.attack(zilong)
alucard.attack(zilong)

print(alucard.info)

