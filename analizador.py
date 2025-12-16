import statistics

def leer_datos():
    datos = input("Ingresa números separados por comas: ")
    lista = [float(x) for x in datos.split(",")]
    return lista

def mostrar_resultados(datos):
    print("\nResultados estadísticos:")
    print("Media:", statistics.mean(datos))
    print("Mediana:", statistics.median(datos))
    print("Moda:", statistics.mode(datos))
    print("Varianza:", statistics.variance(datos))
    print("Desviación estándar:", statistics.stdev(datos))

def main():
    print("Analizador estadístico básico")
    datos = leer_datos()

    if len(datos) < 2:
        print("Se necesitan al menos dos datos.")
        return

    mostrar_resultados(datos)

main()
