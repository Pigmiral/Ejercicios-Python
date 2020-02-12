i=1
n= int(input("Digite el numero de estudiante:"))
suma_notas=0
while i<=n:
    
    nota = float(input("Digite su nota: "))
    suma_notas+=nota
    i+=1

print("el promedio es: ",suma_notas/n)
