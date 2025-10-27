def luhnCheck(cardNumber):
    if type(cardNumber)==int and cardNumber==abs(cardNumber): #проверяем, что cardNumber-натуральное число
        cardNumber = abs(cardNumber)
        digits = [int(d) for d in str(cardNumber) if d.isdigit()]
        control = digits.pop()
        parity = (len(digits))%2
        total = 0
        for i in range(len(digits)):
            if i % 2 == parity:
                doubled = digits[i] * 2
                if doubled > 9:
                    doubled -= 9
                total += doubled
            else:
                total += digits[i]
        return (total + control) % 10 == 0
    else:
        return False
""" print(luhnCheck('проверка'))
print(luhnCheck(524356))
print(luhnCheck(-893353)) """

while True:
    user = int(input("Введите номер карты: "))
    if user==-1: #выход при вводе -1
        exit()
    try:
        k = luhnCheck(user)
        if k:
            print("correct")
        else:
            print("incorrect")
        break
    except ValueError:
        print("incorrect")
