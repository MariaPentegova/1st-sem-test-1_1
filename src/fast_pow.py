def fastPow(number, power):
    if power == 0: #если степень равна 0
        return 1
    else:
        result = number
        k = abs(power) #дополнительная переменная на случай, если степень отрицательная
        while k != 1:
            result = result**2
            k //= 2
    if power>0: #вывод зависит от того, положительна или отрицательна степень
        return result
    else:
        return 1/result
print(fastPow(2, -2))
print(fastPow(-3, 2))
print(fastPow(-3, -2))
