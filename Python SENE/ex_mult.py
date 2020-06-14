#-*-conding:utf-8 -*-
import random

x = random.randint(0,9)
y = random.randint(0,9)

def verif (x,y):
    z=0
    while z!=(x*y):
        z = int(input("""Qual o produto dos numeros {} e {}?
""".format(x,y)))
        if (z == (x*y)):
            print("Parabéns, voce acertou!")
        else:
            print("tente novamente")
verif(x,y)
