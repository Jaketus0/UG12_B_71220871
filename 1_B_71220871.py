print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
a=int(input("Masukkan angka: "))
print(' '*(a-1), '*')
for i in range ((a-1),0,-1):
    print(' '*(i-1),'**')
print('**'*a)