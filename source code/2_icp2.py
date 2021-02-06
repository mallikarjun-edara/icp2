#2.Given a non-negative integer num, return the number of steps to reduce it to zero.
#If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.”
def count(m):##function declaration
    if(m==0):
        return 0
    else:
        return 1 + count(m // 10)
def countSteps(x):##function declaration
    c = 0###declaration
    last = x
    while(last):###while loop starts
        digits = count(last)
        digits -= 1
        divisor = pow(10, digits)
        first = last // divisor
        lastnumber = first * divisor
        skipped = (last - lastnumber) // first
        skipped += 1
        c += skipped
        last = last - (first * skipped)
    return c
n=int(input("input number:"))###asking input from user
print("no of steps taken",countSteps(n))###printing the result
