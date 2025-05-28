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

for k in encrypt[:5]:
    print(k, end=" ")

print()
for k in encrypt[5:14]:
    print(" ", k, end=" ")

print()
for k in encrypt[14:]:
    print("   ", k, end=" ")
print()

print(f"Encrypted:  {encrypt}")
print(f"Decrypted: {text}")
