import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
inventory_path = os.path.join(my_path, "../data/inventory.csv")

# class method calls itself outputs a list inventory of objects with key/values of the inventory
# 

class VideoInventory:
  all_movies = []
  
  def __init__(self,id,title,rating,copies_available):
    self.id = id
    self.title = title
    self.rating = rating
    self.copies_available = copies_available
    # self.user_posts = []

  @classmethod
  def get_inventory(cls):
        with open(inventory_path, 'r') as movie_file:
            inventory = csv.DictReader(movie_file)
            movies_list = []
        for movie in inventory:
            movies_in_store = VideoInventory(movie['title'], movie['rating'], movie['copies_available'])
            movies_list.append(movies_in_store)
        return movies_list

  @classmethod
  def get_all_posts(cls):
    with open(path, 'r') as posts_file:
      posts = csv.DictReader(posts_file)
      posts_list = []
      for post in posts:
        new_post = Post(post['user_id'], post['title'], post['body'])
        posts_list.append(new_post)
      return posts_list
