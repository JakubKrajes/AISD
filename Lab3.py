def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))


def power(number: int, n: int) -> int:
    if n <= 0:
        return 1
    return(number*power(number,n-1))

print(power(2, 6))


def reverse(txt: str)->str:
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

print(reverse("pies"))
