talent = float(input("one talent is "))
pound = float(input("one pound is "))
lot = float(input("one lot is "))
weight = (talent*pound*lot)+(pound*lot)+lot
print("The weight in modern units: "+ str(weight/1000) +" kilograms " + "and " + str(weight) + " grams ")