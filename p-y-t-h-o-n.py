a=input()
len=len(a)
b=a[0]
for i in range(1,len):
    b=b+"-"+a[i]
print(b)