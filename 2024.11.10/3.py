
def numbers_strip(listofnumbers = list[float],num=1,*,copy = False):

    if copy: workinglist = listofnumbers[:]
    else:workinglist = listofnumbers\

    for _ in range(num):
        workinglist.remove(max(workinglist))
        workinglist.remove(min(workinglist))

    return workinglist
    
    # D:\top academy\Data science\Homework\2024.11.10>python -i 3.py
# >>> numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# >>> id(numbers)
# 2198664434112
# >>> test = numbers_strip(numbers)
# >>> print(test)
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# >>> print(numbers)
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# >>> numbers is test
# True
# >>> test = numbers_strip(numbers,3,copy = True)
# >>> print(numbers)
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# >>> print(test)
# [5, 6, 7, 8, 9, 10, 11]
# >>>

