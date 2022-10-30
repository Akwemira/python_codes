#write program to ask for reverse of a word
#Display on the screen: Your word is: word, and the reverse is: reverse_word. 
#Leverage methods:split,join and reversed
word = input("Give me a word\n\n")
reverse_word = word[::-1]
print("\n")
print(f"Your word is: {word}, and the reverse is: {reverse_word}")
