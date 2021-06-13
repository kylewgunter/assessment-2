# Create interface with multiple options
# 1. view video inventory = list of current videos in store init video inventory module
# 2. view rentals initiate a list of current rentals per customer
# 3. rent video module iterates over video list in store and decrements with a match of title and pops off list?
# if title has 0, runner throws an exception 
# 4. return module increments value dict for match
# 5. add a new customer adds customer to database and assigns an id number that isnt in database already
# 6 exit -- done
import re
import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
inventory_path = os.path.join(my_path, "../data/inventory.csv")


from .VideoInventory import VideoInventory
# from .customer import Customer

# 1. view video inventory = list of current videos in store init video inventory module
# Interface init creates a list of movies var that is empty.
class Interface:    
    def __init__(self):
        pass
        self.video_inventory = []

    def run(self):
        while True:
            print("\n----- Welcome to Code Platoon Video! -----\n------------------------------------------\n")
            print("Please select one of the following options")
            mode = input("\n1. View video inventory\n2. View customer's rented videos \n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n\nSelect an option: ")

            if mode == '1':
                print("\n")
                inventory = Interface()
                inventory.get_inventory()
                # inventory = Video_Inventory()
                # inventory.get_inventory_list()
                # print('\n***test***')
                # list_inventory = Video_Inventory()
                # return list_inventory
            # elif mode == '2':
            #    view_rentals = Customer.objects()

            # elif mode == '3':
            # #    rent_video = rent()

            elif mode == '6':
                print("\n--- Goodbye! ---\n")
                break

    def view_inventory(self):
        for video in self.video_inventory:
            print(video)
   
    # creates a list of inventory objects
    @classmethod
    def get_inventory(cls):
        with open(inventory_path, 'r', newline='') as movie_file:
            inventory = csv.DictReader(movie_file)
            video_list = []
            for movie in inventory:
                movies_in_store = VideoInventory(movie['id'], movie['title'], movie['rating'], movie['copies_available'])
                video_list.append(movies_in_store)
                print(f"ID: {movie['id']}\nTitle: {movie['title']}\nRating: {movie['rating']}\nCopies in store: {movie['copies_available']} ")





# @classmethod
#   def get_all_users_from_db(cls):
#     with open(user_path, 'r') as users_file:
#       users = csv.DictReader(users_file)
#       users_list = []
#       for user in users:
#         if user['tier'] == 'p':
#           premium_user = PremiumUser(user['name'], user['email_address'], user['driver_license'])
#           users_list.append(premium_user)
#         else:
#           free_user = FreeUser(user['name'], user['email_address'], user['driver_license'])
#           users_list.append(free_user)
#       return users_list 
