def sum(*args):
    # args will be a tuple of all the values passed to sum
    print(args)
    total = 0 
    for i in args:
        total += i
    return total

'''It will work for any numbers of argument'''
print(sum(4,4,60,10)) 