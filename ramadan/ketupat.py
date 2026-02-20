def gambar_ketupat(n):
    gantungan(n)
    for i in range(n * 2 + 1):
        # Skip garis pertama dan terkahir supaya 
        # gambar ketupatnya nyambung dengan gantungan dan tali_bawah
        if i == 0 or i == n * 2:
            continue
        for j in range(n * 2 + 1):
            # Kotak Luar
            if i + j == n:
                print("/", end="")
            elif j - i == n:
                print("\\", end="")
            elif i - j == n:
                print("\\", end="")
            elif i + j == n * 3:
                print("/", end="")
            # Pola anyaman dalam
            elif n < i + j < n * 3 and abs(i - j) < n:
                if (i + j) % 2 == 0:
                    print("-", end="")
                else:
                    print("|", end="")
            else:
                print(" ", end="")
        print()
    tali_bawah(n)

def gantungan(n):
    for i in range(n // 3):
        print(" " * (n - 1) + "||")

def tali_bawah(n):
    for i in range(n // 3):
        offset = i + 1
        baris = [" "] * (n * 3)
        baris[n - offset] = "/"
        baris[n - offset - 1] = "/"
        baris[n + offset] = "\\"
        baris[n + offset + 1] = "\\"
        print("".join(baris))

gambar_ketupat(7)