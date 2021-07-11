
import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
inventory_path = os.path.join(my_path, "../data/inventory.csv")
inventory_backup_path = os.path.join(my_path, "../data/inventory_backup.csv")
customer_path = os.path.join(my_path, "../data/customers.csv")
customer_backup_path = os.path.join(my_path, "../data/customer_backup.csv")


from modules.customer import Customer
from .VideoInventory import VideoInventory

class Interface:    
    def __init__(self):
        pass
        self.inventory = []
        self.customers = []
        self.inventory_backup()
        self.customer_backup()

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

            elif mode == 4:
                self.return_video()
                print(return_menu)
                mode == 0
            
            elif mode == 5:
                self.add_customer()
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
        customer_data = input("Enter customer ID: ")
        rental_data = []
        for customer in self.customers:
            if customer.id == customer_data:
                rental_data = customer.current_video_rentals.split('/')
                rented = ", ".join(rental_data)
                print(f"\n--------------------\n\nMember ID: {customer.id}\nCustomer: {customer.first_name} {customer.last_name}")
                print(f"Active rentals: {rented}\n\n--------------------\n")

    def rent_video(self):
        self.rent = Interface.customer_info()
        self.store_inventory()
        rental_number = 0
        rental_data = []
        customer_data = input("Enter customer ID: ")
        for customer in self.rent:
            if customer.id == customer_data:
                rental_data = customer.current_video_rentals.split('/')
                rented = ", ".join(rental_data)
                rental_number = len(rental_data)
                rental_info = print(f"\nMember ID: {customer.id}\nCustomer: {customer.first_name} {customer.last_name}\nCurrent rentals: {rented}\nActive number of rentals: {rental_number}")
                
                if rental_number == 3:
                    print(f"\n* Notify customer to return videos first \n\n--------------------\n")

                else:
                    movie_id = (input("Enter movie by title: "))
                    for index, movie in enumerate(self.inventory):
                        if movie_id == index+1:
                            if rental_data == ['']:
                                rental_data.append(movie.title)
                                customer.current_video_rentals = "".join
                            else:
                                rental_data.append(movie.title)
                                customer.current_video_rentals = "/".join(rental_data)
                                checkout = int(movie.copies_available) - 1
                                movie.copies_available = checkout
                    print(f"\n----- Please return in 3 days to avoid late fees -----\n")
                    self.update_customers()
                    # self.update_inventory()
    
    def update_customers(self):
        with open(customer_path, 'w') as update_customers:
            update = csv.writer(update_customers)
            inventory = []
            for customer in inventory:
                customer_update = (Customer(customer['id'], customer['first_name'], customer['last_name'], customer['current_video_rentals']))
                inventory.append(customer_update)
                return inventory


    # def update_inventory(self):
        
    
    def inventory_backup(self):
        with open(inventory_backup_path, 'r', newline='') as video_file:
            inventory = csv.DictReader(video_file)
            video_inventory = []
            for video in inventory:
                videos_in_store = VideoInventory(video['id'], video['title'], video['rating'], video['copies_available'])
                video_inventory.append(videos_in_store)
            return video_inventory
    
    def customer_backup(self):
        with open(customer_path, 'r', newline='') as customer_file:
            customer_info = csv.DictReader(customer_file)
            customer_data = []
            for customer in customer_info:                
                info = Customer(customer['id'], customer['first_name'], customer['last_name'], customer['current_video_rentals'])
                customer_data.append(info)
            return customer_data
                   
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