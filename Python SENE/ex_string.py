texto = "Teste de testo"
#retorna o tamanho da string
print(len(texto))

for i in range(0,len(texto)):
    print (i)
    print(texto[i])

#replace
texto = texto.replace("Teste","Testes")
print (texto)

#count
print(texto.count('a'))

#procura a primeira aparição e retorna a posição
print(texto.find("st"))

#separa a string, caso sem parametro, separa as plavras por espaço
#também é possivel separar logo no input retornando uma lista, com .split()
print(texto)
texto = texto.split();
print(texto)
#como o valor retornado é uma lista, pode-se usar como parmetro no for, assim pode-se procurar coisas epecificas
for i in texto:
    if i=="de":
        print("A palvra de existe no texto")

#função join funciona da mesma forma que a função split, mas coloca determinado elemento junto de várias cópias da string

#função upper() coloca tudo em caixa alta
texto = "Teste de testo"
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
# a função title coloca tods as primeiras letras como maiusculas
print(texto.title())
#swapcase troca maiusculas e minlusculas
print(texto.swapcase())
#existe isupper islower e istitle, e isalnum retorna bool se alfa numerico, isalpha e isdigit e isspace

#melhor form de printar algo -e com range(0,-1), ou string[0,-1] mias o passo
