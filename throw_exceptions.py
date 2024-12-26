def remainder_division(a, b):
    if b == 0:
        raise Exception('Divisor cannot be 0')
    # you can also raise ZeroDivisionError here.... 


    result = a//b
    remainder = a%b
    print(a, '/', b, 'is', result, 'remainder', remainder)


# calls invalid dividable params
    remainder_division(10,0)