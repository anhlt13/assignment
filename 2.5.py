talents = float(input("enter talents: "))
pounds = float(input("enter pounds: "))
lots = float(input("enter lots: "))
total_grams= talents*20*32*13.3+pounds*32*13.3+lots*13.3
kilograms = total_grams//1000
grams = total_grams%1000
print(f"the weight in the modern units: {round(kilograms)} kilograms and {grams:5.2f} grams")



