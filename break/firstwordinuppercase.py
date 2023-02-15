n=input()
first_space_index=0
for char in n:
    if char==" ":
        break
    else:
        first_space_index=first_space_index+1
first_word=n[:first_space_index]
uppercase=first_word.upper()
print(uppercase)