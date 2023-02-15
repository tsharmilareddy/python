age=int(input())
output=""
if age>=20:
    output="you are of age"+str(age)+"you are an adult now"
elif age>12:
    output="you are of age"+str(age)+"you are a teenager now"
else:
    output="you are of age"+str(age)+"you are a child now"
print(output)