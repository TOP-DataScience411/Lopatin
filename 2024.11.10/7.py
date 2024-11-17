
def int_base(number:str,base:int,new_base:int):
    number = number.lower()
    Dictionary = dict()
    for el in range(10):
        Dictionary[str(el)]=el

    # посмотрел тут, разобрался с функциями map, zip, zip_longest,ord  https://stackoverflow.com/questions/16060899/alphabet-range-in-python

    list_of_chars = list(map(chr,range(ord('a'),1+ord('z'))))
    for value,key in enumerate(list_of_chars,10):
        Dictionary[key]=value
    temp =0
    if '.' in number:
        i=len(number[:number.index('.')])-1
        number = number.replace('.','')
    else:i=len(number)-1

    for el in number:
        if el in Dictionary.keys():
            if Dictionary[el]>=base:return None
            temp+=Dictionary[el]*base**i
            i-=1
        else: return None

    if new_base == 10:return str(temp)

    ans = ''
    less = temp%1
    temp = int(temp)
    while True:
        ans+= str(temp % new_base)
        temp//=new_base
        if temp<new_base:
            ans+=str(temp)
            ans=ans[::-1]
            break

    if not less:
        return ans
    else:ans+='.'

    while True:
        less*=new_base
        ans +=str(int(less))
        less-=int(less)
        if not less:return ans