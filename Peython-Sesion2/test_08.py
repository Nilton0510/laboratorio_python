Lista_1 = []
Lista_2 = []

Lista_1.append("Nilton")
Lista_1.append(22)
Lista_1.append("Economista")

Lista_2.append("Cristhian")
Lista_2.append(20)
Lista_2.append("Psicologo")

suma_listas = Lista_1 + Lista_2

print("La lista es: {}".format(suma_listas))

suma_listas.reverse()

print("La lista actualizada es: {}".format(suma_listas))

suma_listas.remove(22)
suma_listas.remove(20)

print("La lista actualizada es: {}".format(suma_listas))