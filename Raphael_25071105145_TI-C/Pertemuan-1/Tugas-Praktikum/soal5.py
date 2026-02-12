# Buat sebuah fungsi bernama hitung(a, b) 
# Menerima dua parameter a dan b
# Mengembalikan hasil penjumlahan a + b
#Mengembalikan hasil pengurangan a - b


def hitung(a, b):
    return a + b, a - b

penjumlahan, pengurangan = hitung(5, 3)
print("Penjumlahan =", penjumlahan, "\nPengurangan =", pengurangan)