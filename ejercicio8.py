def bitcoinToEuros(bitcoin_amount, bitcoin_euros_value):
    if (bitcoin_euros_value < 30000):
        print("Alerta")
    elif (bitcoin_euros_value < 30000):
        print("Todo correcto")
    return

bitcoin_amount = input("Introduce la cantidad de bitcoin: ")
valor_bitcoin = 30000
bitcoin_euros_value = bitcoin_amount * valor_bitcoin
print("Tienes: " + bitcoin_euros_value + "euros")


