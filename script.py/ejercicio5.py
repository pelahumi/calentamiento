dinero  = 2000
hambre = 18

print("Compro un helado")

dinero  = dinero - 100
hambre = hambre + 20

if hambre < 85:
    print("Tengo hambre")

print("Compro un helado")

dinero = dinero - 100
hambre = hambre + 20

if hambre < 85:
     print("Sigo teniendo hambre")

print("Compro otro helado")

dinero = dinero - 100
hambre = hambre + 20

if hambre < 85:
    print("Aun tengo hambre")

print("Compro otro helado")

dinero = dinero - 100
hambre = hambre + 20

if hambre < 85:
    print("Necesito más helado")
else:
    print("Estoy lleno")
    print("Me quedan: " + str(dinero) + " euros")
    print("Estoy al " + str(hambre) + " de mi capacidad")