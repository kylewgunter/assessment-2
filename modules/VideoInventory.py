import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
inventory_path = os.path.join(my_path, "../data/inventory.csv")

# class method calls itself outputs a list inventory of objects with key/values of the inventory
# 

class VideoInventory:
  
  def __init__(self,id,title,rating,copies_available):
    self.id = id
    self.title = title
    self.rating = rating
    self.copies_available = copies_available

  @classmethod
  def get_inventory(cls):
    with open(inventory_path, 'r', newline='') as video_file:
      inventory = csv.DictReader(video_file)
      video_inventory = []
      for video in inventory:
        videos_in_store = VideoInventory(video['id'], video['title'], video['rating'], video['copies_available'])
        print(video_inventory)
        video_inventory.append(videos_in_store)
      return video_inventory

  def __str__(self):
    return f"ID: {self.id}\nTitle: {self.title}\nRating: {self.rating}\nCopies in Store: {self.copies_available}\n--------------------\n"

