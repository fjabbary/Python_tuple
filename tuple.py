# ================== Task 1 ===================
def flight_itinerary(list_of_tuples):
    for index, item in enumerate(list_of_tuples):
      print(f"Itinerary {index + 1}: {item[0]} - From {item[1]} to {item[2]}")

flight_itinerary([("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("John Doe", "Sacramento", "Chicago")])


# ================== Task 2 ===================
# list has initial values
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def manage_library(book_library):
  while True:
    action = input("Enter add book or quit ")
    if action == "add book":
      book_title = input("Enter the title of the book: ").strip()
      author = input("Enter the author's: ").strip()
      my_tuple = (book_title, author)
    
      if my_tuple not in book_library:
        book_library.append(my_tuple)
        print(book_library)
      else:
        print(f"tuple {my_tuple} already exist" )  
        
    elif action == "quit":
      break
  
  return book_library
  
  
print(manage_library(library))

# ================== Task 3 ===================

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Michael", "chair", 7),
]

def display_orders(customers_orders):
  for order in customers_orders:
    customer, product_name, quantity = order
    print(f"{customer} ordered {quantity} {product_name}(s)")
  
display_orders(orders)