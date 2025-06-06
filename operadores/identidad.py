text1 = input("Introduce un texto")

help(id)

print("text1 ", id(text1))

text2 = input("Introduce un texto")
print("text2 ", id(text2))

print(text1 is text2)

print("IDENTIDAD", text1 is text2)
print("COMPARACION", text1 == text2)
print("IDENTIDAD 'is not' ", text1 is not text2)
#IDENTIDAD: "is" TRUE si x e Y son el mismo objeto
#IDENTIDAD: "is not" => TRUE si X e Y NO son el msmo objeto

#text1 is text2 

