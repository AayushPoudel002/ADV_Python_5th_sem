#list knowledge
my_list=[1,2,3,4,5]
# breakpoint() # Set a breakpoint here to inspect 'my_list' variable

# my_list
# [1, 2, 3, 4, 5]
# my_list.append(20) adds element at the end
# my_list
# [1, 2, 3, 4, 5, 20]
# my_list.insert(-1,21) adds element at the second last position
# my_list
# [1, 2, 3, 4, 5, 21, 20]
# my_list.insert(-1,23) adds element at the second last position
# my_list
# [1, 2, 3, 4, 5, 21, 23, 20]
# my_list.reverse() reverses the list
# my_list
# [20, 23, 21, 5, 4, 3, 2, 1]
# my_list.insert(-1,24) adds element at the second last position
# my_list
# [20, 23, 21, 5, 4, 3, 2, 24, 1]
# my_list.sort() sorts the list
# my_list       
# [1, 2, 3, 4, 5, 20, 21, 23, 24]
# my_list.pop(23) removes element at index 23
# *** IndexError: pop index out of range
# my_list.pop(7) removes element at index 7
# 23
# my_list        
# [1, 2, 3, 4, 5, 20, 21, 24]
# my_list.count(5) counts occurrences of 5
# 1
# my_list.count(6) counts occurrences of 6
# 0
# my_list.index(5) finds index of first occurrence of 5
# 4

#Tuple Knowledge
my_tuple=(1,2,3,4,5)


#Learn Dictionary
my_dict={}
breakpoint() # Set a breakpoint here to inspect 'my_dict' variable

# clear() method removes all items from the dictionary
# my_dict.clear()
# copy() method returns a shallow copy of the dictionary
# mydict.copy()
# fromkeys() method creates a new dictionary with keys from iterable and values set to value
# get() method returns the value for the specified key if key is in dictionary
# my_dict.get('key', 'default_value')
# items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
# my_dict.items()
# keys() method returns a view object that displays a list of all the keys in the dictionary
# my_dict.keys()
# pop() method removes the item with the specified key and returns its value
# my_dict.pop('key', 'default_value')
# popitem() method removes and returns the last inserted key-value pair as a tuple
# my_dict.popitem()
# setdefault() method returns the value of a key if it is in the dictionary; if not, it inserts the key with a specified value
# my_dict.setdefault('key', 'default_value')
# update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs
# my_dict.update({'key': 'value'})
# values() method returns a view object that displays a list of all the values in the dictionary
# my_dict.values()
