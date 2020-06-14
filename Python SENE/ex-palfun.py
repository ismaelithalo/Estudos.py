def palin (palavra):
    palavra_a = ""
    for i in range(len(palavra)-1,-1,-1):
        palavra_a += palavra[i]
    if palavra == palavra_a:
        return True
    else:
        return False

palavra = input("""Insira uma palavra
""")
x = palin(palavra)
print(x)
