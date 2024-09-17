             # itterative method

l = list()
n = int(input("enter the how many number to add: "))
print("enter", n , "elements")
for i in range(n):
    l.append(int(input()))
    l.sort()

s= int(input("enter the number: "))
low = 0
high = len(l)
mid = 0

while low<=high:
    mid = (low+high)//2
    if l[mid] == s:
        print(s,"The element is found",mid+1)
        break
    elif l[mid]>s:
        high = mid-1
    else:
        l[mid]<s
        low = mid+1

else:
    print(s,"the element is not found")

