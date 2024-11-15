def orth_triangle(cathetus1=None,cathetus2=None, hypotenuse=None):

    if cathetus1 == None: cathetus1 = cathetus2
    if cathetus1 == None:return None
    if hypotenuse and hypotenuse < cathetus1:return None


    if cathetus1 != None != cathetus2:
        ans = pow((cathetus1**2+cathetus2**2),1/2)
        return ans
    elif (cathetus2!=None or cathetus1!=None) and hypotenuse!= None:
        ans = pow(hypotenuse ** 2 - cathetus1 ** 2, 1 / 2)
        return ans
    else: return None
    
    # >>> print(orth_triangle(cathetus1=8, cathetus2=15))
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3,cathetus1=9))
# None
# >>> print(orth_triangle(cathetus1=3, hypotenuse=5))
# 4.0
# >>> print(orth_triangle(cathetus1=8, cathetus2=15))
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3,cathetus1=9))
# None
# >>>