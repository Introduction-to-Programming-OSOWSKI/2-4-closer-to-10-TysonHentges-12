#WRITE YOUR CODE IN THIS FILE
def close10(x,y):
    if abs(10-x)>abs(10-y):
        return y
    elif abs(10-x)<abs(10-y):
        return x
    else:
        return 0
print(close10(5,12))
print(close10(9,50))
print(close10(8,12))