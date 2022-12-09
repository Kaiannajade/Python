# declare a class and give it name Shoe
class Shoe:		
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
    	self.price = 69.99
    	self.in_stock = True

skater_shoe = Shoe()
dress_shoe = Shoe()
# Accessing the instance's attributes
print(skater_shoe.type) # Classic Sk8-Hi
print(dress_shoe.type)	# Classic Sk8-Hi

skater_shoe.type = "Low-top Trainers"
print(skater_shoe.type)
# output: Low-top Trainers
dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)
# output: Ballet Flats

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
    	self.price = price
    	# the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
# Create two shoe instances
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
        
# The skater shoes go on sale by 20% reduced price:
skater_shoe.price = skater_shoe.price * (1 - 0.2)
        
# The dress shoes go on sale by 10% reduction:
dress_shoe.price = dress_shoe.price * (1 - 0.1)
        
# The skater shoes go on sale AGAIN by another 10%:
skater_shoe.price = skater_shoe.price * (1 - 0.1)

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)
