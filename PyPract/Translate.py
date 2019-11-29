def translate(word):
    translation = ''
    for letter in word:
        if letter in 'AEIOUaeiou':
            translation += 'g'
        else:
            translation += letter
    return translation


print(translate(input('Enter a phrase: ')))

