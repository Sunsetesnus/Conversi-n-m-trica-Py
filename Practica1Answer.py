Euro_Mxn = 23.7
USD_MXN = 20.75


conversion = input("ingrese la moneda origen (USD/EUR)")
Cambio = float(input("Ingrese el monto a convertir: "))

if conversion.upper() == "EUR":
    resultado = Cambio * Euro_Mxn
    print("El resultado de la conversión de EUR a MXN es: ", resultado)

elif conversion.upper() == "USD":
    resultado = Cambio * USD_MXN
    print("El resultado de la conversión de USD a MXN es:", resultado)

else:
    print("No está disponible este tipo de conversión")