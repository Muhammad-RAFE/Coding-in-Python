def mysum(seq):
    return reduce(lambda a, b: a +b , seq , 0)
print mysum([1,2,3,4])