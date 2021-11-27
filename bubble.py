import time
def bubbleSort(arr):
    n = len(arr)
  
   
    for i in range(n):
        swapped = False
 
       
        for j in range(0, n-i-1):
  
            
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
 
       
        if swapped == False:
            break
          

arr=[]
n=int(input("enter no of elements:"))
print("Enter THe Elemnts : \n")
for i in range(0,n):
    element=int(input())
    arr.append(element)

bubbleSort(arr) 
print ("Sorted array :")
for i in range(len(arr)):
    print ("%d" %arr[i],end=" ")
input("\nPress any key to continue...")


