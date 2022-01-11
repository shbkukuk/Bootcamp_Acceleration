new_list = []
def list_check(l):
    if type(l) != type([]): return False
    else: return True
def reverse(val,f):
    for i in range(0,len(val)):
        if f(val[i]):
            new_list.append(val[i][::-1])
    return (new_list[::-1])
reverse(l,list_check)
             



