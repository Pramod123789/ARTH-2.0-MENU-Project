def binarySearch(arr, l, r, x):
     
    
    if r >= l:
 
        mid = l + (r - l) // 2
 
       
        if arr[mid] == x:
            return mid
 
        
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        
        return -1
 
    
arr=[]
n=int(input("enter no of elements:\n"))
print("\n")
print("Enter the Elemnts \n")
for i in range(0,n):
    element=int(input())
    arr.append(element)
print("enter the element to search")
item=int(input())
result=binarySearch(arr,0,len(arr)-1,item)
if result != -1:
    print("Element is present at index % d " % result)
else:
    print("Element is not present in array")
input("\nPress any key to continue...")