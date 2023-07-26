# Made on 19.5.2023. Inspired by Codezilla YouTube channel tutorial
# Takes a string then search for vowels to replace them with 'X' and Prime numbers '12357' with 'Prime'

def translator(str):
    translation = ''
    for letter in str:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'X'
            else:
                translation = translation + 'x'
        elif letter in '12357':
            translation = translation + 'Prime'
        else:
            translation = translation + letter
    return translation


print(translator(input('Enter a phrase: ')))