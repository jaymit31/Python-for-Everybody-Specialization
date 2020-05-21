hrs = input("Enter Hours:")
rate = input("Enter Rate:")
if hrs<=40:
	pay = float(hrs)*float(rate)
else:
    pay = 40*float(rate)-(40-float(hrs))*float(rate)*1.5
print(pay)
