def calcular(x, y):
    return (x+y, x-y, x*y, x/y)

if __name__ == "__main__":
    carros = "Hilux", "Doblo", "Jeep", "Toro", "Fusca"
    print(carros)
    print(carros[1:])
    print(carros[1:-1])
    print(carros[1:-2])
    print(sorted(carros))

    carros_ordenados = sorted(carros)
    carros_ordenados[0] = "Twingo"
    print(carros_ordenados)


    print("-----------------")
    resultado = calcular(10, 2)
    print(resultado)