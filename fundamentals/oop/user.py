#1.display_info(self) - Have this method print all of the users' details on separate lines.
#2.enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
#3.spend_points(self, amount) - have this method decrease the user's points by the amount specified.


class User:
    def __init__(self, first_name, last_name, email, age):
        self.is_rewards_member = False
        self.gold_card_points = 0

        self.first_name = first_name
        self.last_name= last_name
        self.email= email
        self.age= age

#-------------------------------------

    def display_info(self):
        for key, value in self.__dict__.items():
            print(key,value)
        print(self.first_name)   
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)


    def enroll_self(self):
        self.is_rewards_member = True

my_user = User("Kaianna","Jade", "onelove@gmail.com",40)
print(my_user.first_name)   
print(my_user.last_name)
print(my_user.email)
print(my_user.age)
print(my_user.is_rewards_member)
print(my_user.gold_card_points)

my_user.display_info()

my_user2 = User("Jada","Naomi","jnaomi@gmail.com",18)
    
my_user2.display_info()  
print("test")  






#In the outer scope, create a user instance and call the display_info method to test.




#dd the enroll method to the User class, implement and test by calling the method on the user in the outer scope.

#Make 2 more instances of the User class.

# Implement the spend_points(self, amount) method

# Have the first user spend 50 points

# Have the second user enroll.

# Have the second user spend 80 points

# Call the display method on all the users.

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.

# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.

# class Shoe:
#     # now our method has 4 parameters (including self)!
#     def __init__(self, brand, shoe_type, price):
#     	# we assign them accordingly
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         # the status is set to True by default
#         self.in_stock = True
    
#     # Takes a float/percent as an argument and reduces the
#     # price of the item by that percentage.
#     def on_sale_by_percent(self, percent_off):
#         self.price = self.price * (1-percent_off)


