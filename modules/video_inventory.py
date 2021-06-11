import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
video_path = os.path.join(my_path, "../assessment-2/data/inventory.csv")

# class method calls itself outputs a list inventory of objects with key/values of the inventory
# 

class Video_Inventory:
    
    def __init__(self):
      pass
      # self.movie_list = []

    @classmethod
    def inventory_list(cls):
      inventory = []
      with open(video_path, 'r') as csvfile:
        inventory = csv.DictReader(csvfile)
        for row in inventory:
          movies = Video_Inventory(row['title'], row['rating'], row['copies_available'])
          inventory.append(movies)
      return inventory

    def __str__(self):
      return f"Title: {self.title} Rating: {self.rating} Copies in store: {self.copies}"