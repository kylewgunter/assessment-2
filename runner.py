# Write your solution here!
# ---- TEST CRITERIA
# Your Video Inventory Management application should manage the following data:
# - Manage customer information:
#   - customer id
#   - first name
#   - last name
#   - current list of video rentals (*by title*)
# - Manage the store's video inventory:
#   - video id
#   - video title
#   - video rating
#   - number of copies currently available in-store

# --- MENU
# Your menu should look something like this: 
# ```
# Welcome to Code Platoon Video!
# 1. View video inventory
# 2. View customer's rented videos
# 3. Rent video
# 4. Return video
# 5. Add new customer
# 6. Exit
# ```

# PSEUDO CODE
# classes - customer base class - 
# instance - add new customer - id - name
# takes in name and reads over customer database and appends with a new id that isnt in database
# 
# 1. view video inventory


# modules - view store inventory - rent video - return video
# 



# Classes

import csv
import os.path

class Customer:

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
        pass
    
    # Takes in name, read over database and add new customer info with new id

    def add_new_customer(self):
        my_path = os.path.abspath(os.path.dirname())
        path = os.path.join(my_path, "./data/customers.csv")

        with open(path, 'a', newline= '') as csvfile:
            new_customer_csv = csv.writer(csvfile, delimiter=',')
            new_customer_csv.writerow(['name', 'age', 'role', 'school_id', 'password'])
            for student in self.students:
                student_csv.writerow([student.name, student.age, student.role, student.school_id, student.password])



        # self.first, self.last
        # self.id = id


# ----------------------------------
class Interface:

    def __init__(self):
        pass

    def run(self):
        pass
    while True:
        mode = input(self.menu())
        
        if mode == '1':
            # school.list_students()
        elif mode == '2':
            # student_id = input('Enter student id:')
            # student_string = str(school.find_student_by_id(student_id))
            # print(student_string)
        elif mode == '3':
            # student_data = {'role':'student'}
            # student_data['name']      = input('Enter student name:\n')
            # student_data['age']       = input('Enter student age: \n')
            # student_data['school_id'] = input('Enter student school id: \n')
            # student_data['password']  = input('Enter student password: \n')
            
            # school.add_student(student_data)
        elif mode == '4':
            # student_id = input("Please enter the student's id:\n")
            # school.delete_student(student_id)
        elif mode == '5':
            break 

    def main_menu(self):
        print("----- Welcome to Code Platoon Video! ----\n")
        print("\nPlease select one of the following options\n")

# ----------------------------------

# Modules


        