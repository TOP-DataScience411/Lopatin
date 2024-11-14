
def taxi_cost(lengh = None,time = 0):
    if lengh == None or lengh<0:return None
    if lengh == 0:
        return 160+time*3
    else: return round(80+time*3+lengh*6/150)
    
    # D:\top academy\Data science\Homework\2024.11.10>python -i 2.py
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None
# >>>