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


#LISTS
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_second_list = ["A", "B", "C"]
my_newest_list = []

print(type(my_list))
my_list.insert(5, "Seth")
print(my_list)
my_list.remove(9)
print(my_list)

my_newest_list.insert(0, my_list[0])
my_newest_list.insert(1, my_list[1])
my_newest_list.insert(2, my_list[2])
my_newest_list.insert(3, my_list[3])
my_newest_list.insert(4, my_list[4])
my_newest_list.insert(5, my_list[5])
my_newest_list.insert(6, my_list[6])
my_newest_list.insert(7, my_list[7])
my_newest_list.insert(8, my_list[8])
my_newest_list.insert(9, my_list[9])
my_newest_list.insert(10, my_second_list[0])
my_newest_list.insert(11, my_second_list[1])
my_newest_list.insert(12, my_second_list[2])
print(my_newest_list)

#TUPLES
ca_provinces = ('Manitoba', 'Saskatchewan', 'Ontario', 'Quebec')
print(type(ca_provinces))
print(ca_provinces)


#DICTIONARIES
coin_values = {'nickel' : 0.05, 'dime' : 0.1, "quarter" : 0.25}
print(type(coin_values))
print(coin_values)

coin_values['nickel'] = round(coin_values['nickel'] * 100)
coin_values['dime'] = round(coin_values['dime'] * 100)
coin_values['quarter'] = round(coin_values['quarter'] * 100)
print(coin_values)

coin_values['loonie'] = 100
coin_values['toonie'] = 200
print(coin_values)


#SETS
odd_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(type(odd_numbers))
print(odd_numbers)

fives = {5, 10, 15, 20}
print(fives)

unique_values = odd_numbers.union(fives)
print(unique_values)

common_values = odd_numbers.intersection(fives)
print(common_values)

multiples_of_2 = odd_numbers - fives
print(multiples_of_2)

multiples_of_5 = fives - odd_numbers
print(multiples_of_5)

