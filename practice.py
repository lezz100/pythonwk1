x = {}
x[2] = 10
x[1] = [20,30,40]
print(x[1][2])

#WEEKLY CODING CHALLENGE
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

def get_integer_list():
  """Prompts the user for integers and returns a list of integers."""
  integer_list = []
  while True:
    user_input = input("Enter an integer (or 'q' to quit): ")
    if user_input.lower() == 'q':
      break
    try:
      integer = int(user_input)
      integer_list.append(integer)
    except ValueError:
      print("Invalid input. Please enter an integer.")
  return integer_list

def calculate_sum(integer_list):
  """Calculates the sum of all integers in the list."""
  total_sum = 0
  for num in integer_list:
    total_sum += num
  return total_sum

def main():
  """Gets user input, calculates the sum, and prints the result."""
  integer_list = get_integer_list()
  if integer_list:  # Check if the list is not empty
    total_sum = calculate_sum(integer_list)
    print(f"The sum of the integers is: {total_sum}")
  else:
    print("No integers were entered.")

if __name__ == "__main__":
  main()

# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
# Create a tuple of book names
favorite_books = ("A Hitchhiker's Guide to the Galaxy", "The Martian", 
                  "Pride and Prejudice", "The Lord of the Rings", 
                  "Dune")

# Print each book name on a separate line using a for loop
for book in favorite_books:
  print(book)

# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
def get_person_info():
  """Prompts the user for personal information and returns a dictionary."""
  person_info = {}
  person_info["name"] = input("Enter your name: ")
  person_info["age"] = int(input("Enter your age: "))
  person_info["favorite_color"] = input("Enter your favorite color: ")
  return person_info

def main():
  """Gets person information, stores it in a dictionary, and prints it."""
  person_info = get_person_info()
  print("Person Information:")
  for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")  # Capitalize the first letter of the key

if __name__ == "__main__":
  main()

# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

def get_integer_set(message):
  """Prompts the user for integers and returns a set of integers."""
  integer_set = set()
  while True:
    user_input = input(f"Enter integers for set {message} (or 'q' to quit): ")
    if user_input.lower() == 'q':
      break
    try:
      integer = int(user_input)
      integer_set.add(integer)
    except ValueError:
      print("Invalid input. Please enter integers separated by spaces.")
  return integer_set

def find_common_elements(set1, set2):
  """Finds the common elements between two sets and returns a new set."""
  return set1.intersection(set2)  # Use set intersection method

def main():
  """Gets user input for sets, finds common elements, and prints the result."""
  set1 = get_integer_set("1")
  set2 = get_integer_set("2")
  common_elements = find_common_elements(set1, set2)
  if common_elements:
    print("Common elements in both sets:", common_elements)
  else:
    print("There are no common elements between the sets.")

if __name__ == "__main__":
  main()
