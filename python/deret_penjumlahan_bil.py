def jumlah1(a,b):
	for x in range(a,b+1):
		if x < b:
			print(f"{x} + ", end="")
		else:
			print(x, end="")

def jumlah2(a,b):
	hasil = ""
	for x in range(a,b+1):
		if x < b:
			hasil += f"{x} + "
		else:
			hasil += f"{x}"
	return hasil

bil_A = 5
bil_B = 10
jumlah1(bil_A, bil_B)
print()

hasil = jumlah2(bil_A, bil_B)
print(hasil)
