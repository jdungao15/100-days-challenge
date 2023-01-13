#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/names/invited_names.txt", "r") as names:
    names = names.readlines()

stripped_names = []
for name in names:
    stripped_names.append(name.strip("\n"))

with open("./input/letters/starting_letter.txt", "r") as letter:
    letter_t = letter.readlines()
    print(letter_t)
# letter_template = ''.join(letter_t)

# for name in stripped_names:
#     with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
#         letter.write(letter_template.replace("[name]", name))
# print(letter_template)