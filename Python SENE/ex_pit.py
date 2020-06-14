cat1 = int(input("Insira o primeiro cateto"))
cat2 = int(input("Insira o segundo cateto"))

hip = (cat1**2 + cat2**2)**(0.5)

#print("A hipotenusa é ", hip)

print (""" Essa é a hipotenusa do trinagulo: {var1} e esses sãos os catetos: {var2},{var3}""" .format(var1=hip,var2=cat1,var3=cat2))