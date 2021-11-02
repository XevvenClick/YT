import random
import os

pl_score = 0
com_score = 0

suit_obj = ["", "Batu", "Gunting", "Kertas"]
pl_pick = None

game_count = 3
while pl_pick != 0 and game_count > 0:
	os.system("cls") # clear 
	print(f"Player [{pl_score}]:[{com_score}] Komputer")
	for x in range(1,4):
		print(f"{x}. {suit_obj[x]}")
	print()
	print("0. Keluar")

	pl_pick = int(input(">> "))
	print(f"Kamu memilih {suit_obj[pl_pick]}")

	com_pick = random.randint(1,3)
	print(f"Lawan memilih {suit_obj[com_pick]}")

	if pl_pick == com_pick:
		print("- Hasilnya Seri")
	else:
		if(pl_pick==1 and com_pick==2) \
		or(pl_pick==2 and com_pick==3) \
		or(pl_pick==3 and com_pick==1):
			print("- Kamu Menang!!")
			pl_score += 1
		else:
			print("- Kamu Kalah, Coba Lagi")
			com_score += 1
		game_count -= 1

	input("Enter untuk lanjut >> ")

	if pl_score == 2 or com_score == 2:
		break

os.system("cls")
print("Hasil Pertandingan")
print(f"Player [{pl_score}]")
print(f"Komputer [{com_score}]")

if pl_score > com_score:
	print("- Kamu Memengankan Pertandingan")
else:
	print("- Kamu Kalah Dalam Pertandingan")
