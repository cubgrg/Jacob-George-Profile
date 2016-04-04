#Program that calculates regular hour pay plus over time pay 
hrs = raw_input("Enter Hours: ")
hrs = float(hrs)
rate = raw_input("Enter Rate of Pay: ")
rate = float(rate)
if hrs>40:
    pay = (40*rate)+((hrs-40)*rate*1.5)
else:
    pay = hrs*rate

print pay 