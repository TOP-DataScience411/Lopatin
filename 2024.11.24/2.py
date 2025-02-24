
    
def product(iter):
    if len(iter)==1:
        return float(iter[0])
    return iter[0]*product(iter[1:])


    # >>> product(range(10, 60, 10))
    # 12000000.0
    # >>> 
    # >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
    # 0.0