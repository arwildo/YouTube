
TEKS = "Selamat Idul Fitri 1447 H"
LEBAR, TINGGI = 60, 30
pusat_x, pusat_y = LEBAR / 2, TINGGI / 2
radius_bulan   = 27
radius_lubang  = 22
geser_lubang   = 11
rasio_karakter = 2

indeks_teks = 0
for baris_y in range(TINGGI):
    baris = ""
    for kolom_x in range(LEBAR):
        jarak_x = kolom_x - pusat_x
        jarak_y = (baris_y - pusat_y) * rasio_karakter
        dalam_bulan  = jarak_x**2 + jarak_y**2 <= radius_bulan**2
        dalam_lubang = (jarak_x - geser_lubang)**2 + jarak_y**2 <= radius_lubang**2
        if dalam_bulan and not dalam_lubang:
            baris += TEKS[indeks_teks % len(TEKS)]
            indeks_teks += 1
        else:
            baris += " "
    print(baris)



