def multi (*numeros):
    x = 1
    for numero in numeros:
         x *= numero
    print (x)

multi(5,5,5,5,5)