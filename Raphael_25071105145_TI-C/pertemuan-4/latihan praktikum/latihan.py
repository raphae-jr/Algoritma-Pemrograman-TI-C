print("=== Program Pembagian Dua Angka ===")

try:
    # User Input
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Operasi pembagian
    hasil = angka1 / angka2

except ValueError:
    print("Terjadi kesalahan: Input harus berupa angka!")

except ZeroDivisionError:
    print("Terjadi kesalahan: Tidak boleh membagi dengan nol!")

except TypeError:
    print("Terjadi kesalahan: Tipe data tidak sesuai!")

else:
    print("Hasil pembagian adalah:", hasil)

finally:
    print("Program selesai dijalankan.")