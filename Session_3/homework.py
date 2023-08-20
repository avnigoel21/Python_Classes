# Write a program to fill in a letter template given below with name and date

letter = '''
Dear <|NAME|>, 
    You are selected!
<|DATE|>
'''



name = input("Enter your name: ")
date = input("Enter the date: ")

letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)

print(letter)








