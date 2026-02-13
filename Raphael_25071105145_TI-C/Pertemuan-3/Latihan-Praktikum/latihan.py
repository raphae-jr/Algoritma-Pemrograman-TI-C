class Vehicle:
    def __init__(self, jenis, merek, tahun_rilis):
        self.jenis = jenis
        self.merek = merek
        self.tahun_rilis = tahun_rilis

    def teks(self):
        print(f"{self.merek} adalah salah satu merek {self.jenis} tahun {self.tahun_rilis}")


class Mobil(Vehicle):
    def __init__(self, jenis, merek, tahun_rilis):
        super().__init__(jenis, merek, tahun_rilis)
        self.__merek = merek

    def get_merek(self):
        return self.__merek


class Motor(Vehicle):
    def __init__(self, jenis, merek, tahun_rilis):
        super().__init__(jenis, merek, tahun_rilis)
        self.__merek = merek

    def get_merek(self):
        return self.__merek

    def set_merek(self, merek):
        self.__merek = merek

mobil1 = Mobil("Mobil", "Toyota", 2022)
motor1 = Motor("Motor", "Honda", 2021)

mobil1.teks()
motor1.teks()

print("Merek mobil:", mobil1.get_merek())
print("Merek motor:", motor1.get_merek())

motor1.set_merek("Yamaha")
print("Merek motor setelah diubah:", motor1.get_merek())
