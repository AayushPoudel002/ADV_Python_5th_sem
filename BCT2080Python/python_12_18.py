import math ; print (math.sqrt(16))  #importing math module and using sqrt function to calculate square root of 16
import random; print(random.randint(1,10) ) #importing random module and using randint function to generate a random integer between 1 and 10
import datetime; print(datetime.datetime.now()) #importing datetime module and using datetime class to get current date and time
import os; print(os.getcwd()) #importing os module and using getcwd function to get current working directory
import json; data = {'name': 'John', 'age': 30}; json_str = json.dumps(data); print(json_str) #importing json module and using dumps function to convert dictionary to JSON string
import sys; print(sys.version) #importing sys module and using version attribute to get Python version

# Exception handling examples
try:
    print(4/0)  #this will raise ZeroDivisionError
except Exception as e: #except ZeroDivisionError as e:
    print(f"An error occurred: {e}")  #catching the exception and printing the error message




num = int(input("Enter an index to access in the list (0-2): "))
try:
    my_list = [1, 2, 3]
    print(my_list[num])  #this will raise IndexError if num out of range
except Exception as e: #except IndexError as e:
    print(f"An error occurred:{e}") #catching the exception and printing the error message
else:
    print("No exceptions occurred.")  #this block will execute if no exception occurs
finally:
    print("Execution completed.")  #this block will always execute regardless of exception

age=16

try:
    if age<18:
        raise ValueError("Age must be at least 18.")  #raising ValueError if age is less than 18
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")  #catching the exception and printing the error message
except ValueError as ve: #ValueError is when a function gets argument of correct type but inappropriate value
    print(f"Value error: {ve}")  #catching the ValueError and printing the error message
except NameError as ne: #NameError is when a variable is not defined
    print(f"Name error: {ne}")  #catching the NameError and printing the error message
except Exception as e: #catching any other exception
    print(f"An unexpected error occurred: {e}")  #catching any other exception and printing the error message
else:
    print("No exceptions occurred.")  #this block will execute if no exception occurs
finally:
    print("Execution completed.")  #this block will always execute regardless of exception


#File handling example
with open("example.txt", "w") as file:  #using with statement to open a file in write mode
    file.write("Hello, World!")  #writing to the file
    file.write("\nWelcome to File Handling in Python.")
    file.write("\nThis is an example file.")
    #data = file.read()  #this will raise an error as file is opened in write mode
    #print(data)  #this line will not execute as above line raises error

with open("example.txt", "r") as file:  #using with statement to open a file in read mode
    data = file.read()  #reading from the file
    print(data)  #printing the data read from the file

#r:read mode (default mode)
#w:write mode
#a:append mode
#b:binary mode (mostly used for non-text files like images, audio, etc.)
#rb:read binary mode
#wb:write binary mode
#ab:append binary mode
#x:exclusive creation mode (used mostly in binary files for creating new files without overwriting existing files)
with open("example.txt", "a") as file:  #using with statement to open a file in append mode
    file.write("\nAppending new line to the file.")  #appending to the file