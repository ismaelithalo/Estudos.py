#-*- coding:utf-8 -*-
var = int(input("""Digite um numero a ser verificado.
"""))

if (((var%5)==0) and ((var%6)==0)):
    print ("O numero",var,"é divisivel por 5 e 6")
else:
    print ("O numero",var,"não eh divisivel")