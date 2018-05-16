
import random

#Se lleva a cabo 10004 veces
for _ in range(10004):
    #Se eligen 6 números los cuales varian entre 1 y 41.El límite es 42 y por lo tanto este y los demas numeros no se utilizan
    var = random.sample(range(1, 42), 6)
    var.sort()
    print var




