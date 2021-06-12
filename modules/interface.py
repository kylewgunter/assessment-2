# Create interface with multiple options
# 1. view video inventory = list of current videos in store init video inventory module
# 2. view rentals initiate a list of current rentals per customer
# 3. rent video module iterates over video list in store and decrements with a match of title and pops off list?
# if title has 0, runner throws an exception 
# 4. return module increments value dict for match
# 5. add a new customer adds customer to database and assigns an id number that isnt in database already
# 6 exit



from .video_inventory import Video_Inventory
from .customer import Customer

class Interface:

    def __init__(self):
        pass

    def run(self):
        while True:
            print("\n----- Welcome to Code Platoon Video! ----\n")
            print("Please select one of the following options")
            mode = input("\n1. View video inventory\n2. View customer's rented videos \n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n\nSelect an option: ")

            if mode == '1':
                list_inventory = Video_Inventory()
                return list_inventory
            elif mode == '2':
               view_rentals = Customer.objects()

            # elif mode == '3':
            # #    rent_video = rent()

            elif mode == '6':
                print("\n--- Goodbye! ---")
                return
