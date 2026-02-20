def tali(panjang=80):
    print('_' * panjang)

def lampion():
    spasi = "     "
    print(spasi + " _|_ ")
    print(spasi + "|   |")
    print(spasi + "|_x_|")
    print(spasi + "  '  ")

def lampion_berjejer(jumlah=8, spasi=4):
    for i in range(jumlah):
        print(' ' * spasi + " _|_ ", end='')
    print()
    for i in range(jumlah):
        print(' ' * spasi + "|   |", end='')
    print()
    for i in range(jumlah):
        print(' ' * spasi + "|_x_|", end='')
    print()
    for i in range(jumlah):
        print(' ' * spasi + "  '  ", end='')
    print()

tali()
lampion() * 8