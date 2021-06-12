import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
video_path = os.path.join(my_path, "../data/inventory.csv")

# class method calls itself outputs a list inventory of objects with key/values of the inventory
# 

class Video_Inventory:

    # def __init__(self):
    #     pass
    
    def __init__(self, **video):#,title,rating,copies_available
        self.video = video
        # print(len(self.video))
        # self.title = title
        # self.rating = rating
        # self.copies_available = copies_available
        

    # @classmethod
    # def list_inventory(cls):
    #   with open(video_path, 'r') as video_file:
    #     inventory = csv.DictReader(video_file)
    #     video_list = []
    #     for video in inventory:   
    #       video_list.append(video)# list of dicts     
    #       entries = Video_Inventory(**video)
    #     print(video)
    #     return f"Title: {video_list[0]['title']}\nRating: {video_list[0]['id']}\nCopies in store: {video_list[0]['copies_available']}"



    @classmethod
    def list_inventory(cls):
      with open(video_path, 'r') as video_file:
        inventory = csv.DictReader(video_file)
        video_list = []

        for video in inventory:  
        #     print (f"\nTitle: {video['title']}\nRating: {video['rating']}\nCopies in Store: {video['copies_available']}"

        # video_list.append(video)# list of dicts     
        
          entries = Video_Inventory(**entries)

        # print(video)
        # return f"Title: {video_list[0]['title']}\nRating: {video_list[0]['id']}\nCopies in store: {video_list[0]['copies_available']}"

          # for key in video:
          #   print(key) 
          # print(entries)
          # return entries
          # cls.video_list = Video_Inventory(f"ID: {video['id']}, {video['id']},{video['id']}")
          # print(cls.video_list)

    def __str__(self):
        for i in len(self.video):
          return f"ID: {videos[i]['id']}\nTitle: {videos[i]['title']}\nRating: {videos[i]['id']}\nCopies in store: {videos[i]['copies_available']}"



videos = Video_Inventory()
print(videos.list_inventory())


# with open('names.csv', newline='') as csvfile:
# ...     reader = csv.DictReader(csvfile)
# ...     for row in reader:
# ...         print(row['first_name'], row['last_name'])
   


    # @classmethod
    # def get_all_users_from_db(cls):
    #   with open(user_path, 'r') as users_file:
    #     users = csv.DictReader(users_file)
    #     users_list = []
    #     for user in users:
    #       if user['tier'] == 'p':
    #         premium_user = PremiumUser(user['name'], user['email_address'], user['driver_license'])
    #         users_list.append(premium_user)
    #       else:
    #         free_user = FreeUser(user['name'], user['email_address'], user['driver_license'])
    #         users_list.append(free_user)
    #     return users_list


    # def __str__(self):
    #   return f"Title: {self.title} Rating: {self.rating} Copies in store: {self.copies}"