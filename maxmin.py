def maxminposition(arr, n):
   minposition = arr.index(min(arr))
   maxposition = arr.index(max(arr)) 
   print ("The Maximum number in given array is:",arr[maxposition])
   print ("The Minimum number in given array is:",arr[minposition])

arr=[]
n=int(input("Enter the length of the array :"))
print("Enter the Element :")
for i in range(int(n)):
   a=int(input(""))
   arr.append(a)
maxminposition(arr,n)