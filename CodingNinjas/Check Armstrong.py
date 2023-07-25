n=input()

total=0

for i in n:
    total+=int(i)**len(n)

print('true' if total==int(n) else 'false')