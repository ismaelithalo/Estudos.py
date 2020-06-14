texto = input("""Digite seu texto:
""")
cont = 0
palavra = ""
for i in range(0,len(texto)):
    texto=texto.title()
    if texto[i].isupper():
        palavra = palavra+texto[i]
for i in range(0,len(palavra)):           
    if palavra[i]==palavra[len(palavra)-1]:
        if palavra[i]==palavra[i-1]:
            cont=cont+1    
    elif palavra[i]==palavra[i+1]:
        cont = cont+1

print("Possuem {} aliteracoes".format(cont))
