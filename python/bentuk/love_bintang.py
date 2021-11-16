import time

size = 15
s2 = size // 3
size = s2 * 3

# BENTUK ATAS
obj1 = []
for row in range(s2):
    s = ""
    for col in range(s2):
        if col < s2/2-row:
            s += "  "
        else:
            s += "**"
    obj1.append(s)

obj2 = []
for row in range(s2):
    s = ""
    for col in range(s2):
        if(col > row) and(col < s2-row-1):
            s += "  "
        else:
            s += "**"
    obj2.append(s)

obj3 = [s[::-1] for s in obj1]
obj4 = [a+b+c for a,b,c in zip(obj1,obj2,obj3)]

# PIRAMID
pr = range(size,0,-2)
sp = range(0,len(pr),1)

piramid = [("  "*s)+("**"*p) for p,s in zip(pr,sp)]
love = obj4 + piramid

for s in love:
    print(s)
    time.sleep(0.25) # jeda waktu 250 mili detik
