dinero  = 2000
hambre = 18
precio_helado = 100
interes = precio_helado * 0.2 

print("Compro un helado")

dinero  = dinero - precio_helado
hambre = hambre + 18

if hambre < 85:
    print("Tengo hambre")

print("Compro un helado")

interes = precio_helado * 0.2
precio_helado = precio_helado + interes
dinero = dinero - precio_helado 
hambre = hambre + 18

if hambre < 85:
     print("Sigo teniendo hambre")

print("Compro otro helado")

interes = precio_helado * 0.2
precio_helado = precio_helado + interes
dinero = dinero - precio_helado
hambre = hambre + 18

if hambre < 85:
    print("Aun tengo hambre")

print("Compro otro helado")

interes = precio_helado * 0.2
precio_helado = precio_helado + interes
dinero = dinero - precio_helado
hambre = hambre + 18

if hambre < 85:
    print("Necesito más helado")
else:
    print("Estoy lleno")
    print("Me quedan: " + str(dinero) + "€")
    print("Estoy al " + str(hambre) + " de mi capacidad")
