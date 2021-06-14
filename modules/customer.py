import csv
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
customer_path = os.path.join(my_path, "../data/customers.csv")


class Customer:
    def __init__(self,id,first_name,last_name,current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    @classmethod
    def customer_info(cls):
        with open(customer_path, 'r', newline='') as customer_file:
            customer_info = csv.DictReader(customer_file)
            customer_data = []
            for customer in customer_info:
                data = Customer(customer['id'], customer['first_name'], customer['last_name'], customer['current_video_rentals'])
                print(customer_data)
                customer_data.append(data)
            return customer_data

    def __str__(self):
        return f"ID: {self.id}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nCurrent Rentals: {self.current_video_rentals}\n--------------------\n"


    # @classmethod
    # def customer_rentals(cls):
    #     customers = []
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../data/customers.csv")
    #     with open(path) as csvfile:
    #         reader = csv.DictReader(csvfile)










    # def run(self, id,first_name,last_name,current_video_rentals):
    #     self.id = id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.current_rentals = current_video_rentals
    #     # self.current_rentals = current_video_rentals

              
            # for customer in reader:
            #     customers.append()
            #     print

                # print(f"ID: {customer['id']}\nName: {customer['first_name']},{customer['last_name']}\nRentals: {customer['current_video_rentals']}\n-------------\n")

                # id,first_name,last_name,current_video_rentals

        # for entries in enumerate(customers):
        #     print(entries)


    # def print_customer_rentals(self):
    #     print(f"Customer {self.first_name} ID:{self.id}, currently has these rentals: {self.current_rentals}")