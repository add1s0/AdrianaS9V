words=["level","python","radar","java","civic","kotlin","refer"]

palindromes=[]

for w in words:
    is_palindrome=True
    for i in range(len(w)//2):
        if w[i]!=w[-i-1]:
            is_palindrome=False
            break
    if is_palindrome:
        palindromes.append(w)

print(palindromes)
