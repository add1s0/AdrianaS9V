numbers=[5,12,18,21,33,42,50,77,90]

special_numbers=[]
for n in numbers:
    if n>20 and n%3==0 and n%5!=0:
        special_numbers.append(n)

print(special_numbers)
