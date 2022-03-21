# Print odd numbers between 102 and 66 in decreasing order
print("Odd numbers between 102 and 66 in decreasing order:")
for i in range(102, 66, -1):
    if i % 2 != 0:
        print(i, end=" ")
