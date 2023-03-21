gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
q1 = int(input(''' Te gusta el amanecer o atardecer?
               1)Amanecer
               2)Atardecer
               Respuesta: '''))
if q1 == 1:
    gryffindor =+ 1
    ravenclaw =+ 1
elif q1 == 2:
    hufflepuff =+ 1
    slytherin =+ 1
else:
    print('¡Entrada incorrecta!')
    
q2 = int(input(''' Cuando muera, quiero que la gente me recuerde como:
               1) Bueno
               2) Grande
               3) Sabio
               4) Valiente
               Respuesta: '''))
if q2 == 1:
    hufflepuff =+ 2
elif q2 == 2:
    slytherin =+ 2
elif q2 == 3:
    ravenclaw =+ 2
elif q2 == 4:
    gryffindor =+ 2
else:
    print('Entrada incorrecta')
    
q3 = int(input(''' Qué tipo de instrumento agrada mas a tu oido?:
               1) Violin
               2) Trompeta
               3) Piano
               4) Bateria
               Respuesta: '''))

if q3 == 1:
    slytherin =+ 4
elif q3 == 2:
    hufflepuff =+ 4
elif q3 == 3:
    ravenclaw =+ 4
elif q3 == 4:
    gryffindor =+ 4
else:
    print('Entrada incorrecta')
    

houses = {'🦁 Gryffindor': gryffindor, '🦅 Ravenclaw': ravenclaw, '🦡 Hufflepuff': hufflepuff, '🐍 Slytherin': slytherin}
max_points= max(houses.values())
house_select = [house for house, points in houses.items() if max_points == points]
print(f'La casa seleccionada para ti sera {house_select[0]}')