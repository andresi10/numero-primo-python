#Definimos la funcion a utilizar
def es_primo(numero):
    if numero < 2:
        print(f"El número ingresado es {numero} y NO es primo.")
    else:
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            #Usamos int(numero**0.5) para que el loop sea más eficiente 
            # (no revisamos más allá de la raíz cuadrada).
            if numero % i == 0:
                es_primo = False
                print(f"El número ingresado NO es primo. Es divisible por {i}.")
                break
        if es_primo:
            print("El número ingresado ES primo.")

numero = int(input("Ingresar un número mayor o igual a 0: ")) 
es_primo(numero)

input("Presione Enter para salir...")
