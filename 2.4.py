A=0,B=input("Number for convert in hex ::  ")
for i, j in enumerate(reversed(h)):
    A+= int(j, 16) * (16 ** i)
    print(A)