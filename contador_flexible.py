# Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lownum = int(input("Ingresa un numero inicio: "))
highnum = int(input("Ingresa un numero Final: "))
mult = int(input("ingresa un numero que imprimirá en el rango inicio fnal los multiplos de dicho rango: "))

for i in range(lownum,highnum+1):
    if (i%mult==0):
        print(i)