l= list()
n = int(input("enter the number of list to enterd "))
print("enter",n,"values")
for i in range(n):
    l.append(int(input()))

s = int(input("enter the target searched "))
for i in range(len(l)):
    if l[i] == s:
        print(s," is  found at position",i+1)
        break
else:
    print("the list is not found")