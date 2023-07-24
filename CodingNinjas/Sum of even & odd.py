number=input()

evens, odds=0, 0
for i in number:
    i=int(i)
    if i%2==0:
        evens+=i
    else:
        odds+=i
print(evens, odds)