def binary_search(l,target):
    l.sort()
    low,high=0,len(l)-1
    while low<=high:
        mid  = (low+high)//2

        if l[mid]==target:
            return mid
        
        elif l[mid]< target:
            low =mid+1
        else:
            l[mid]> target
            high = mid-1

    return-1



l = [5,10,90,56,85,26]
target = 56
result = binary_search(l,target)

if result != -1:
    print(f"{target}, the element is found at position,{result}")
else:
    print("the element is not found")
    