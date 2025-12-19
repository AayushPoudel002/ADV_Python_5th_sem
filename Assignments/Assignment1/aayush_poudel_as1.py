#Variables and inputs
my_age = 21
print("My age is:",my_age)

fav_food=input("Enter you Favourite Food:")
print("His Favourite Food is:",fav_food)


# Type Conversion

String="42"
integer=int(String)

print("string convereted to integer:",integer)

float_value=3.14159
String2=str(float_value)

print("Float Converted to string:",String2)


#Strings

str1="Hello"
str2="World!"
print(str1+str2)


#Use String indexing to extract the third character from string "Python"
str3="Python"
third_char = str3[2]
print("Third character in",str3,"is",third_char)

#take a sentence as input adn display only the first five words

sentence = input("ENter a long sentence more than 5 words:")
"I am Aayush and I am 20 yeard old"
"I" "am" "Aayush" "and" "I" "am" "20" "yrs" "old"
print(sentence)
words = sentence.split() #words store the splitted words from the sentence
five_words = " ".join(words[:5])#joins the first five words where words[:5] extracts first five words where : indicates from start to index 5 (not inclusive)
print(five_words)
