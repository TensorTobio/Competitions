#1)

rows = int(input("Enter the no. of rows : "))
col = int(input("Enter the no. of columns : "))

matrix = []
for x in range(rows):
    x = input("Enter grid row by row (characters without spaces) : ")
    matrix.append(x)

for j in range(len(matrix)):
    print(matrix[j])

print()

maxi = 0
maxipal = ""
for i in range(rows):
    pali = matrix[i]
    p = str(matrix[i])
    p = p[::-1]
    if p == pali:
        print("Palindrome found.")
        print(pali)
        print("left-right")
        print("length = ", len(pali))
        x = len(pali)
        if x > maxi:
            maxi = x
            maxipal = pali
    else:
        print("No palindrome")

if maxi != 0:
    print("The biggest palindrome is ", maxipal, "Length is ", maxi)



#2)
text = input("Enter the text to be encrypted : ")
rows = int(input("Enter the no. of rows : "))
x = len(text)
encrypt = ""

# For rows = 3
for j in range(rows):
    if (j + 1) % 2 == 0:
        for i in range(j, x, rows - 1):
            encrypt = encrypt + text[i]
    else:
        for i in range(j, x, rows + 1):
            encrypt = encrypt + text[i]

"""for k in encrypt[:5]:
    print(k, end=" ")

print()
for k in encrypt[5:14]:
    print(" ", k, end=" ")

print()
for k in encrypt[14:]:
    print("   ", k, end=" ")
print()"""

print(f"Encrypted:  {encrypt}")
print(f"Decrypted: {text}")
