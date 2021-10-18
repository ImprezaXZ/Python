amount = int(input ("Total amount\n"))
tax =  float(input("Tax%\n"))
tax = tax / 100
total = amount + amount * tax 
print(total)
