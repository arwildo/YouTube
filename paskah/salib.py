import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# bentuk full salib
salib = [
"                   _                ",
"                  | |              ",
"                  | |              ",
"           _______| |______       ",
"          |_______   ______|       ",
"                  | |              ",
"                  | |              ",
"                  | |              ",
"                  | |              ",
"                  | |              ",
"                  | |              ",
"                  | |              ",
"                  | |              ",
"                  |_|              "
]

tinggi = len(salib)

# animasi build dari bawah ke atas
for i in range(1, tinggi + 1):
    clear()
    
    tampil = salib[tinggi - i:]
    spasi = [""] * (tinggi - i)
    frame = spasi + tampil
    
    for line in frame:
        print(line)
    time.sleep(0.3)

print("\nDIA telah BANGKIT!🙌✨")
