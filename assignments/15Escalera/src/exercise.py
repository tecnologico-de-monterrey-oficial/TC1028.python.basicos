import math
def main():
    #escribe tu código abajo de esta línea
    altura=float(input("Altura de la casa: "))
    angulo=int(input("Angulo en grados: "))
    radianes=math.radians(angulo)
    largo=round(altura/math.sin(radianes))
    print(f"Largo de la escalera: {largo}")

if __name__ == '__main__':
    main()
