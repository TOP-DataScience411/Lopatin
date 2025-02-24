def tree_leaves(tree):
    res =0
    for el in tree:
        if el == "leaf":
            res+=1
        else:res+=tree_leaves(el)
    return res
    
    
    
# >>> tree_leaves(['leaf'])
# 1

# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>> tree_leaves(tree)
# 38
# >>>