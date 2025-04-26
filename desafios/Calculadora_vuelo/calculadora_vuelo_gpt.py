# calculadora_vuelo.py

# 🛫 Calculadora de Vuelo
# Velocidad del avión: 800 km/h
# Autonomía máxima sin escala: 4 horas
# Cada escala agrega 1 hora extra

def calcular_tiempo_de_vuelo(distancia_km):
    """Calcula el tiempo de vuelo basado en la distancia y la velocidad."""
    velocidad = 800  # km/h
    tiempo = distancia_km / velocidad
    return tiempo

def calcular_escalas(tiempo_vuelo):
    """Calcula la cantidad de escalas necesarias."""
    if tiempo_vuelo > 4:
        escalas = int(tiempo_vuelo // 4)  # División entera para contar escalas completas
    else:
        escalas = 0
    return escalas

def main():
    try:
        distancia = int(input('Ingresá la distancia en kilómetros: '))
        if distancia <= 0:
            print("Por favor, ingresá una distancia mayor a 0 km.")
            return

        horas_vuelo = calcular_tiempo_de_vuelo(distancia)
        escalas_necesarias = calcular_escalas(horas_vuelo)
        tiempo_total = horas_vuelo + escalas_necesarias

        print(f'\n✈️ Resultado del cálculo:')
        print(f'- Tiempo de vuelo sin escalas: {horas_vuelo:.2f} horas')
        print(f'- Cantidad de escalas necesarias: {escalas_necesarias}')
        print(f'- Tiempo total incluyendo escalas: {tiempo_total:.2f} horas')

    except ValueError:
        print("⚠️ Entrada inválida. Por favor, ingresá un número entero.")

if __name__ == "__main__":
    main()
