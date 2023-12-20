# # ZERODIV ERR
# n=10
# m=0
# print(n/m)

# #IMPORT ERR
# import xyz

# #INDEX ERR
# list_data = [1, 2, 3, 4, 5]
# x = list_data[6]

# #KEYBOARD INTERR
# name=input('number enter:')

# #KEY ERR
# dict_data = {'2':'Two', '4':'Four', '6':'Six'}
# dict_data['1']

# #NAME ERR
# alpha=['r','ww']
# alphax

# #ATTRIBUTE ERR
# alpha=['r','ww']
# alpha.lower()

# #TYPE ERR
# alpha=['r','ww']
# alpha/2

# #STOP ITER
# XS=iter(['apple','pear','guava','cherry'])
# print(next(XS))
# print(next(XS))
# print(next(XS))
# print(next(XS))
# print(next(XS))

class BaseError(Exception):
    pass

class HighValueError(BaseError):
    pass

class LowValueError(BaseError):
    pass

value = 5

while True:
    try:
        n = int(input("Enter a number: "))
        if n > value:
            raise HighValueError
        elif n < value:
            raise LowValueError
    except LowValueError:
        print("Very low value, give input again.")
        print()
    except HighValueError:
        print("Very high value, give input again.")
        print()
    else:
        print("Nice! Correct answer!")
        break
        