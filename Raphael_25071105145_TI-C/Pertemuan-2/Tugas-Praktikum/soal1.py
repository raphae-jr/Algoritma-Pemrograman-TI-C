def rata_rata_nilai(nilai):

    if len(nilai) == 0:
        return "Data kosong"
    
    return sum(nilai) / len(nilai)

data = [80, 75, 90, 60, 85]
hasil = rata_rata_nilai(data)
print("Rata-rata:", hasil)
