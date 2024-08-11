Euro = 4525
USD = 4139

Cambio = input("Ingrese la moneda de origen para la conversión (EUR/USD)")
Monto = input("Ingrese el monto a convertir ", )
# En este de abajo en vez de "float" tenía "int". PEro como el resultado va a dar en decimales, 
# es importante dejarlo en el "float". 

Numero=float(Monto)
# Ahora el .upper lo que hace es que convierte en la consola el input que entra en minuscula y lo convierte en May
# También noté que este "upper" es mejor ponerlo en estos condicionales if, elif y así. Ah! y seguido del ().

if Cambio.upper() == "EUR":
    print("El cambio de Euros a pesos COP es de: ", Euro*Numero, "Pesos colombianos")

elif Cambio.upper() == "USD":
    print("Parcero colombiano, el cambio de moneda gringa es de: ", USD*Numero, "Pesos COP")
else:
    print("Púdrete bitch") 
