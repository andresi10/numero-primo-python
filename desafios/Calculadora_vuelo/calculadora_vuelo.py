# Calculadora de Vuelo
# v = 800 km/h autonomía = 4hs si escala += 1 hs

# t =  d / v
def calcular_tiempo_de_vuelo(dist):
    tiempo = float(dist / 800)
    return tiempo    
   
#  Tiempo de vuelo sin escalas
#  Cantidad de escalas necesarias
#  Tiempo total incluyendo escalas

distancia = int(input('Ingresa la distancia en kms: '))
horas = calcular_tiempo_de_vuelo(distancia)

if horas > 4:
    escalas = int (horas/4)     
    tiempototal = horas + escalas 
else: 
    escalas = 0 
    tiempototal = horas
    
print(f'El tiempo de vuelo es: {horas:.2f}')
print(f'Cantidad de escalas necesarias: {escalas}')
print(f'Tiempo total incluyendo escalas: {tiempototal:.2f}')
