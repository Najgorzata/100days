total = 0
for n in range (1,101):
    if n%2 == 0:
        total=total+n

print(total)

total=0
for n in range (2, 101, 2):
    total += n 
print (total)