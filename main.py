A = [10,5,13,8,2, 5, 3, 4, 7, 8]

for i in range(1, len(A)):
    value = A[i]

    j = i-1
    while j >= 0 and value < A[j]:
        A[j+1] = A[j]
        j -= 1
        A[j + 1] = value

print("Sorted Array")
for i in range(len(A)):
    print("%d" %A[i],end=" ")