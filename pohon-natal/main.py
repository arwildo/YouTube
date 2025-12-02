
tinggi_daun = 9
tinggi_batang = 3

for i in range(tinggi_daun):
    spasi = " " * (tinggi_daun - i)
    daun = "*" * (2 * i + 1)
    print(spasi + daun)

for j in range(tinggi_batang):
    spasi = " " * (tinggi_daun - 1)
    batang = "|" * 3
    print(spasi + batang)
