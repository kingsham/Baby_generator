import random,string # 

vowels="aeiouy"    #Varible to hold the vowel letters
consonants="bcdfghjklmnpqrstvwxz" #Variable to hold the consonants
letter= string.ascii_lowercase
letter1=random.choice(string.ascii_lowercase) ###Generates random letters in lowercase only
letter2=random.choice(string.ascii_lowercase)
letter3=random.choice(string.ascii_lowercase)
letter4=random.choice(string.ascii_lowercase)
letter5=random.choice(string.ascii_lowercase)




letter_input_1=input('Choose a letter..."v" for vowels,"c" for consonants,"l" for any other letter:') ### User inputs the corresponding letter to determine where the randomizer will pull from 
letter_input_2=input('Choose a letter..."v" for vowels,"c" for consonants, "l" for any other letter:')
letter_input_3=input('Choose a letter..."v" for vowels,"c" for consonants, "l" for any other letter:')
letter_input_4=input('Choose a letter..."v" for vowels,"c" for consonants, "l" for any other letter:')
letter_input_5=input('Choose a letter..."v" for vowels,"c" for consonants, "l" for any other letter:')



def generator():
    if letter_input_1 == "v":       # if user chooses v then the randomizer will select a letter from the vowels variable
        letter1=random.choice(vowels)

    elif letter_input_1 =="c":              # if the user chooses c then the randomizer will select a letter from consonants variable
          letter1=random.choice(consonants)
    elif letter_input_1 =="l":               # if the user chooses l then the randomizer will select a letter from the letter variable 
          letter1=random.choice(letter)
    else:
          letter1=letter_input_1 .        ### Same process for the remaining inputs

    if letter_input_2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input_2 == "c":
         letter2 = random.choice(consonants)
    elif letter_input_2 == "l":
          letter2 = random.choice(letter)
    else:
          letter2 = letter_input_2

    if letter_input_3 == "v":
          letter3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input_3 == "l":
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3

    if letter_input_4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input_4 == "l":
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input_4

    if letter_input_5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input_5== "c":
        letter5 = random.choice(consonants)
    elif letter_input_5 == "l":
        letter5 = random.choice(letter)
    else:
        letter5= letter_input_5

    name = letter1 + letter2 + letter3 + letter4 + letter5  # This will combine the inputs into one individual name 
    return(name)

for babynames in range(20):  # loops through the entire program to generate 20 random names
    print(generator())


