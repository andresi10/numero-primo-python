def esPrimo(numero):
    if numero == 0:
        print('El numero ingresado es 0')
    elif numero == 1:
        print('El numero ingresado es 1')
    elif numero == 2:
        print('El numero ingresado es Primo')
    elif numero > 1:
        for i in range(2,numero):
            if numero % i == 0:
                print('El numero ingresado NO es Primo')
                print(f'El numero es divisible por {i}')
                break
            else: print('Es PRIMO')
            break
            
numero = int(input('Ingresar un numero(mayor a 1): '))
esPrimo(numero)

input('Press any key to exit')