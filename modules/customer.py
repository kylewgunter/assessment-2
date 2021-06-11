
import csv
import os.path

class Customer:

    def __init__(self, id,first_name,last_name,current_video_rentals):
        self.id = id
        self.first = first_name
        self.last = last_name
        self.current_rentals = current_video_rentals
        # self.current_rentals = current_video_rentals

    @classmethod
    def objects(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../assessment-2/data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(row)
                # customers.append(Customer())
                # print(row)
                # print(dict(row))
        return customers

    def print_customer_rentals(self):
        print(f"Customer {self.first_name} ID:{self.id}, currently has these rentals: {self.current_rentals}")

        

# all_customers = Customer.objects()
# print(all_customers)