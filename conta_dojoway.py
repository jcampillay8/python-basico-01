# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for i in range(1,101):
    if i%5==0:
        print("Conding")
    if i%10 ==0:
        print("Coding Dojo")
    print(i)