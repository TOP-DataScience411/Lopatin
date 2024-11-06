inp =int(input("введите количество разрядов. целое неотрицательное число: "))
Max = 10**inp
Min = Max/10

primes = [2, 3, 5, 7, 11, 13]
i = 2
maxPrime = primes[-1]
while Max > maxPrime:
    Flag = True
    for el in primes:
        if not (maxPrime+i)%el:
            i+=1
            Flag = False
            break
        if (maxPrime+i)**(1/2)<el:
            break
    if Flag:
        maxPrime += i
        primes.append(maxPrime)
        i=2

count = -2
for el in primes[::-1]:
    count+=1
    if el <Min:
        break

Min='1'+'0'*(inp-1)
Max='1'+'0'*inp

print(f"сумма всех простых чисел между {Min} и {Max} равна {count}")

# Это было очень сложно
# введите количество разрядов. целое неотрицательное число: 7
# сумма всех простых чисел между 1000000 и 10000000 равна 586081
