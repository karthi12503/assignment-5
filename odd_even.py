def CountingEvenOdd(arr, arr_size):
    even_count = 0
    odd_count = 0
    for i in range(arr_size):
        if (arr[i] & 1 == 1):
            odd_count += 1
        else:
            even_count += 1
 
    print("Number of even elements = ", 
           even_count)
    print("Number of odd elements = ",
          odd_count)
arr = []
n = int(input("Enter the length of an array:"))
for i in range(n):
    x=int(input("Enter the value:"))
    arr.append(x)
print("Array:",arr)
CountingEvenOdd(arr, n)