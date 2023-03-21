height = int(input('Cual es tu altura, por favor en cm: '))
credits = int(input('Cuantos creditos tienes?: '))
with_taller_person = True

if height >= 137 and credits >= 10:
    print('Disfruta del viaje!')
elif height < 137:
    if height < 100 or not with_taller_person:
        print('Todavia no eres lo suficientemente alto para este paseo')
    elif height >= 100 and with_taller_person:
        print('Disfruten del viaje!')
elif credits < 10:
    print('No tienes suficientes creditos para entrar')
else:
    print('Datos no validos')