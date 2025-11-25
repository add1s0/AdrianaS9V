def sum_list(numbers):  # definira funkciq za suma na spisuk
    total = 0            # zapochvame s obshto 0
    for number in numbers:   # obhojdame vsichki chisla v spisuka
        total = total + number  # dobavqme chisloto kum obshtata suma
    return total          # vrushtame rezultata

def sum_list_rec(numbers):  # definira rekursivna funkciq za suma na spisuk
    if len(numbers) == 0:     # ako spisuka e prazen
        return 0               # vrushtame 0
    else:
        return numbers[0] + sum_list_rec(numbers[1:])  # vzimame purvoto chislo + suma na ostanalite

# primer
my_list = [1, 2, 3, 4, 5]  # suzdavame spisuk ot chisla
print("Sumata s rekursiq e:", sum_list_rec(my_list))  # izvikvame rekursivnata funkciq i printirame rezultata

def reverse_string(text):  # definira funkciq za obrushtane na niz
    reversed_text = ""      # suzdavame prazen niz za rezultata
    for char in text:       # obhojdame vseki simvol v niza
        reversed_text = char + reversed_text  # dobavqme simvola otpred kum rezultata
    return reversed_text    # vrushtame niza

def reverse_string_rec(text):  # definira rekursivna funkciq za obrushtane na niz
    if text == "":              # ako niza e prazen
        return ""               # vrushtame prazen niz
    else:
        return reverse_string_rec(text[1:]) + text[0]  # obrushame ostanalata chast + purviq simvol

def fib(n):                  # definira funkciq za n-toto chislo na Fibonacci 
    if n == 0:                # ako n e 0
        return 0              # vrushtame 0
    elif n == 1:              # ako n e 1
        return 1              # vrushtame 1
    else:
        a = 0                 # purvo chislo v redicata
        b = 1                 # vtoro chislo v redicata
        for i in range(2, n + 1):  # obhojdame ot 2 do n
            c = a + b         # subirame predishnite dve chisla
            a = b             # a stava predishnoto vtoro chislo
            b = c             # b stava novoto chislo
        return b              # vrashtame n-toto chislo

def fib_rec(n):              # rekursivna funkciq za n-toto chislo na Fibonacci
    if n == 0:               # ako n e 0
        return 0             # vrashtame 0
    elif n == 1:             # ako n e 1
        return 1             # vrashtame 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)  # rekursivno izchislqvame predishnite dve chisla i gi subirame
