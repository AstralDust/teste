def fatorial(n):
    '''
        algoritmo interativo para resolver fatorial
        input:
            n:int - um valor inteiro qualquer >0
        output:
            result - Um valor inteiro >0
    '''
    pass


try:
    print('===== fatotial =======')
    n= int(input("digite um numero"))
    print(n)
except ValueError: 
    print('Erro, voce deve entrar com um numero')
else:
    y = (n-1)
    factorial = n
    while y != 1:
        factorial = factorial * y
        y = y - 1


print('O resultado do fatorial: ', factorial)





