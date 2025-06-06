#LOGICOS: Modifica expresiones evaluadas en num contexto de TRUE/FALSE para crear condiciones mas complejas
#'not' => (not x) TRUE si X es False  | FALSE si X es TRUE
#'or' => (x or y ) TRUE si X or Y son verdaderas(una de las dos)
#'and' => (x and y) TRUE solo si X e Y son verdaderas

num = 5
print( num > 10)
print("NOT", not num > 10)

#OR
num1 = 5
num2 = 10
print( num1 < 4)
print("OR",  num1 < 4 or num2 > 5)

#AND 
num1 = 5
num2 = 10
print(num1 < 4)
print("AND", num1 < 4 and num2 > 5)
