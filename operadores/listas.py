#LISTAS: Dato complejo. Corresponde a una colección arbitraria de objetos.
#list[oj1, obj2, obj3,.........objn,]

lista = [1, 2, 3, 4, 5]
print(type(lista))

lista2 = ["texto1", "texto2", "texto3"]
print(type(lista2))


print(lista2)
lista3 = ["texto2", "texto1", "texto3"]
print(lista2 == lista3)

print(lista2 == ["texto1", "texto2", "texto3"])
print(lista2 is ["texto1", "texto2", "texto3"])

lista4 = [1, 2, "texto", "texto1"]
print(lista4)

def func():
    print("Hola")
lista5 = [1, 3, "texto", func]
print(lista5)

print(lista4[1:3])
print(lista4[0:3:2])#stry
print(lista4[::-1])
lista5 = lista4[::-1]
print(lista5)

lista5 = [1, 3, "texto", func]
lista5[3]()

texto = "Hola Mundo"
print(texto[:])
texto1 = texto[:]
print(texto[:]is texto)

print("texto1", id(texto1))
print("texto", id (texto))

lista6 =[1,2, 3]
lista7 =lista6[:]
lista7 [0] = 99
print(lista7)

#OPERACIONES CON LISTAS

lista6 =  [1, 2, 3]
lista7 = [4, 5, 6]
print(lista6 + lista7)
print(len(lista6))
print(min(lista6))
print(max(lista6))
lista3 =["texto1","texto2","texto3"]
print(min(lista3))
print(max(lista3))
lista7 + [4,5,6]
print(lista7 + [9])
lista7[0]+= 80
print(lista7)
lista8 =[1,[2,[3,4],5],6]
print(lista8[2])
print(lista8[1][1][0])
print([3,4]in lista8[1])

lista3 =["texto1","texto2","texto3"]
del lista3[1]
print(lista3)

lista3 += ["texto4", "texto5", "texto6"]
print(lista3)

lista3[0:2] =[99,86]
print(lista3)

lista3[3:3] = ["textonuevo", 3, 87, 9.0]
print(lista3)

lista3[0] = ["textonuevo", 3, 87, 9.0]
print(lista3)

lista3[:0] =[]
print(lista3)
