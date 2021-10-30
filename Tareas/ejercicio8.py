bitcoin_amount = input("Introduzca sus bitcoins: ")
bitcoin_euros_value = 40000

def bitcoinToEuros(bitcoin_amount, bitcoin_euros_value):
    euros_amount = float(bitcoin_amount) * bitcoin_euros_value
    if euros_amount < 30000:
        print("Alerta su valor de Bicoin es de: " + str(euros_amount) + "€")
    else:
        print("Su valor de Bitoin ha subido a: "+ str(euros_amount) + "€")
   
bitcoinToEuros(bitcoin_amount,bitcoin_euros_value)


bitcoin_amount = input("Introduzca sus bitcoins: ")
bitcoin_euros_value = 25000

def bitcoinToEuros(bitcoin_amount, bitcoin_euros_value):
    euros_amount = float(bitcoin_amount) * bitcoin_euros_value
    if euros_amount < 30000:
        print("Alerta su valor de Bicoin es de: " + str(euros_amount) + "€")
    else:
        print("Su valor de Bitoin ha subido a: "+ str(euros_amount) + "€")
   
bitcoinToEuros(bitcoin_amount,bitcoin_euros_value)
