a=input()
b=input()
sequance_index=0
sequance_length=len(b)
for char in a:
    if char == b[sequance_index]:
        seqance_index +=1
        if sequance_index ==sequance_length:
            break
if sequance_index ==sequance_length:
    print("Yes")
else:
    print("No")
