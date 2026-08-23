#Program 33: Programs with favourites
# Favourite Movies
movies = input("Enter your favorite movies separated by commas: ").split(",")
print("You entered:", movies)
#Sort Favourites Alphabetically
movies = input("Enter your favorite movies separated by commas: ").split(",")
print("You entered:", movies)
#Search favouritew Items
favorites = ["pizza", "burger", "pasta", "icecream"]
item = input("Enter an item to search: ")
if item.lower() in favorites:
    print(item, "is in your favorites!")
else:
    print(item, "is not in your favorites.")
#Count Favourites
favorites = input("Enter your favorite songs separated by space: ").split()
print("You have", len(favorites), "favorite songs!")
#Random Favourites Picker
import random
favorites = input("Enter your favorite foods separated by space: ").split()
print("Today’s choice:", random.choice(favorites))

