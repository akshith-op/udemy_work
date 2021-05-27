#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()
    with open("Input/Letters/starting_letter.txt", 'r') as letter:
        letter_contents = letter.read()
        for i in name_list:
            stripeed = i.strip()
            new_letter = letter_contents.replace("[name]", stripeed)
            print(new_letter)
            with open(f"./Output/ReadyToSend/letter_for{stripeed}.txt", 'w') as invite:
                invite.write(new_letter)