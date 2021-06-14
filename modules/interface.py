# Create interface with multiple options
# 1. view video inventory = list of current videos in store init video inventory module
# 2. view rentals initiate a list of current rentals per customer
# 3. rent video module iterates over video list in store and decrements with a match of title and pops off list?
# if title has 0, runner throws an exception 
# 4. return module increments value dict for match
# 5. add a new customer adds customer to database and assigns an id number that isnt in database already
# 6 exit -- done

import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
inventory_path = os.path.join(my_path, "../data/inventory.csv")
customer_path = os.path.join(my_path, "../data/customers.csv")


from modules.customer import Customer
from .VideoInventory import VideoInventory


# 1. view video inventory = list of current videos in store init video inventory module
# Interface init creates a list of movies var that is empty.
class Interface:    
    def __init__(self):
        pass
        self.inventory = []
        self.customers = []

    def run(self):
        print("\n----- Welcome to Code Platoon Video! -----\n")
        print("Please select one of the following options")
        
        while True:
            mode = int(self.menu_options())
            return_menu = ("What else would you like to do?")
            
            if mode == 0:
                continue

            if mode == 1:
                self.store_inventory()
                print(return_menu)
                mode == 0

            elif mode == 2:
                self.get_customer_info()
                print(return_menu)
                mode == 0

            elif mode == 3:
                self.rent_video()
                print(return_menu)
                mode == 0
            
            elif mode == 6:
                print("\n--- Goodbye ---\n")
                break

    def menu_options(self):
       mode = int(input("\n1. View video inventory\n2. View customer's rented videos \n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n\nSelect an option: "))
       return mode

    def return_options(self):
       mode = int(input("What else would you like to do?\n1. View video inventory\n2. View customer's rented videos \n3. Rent video\n4. Return video\n5. Add new customer\n6. to Exit application\nSelect an option: "))
       return mode
    
    def store_inventory(self):
        self.inventory = Interface.get_inventory()
        inventory = self.inventory
        for video in inventory:
            print(video)

    def get_customer_info(self):
        self.customers = Interface.customer_info()
        customer_data = self.customers
        for customer in customer_data:
            print(customer)

    def rent_video(self):
        self.enter_id = input('Enter Customer Id: ')
        # numbers = self.number_of_rentals()

        # self.data_backup()

    def number_of_rentals(self):
        rental_count = 0
        # check_rentals = Interface.get_customer_info()
        with open(customer_path, 'r', newline='') as customer_file:
            customer_info = csv.DictReader(customer_file)
            rental_data = []
            for row in customer_info:
                print(row.current_video_rentals)
                 

            # rental_data = []
            # count_rentals = self.customers
            # for rentals in count_rentals:
            #     rental_data.append(rentals)
            
        # for rentals in self.customers:
        #     if rentals.id == self.customers.id:
        #         num_posts += 1
        #     return num_posts
    

    @classmethod
    def get_inventory(cls):
        with open(inventory_path, 'r', newline='') as video_file:
            inventory = csv.DictReader(video_file)
            video_inventory = []
            for video in inventory:
                videos_in_store = VideoInventory(video['id'], video['title'], video['rating'], video['copies_available'])
                video_inventory.append(videos_in_store)
            return video_inventory

    @classmethod
    def customer_info(cls):
        with open(customer_path, 'r', newline='') as customer_file:
            customer_info = csv.DictReader(customer_file)
            customer_data = []
            for customer in customer_info:
                info = Customer(customer['id'], customer['first_name'], customer['last_name'], customer['current_video_rentals'])
                customer_data.append(info)
            return customer_data