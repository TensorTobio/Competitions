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
