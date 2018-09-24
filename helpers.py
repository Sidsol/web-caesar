def alphabet_position(letter):
    #funtion will convert letters to lowercase then return the ordinal value
    lower_letter = letter.lower()
    ord_alpha = ord(lower_letter) % 97

    return ord_alpha

def rotate_character(char, rot):
    alphabet_L= 'abcdefghijklmnopqrstuvwxyz'
    alphabet_U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot_str = ''
    #Checks if character is a special character, if it is return char without modifying it
    if char.isalpha() != True:
        rot_str = char
    #Checks if character is lower case
    elif char.islower() == True:
        #this will set take the ordinal value of the passed in char, and add the value of rot to it.
        rotated_index = alphabet_position(char)+ rot
        #if statement will check if the value of rotated_index is less than 26
        if rotated_index < 26:
            #if less than 26 get the value from alphabet_L[rotated_index] and add it to rot_str
            rot_str = alphabet_L[rotated_index]
            #Else modulo the rotated_index by 26 to reset the positioning
        else:
            rot_str = alphabet_L[rotated_index % 26]
    else:
        #this will do the same as the code above but for uppercase characters instead of lower case
        rotated_index = alphabet_position(char)+ rot
        if rotated_index < 26:
            rot_str =  alphabet_U[rotated_index]
        else:
            rot_str = alphabet_U[rotated_index % 26]
    
    return rot_str