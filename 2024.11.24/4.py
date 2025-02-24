import  random
def tree_generator(start =2,stop = 5):
    random_val = random.randrange(start,stop)
    if start>0:start-=1
    elif stop>0:stop-=1
    result=[]
    for el in range(random_val):
        if bool(random.getrandbits(1)):
            result.append("leaf")
        else:result.append(tree_generator(start,stop))
    return result
    
    
    
    # >>> tree_generator()
# ['leaf', 'leaf', ['leaf', [], 'leaf', [['leaf', ['leaf'], 'leaf'], 'leaf', 'leaf', 'leaf']], 'leaf']
# >>> tree_generator()
# [['leaf', 'leaf', 'leaf'], [[['leaf', 'leaf']]], 'leaf', [['leaf', ['leaf'], 'leaf', ['leaf', [], []]]]]
# >>> tree_generator()
# [[[['leaf', ['leaf'], 'leaf'], 'leaf'], 'leaf', [[[], 'leaf', [[[]]]], ['leaf', [['leaf'], 'leaf']]]], 'leaf']
# >>> tree_generator()
# ['leaf', ['leaf'], 'leaf', 'leaf']
# >>> tree_generator()
# ['leaf', 'leaf', [['leaf', []], [[[], 'leaf', 'leaf']], ['leaf', 'leaf', 'leaf'], 'leaf'], ['leaf', [['leaf'], [[['leaf'], ['leaf']], 'leaf', 'leaf'], [], [['leaf'], 'leaf']], 'leaf', ['leaf', [['leaf'], 'leaf']]]]
# >>> tree_generator()
# ['leaf', ['leaf']]