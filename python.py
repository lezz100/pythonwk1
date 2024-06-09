class Person:
  """
  A class representing a person with attributes for name, age, and gender.
  """

  def __init__(self, name, age, gender):
    """
    Initializes a Person object with the given name, age, and gender.

    Args:
        name (str): The person's name.
        age (int): The person's age.
        gender (str): The person's gender.
    """

    self.name = name
    self.age = age
    self.gender = gender

# Example usage
person1 = Person("Alice", 30, "Female")
person2 = Person("Bob", 25, "Male")

print(f"Person 1: {person1.name}, {person1.age}, {person1.gender}")
print(f"Person 2: {person2.name}, {person2.age}, {person2.gender}")
