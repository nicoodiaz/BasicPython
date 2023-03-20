'''
Bienvenido al conversor de monedas
'''
yuan = int(input('Cuantos yuanes tienes?: '))
yen = int(input('Cuantos yenes tienes?: '))
won = int(input('Cuantos wones tienes?: '))

conversion_yuan = yuan * 0.15
conversion_yen = yen * 0.0076
conversion_won = won * 0.00077
total = conversion_yen + conversion_yuan + conversion_won
print(total)

# En este apartado creamos un programa donde se tira la moneda al aire y sale 'Cara' o 'Cruz'
import random

num = random.randint(0, 1)   # RNGesus will give us a random number that is either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')