import sys

def sumar(num):
    suma = sum(num)
    return suma

def promedios(num):
    suma = sum(num)
    promedio = suma / len(num)
    return promedio

def main():
    if len(sys.argv) < 2:
        print("Usage: python programa.py num1,num2,num3,...")
        sys.exit(1)

    num_str = sys.argv[1]
    numeros = [float(num) for num in num_str.split(',')]
    
    suma = sumar(numeros)
    promedio = promedios(numeros)

    print(f"La suma es: {suma}")
    print(f"El promedio es: {promedio}")

if __name__ == "__main__":
    main()
