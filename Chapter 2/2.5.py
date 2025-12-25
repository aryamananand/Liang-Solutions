subtotal = eval(input("Enter subtotal:"))
gratuityrate = eval(input("Enter gratuity rate:"))

gratuity = (gratuityrate / 100) * subtotal

total = subtotal + gratuity

print("The gratuity is:", gratuity, "and the total is:", total)
