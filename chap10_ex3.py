'''“Exercise 3: Write a program that reads a file and prints the letters in 
decreasing order of frequency. Your program should convert all the input to 
lower case and only count the letters a-z. Your program should not count spaces, 
digits, punctuation, or anything other than the letters a-z. Find text samples 
from several different languages and see how letter frequency varies between 
languages. Compare your results with the tables at 
https://wikipedia.org/wiki/Letter_frequencies.”
'''

# dictionary to count the letters
letter_count = {}
#open file
#fhand = open('mbox-short.txt')
file_name = input('Enter the name of the file, please include the file format: ')
try:
    fhand = open(file_name)

except FileNotFoundError:
    print('File "'+ file_name +'" could not be found. Please try again')
    quit()

# read the file
read_text_file = fhand.read()

#iterate through each charatacter in the file
for char in read_text_file:
    #check if the character is a letter
    if char.isalpha():
        #convert all letters to lower-case
        char = char.lower()

        #update letter in the dictionary
        letter_count[char] = letter_count.get(char, 0)+1


sorted_letter_count = sorted(letter_count.items(), key = lambda item: item[1], reverse = True)

'''
lst =list()
#print the results
for key, value in list(letter_count.items()):
    lst.append((key,value))
lst.sort(reverse = True)'''

print(lst[2])
for key, value in sorted_letter_count:
    print(key, value)
    
