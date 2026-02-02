# 1. Se coloca un capital C, a un interés I (que oscila entre 0 y 100), durante M años y se desea
# saber en cuanto se habrá convertido ese capital en “M” años, sabiendo que es acumulativo.
# (Desarrollarlo con un algoritmo iterativo –for, while, etc-).

capital = int(input("ingresar capital: "))


while True:
    try:
       interes = float(input("ingresar interes: "))
       if 0 < interes < 100 :
           print("interes correcto")
           break
       else:
           print("interes incorrecto")
    except ValueError:
        print("valor incorrecto")
        input("ingrese cualquier tecla")

años = int(input("ingresar años: "))
total = capital

for i in range(1, años + 1):
    total += total * interes / 100
    print(f"año {i} = {total:.2f}")
print(f"Total final: {total:.2f}")
    
    



