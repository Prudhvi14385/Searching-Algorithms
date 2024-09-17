
    # def method

def search(arr,lenght):
    for i in range(len(arr)):
        if arr[i]== target:
            return i
    return -1

arr = [10,52,68,96,78,25,63]
target = 63

result = search(arr,target)

if result !=-1:
    print(f"element found at index {result}")

else:
    print("element is not found")