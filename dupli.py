array = []
num = int(input("Enter the length of an array:"))
for i in range(num):
    x=int(input("Enter the value:"))
    array.append(x)
print("Array:",array)
  
for i in range(0, len(array)):    
    for j in range(i+1, len(array)):    
        if(array[i] == array[j]):    
            print("Duplicate elements in given                               array: ");  
            print(array[j]);    
            