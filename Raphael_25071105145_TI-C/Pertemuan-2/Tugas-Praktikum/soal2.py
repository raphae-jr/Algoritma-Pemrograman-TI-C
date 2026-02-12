def bilangan_prima(n):
    hasil = []

    for i in range(2, n + 1):   
        prima = True

        for j in range(2, i):
            if i % j == 0:
                prima = False

        if prima:
            hasil.append(i)

    return hasil


print(bilangan_prima(50))