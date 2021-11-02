tinggi = 11
for spasi, piramid in zip( range(tinggi,-1,-1), range(1,tinggi*2,2) ):
	print( (" "*(spasi-1)) + ("*"*piramid) )

N = (tinggi * 2) - 1
M = N // 4
L = N - (M*2)

for x in range(tinggi):
	print( (" "*M) + ("*"*L) + (" "*M) )
