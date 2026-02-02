# 2. ¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?. Use el
# algoritmo de la criba de Eratóstenes.
# El algoritmo de la criba de Eratóstenes se puede explicar a tus estudiantes como un
# juego de “ir tachando” números que NO son primos hasta que solo queden los primos.
# i. Se escribe una lista con todos los números desde 2 hasta el límite que se desee
# (por ejemplo, 100).
# ii. Se busca el primer número de la lista que no esté tachado; ese número es primo.
# iii. Se tachan todos los múltiplos de ese número (excepto él mismo).
# iv. Se repiten los pasos 2 y 3 hasta que ya no queden números nuevos para revisar.
# v. Los números que queden sin tachar son los primos.
def construir_cadena(max):
    cad = ""
    for i in range(2, max+1):
        cad += f"{i},"
    return cad.rstrip(",")

def quitar_cadena(str, num):
    cad = ""
    for n in str.split(","):
        if n != num:
            if int(n) % int(num) != 0:
                cad += f"{n},"
        else:
            cad += f"{n},"

    return cad.rstrip(",")



MAX = 1000
str = construir_cadena(MAX)
for snum in str.split(","):
    new_str= quitar_cadena(str, snum)
    if len(new_str) == len(str): 
        str = new_str
        break # pare si no hay cambios
    str

print(str)
