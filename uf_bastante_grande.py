# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
def sum():
    suma=0
    for i in range(500001):
        if i%2!=0:
            suma+=i
            
    return suma

print(sum())