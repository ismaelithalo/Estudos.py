import random
num1 = random.randint(0,9)
num2 = random.randint(0,9)

if num1 < num2: 
    num1,num2 = num2,num1
res = num1 - num2

resposta = int(input("""Qual e a subtração dos numeros {} e {}?
""".format(num1,num2)))

while resposta != res:
    resposta = int(input("""Qual e a subtração dos numeros {} e {}?
""".format(num1,num2)))

print ("Parabens!")