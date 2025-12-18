my_list = [1,2,3,4]

for index, value in enumerate(my_list):
    print(f"Index:{index}, Value:{value}")

my_list1=[5,6,7,8,9]

for a in zip(my_list, my_list1): #zip function is used to combine two lists that are of same length and discard the remaining elements of longer list
    print(a)

str1="Advanced|Python|Programming|Course"
str1.split("|") #split function is used to split a string based on a delimiter and return a list of substrings in tuple form
print(str1.split("|"))

str2 = "dlrow nohtyp"
print(str2[::-1])  #slicing to reverse a string ::-1 reverses the string
#str2.reverse() #This will give error as strings are immutable in Python
#str2[::-1] in this ::-1 indicates step value, meaning to take characters from the end to the start, effectively reversing the string.




input = "nohtyp dlrow"
#convert nohtyp dlrow into python world using slicing keeping python in front and world at the back
word1 = input[0:5]  #slice to get 'python'   
word2 = input[6:12] #slie to get 'world'
print(word1[::-1],word2[::-1]) #seperating using input[0:5] does the job but not a good practice

#better way is to split the string first and then reverse each word
words = input.split() #splitting the string into words based on space
reversed_words = [word[::-1] for word in words] #reversing each word using list comprehension
result = ' '.join(reversed_words) #joining the reversed words back into a single string 
print("rersed word in list=",reversed_words)
print("Joint word using .join(reversed word)=",result)

#to do in lenghty way using loops
for element in input.split():
    temp = element[::-1]
    print(temp,end=" ")

#DEFINING A FUNCTION
def example_fucntion():
    print("This is an example function")
    local_variable = "i am local variable"
    print(local_variable)

example_fucntion()
#print(local_variable) #this will give error as local_variable is not defined outside the function

def outer_funtion():
    outer_variable="i am outer nonlocal non modified variable"
    print(outer_variable) # printing outer variable before modification in inner function

    def inner_function():
        nonlocal outer_variable #to modify the outer variable inside inner function we use nonlocal keyword
        outer_variable="i am modified outer variable"
        print(outer_variable) # printing modified outer variable
    
    inner_function()
    print(outer_variable) # printing outer variable after modification in inner function
    #once modified the outer_variable will retain its modified value even outside the inner function

outer_funtion()
#print(outer_variable) #this will give error as outer_variable is not defined outside the outer_function


#Comment in python is done using # for single line comment and ''' ''' or """ """ for multi line comments
'''This is a multi line comment
in python '''
"""This is another way of writing multi line comment
in python"""
#shortcut key for commenting multiple lines in python is CTRL + / and uncommenting is the same shortcut key

#Pass statement in python is used as a placeholder for future code
def placeholder_function():
    pass #this function does nothing for now


# def my_function():
#     print("Before continue")
#     continue
#     print("After continue") #this will give syntax error as continue cannot be used outside a loop
# my_function()
    