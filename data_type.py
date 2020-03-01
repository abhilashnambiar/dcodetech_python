odd = []
even = []
data = input()
req = data.split(" ")
print(req)
for i in req:
    if(i.isdigit()):
        i = int(i)
        if(i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)

even.sort()
odd.sort(reverse=True)

print(even)
print(odd)