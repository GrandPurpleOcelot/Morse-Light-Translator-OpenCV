import re

def space_estimator(input_string) -> list:
    space_lengths = []
    space_counter = 0

    for i in input_string[1:]: # first itteration is alway a non-space character, so skip the first element
        if i == ' ':
            space_counter += 1
        else:
            space_lengths.append(space_counter)
            space_counter = 0

    return space_lengths


def morse_cleaner(decoded_list) -> str:
    decoded_string = ''.join(decoded_list).strip()

    while len(decoded_string) > 60:
        try:
            space_lengths = space_estimator(decoded_string)

            min_space = min(space_lengths) # this is the space between each dit-dah
            #any length above this is the space between each morse letter

            max_space = max(space_lengths) # large space suggest space between words

            ''' 
            this section describes morse code generation using the morse code timing
            Dit: 1 unit
            Dah: 3 units
            Intra-character space (the gap between dits and dahs within a character): 1 unit
            Inter-character space (the gap between the characters of a word): 3 units
            Word space (the gap between two words): 7 units
            '''
            dit_dah = ''
            space_counter = 0
            for i in decoded_string:
                if i != ' ':
                    dit_dah += i
                    space_counter = 0
                else:
                    space_counter += 1
                    if space_counter / min_space >= (max_space-1) / min_space :
                        dit_dah += ' _ '
                    elif space_counter > min_space + 2:
                        dit_dah += ' '
                    else:
                        pass

            clean_morse_code = re.sub(' +', ' ', ''.join(dit_dah)).strip()

            return clean_morse_code
            break
        except ValueError:
            print("Morse sequence is too short!")
            pass

# test_case = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', '.']
# print(morse_cleaner(test_case))