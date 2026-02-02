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
for n in range(2, 1001):
    es_primo = True
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            es_primo = False
            break
    if es_primo:
        print(n)
