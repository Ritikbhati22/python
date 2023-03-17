letter = '''Dear Name
You are Selecter
             Date'''
name = input("Name")
date = input("date")
letter = letter.replace("Name",name)
letter = letter.replace("Date",date)
print(letter)