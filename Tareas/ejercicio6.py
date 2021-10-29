customer_basket_cost = 34
customer_basket_weight = 44
shipping_cost = customer_basket_weight * 1.2

#Write if statement here to calculate the total cost

if customer_basket_weight >= 100:
    coste_cesta = customer_basket_cost
    print("Total: " + str(coste_cesta) + " euros")
else:
    coste_cesta = customer_basket_cost + shipping_cost
    print("Total: " + str(coste_cesta) + " euros")
