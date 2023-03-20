menu = """
Bienvenidos a la casa de cambio de Steve 💵💵
Usted tiene que elegir entre las 3 opciones que tenemos
1- Pesos argentinos
2- Real (Brasil)
3- Peso uruguayo
"""
opcion = int(input(menu))
if opcion == 1:
    pesos = input('Cuantos pesos argentinos tiene usted?: ')
    pesos = float(pesos)
    tipo_de_cambio= 385
elif opcion == 2:
    pesos = input('Cuantos reales tiene usted?: ')
    pesos = float(pesos)
    tipo_de_cambio = 5.11
elif opcion == 3:
    pesos = input('Cuantos pesos uruguayos tiene usted?: ')
    pesos = float(pesos)
    tipo_de_cambio = 39.13
else:
    print('Por favor, elegi bien entre las opciones, gracias')
    pesos = None
dolares = round((pesos / tipo_de_cambio), 2)
print(f'Usted de este local se puede llevar {dolares} en dolares.')