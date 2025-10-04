grades=[95,82,67,54,100,73,88,42]

excellent=[]
good=[]
passed=[]
failed=[]

for g in grades:
    if g>=90:
        excellent.append(g)
    else:
        if g>=70:
            good.append(g)
        else:
            if g>=50:
                passed.append(g)
            else:
                failed.append(g)

print("excellent:", excellent)
print("good:", good)
print("pass:", passed)
print("fail:", failed)
