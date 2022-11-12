# This dictionary will contain 2 dictionaries:
# 1 dictionary with french words as key & their english equivalent as values
# Another dictionary with english woirds as key & their french equivalent as values
# "word does not exist" will be printed if user input word not in both dictionaries

dictionary = {
    "french-to-english" : {
    "prune" : "african plum",  
    "belle" : "pretty", 
    "eglise" :"church",
    "meilleur" : "best",
    "frère" : "brother",
    "maman" : "mother"
},
"english-to-french" : {
    "african plum" : "prune",
    "pretty" : "belle",
    "church" : "eglise",
    "best" : "meilleur",
    "brother" : "frère",
    "mother" : "maman"
    }
}

input_word = input("Give me a word in French or English\n").lower() #word from user set to lowercase
french_to_english = dictionary["french-to-english"].get(input_word)
english_to_french = dictionary["english-to-french"].get(input_word)
if french_to_english:
    print(f"The English equivalent is {french_to_english}")
elif english_to_french:
    print(f"The French equivalent is {english_to_french}")
else:
    print(f"Your word does not exist in this dictionary")
