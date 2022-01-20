new_list = []
def list_check(l):
    if type(l) != type([]): return False
    else: return True
def flat(values,f):
    for i in values:
        if f(i):
            flat(i,f)
        else:
            new_list.append(i)
    return(new_list)


flat(l,list_check)
