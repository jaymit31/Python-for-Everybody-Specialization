def computepay(h,r):
    h = input("Enter Hours:")
    r = input("Enter rate:")
    if h<40:
    	pay = float(h)*float(r)
    elif h>= 40:
    	pay = (float(h)-40)*0.5*float(r) + float(h)*float(r)
    return pay


p = computepay(10,20)
print("Pay", p)
