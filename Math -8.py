

def myfunction():
    lista = list(range(1, 11))
    print(len(lista))

myfunction()

def func(p : int):
    print(p)

func("a")


def newfunc(n1 : int, n2 : int):
    if not isinstance(n1 , int) or (n2, int):
        return "error"
    return print(n1 + n2)

newfunc(1, 2)

lista = list(range(1, 11))

def sumlist(lista):
    return sum(lista)

print(sumlist(lista))

