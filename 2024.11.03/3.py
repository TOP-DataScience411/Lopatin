number = int(input("введите целое неотрицательное число: "))
if number <0:
    quit()

dividor = 1
dividors = []

while dividor<=number/2:
    if not number%dividor:
        dividors.append(dividor)
    dividor+=1
        
print(f"сумма всех делителей - {sum(dividors)+number}")
    
# введите целое неотрицательное число: 5874
# сумма всех делителей - 12960