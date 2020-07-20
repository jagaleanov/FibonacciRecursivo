
def fibo( n ):

    if n <= 2 :
        return 1
    else:
        return fibo (n-1) + fibo(n-2)

n = int( input( "Ingrese número para calcular fibonacci: " ) )

numero_fibo = fibo( n )
print( "El número " + repr( n ) + " en la serie de fibonacci es " + repr( numero_fibo ) )