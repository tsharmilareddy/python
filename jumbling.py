s=input()
len=len(s)
b=""
for i in range(len):
    i=int(input())
    b=b+b[i]
print(b)