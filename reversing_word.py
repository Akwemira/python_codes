#This program will ask the user for a word and will output the reverse of the word
#Then will display on the screen: Your word is: word, and the reverse is: reverse_word. 

word = input("Give me a word\n\n")
reverse_word = word[::-1]
print("\n")
print(f"Your word is: {word}, and the reverse is: {reverse_word}")
