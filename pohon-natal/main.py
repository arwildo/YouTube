import random

tinggi_daun = 10
tinggi_batang = 3

POLA_DAUN = ["^", "^", "^", "o"]

for i in range(tinggi_daun):
    spasi = " " * (tinggi_daun - i)
    if i == 0: 
        print(spasi + "*")
    else:
        baris_daun = []
        for k in range(2 * i + 1):
            pola_sekarang = random.choice(POLA_DAUN)
            baris_daun.append(pola_sekarang)
        print(spasi + ''.join(baris_daun))


for j in range(tinggi_batang):
    spasi = " " * (tinggi_daun - 1)
    batang = "| " * 2
    print(spasi + batang)
