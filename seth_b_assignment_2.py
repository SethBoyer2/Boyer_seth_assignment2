__author__ = "Seth Boyer"
__version__ = "1.0.0"


# SIMPLE DATA TYPES

name = "Seth"
has_license = False
current_year = 2025

print(f"name: {name} type: {type(name)}")
print(f"has license: {has_license} type: {type(has_license)}")
print(f"this year: {current_year} type: {type(current_year)}")

#Increment year by 1 
current_year = current_year + 1

print(f"Next year: {current_year} type: {type(current_year)}")

# MATHEMATICAL OPERATIONS

car_price = 75930

gst_total = (car_price * 0.05)
pst_total = (car_price * 0.07)
final_price = gst_total + pst_total + car_price

print("Purchase price:", car_price, "Provincial tax:",
       pst_total, "Federal tax", gst_total, "Total", final_price)

print(f"Purchase price: ${car_price:,.2f} Provincial Tax: ${pst_total:,.2f} Federal Tax: ${gst_total:,.2f} Total: ${final_price:,.2f}")