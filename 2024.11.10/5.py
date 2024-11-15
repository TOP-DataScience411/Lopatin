
    
def central_tendency(*numbers):
    ans = dict()
    numbers=list(numbers)
    temp = sum(numbers,[]) #список списков в список

    temp.sort()
    numbers = temp
    if  len(numbers) % 2:
        ans['median']=numbers[int(len(numbers)/2)]
    else:ans['median']=(numbers[int(len(numbers)/2)]+numbers[int(len(numbers)/2)+1])/2
    ans['arithmetic']=sum(numbers)/len(numbers)
    temp =1
    for el in numbers:
        temp *= el
    ans['geometric']=pow(temp,(1/len(numbers)))
    temp=0
    for el in numbers:
        temp+=1/el
    ans['harmonic']=len(numbers)/temp
    return ans


# >>> print(central_tendency([1, 2, 3, 4, 5]))
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>>