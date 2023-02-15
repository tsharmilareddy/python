n=int(input())
left_spaces=" "* (n-1)
row_output=left_spaces+"*"
print(row_output)

# upper traingle
hollow_spaces_count= -1

for row in range(2,n+1):
    left_spaces_count=n-row
    left_spaces=" "*left_spaces_count
    hollow_spaces_count=hollow_spaces_count+2
    hallow_spaces=" "* hollow_spaces_count
    row_output=left_spaces + "*"+hallow_spaces+ "*"
    print(row_output)
# lower traingle

for row_lower in range(1,n-1):
    left_spaces_count=row_lower
    left_spaces =" " * left_spaces_count
    hollow_spaces_count=hollow_spaces_count-2
    hallow_spaces=" " * hollow_spaces_count
    row_output=left_spaces + "*"+hallow_spaces+ "*"
    print(row_output)
left_spaces=" "* (n-1)
row_output=left_spaces+"*"
print(row_output)