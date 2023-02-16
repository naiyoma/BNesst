# def shout(text):
#     return text.upper()

# def shout(text):
# 	return text.upper()

# def whisper(text):
# 	return text.lower()

# def greet(func):
#     def inner_function():
#         print("Hello, ")
#         check_values = func(*args)
#         return check_values
#     return inner_function

# def say_hello():
#     print("wow today is great")


# greeting = greet(say_hello)
# greeting()

# def greet(func):
#     def inner_function(*args):
#         print("Hello, ")
#         check_values = func(*args)
#         return check_values
#     return inner_function

# def say_hello():
#     print("wow today is great")


# greeting = greet(say_hello)
# greeting()

    

# def authorize(func):
#     def wrapper(*args):
#         if check_authorize():
#             return func(*args)
#         return "Unauthorized Access"
#     return wrapper

# def check_authorize():
#     user_input = int(input("enter a number"))
#     if user_input:
#         return True
#     else:
#         return False

# @authorize
# def secret_data():
#     if check_authorize:
#         print("this is confidential data")

# secret_data()

# def validate(func):
#     def wrapper(*args):
#         for arg in args:
#             # import pdb; pdb.set_trace()
#             if not str(arg).isnumeric():
#                 return "Error: Arguments must be integers."
#         return func(*args)
#     return wrapper

# @validate
# def add_numbers(*args):
#     return sum(args)

# print(add_numbers(1, 2, 3))
# print(add_numbers(1, 2, "3"))


# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#             return False
#         return True
#     else:
#         return False

# def prime_numbers(n):
#     count = 0
#     num = 2
#     while count < n:
#         if is_prime(num):
#         yield num
#         count += 1
#         num += 1

# prime_generator = prime_numbers(10)
# print(list(prime_generator))

# def is_prime(num):
#     if num < 2:
#         return False
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#             else:
#                 return True


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def prime_numbers(n):
#     total = 0
#     num = 2
#     while total < n:
#         if is_prime(num):
#             yield num
#             total= total +  1
#             num = num + 1

# prime_generator = prime_numbers(10)
# print(list(prime_generator))


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def prime_numbers(n):
#     total = 0
    # num = 2
#     while total < n:
#         if is_prime(num):
#             yield num
#             total += 1
#         num += 1

# prime_generator = prime_numbers(10)
# print(list(prime_generator))


# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([ k for i in lists for k in i])

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# print([(i,k) for i in list1 for k in list2])
# import re
# validate_phone_number_pattern = "^([1-9][0-9]{2})([0-9]{3})([0-9]{4})$"
# phone_number = "123-456-7890"
# match = re.search(validate_phone_number_pattern, phone_number)
# print(match)
# formatted_phone_number = "{}-{}-{}".format(match.group(1), match.group(2), match.group(3))
# print("Match found:", formatted_phone_number)
# import re
# text = "hello world"
# text_pattern = "^\w+\s+\w+$"
# try:
#     match = re.search(text_pattern, text)
#     print("Match:", text)
# except:
#   print("No Match.")


# 1. Create methods in a class: 
# In the Person class, add methods like introduce() and greet().
# The introduce() method should print a brief introduction about the person
# and the greet() method should print a friendly greeting.


# Inheritance: Create a subclass called Student that inherits
#  from the Person class. Add a new attribute called university
#   to the Student class and initialize it in the constructor. 
#   Also, override the introduce() method
#    to include information about the student's university.


# class Person:
#     def __init__(self, first_Name, last_Name):
#         self.first_Name = first_Name
#         self.last_Name = last_Name
    
#     def introduce(self):
#         print("hello", self.first_Name)
    
#     def greet(self):
#         print(self.last_Name, "this is a friendly lace")

# class Student(Person):
#     def __init__(self, first_Name, last_Name, uni):
#         super().__init__(first_Name, last_Name)
#         self.university = uni
#     def introduce(self):
#         print("Hello", self.first_Name, "you are in", self.university)

# # p = Person("Mona", "Lisa")
# # p.introduce()
# # p.greet()
# s = Student("Lina", "Tina", "UNI_India")
# s.introduce()


# 5. Class Variables: 
# Define a class BankAccount with a class variable bank_name and instance variables account_holder_name, 
# balance. Initialize the class variables in the constructor and add methods like deposit() and withdraw() 
# to perform transactions. Create two instances of the BankAccount class and verify that the class variable is 
# shared among all instances.

# class BankAccount:
#     def __init__(self, bank_name, account_holder_name, balanace):
#         self.bank_name = bank_name
#         self.account_holder_name = account_holder_name
#         self.balance = balanace
    
#     def deposit(self, user_amount):
#         self.balanace = self.balance +user_amount
    
#     def withdraw(self, user_amount):
#         self.balance = self.balanace-user_amount


# BA = BankAccount("ABSA", "jOHN", 5000)
# BA.deposit(300)
# BA.withdraw(100)

# print(BA.balanace)

# 2. Write a lambda function that takes a list of dictionaries
#  and returns a new list of dictionaries sorted by a specified key.


# dict = [
#     {"STUDENT": "Kenya", "GPA":3.5 },
#     {"STUDENT": "KIANA", "GPA":4.5 },
#     {"STUDENT": "TINA", "GPA":3.6 },
    
# ]

# print(sorted(dict, key=lambda x: x['GPA']))


# animals = ['dog', 'cat']

# animals = list(map(lambda animal: animal.capitalize(), animals))

# print(animals)


students= [{"STUDENT": "Kenya", "GPA": 3.5},    {"STUDENT": "KIANA", "GPA": 4.5},    {"STUDENT": "TINA", "GPA": 3.5},]

filtered_data = filter(lambda x: x['GPA'] > 3.6, students)
print(list(filtered_data))