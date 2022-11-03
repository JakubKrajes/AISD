def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))


def power(number: int, n: int)-> int:
    if n <= 0:
        return 1
    return(number*power(number,n-1))

print(power(2, 6))


def reverse(txt: str)-> str:
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

print(reverse("pies"))

def factorial(n:int)- >int:
    if n==1 or n==0:
        return 1

    return n*factorial(n-1)

def prime(n:int, i=2)-> bool:
    if n==i:
        return True

    if n%i==0:
        return False

    return prime(n,i=i+1)
    
def remove_duplicates(txt:str)-> str:
    if len(txt) == 1:
        return txt
    
    if txt[0] == txt[1]:
        return remove_duplicates(txt[1:])
    
    return txt[0] + remove_duplicates(txt[1:])
