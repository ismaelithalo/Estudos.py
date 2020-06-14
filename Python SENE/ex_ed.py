#list []
#dict {}
#tuple = ()

lista_frutas = ["abacate","tomate","morango"]
lista_frutas.append("maca")
lista_frutas.remove("abacate")
print(len(lista_frutas))
#acessa por posição

dict_matriculas = {"Guilherme":170000000, "Prado": 180000000, "Lucas": 150000000}
print(dict_matriculas.keys())
print(dict_matriculas["Guilherme"])
#acessa por chave

tuple_frutas = ("tomate","morango","abacaxi")
#funcion como lista, mas é imutável