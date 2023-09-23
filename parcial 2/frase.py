def contar_letra(palabra, letra):
    palabra = palabra.lower()
    letra = letra.lower()

    cont = palabra.count(letra)

    return cont

palabra = input("Ingrese una palabra o frase: ")
letra = input("Ingrese la letra: ")

result = contar_letra(palabra, letra)
print(f"La letra '{letra}' aparece {result} veces en la cadena.")