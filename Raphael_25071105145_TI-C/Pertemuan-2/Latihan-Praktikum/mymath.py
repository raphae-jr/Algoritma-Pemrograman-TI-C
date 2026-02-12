#penambahan 

def tambah(a, b):
  return a + b

def kurang(a,b):
  return a-b

def perkalian(a, b):
  return a * b

def pembagian (a, b):
    return a / b
if pembagian == 0:
   print("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")

def modulus(a,b):
   return a%b

def fibonaciI(n):
   a, b = 0,1
   yield a
   a,b = b , a + b

   hasil = fibonaciI(n)
   for _ in range(n):
      print(next(hasil))

