# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

numbers = ["0","1","2","3","4","5","6","7","8","9"]
word = input("Enter a word: ").upper()
on = True
while on:
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        word = input("Enter a word: ").upper()
    else:
        print(output_list)
        on = False



# on = True
# while on:
#     word = input("Enter a word: ").upper()
#     for i in numbers:
#         print(i)
#         print(type(i))
#         if i in word:
#             print("True")
#             pass
#         else:
#             output_list = [phonetic_dict[letter] for letter in word]
#             on = False
# print(output_list)
