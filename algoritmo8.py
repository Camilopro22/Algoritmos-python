# Si tengo una cantidad de soles, dar su equivalente en dólares
# y después en euros. Se sabe que 1 dólar =3.25 soles y 1
# euro=3.83 soles.

print("_____________________________________________________________")

print("Programa para convertir soles a euro y a dolares.")
print("______________________________________________________________")

euro = 3.84
dolar = 2.82

soles = float(input("Ingrese la cantidad de soles a convertir: "))
d = soles/dolar
e = soles/euro

print(f"la cantidad de soles a euro es de: {e}")
print(f"La cantidad de soles a dolares es de: {d}")