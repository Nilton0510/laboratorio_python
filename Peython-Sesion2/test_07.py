"""
Crear 3 variables: nombre, edad y distrito

Requisitos:
- Nombre: string, edad: int, distrito: string
- Concatenar ests 2 datos e indicar una oración como la siguiente:
José tiene X años y es de "Distrito"
-Obtener el módulo de su edad al usarlo con el número 5
"""

var_1 = "Nilton"
var_2 = 22
var_3 = "Moyobamba"
modulo = var_2 % 5
print("Mi nombre es {} tengo {} años y vivo en {}".format(var_1, var_2, var_3) )
print("El modulo es: {}".format(modulo) )