def simple_multiplication(number) :
    return number * 8 if number % 2 ==0 else number * 9


#2nd style of solution :


def simple_multiplication(number) :
    if number % 2 ==0 :
        return number * 8
    else:
        return number * 9