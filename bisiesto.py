def esbisiesto (anio):
    if  anio%4==0 and anio%100!=0 or anio%400==0:
        print("Bisiesto")
    else:
        print("Normal")

print("Hey")

esbisiesto(2100)
esbisiesto(2300)
esbisiesto(2000)


































